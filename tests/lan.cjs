const {chromium}=require('playwright');
const {WebSocket}=require('ws');
const {spawn}=require('node:child_process');
const assert=require('node:assert/strict');
(async()=>{
 let relay;try{await fetch('http://127.0.0.1:8765')}catch{relay=spawn(process.execPath,['lan/dev-server.cjs'],{stdio:'ignore'});await new Promise(r=>setTimeout(r,300))}
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_EXECUTABLE_PATH||undefined,args:['--no-sandbox']}),context=await browser.newContext(),host=await context.newPage(),guest=await context.newPage(),errors=[];
 for(const page of [host,guest])page.on('pageerror',e=>errors.push(e.message));
 for(const[page,name]of[[host,'Host'],[guest,'Convidado']]){await page.goto('http://127.0.0.1:8000');await page.evaluate(()=>openCoop());await page.locator('#coopName').fill(name)}
 await host.locator('#coopCreate').click();await guest.locator('#coopIP').fill('127.0.0.1');await guest.locator('#coopJoin').click();
 await host.waitForFunction(()=>coop.connected);await guest.waitForFunction(()=>coop.joined);
 assert.equal(await host.evaluate(()=>coop.peer.name),'Convidado');
 const third=new WebSocket('ws://127.0.0.1:8765/join');const thirdResult=await new Promise(resolve=>{third.on('open',()=>resolve('open'));third.on('error',()=>resolve('rejected'))});assert.equal(thirdResult,'rejected','third client rejected');
 const start=await host.evaluate(()=>coop.peer.x);await guest.evaluate(()=>{GameInput.stick.x=1});await host.waitForFunction(x=>coop.peer.x>x+8,start);await guest.evaluate(()=>{GameInput.stick.x=0});
 const key=await host.evaluate(()=>{
   const p=coop.peer;for(let y=6;y<MH-6;y++)for(let x=6;x<MW-6;x++){const k=(y+1)*MW+x;if(g[y+1][x]===0&&!sol[k]&&!cr[k]){p.x=x*T+8;p.y=y*T+8;p.d=0;p.sel=2;p.seedIndex=0;soil[k]=1;delete cr[k];p.inventory.s0=5;return k}}throw Error('no crop tile')
 });
 await guest.evaluate(()=>GameInput.reset());await host.evaluate(()=>{coop.peerInput={x:0,y:0}});await new Promise(r=>setTimeout(r,250));
 const pulse=async tool=>guest.evaluate(tool=>coopWire({type:'INPUT',seq:++coop.seq,moveX:0,moveY:0,run:false,action:!tool,tool}),tool);
 await pulse(true);await host.waitForFunction(k=>!!cr[k],key);assert.equal(await host.evaluate(k=>cr[k].t,key),0);
 await host.evaluate(()=>{coop.peer.sel=1});await new Promise(r=>setTimeout(r,150));await pulse(true);await host.waitForFunction(k=>wet[k]===1,key);
 await host.evaluate(k=>{cr[k].a=CT[cr[k].t].g;coop.peer.sel=2},key);await new Promise(r=>setTimeout(r,150));await pulse(false);await host.waitForFunction(k=>!cr[k],key);assert.equal(await host.evaluate(()=>coop.peer.inventory.nabo),1);
 await host.evaluate(()=>{coop.peer.x=57*T;coop.peer.y=20*T;money=200;tm=540});
 await guest.evaluate(()=>coopSendCommand('BUY',{item:0}));await host.waitForFunction(()=>coop.peer.inventory.s0===5);const afterBuy=await host.evaluate(()=>money);assert.equal(afterBuy,200-await host.evaluate(()=>CT[0].s));
 await guest.evaluate(()=>coopSendCommand('SELL',{item:'nabo'}));await host.waitForFunction(()=>coop.peer.inventory.nabo===0);assert.ok(await host.evaluate(value=>money>value,afterBuy));
 const animal=await host.evaluate(()=>{const b={id:farm.nextId++,kind:'coop',x:10,y:10,level:0,water:12,clean:100};farm.buildings.push(b);const a=createAnimal('chicken',b,'Pipoca LAN');coop.peer.x=a.x;coop.peer.y=a.y+20;return a.id});
 await guest.evaluate(id=>coopSendCommand('CARE',{animal:id,action:'pet'}),animal);await host.waitForFunction(id=>farm.animals.find(a=>a.id===id)?.pet===day,animal);
 const oldDay=await host.evaluate(()=>day);await host.evaluate(()=>{newDay();rain=1;queueSave()});await guest.waitForFunction(d=>day===d+1&&rain===1,oldDay);
 const peerSaved=await host.evaluate(()=>{save();return {x:world.coop.x,seed:world.coop.inventory.s0}});
 await guest.evaluate(()=>coop.transport.close());await guest.waitForFunction(()=>coop.joined,{timeout:10000});assert.equal(await host.evaluate(()=>coop.connected),true);
 await host.reload();const restored=await host.evaluate(()=>({x:world.coop?.x,seed:world.coop?.inventory.s0}));assert.deepEqual(restored,peerSaved);
 await guest.waitForFunction(()=>coop.mode==='off');assert.equal(await guest.evaluate(()=>localStorage.getItem(SAVE_KEY)),null,'guest never writes host world into its local single-player slot');
 assert.deepEqual(errors,[]);await browser.close();if(relay)relay.kill();console.log('PASS LAN: 2 instances, third rejected, movement, plant/water/harvest, buy/sell, animal care, day/weather, reconnect, host save/reload');
})().catch(e=>{console.error(e);process.exit(1)});
