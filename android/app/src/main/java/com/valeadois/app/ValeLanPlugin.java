package com.valeadois.app;

import android.net.nsd.NsdManager;
import android.net.nsd.NsdServiceInfo;
import android.os.Handler;
import android.os.Looper;
import android.util.Base64;
import com.getcapacitor.JSArray;
import com.getcapacitor.JSObject;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.Enumeration;
import java.util.Locale;

@CapacitorPlugin(name="ValeLan")
public class ValeLanPlugin extends Plugin {
    private static final String SERVICE="_valea2._tcp.";
    private final Object guard=new Object();
    private ServerSocket server;
    private Socket peer;
    private boolean connecting=false;
    private volatile boolean running=false;
    private Thread acceptThread;
    private NsdManager nsd;
    private NsdManager.RegistrationListener registration;

    @PluginMethod
    public void start(PluginCall call) {
        int port=call.getInt("port",8765);
        if(port<1024||port>65535){call.reject("Invalid port");return;}
        if(running){JSObject result=new JSObject();result.put("ip",localIp());result.put("port",port);call.resolve(result);return;}
        try {
            server=new ServerSocket(port);
            running=true;
            acceptThread=new Thread(this::acceptLoop,"ValeLanAccept");
            acceptThread.start();
            registerService(call.getString("name","Vale a Dois"),port);
            JSObject result=new JSObject();result.put("ip",localIp());result.put("port",port);call.resolve(result);
        } catch(Exception e) {running=false;call.reject("Cannot open LAN server: "+e.getMessage());}
    }

    @PluginMethod
    public void stop(PluginCall call){shutdown();call.resolve();}

    @PluginMethod
    public void send(PluginCall call){
        String text=call.getString("text","");
        if(text.length()>800000){call.reject("Message too large");return;}
        synchronized(guard){
            if(peer==null||peer.isClosed()){call.reject("No peer connected");return;}
            try{writeFrame(peer.getOutputStream(),1,text.getBytes(StandardCharsets.UTF_8));call.resolve();}
            catch(Exception e){call.reject("LAN send failed: "+e.getMessage());}
        }
    }

    @PluginMethod
    public void discover(PluginCall call){
        NsdManager manager=(NsdManager)getContext().getSystemService(android.content.Context.NSD_SERVICE);
        if(manager==null){call.reject("NSD unavailable");return;}
        JSArray rooms=new JSArray();
        final NsdManager.DiscoveryListener[] ref=new NsdManager.DiscoveryListener[1];
        ref[0]=new NsdManager.DiscoveryListener(){
            public void onDiscoveryStarted(String type){}
            public void onServiceFound(NsdServiceInfo info){
                if(!SERVICE.equals(info.getServiceType()))return;
                try{manager.resolveService(info,new NsdManager.ResolveListener(){
                    public void onResolveFailed(NsdServiceInfo service,int error){}
                    public void onServiceResolved(NsdServiceInfo service){
                        InetAddress host=service.getHost();
                        if(!(host instanceof Inet4Address))return;
                        JSObject room=new JSObject();room.put("name",service.getServiceName());room.put("ip",host.getHostAddress());room.put("port",service.getPort());rooms.put(room);
                    }
                });}catch(Exception ignored){}
            }
            public void onServiceLost(NsdServiceInfo info){}
            public void onDiscoveryStopped(String type){}
            public void onStartDiscoveryFailed(String type,int error){try{manager.stopServiceDiscovery(ref[0]);}catch(Exception ignored){}call.reject("NSD failed: "+error);}
            public void onStopDiscoveryFailed(String type,int error){}
        };
        try{manager.discoverServices(SERVICE,NsdManager.PROTOCOL_DNS_SD,ref[0]);
            new Handler(Looper.getMainLooper()).postDelayed(()->{try{manager.stopServiceDiscovery(ref[0]);}catch(Exception ignored){}JSObject out=new JSObject();out.put("rooms",rooms);call.resolve(out);},3500);
        }catch(Exception e){call.reject("NSD failed: "+e.getMessage());}
    }

    private void registerService(String name,int port){
        try{
            nsd=(NsdManager)getContext().getSystemService(android.content.Context.NSD_SERVICE);
            if(nsd==null)return;
            NsdServiceInfo info=new NsdServiceInfo();info.setServiceName(name);info.setServiceType(SERVICE);info.setPort(port);
            registration=new NsdManager.RegistrationListener(){
                public void onServiceRegistered(NsdServiceInfo service){}
                public void onRegistrationFailed(NsdServiceInfo service,int error){}
                public void onServiceUnregistered(NsdServiceInfo service){}
                public void onUnregistrationFailed(NsdServiceInfo service,int error){}
            };
            nsd.registerService(info,NsdManager.PROTOCOL_DNS_SD,registration);
        }catch(Exception ignored){}
    }

