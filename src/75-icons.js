// Ícones finais em PNG, acompanhados pelos nomes em HTML acessível.
const iconCache={};function iconURL(k){if(iconCache[k])return iconCache[k];const f=ART.frames[ART.icons?.[k]];if(!f||!artReady)return '';const c=document.createElement('canvas');c.width=f.w;c.height=f.h;c.getContext('2d').drawImage(atlasImages[f.atlas],f.x,f.y,f.w,f.h,0,0,f.w,f.h);return iconCache[k]=c.toDataURL()}
function itemIcon(k){const url=iconURL(k);return url?'<img class="art-icon" alt="" aria-hidden="true" src="'+url+'">':''}
function toolIcon(i){return itemIcon(i===2?'s'+seedIndex:['hoe','wateringcan','seed','bag','journal','axe','rod'][i])||TL[i][0]}
const iconPanelBase=panel;panel=function(title,body){iconPanelBase(title,body);for(const b of $('shop').querySelectorAll('button[onclick]')){const match=b.getAttribute('onclick').match(/(?:sell|cook|buyMarketItem|giveGift|giftRainara|loadDonkey|donateFood|fairContribution|festivalMeal|buyCareItem|eat)\([^']*'([a-z_0-9]+)'/);if(match&&ART.icons[match[1]])b.insertAdjacentHTML('afterbegin',itemIcon(match[1]))}};
// Decoração de cercas mantém conexões reais e deixa o portão aberto legível.
const connectedFence=drawFence;drawFence=function(k,f){connectedFence(k,f);const x=k%MW*T,y=(k/MW|0)*T;for(const [off,dx,dy]of [[-1,-4,0],[1,12,0],[-MW,4,-5],[MW,4,10]])if(farm.fences[k+off]&&(f.kind!=='gate'||!f.open))R(x+dx,y+dy,8,2,'#e1cea2')};
// Casas e viveiro exibem as melhorias persistentes sem alterar o footprint lógico.
const upgradedHouse=house;house=function(b){upgradedHouse(b);if(home.level){R(b.x*T+12,b.y*T+51,18,2,'#c79b48');worldSprite('flower',(b.x+6)*T,(b.y+b.h)*T)}};
const expandedTown=drawTownBuilding;drawTownBuilding=function(b){expandedTown(b);if(b.id==='nursery'&&world.projects.nursery&&done('Q22'))worldSprite('native_flower',(b.x+3)*T,(b.y+b.h)*T)};
