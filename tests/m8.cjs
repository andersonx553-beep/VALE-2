const {chromium}=require('playwright');
const assert=require('node:assert/strict');
(async()=>{
  const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});
  {
    const context=await browser.newContext({viewport:{width:1280,height:720}}),page=await context.newPage(),errors=[];
    page.on('pageerror',e=>errors.push(e.message));await page.goto('http://127.0.0.1:8000');await page.locator('#go').click();
    assert.equal(await page.evaluate(()=>typeof GameInput.packet),'function');
    const safe=await page.evaluate(()=>{profile.configured=true;story.scene=null;scenePlaying=false;closeShop();GameInput.reset();for(let ty=3;ty<MH-3;ty++)for(let tx=3;tx<MW-3;tx++){const x=tx*T+8,y=ty*T+8;if(!bl(x,y)&&!bl(x-18,y)&&!bl(x+18,y)&&!bl(x,y-18)&&!bl(x,y+18)&&!bl(x-14,y-14)&&!bl(x+14,y-14)&&!bl(x-14,y+14)&&!bl(x+14,y+14))return {x,y}}throw Error('no safe movement tile')});
    const straight=await page.evaluate(({x,y})=>{P.x=x;P.y=y;GameInput.reset();const before=GameInput.vector();dispatchEvent(new KeyboardEvent('keydown',{code:'KeyW',key:'w',bubbles:true}));const vector=GameInput.vector();upd(.2);dispatchEvent(new KeyboardEvent('keyup',{code:'KeyW',key:'w',bubbles:true}));return {distance:Math.hypot(P.x-x,P.y-y),vector,before}},safe);
    const diagonal=await page.evaluate(({x,y})=>{P.x=x;P.y=y;GameInput.reset();dispatchEvent(new KeyboardEvent('keydown',{code:'KeyW',key:'w',bubbles:true}));dispatchEvent(new KeyboardEvent('keydown',{code:'KeyD',key:'d',bubbles:true}));const vector=GameInput.vector();upd(.2);dispatchEvent(new KeyboardEvent('keyup',{code:'KeyW',key:'w',bubbles:true}));dispatchEvent(new KeyboardEvent('keyup',{code:'KeyD',key:'d',bubbles:true}));return {distance:Math.hypot(P.x-x,P.y-y),vector}},safe);
    assert.deepEqual(straight.before,{x:0,y:0});assert.ok(straight.vector.y<-.9,'keyboard input vector');assert.ok(straight.distance>5,'keyboard movement');assert.ok(diagonal.vector.x>.65&&diagonal.vector.y<-.65,'diagonal input vector');assert.ok(Math.abs(straight.distance-diagonal.distance)<1.2,'diagonal speed normalized');
    assert.equal(await page.evaluate(()=>setInputBinding('action','KeyF')),true);assert.equal(await page.evaluate(()=>setInputBinding('run','KeyF')),false,'conflict rejected');
    assert.equal(await page.evaluate(()=>{let n=0,old=act;act=()=>n++;dispatchEvent(new KeyboardEvent('keydown',{code:'KeyF',key:'f',bubbles:true}));dispatchEvent(new KeyboardEvent('keyup',{code:'KeyF',key:'f',bubbles:true}));act=old;return n}),1,'remapped action');
    await page.evaluate(()=>{inputSettingChange('runMode','toggle');GameInput.runToggle=false;dispatchEvent(new KeyboardEvent('keydown',{code:inputPrefs.bindings.run,key:'Shift',bubbles:true}));dispatchEvent(new KeyboardEvent('keyup',{code:inputPrefs.bindings.run,key:'Shift',bubbles:true}))});
    assert.equal(await page.evaluate(()=>GameInput.isRunning()),true,'toggle run');
    await page.evaluate(()=>{GameInput.stick.x=.8;GameInput.stick.y=-.6;GameInput.runToggle=true});const packet=await page.evaluate(()=>GameInput.packet());assert.deepEqual(Object.keys(packet),['moveX','moveY','run','action','tool']);assert.equal(packet.run,true);
    await page.evaluate(()=>{inputSettingChange('controlScheme','dpad');inputSettingChange('leftHanded',true)});assert.equal(await page.locator('#mDpad').evaluate(e=>getComputedStyle(e).display),'grid');assert.ok(await page.locator('#tc').evaluate(e=>e.classList.contains('left-handed')));
    assert.deepEqual(errors,[]);await context.close();
  }
  {
    const context=await browser.newContext({viewport:{width:800,height:360},isMobile:true,hasTouch:true}),page=await context.newPage(),errors=[];page.on('pageerror',e=>errors.push(e.message));await page.goto('http://127.0.0.1:8000');await page.locator('#go').click();
    await page.evaluate(()=>{inputSettingChange('controlScheme','joystick');inputSettingChange('joystickMode','fixed');inputSettingChange('runMode','hold');GameInput.reset();applyInputPreferences()});
    assert.equal(await page.locator('#joyZone').evaluate(e=>getComputedStyle(e).display),'block');
    const box=await page.locator('#joyZone').boundingBox();assert.ok(box&&box.width>100&&box.height>80);
    await page.locator('#joyZone').dispatchEvent('pointerdown',{pointerId:11,pointerType:'touch',clientX:box.x+box.width*.32,clientY:box.y+box.height*.66,bubbles:true});await page.locator('#joyZone').dispatchEvent('pointermove',{pointerId:11,pointerType:'touch',clientX:box.x+box.width*.72,clientY:box.y+box.height*.35,bubbles:true});
    const v=await page.evaluate(()=>GameInput.vector());assert.ok(v.x>.2&&v.y<-.15,'analog vector');
    await page.locator('#mRun').dispatchEvent('pointerdown',{pointerId:22,pointerType:'touch',bubbles:true});assert.equal(await page.evaluate(()=>GameInput.isRunning()),true,'multitouch run can coexist');
    await page.locator('#joyZone').dispatchEvent('pointerup',{pointerId:11,pointerType:'touch',bubbles:true});await page.locator('#mRun').dispatchEvent('pointerup',{pointerId:22,pointerType:'touch',bubbles:true});assert.deepEqual(await page.evaluate(()=>GameInput.vector()),{x:0,y:0});assert.equal(await page.evaluate(()=>GameInput.isRunning()),false);
    await page.evaluate(()=>{GameInput.stick.x=.6;GameInput.run=true;dispatchEvent(new Event('blur'))});assert.deepEqual(await page.evaluate(()=>[GameInput.stick.x,GameInput.stick.y,GameInput.run]),[0,0,false]);
    assert.ok(await page.locator('#mAction').getAttribute('aria-label'));assert.ok(await page.locator('#mTool').getAttribute('aria-label'));assert.deepEqual(errors,[]);await context.close();
  }
  await browser.close();console.log('PASS M8: keyboard remap, diagonal normalization, analog joystick, multitouch, run modes, handed layout, reset and packet');
})().catch(e=>{console.error(e);process.exit(1)});
