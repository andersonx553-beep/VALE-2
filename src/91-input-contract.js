// Completa o contrato semântico usado por teclado, toque e comandos LAN.
GameInput.slot=null;GameInput.diary=false;GameInput.map=false;
const contractVector=GameInput.vector;GameInput.vector=function(){const v=contractVector.call(this);this.moveX=v.x;this.moveY=v.y;return v};
const contractReset=GameInput.reset;GameInput.reset=function(){contractReset.call(this);this.moveX=this.moveY=0;this.slot=null;for(const k of ['action','tool','nextItem','previousItem','inventory','diary','map','cancel'])this[k]=false};
const contractSlot=selectSlot;selectSlot=function(i){contractSlot(i);GameInput.slot=sel};
const contractInventory=openInventory;openInventory=function(){GameInput.pulse('inventory');contractInventory()};
const contractDiary=openNotebook;openNotebook=function(){GameInput.pulse('diary');contractDiary()};
const contractMap=openRouteMap;openRouteMap=function(){GameInput.pulse('map');contractMap()};
addEventListener('keydown',e=>{if(e.code==='Escape')GameInput.pulse('cancel')},{capture:true});
addEventListener('wheel',()=>setTimeout(()=>{GameInput.slot=sel;if(window.ValeCoop?.mode==='client')coopSendCommand('SLOT',{slot:sel})},0),{passive:true});
