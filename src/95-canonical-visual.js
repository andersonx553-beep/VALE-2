/* ===== REMODELAÇÃO VISUAL: luz, bloom, fonte, casas floridas, rostos estáveis ===== */
(()=>{
const glows=[],E=(x,y,rx,ry,f)=>{ctx.beginPath();ctx.ellipse(x,y,rx,ry,0,0,7);ctx.fillStyle=f;ctx.fill()};
const gl=(x,y,r,c,a)=>glows.push([x,y,r,c,a]),night=()=>Math.min(1,dark()/.62);
const bC=document.createElement('canvas'),bX=bC.getContext('2d');bC.id='bloom';cv.after(bC);
const st=document.createElement('style');st.textContent='#c{}#bloom{position:fixed;left:0;top:0;pointer-events:none;mix-blend-mode:screen;image-rendering:pixelated;opacity:.26}.p{background:#2a2420cc!important;backdrop-filter:blur(6px);border-color:#e8cf9a!important;border-radius:14px!important;box-shadow:0 4px 14px #0005}#dlg,#shop{border-radius:16px!important;box-shadow:0 10px 30px #0006}.sl{border-radius:12px!important}#intro{background:radial-gradient(ellipse at 50% 20%,#f3b872 0,#7a5a6e 38%,#1b2a38 100%)!important}#intro h1{text-shadow:0 3px 18px #ffb35a}@media(max-height:500px){#bloom{display:none}}';document.head.appendChild(st);
const wrap=(n,f)=>{try{const o=eval(n);eval(n+'=f(o)')}catch(e){}};
// ---- rostos estáveis: a direção só muda se persistir por 130ms (sem piscar ao virar) ----
const stable=(a,k,fn)=>{const now=performance.now();if(a._f===undefined){a._f=a[k]??0;a._t=now}if(a[k]!==a._f&&now-a._t>130){a._f=a[k];a._t=now}const o=a[k];a[k]=a._f;try{fn()}finally{a[k]=o}};
const shadow=(x,y,r)=>{ctx.fillStyle='rgba(30,20,40,.3)';ctx.beginPath();ctx.ellipse(x,y+1,r,r*.38,0,0,7);ctx.fill()};
wrap('drawActor',o=>function(id,a,s){shadow(a.x,a.y,7);stable(a,a.d!==undefined?'d':'dir',()=>o(id,a,s))});
wrap('drawCreature',o=>function(kind,a){shadow(a.x,a.y+1,kind==='cow'||kind==='horse'?9:5);stable(a,'d',()=>o(kind,a))});
// ---- casas: floreiras, janelas acesas, lanternas ----
function decor(key,X,Y){const f=ART.frames[key];if(!f)return;const ox=X-f.anchor[0],oy=Y-f.anchor[1],W=f.w,H=f.h,n=night();
for(const[a,b]of[[.12,.29],[.66,.84]]){const x0=ox+a*W,x1=ox+b*W,y0=oy+.46*H,y1=oy+.63*H,w=x1-x0;
if(n>.12){ctx.fillStyle='rgba(255,200,115,'+(.45+n*.35)+')';ctx.fillRect(x0,y0,w,y1-y0);R(x0+w/2,y0,1,y1-y0,'#7a5535');R(x0,(y0+y1)/2,w,1,'#7a5535');gl((x0+x1)/2,(y0+y1)/2,30,'255,185,95',.55*n)}
R(x0-1,y1+1,w+2,3,'#8a5a3a');for(let i=0;i<6;i++){R(x0+i*w/5.5,y1-1+(i%2),2,2,['#f58fa8','#ffd36b','#fff6e8','#c9a0ff','#ff9d6b','#f58fa8'][i]);R(x0+i*w/5.5,y1+1,1,1,'#4f8f4a')}}
const lx=[ox+.47*W,ox+.74*W];for(const x of lx){R(x,oy+.6*H,1,3,'#3a2a22');R(x-1,oy+.6*H+3,3,3,n>.1?'#ffd98a':'#e9c779');if(n>.1)gl(x,oy+.6*H+4,22,'255,200,110',.6*n)}
if(key==='building.house')for(let i=0;i<3;i++){const t=(time*.25+i/3)%1;ctx.fillStyle='rgba(235,235,240,'+(.5*(1-t))+')';ctx.beginPath();ctx.arc(ox+.82*W+Math.sin(t*6+i)*3,oy+3-t*20,2+t*4,0,7);ctx.fill()}}
wrap('house',o=>b=>{o(b);decor(ART.buildings.house,b.x*T,(b.y+b.h)*T)});
wrap('shop',o=>b=>{o(b);decor(ART.buildings.shop,b.x*T,(b.y+b.h)*T)});
wrap('drawTownBuilding',o=>b=>{o(b);if(ART.buildings[b.id])decor(ART.buildings[b.id],b.x*T,(b.y+b.h)*T)});
// ---- fonte da praça: três níveis, jatos, ondas, pétalas e brilho ----
function fountain(cx,cy){const n=night();shadow(cx,cy+8,28);
E(cx,cy+4,25,12,'#a89c86');E(cx,cy+1,25,12,'#e2d7c0');E(cx,cy+1,21.5,9.5,'#bfb39b');
const g=ctx.createLinearGradient(cx-20,cy-8,cx+20,cy+10);g.addColorStop(0,'#7fd3de');g.addColorStop(1,'#3a93b5');ctx.fillStyle=g;ctx.beginPath();ctx.ellipse(cx,cy+2,20,8.2,0,0,7);ctx.fill();
ctx.strokeStyle='rgba(255,255,255,.45)';ctx.lineWidth=1;for(let i=0;i<3;i++){const t=(time*.5+i/3)%1;ctx.globalAlpha=1-t;ctx.beginPath();ctx.ellipse(cx,cy+3,4+t*15,1.6+t*6,0,0,7);ctx.stroke()}ctx.globalAlpha=1;
for(let i=0;i<5;i++){const a=time*.35+i*1.26;R(cx+Math.cos(a)*14,cy+3+Math.sin(a)*5.5,2,1,i%2?'#ffc4d2':'#fff2c8')}
R(cx-3,cy-14,6,15,'#d9cdb6');R(cx-3,cy-14,2,15,'#efe6d2');R(cx+2,cy-14,1,15,'#b9ad96');
E(cx,cy-13,12,4.5,'#a89c86');E(cx,cy-14.5,12,4.5,'#e8dec9');E(cx,cy-14.5,9.5,3.2,'#6fc7d6');
R(cx-1,cy-24,2,10,'#d9cdb6');E(cx,cy-25,3,3,'#f2e9d4');
for(let i=0;i<14;i++){const u=(time*1.3+i/14)%1,s=(i%2?1:-1)*(1+i%4)/4,dx=s*u*15,dy=-27-34*u*(1-u)+(i%3?26:13)*u*u;ctx.fillStyle='rgba(225,247,255,'+(.95-u*.5)+')';ctx.fillRect(Math.round(cx+dx),Math.round(cy+dy),2,2)}
for(let i=0;i<8;i++){const u=(time*1.1+i/8)%1;ctx.fillStyle='rgba(225,247,255,'+(.8-u*.6)+')';ctx.fillRect(Math.round(cx+(i-3.5)*1.2*(.4+u)),Math.round(cy-14-12*u*(1-u)*2+u*10),1,1)}
gl(cx,cy-12,44,'150,225,255',.16+.3*n);if(n>.1)gl(cx,cy-18,26,'255,230,160',.35*n)}
wrap('drawPublicPoint',o=>p=>{if(p.type==='water')fountain(p.x*T+8,p.y*T+4);else o(p)});
wrap('interactPublic',o=>p=>{const r=o(p);if(p.type==='water'){const x=p.x*T+8,y=p.y*T;for(let i=0;i<22;i++)pt(x+(Math.random()-.5)*34,y-6,1,['#bfefff','#ffe08a','#fff6d8'][i%3],1);
setTimeout(()=>{const W=['Você jogou uma moeda e desejou uma colheita farta. ✨','A água brilha... o vale sorri para você. 💧','Um desejo sussurrado: dias bons ao lado de quem importa. 🌸','As gotas dançam. Algo bom vem aí! 🍀'];if(Math.random()<.12){money+=5;flt(x,y-20,'+5');toast('Uma moeda brilha no fundo: +5 🪙');queueSave&&queueSave()}else toast(W[Math.random()*W.length|0])},900)}return r});
// ---- pós-processamento: grade de cor, raios de luz, brilhos, vagalumes, vinheta, bloom ----
let fxFrame=0;function fx(){const w=VW,hh=VH,n=night(),q=tm/60%24,compact=window.innerHeight<500;if(compact){glows.length=0;return}ctx.save();ctx.setTransform(1,0,0,1,0,0);
const warm=(q>=16&&q<20?Math.sin((q-16)/4*Math.PI):0)+(q>=5.5&&q<8.5?Math.sin((q-5.5)/3*Math.PI):0);
ctx.globalCompositeOperation='soft-light';ctx.fillStyle=warm>0?'rgba(255,150,85,'+warm*.4+')':n>.3?'rgba(70,90,200,'+n*.28+')':'rgba(255,238,190,.14)';ctx.fillRect(0,0,w,hh);
ctx.globalCompositeOperation='lighter';
if(n<.3&&!inside&&!rain)for(let i=0;i<(compact?1:4);i++){const x0=((i*97+time*3)%(w+140))-70,gr=ctx.createLinearGradient(x0,0,x0+hh*.5,hh);gr.addColorStop(0,'rgba(255,238,190,.11)');gr.addColorStop(1,'rgba(255,238,190,0)');ctx.fillStyle=gr;ctx.beginPath();ctx.moveTo(x0,0);ctx.lineTo(x0+24,0);ctx.lineTo(x0+24+hh*.5,hh);ctx.lineTo(x0+hh*.5,hh);ctx.fill()}
if(!inside&&world.region==='farm'){LP.forEach(([x,y])=>gl(x*T+8,y*T-4,36,'255,205,125',.5*n));lakes.forEach(([lx,ly,a,b],li)=>{for(let i=0;i<9;i++){const t=h(i,li+3)*6.28,r=Math.sqrt(h(i+9,li))*.85,x=(lx+Math.cos(t)*a*r)*T+8-cam.x|0,y=(ly+Math.sin(t)*b*r)*T+8-cam.y|0,s=Math.sin(time*1.7+i*2.1);if(s>.5&&x>0&&y>1&&x<w&&y<hh){ctx.fillStyle='rgba(255,255,255,'+(s-.5)*1.3+')';ctx.fillRect(x,y,2,1);ctx.fillRect(x,y-1,1,3)}}})}
gl(P.x,P.y-8,40,'255,215,150',.38*n);
for(const[x,y,r,c,a]of glows){const sx=x-cam.x,sy=y-cam.y;if(sx<-r||sy<-r||sx>w+r||sy>hh+r)continue;const g=ctx.createRadialGradient(sx,sy,0,sx,sy,r);g.addColorStop(0,'rgba('+c+','+a+')');g.addColorStop(1,'rgba('+c+',0)');ctx.fillStyle=g;ctx.fillRect(sx-r,sy-r,r*2,r*2)}glows.length=0;
if(!rain)for(let i=0;i<(compact?8:28);i++){const x=((h(i,5)*w*1.4+time*(3+h(i,9)*4)-cam.x*.4)%w+w)%w,y=((h(i,6)*hh+Math.sin(time*.8+i)*6-cam.y*.4)%hh+hh)%hh;if(n>.3){const a=.5+.5*Math.sin(time*2.3+i*3);const g=ctx.createRadialGradient(x,y,0,x,y,5);g.addColorStop(0,'rgba(210,255,130,'+a*.8+')');g.addColorStop(1,'rgba(210,255,130,0)');ctx.fillStyle=g;ctx.fillRect(x-5,y-5,10,10)}else{ctx.fillStyle='rgba(255,246,205,.4)';ctx.fillRect(x|0,y|0,1,1)}}
ctx.globalCompositeOperation='source-over';const v=ctx.createRadialGradient(w/2,hh/2,hh*.38,w/2,hh/2,Math.hypot(w,hh)*.62);v.addColorStop(0,'rgba(25,12,35,0)');v.addColorStop(1,'rgba(25,12,35,.4)');ctx.fillStyle=v;ctx.fillRect(0,0,w,hh);ctx.restore();
const bw=w>>2,bh=hh>>2;if(bC.width!==bw||bC.height!==bh){bC.width=bw;bC.height=bh}bC.style.width=cv.style.width;bC.style.height=cv.style.height;if((++fxFrame%3)===0)bX.drawImage(cv,0,0,bw,bh)}
wrap('draw',o=>function(){o();fx()});
})();