    private String localIp(){
        String fallback="127.0.0.1";
        try{Enumeration<NetworkInterface> list=NetworkInterface.getNetworkInterfaces();while(list.hasMoreElements()){
            NetworkInterface nic=list.nextElement();if(!nic.isUp()||nic.isLoopback())continue;
            Enumeration<InetAddress> ips=nic.getInetAddresses();while(ips.hasMoreElements()){
                InetAddress ip=ips.nextElement();if(ip instanceof Inet4Address&&ip.isSiteLocalAddress()){
                    if(nic.getName().toLowerCase(Locale.ROOT).startsWith("wlan"))return ip.getHostAddress();
                    fallback=ip.getHostAddress();
                }
            }
        }}catch(Exception ignored){}return fallback;
    }

    private void acceptLoop(){
        while(running){
            try{
                Socket socket=server.accept();
                synchronized(guard){if(connecting||peer!=null&&!peer.isClosed()){
                    socket.getOutputStream().write("HTTP/1.1 409 Conflict\r\nConnection: close\r\n\r\n".getBytes(StandardCharsets.US_ASCII));socket.close();continue;
                }connecting=true;}
                new Thread(()->serve(socket),"ValeLanPeer").start();
            }catch(Exception e){if(running)notifyPeer(false);}
        }
    }

    private void serve(Socket socket){
        try{
            socket.setSoTimeout(30000);
            InputStream in=socket.getInputStream();OutputStream out=socket.getOutputStream();
            ByteArrayOutputStream header=new ByteArrayOutputStream();int a=-1,b=-1,c=-1,d=-1,n;
            while(header.size()<8192&&(n=in.read())!=-1){header.write(n);a=b;b=c;c=d;d=n;if(a=='\r'&&b=='\n'&&c=='\r'&&d=='\n')break;}
            String request=header.toString(StandardCharsets.US_ASCII.name()),key=null;
            for(String line:request.split("\r\n"))if(line.toLowerCase(Locale.ROOT).startsWith("sec-websocket-key:"))key=line.substring(line.indexOf(':')+1).trim();
            if(key==null||!request.startsWith("GET ")){socket.close();return;}
            byte[] digest=MessageDigest.getInstance("SHA-1").digest((key+"258EAFA5-E914-47DA-95CA-C5AB0DC85B11").getBytes(StandardCharsets.US_ASCII));
            String accept=Base64.encodeToString(digest,Base64.NO_WRAP);
            out.write(("HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: "+accept+"\r\n\r\n").getBytes(StandardCharsets.US_ASCII));out.flush();
            synchronized(guard){peer=socket;connecting=false;}
            notifyPeer(true);
            while(running&&!socket.isClosed()){
                int h1=in.read(),h2=in.read();if(h1<0||h2<0)break;
                int opcode=h1&15;boolean masked=(h2&128)!=0;long len=h2&127;
                if(len==126)len=(in.read()<<8)|in.read();else if(len==127){len=0;for(int i=0;i<8;i++)len=(len<<8)|in.read();}
                if(!masked||len>800000||len<0)break;
                byte[] mask=readBytes(in,4),payload=readBytes(in,(int)len);if(mask==null||payload==null)break;
                for(int i=0;i<payload.length;i++)payload[i]^=mask[i%4];
                if(opcode==8)break;
                if(opcode==9){synchronized(guard){writeFrame(out,10,payload);}continue;}
                if(opcode!=1)continue;
                String text=new String(payload,StandardCharsets.UTF_8);
                JSObject event=new JSObject();event.put("text",text);notifyListeners("message",event);
            }
        }catch(Exception ignored){}
        finally{try{socket.close();}catch(Exception ignored){}synchronized(guard){if(peer==socket)peer=null;connecting=false;}notifyPeer(false);}
    }

    private void notifyPeer(boolean connected){JSObject event=new JSObject();event.put("connected",connected);notifyListeners("peer",event);}
    private static byte[] readBytes(InputStream in,int len)throws Exception{byte[] data=new byte[len];int pos=0;while(pos<len){int n=in.read(data,pos,len-pos);if(n<0)return null;pos+=n;}return data;}
    private static void writeFrame(OutputStream out,int opcode,byte[] payload)throws Exception{
        out.write(0x80|opcode);
        int len=payload.length;if(len<126)out.write(len);else if(len<65536){out.write(126);out.write((len>>8)&255);out.write(len&255);}else{out.write(127);for(int i=7;i>=0;i--)out.write((int)(((long)len>>(8*i))&255));}
        out.write(payload);out.flush();
    }
    private void shutdown(){running=false;try{server.close();}catch(Exception ignored){}synchronized(guard){try{if(peer!=null)peer.close();}catch(Exception ignored){}peer=null;}if(nsd!=null&&registration!=null)try{nsd.unregisterService(registration);}catch(Exception ignored){}registration=null;}
    @Override protected void handleOnDestroy(){shutdown();super.handleOnDestroy();}
}
