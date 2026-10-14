const {chromium}=require('playwright');
const assert=require('node:assert/strict');
(async()=>{
 const browser=await chromium.launch(),context=await browser.newContext(),page=await context.newPage(),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto('http://127.0.0.1:8000');await page.locator('#go').click();
 const result=await page.evaluate(()=>{
  profile.configured=true;story.scene=null;scenePlaying=false;closeShop();
  day=11;tm=540;N[0].h=0;I.nabo=1;giveGift(0,'nabo');const birthday={friendship:N[0].h,year:N[0].birthdayYear,giftDay:N[0].giftDay};closeShop();
  profile.look='pele-escura';money=3000;I.madeira=200;I.pedra=100;story.completed.push('Q07');upgradeTool('hoe');const hoe=profile.tools.hoe;closeShop();
  const k=20*MW+45;soil[k]=1;cr[k]={t:0,a:CT[0].g,w:1,careDays:CT[0].g};const crop=CT[0].k,before=I[crop];commitHarvest(k);const harvest={items:I[crop]-before,gold:qualitySupply[crop]?.excellent||0};
  I.milho=2;farm.hay=0;storeHay();const hay=farm.hay;closeShop();
  home.level=1;inside=true;startHomeProject();const pending=home.project?.daysLeft;closeShop();newDay();newDay();const home2=home.level;
  for(const k of Object.keys(RELICS)){I[k]++;donateRelic(k)}story.completed.push('Q24','Q05','Q13');finishValeArchive();const archive=world.projects.valeArchive;
  inside=false;switchRegion('bosque',[6,10],true);interactPublic(PUBLIC_POINTS.bosque.find(p=>p.id==='portal_clareira'));const clearing=world.region==='clareira';switchRegion('alto',[34,25],true);interactPublic(PUBLIC_POINTS.alto.find(p=>p.id==='portal_pedreira'));const quarry=world.region==='pedreira';
  save();return {birthday,hoe,harvest,hay,pending,home2,archive,clearing,quarry,look:profile.look};
 });
 assert.deepEqual(result.birthday,{friendship:4,year:1,giftDay:11});assert.equal(result.hoe,1);
 assert.equal(result.harvest.items,1);assert.equal(result.harvest.gold,1);assert.equal(result.hay,4);
 assert.equal(result.pending,2);assert.equal(result.home2,2);assert.equal(result.archive,true);assert.equal(result.clearing,true);assert.equal(result.quarry,true);assert.equal(result.look,'pele-escura');
 await page.reload();const restored=await page.evaluate(()=>({look:profile.look,tools:profile.tools,hay:farm.hay,home:home.level,gold:qualitySupply[CT[0].k]?.excellent,archive:world.projects.valeArchive,birthday:N[0].birthdayYear}));
 assert.equal(restored.look,'pele-escura');assert.equal(restored.tools.hoe,1);assert.equal(restored.hay,4);assert.equal(restored.home,2);assert.equal(restored.gold,1);assert.equal(restored.archive,true);assert.equal(restored.birthday,1);assert.deepEqual(errors,[]);
 await browser.close();console.log('PASS gaps: birthday, gift, avatar, tools, golden harvest, hay, timed works, relic archive, save/reload');
})().catch(e=>{console.error(e);process.exit(1)});
