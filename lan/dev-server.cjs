// Relay LAN para testes no navegador. O Android hospeda a mesma conexão nativamente.
const http=require('node:http');
const {WebSocketServer}=require('ws');
const port=Number(process.env.VALE_LAN_PORT||8765);
const server=http.createServer((req,res)=>{res.writeHead(200,{'content-type':'application/json','access-control-allow-origin':'*'});res.end(JSON.stringify({room:host?'Vale a Dois':null,players:Number(!!host)+Number(!!guest),maxPlayers:2}))});
const sockets=new WebSocketServer({noServer:true,maxPayload:800000});
let host=null,guest=null;
server.on('upgrade',(req,socket,head)=>{const path=req.url?.split('?')[0];if(path==='/host'&&!host||path==='/join'&&host&&!guest){sockets.handleUpgrade(req,socket,head,ws=>{if(path==='/host'){host=ws;ws.send(JSON.stringify({type:'HOST_READY'}))}else guest=ws;ws.on('message',raw=>{const text=raw.toString();if(text.length>800000)return ws.close(1009,'too large');const peer=ws===host?guest:host;if(peer?.readyState===1)peer.send(text)});ws.on('close',()=>{if(ws===host){host=null;if(guest?.readyState===1){guest.send(JSON.stringify({type:'HOST_LEFT'}));guest.close()}guest=null}else if(ws===guest){guest=null;if(host?.readyState===1)host.send(JSON.stringify({type:'PEER_LEFT'}))}})})}else{socket.write('HTTP/1.1 409 Conflict\r\nConnection: close\r\n\r\n');socket.destroy()}});
server.listen(port,'0.0.0.0',()=>console.log('Vale LAN relay listening on '+port));
