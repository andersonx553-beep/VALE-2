const {chromium}=require('playwright');
const assert=require('node:assert/strict');

(async()=>{
  const browser=await chromium.launch({executablePath:process.env.CHROMIUM_EXECUTABLE_PATH||undefined,headless:true,args:['--no-sandbox']});

  // Desktop: real keyboard events, normalized movement, remapping and packet contract.
  {
    const context=await browser.newContext({viewport:{width:1280,height:720}});
    const page=await context.newPage(),errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    await page.goto('http://127.0.0.1:8000');
    await page.locator('#go').click();
    const safe=await page.evaluate(()=>{
      profile.configured=true;story.scene=null;scenePlaying=false;closeShop();GameInput.reset();
      for(let ty=3;ty<MH-3;ty++)for(let tx=3;tx<MW-3;tx++){
        const x=tx*T+8,y=ty*T+8;
        if(!bl(x,y)&&!bl(x-18,y)&&!bl(x+18,y)&&!bl(x,y-18)&&!bl(x,y+18)&&!bl(x-14,y-14)&&!bl(x+14,y-14)&&!bl(x-14,y+14)&&!bl(x+14,y+14))return {x,y};
      }
      throw Error('no safe movement tile');
    });

    await page.evaluate(({x,y})=>{P.x=x;P.y=y;GameInput.reset()},safe);
    await page.keyboard.down('w');
    const straightVector=await page.evaluate(()=>GameInput.vector());
    const straight=await page.evaluate(({x,y})=>{upd(.2);return Math.hypot(P.x-x,P.y-y)},safe);
    await page.keyboard.up('w');
    assert.ok(straightVector.y<-.9,'keyboard input vector');
    assert.ok(straight>5,'keyboard movement');

    await page.evaluate(({x,y})=>{P.x=x;P.y=y;GameInput.reset()},safe);
    await page.keyboard.down('w');await page.keyboard.down('d');
    const diagonalVector=await page.evaluate(()=>GameInput.vector());
    const diagonal=await page.evaluate(({x,y})=>{upd(.2);return Math.hypot(P.x-x,P.y-y)},safe);
    await page.keyboard.up('d');await page.keyboard.up('w');
    assert.ok(diagonalVector.x>.65&&diagonalVector.y<-.65,'diagonal vector');
    assert.ok(Math.abs(straight-diagonal)<1.2,'diagonal speed normalized');

    assert.equal(await page.evaluate(()=>setInputBinding('action','KeyF')),true);
    assert.equal(await page.evaluate(()=>setInputBinding('run','KeyF')),false,'binding conflict rejected');
    await page.evaluate(()=>{window.__m8Act=0;window.__m8OldAct=act;act=()=>window.__m8Act++});
    await page.keyboard.press('f');
    assert.equal(await page.evaluate(()=>window.__m8Act),1,'remapped action');
    await page.evaluate(()=>{act=window.__m8OldAct;restoreInputDefaults();closeShop();inputSettingChange('runMode','toggle');GameInput.runToggle=false});
    await page.keyboard.press('Shift');
    assert.equal(await page.evaluate(()=>GameInput.isRunning()),true,'toggle run');

    await page.evaluate(()=>{GameInput.stick.x=.8;GameInput.stick.y=-.6;GameInput.runToggle=true;GameInput.action=true;GameInput.tool=true});
    const packet=await page.evaluate(()=>GameInput.packet());
    assert.deepEqual(Object.keys(packet),['moveX','moveY','run','action','tool']);
    assert.equal(packet.run,true);assert.equal(packet.action,true);assert.equal(packet.tool,true);

    await page.evaluate(()=>{inputSettingChange('controlScheme','dpad');inputSettingChange('leftHanded',true)});
    assert.equal(await page.locator('#mDpad').evaluate(e=>getComputedStyle(e).display),'grid');
    assert.ok(await page.locator('#tc').evaluate(e=>e.classList.contains('left-handed')));
    assert.deepEqual(errors,[]);
    await context.close();
  }

  // Mobile landscape: analog vector, controls, concurrent movement/run state and reset.
  {
    const context=await browser.newContext({viewport:{width:800,height:360},isMobile:true,hasTouch:true});
    const page=await context.newPage(),errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    await page.goto('http://127.0.0.1:8000');
    await page.locator('#go').click();
    await page.evaluate(()=>{profile.configured=true;story.scene=null;scenePlaying=false;closeShop();inputSettingChange('controlScheme','joystick');inputSettingChange('joystickMode','fixed');inputSettingChange('runMode','hold');GameInput.reset();applyInputPreferences()});
    assert.equal(await page.locator('#joyZone').evaluate(e=>getComputedStyle(e).display),'block');
    const box=await page.locator('#joyZone').boundingBox();assert.ok(box&&box.width>100&&box.height>80);

    // Validate analog math and concurrent run state independently from browser synthetic touch quirks.
    const analog=await page.evaluate(()=>{GameInput.stick.x=.72;GameInput.stick.y=-.54;return GameInput.vector()});
    assert.ok(analog.x>.6&&analog.y<-.45,'analog joystick vector');
    await page.evaluate(()=>{GameInput.run=true});
    assert.equal(await page.evaluate(()=>GameInput.isRunning()),true,'movement and run can coexist');
    assert.ok((await page.evaluate(()=>GameInput.vector())).x>.6,'run does not erase joystick');

    await page.evaluate(()=>{GameInput.stick.x=.6;GameInput.run=true;dispatchEvent(new Event('blur'))});
    assert.deepEqual(await page.evaluate(()=>[GameInput.stick.x,GameInput.stick.y,GameInput.run]),[0,0,false]);
    assert.ok(await page.locator('#mAction').getAttribute('aria-label'));
    assert.ok(await page.locator('#mTool').getAttribute('aria-label'));
    assert.deepEqual(errors,[]);
    await context.close();
  }

  await browser.close();
  console.log('PASS M8: keyboard remap, normalized movement, analog joystick, run modes, handed layout, reset and network packet');
})().catch(e=>{console.error(e);process.exit(1)});
