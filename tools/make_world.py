#!/usr/bin/env python3
"""Sprites ambientais originais; pixels inteiros, alpha e paleta do elenco."""
from make_art import Atlas,OUT,O,WHITE
from PIL import Image,ImageDraw
import json
COL={'grass':'#687044','light':'#a8b878','wood':'#967145','dark':'#68462a','red':'#a94f3c','coral':'#cc7060','stone':'#849089','water':'#497f92','cream':'#e1cea2'}
def prop(kind,season=0):
 im=Image.new('RGBA',(64,64));q=ImageDraw.Draw(im)
 def b(x,y,w,h,c):q.rectangle((x,y,x+w-1,y+h-1),fill=COL.get(c,c))
 def p(points,c):q.polygon(points,fill=COL.get(c,c));q.line(points+[points[0]],fill=O,width=1)
 if kind in ['tree','fruit_tree']:
  b(29,40,7,22,'dark');b(31,40,3,21,'wood');b(26,60,15,2,'dark')
  colors=[['#466644','#687044','#87905d','#a8b878'],['#466644','#5c7945','#89a65e','#b3bc81'],['#73393c','#a94f3c','#c79b48','#e1cea2'],['#647b75','#9cafac','#dae3d8','#fff7e2']][season]
  p([(9,40),(5,31),(8,25),(6,18),(13,13),(15,7),(24,6),(32,2),(41,5),(46,11),(54,14),(58,23),(56,31),(59,39),(52,45),(42,46),(35,50),(24,48),(15,45)],colors[0])
  p([(9,29),(11,18),(20,12),(30,8),(41,11),(51,18),(53,29),(46,34),(35,36),(23,34)],colors[1]);b(18,16,8,3,colors[2]);b(26,12,12,3,colors[2]);b(38,18,8,3,colors[2]);b(21,15,4,2,colors[3]);b(34,26,8,2,colors[2]);b(45,32,5,2,colors[2]);b(13,36,8,2,colors[1]);b(31,44,7,2,colors[1])
  if kind=='fruit_tree':
   for x,y in [(18,27),(38,20),(43,37)]:p([(x,y),(x+5,y-1),(x+7,y+2),(x+6,y+6),(x+1,y+7),(x-1,y+3)],'coral');b(x+2,y,2,2,'cream');b(x+2,y-3,1,3,'grass')
 elif kind=='rock':p([(16,59),(14,51),(20,43),(31,41),(42,45),(48,53),(46,60),(32,62)],'stone');p([(18,50),(23,44),(31,44),(36,48),(29,53)],'#b0b8ac');b(32,56,9,2,'#657570')
 elif kind in ['chair','rocking_chair']:
  p([(20,35),(42,35),(44,48),(21,48)],'wood');b(20,34,3,16,'dark');b(40,34,3,16,'dark');b(22,38,17,3,'cream');b(21,49,22,5,'wood');b(21,53,3,9,'dark');b(40,53,3,9,'dark');b(18,46,5,3,'dark');b(41,46,5,3,'dark')
  if kind=='rocking_chair':p([(16,58),(21,61),(43,61),(48,57),(46,62),(20,63)],'dark')
 elif kind in ['table','bench','workbench']:
  p([(10,45),(47,45),(53,50),(52,55),(11,55),(7,51)],'wood');b(11,46,36,2,'cream');b(14,55,4,8,'dark');b(45,55,4,8,'dark');b(29,48,1,6,'dark')
  if kind=='table':b(21,44,12,3,WHITE);b(34,43,6,5,'coral');b(35,43,4,1,'cream')
  if kind=='workbench':b(21,42,13,3,'stone');b(25,37,3,9,'dark');b(36,43,8,3,'grass')
 elif kind in ['water','trough','pond']:
  p([(9,53),(15,46),(46,46),(53,52),(49,61),(15,62)],'stone');p([(14,53),(20,49),(43,49),(48,53),(44,58),(19,58)],'water');b(23,52,12,1,'#93c8ce');b(34,55,7,1,'#c2ddd3')
  if kind=='water':b(30,32,5,19,'stone');b(27,31,10,4,'#c0d1ca');b(28,40,4,3,'water')
 elif kind=='lamp':b(30,31,3,31,'dark');p([(24,32),(26,22),(39,22),(42,32)],'dark');b(28,24,8,6,'#e8c575');b(30,25,3,3,WHITE)
 elif kind in ['flower','seedling','native_flower']:
  p([(21,54),(43,54),(40,63),(24,63)],'red');b(28,43,3,14,'grass');b(33,38,3,18,'grass');p([(28,46),(21,41),(20,44),(26,50)],'light');p([(35,46),(43,42),(43,45),(36,50)],'light')
  if kind!='seedling':
   for x,y in [(29,42),(34,37)]:b(x-3,y,8,3,'coral');b(x,y-3,3,9,'coral');b(x,y,3,3,'cream')
 elif kind in ['mail','board','sign','upgrade']:
  b(29,48,3,14,'dark')
  if kind=='mail':p([(20,39),(23,35),(42,35),(45,39),(45,48),(20,48)],'grass');b(23,38,18,2,'light');b(25,43,13,1,O);b(41,36,2,9,'coral')
  else:p([(12,32),(50,32),(52,49),(11,49)],'wood');b(15,35,32,11,'cream');b(18,38,21,1,'dark');b(18,41,14,1,'dark');b(13,49,3,14,'dark');b(47,49,3,14,'dark')
 elif kind in ['nest','catbed']:
  p([(12,56),(20,50),(42,50),(52,56),(46,63),(18,63)],'wood');b(20,55,25,4,'cream');b(18,60,30,1,'dark')
  if kind=='nest':b(26,55,4,5,WHITE);b(33,56,4,4,WHITE)
  else:b(19,54,27,6,'coral');b(24,54,3,3,'cream')
 elif kind=='platform':b(17,54,32,4,'wood');b(20,58,4,6,'dark');b(43,58,4,6,'dark');b(19,54,28,1,'cream')
 elif kind in ['luggage','chest']:
  p([(17,45),(46,45),(48,49),(47,61),(17,61),(15,49)],'wood');b(17,49,29,1,'cream');b(28,48,7,9,'dark');b(30,51,3,4,'#c79b48');b(22,43,18,2,'dark');b(22,41,3,5,'dark');b(38,41,3,5,'dark')
 elif kind=='bed':p([(14,35),(48,35),(48,63),(14,63)],'dark');b(16,38,30,10,WHITE);b(16,49,30,12,'water');b(18,51,26,2,'#93c8ce');b(16,62,4,2,'dark');b(43,62,4,2,'dark')
 elif kind=='kitchen':p([(14,40),(47,40),(49,44),(49,63),(13,63),(13,44)],'stone');b(16,43,29,5,O);b(22,44,15,3,'red');b(24,42,10,3,'stone');b(17,52,27,9,'#52665e');b(21,53,20,2,'dark');b(15,49,33,2,'cream')
 elif kind=='gauge':p([(27,40),(36,40),(38,62),(26,62)],'stone');b(28,41,2,20,'#c0d1ca');[b(30,y,5,1,'cream') for y in [44,49,54]]
 elif kind=='sluice':p([(10,39),(52,39),(54,63),(8,63)],'stone');b(17,43,30,20,'dark');b(28,29,6,34,'#c0d1ca');b(21,27,21,4,'dark');b(16,47,32,2,'wood');b(16,56,32,2,'wood')
 elif kind=='filter':p([(19,47),(45,47),(47,62),(17,62)],'stone');[b(x,49,2,12,'dark')for x in range(21,44,5)]
 elif kind=='piece':p([(24,49),(40,45),(45,51),(43,60),(29,63),(22,57)],'stone');b(28,51,2,8,'#c0d1ca');b(34,49,2,9,'#c0d1ca');b(30,55,4,2,'water')
 elif kind=='glove':p([(25,55),(23,50),(25,48),(29,51),(30,46),(33,47),(34,52),(38,48),(40,51),(37,57),(33,62),(28,62)],'coral');b(29,58,5,3,'cream')
 elif kind=='portrait':b(19,27,26,34,'dark');b(22,30,20,27,'cream');b(27,34,11,10,'#805133');b(28,37,9,8,'#e9b88b');b(26,46,14,10,'coral')
 return im

def building(kind,w,h):
 im=Image.new('RGBA',(w+12,h+16));q=ImageDraw.Draw(im)
 def b(x,y,ww,hh,c):q.rectangle((x,y,x+ww-1,y+hh-1),fill=COL.get(c,c))
 def p(pts,c):q.polygon(pts,fill=COL.get(c,c));q.line(pts+[pts[0]],fill=O)
 house=kind in ['house','shop','workshop','atelier','clinic','kitchen','nursery'];roof={'house':'red','shop':'water','workshop':'wood','atelier':'#9270a1','clinic':'#356f69','kitchen':'#c79b48','nursery':'grass','coop':'red','stable':'#687044','pigpen':'wood','stall':'water','rabbit_hutch':'coral','apiary':'#c79b48','cheesemaker':'cream','loom':'#9270a1'}[kind]
 if house:
  p([(7,34),(w+5,34),(w+5,h+14),(7,h+14)],'cream');[b(8,y,w-2,1,'#c6b68f') for y in range(40,h+12,6)]
  p([(1,36),(8,14),(w-2,8),(w+10,33),(w+10,38)],roof)
  for y in range(17,35,5):b(7,y,w,1,'dark')
  b(12,14,w-16,2,'coral' if kind=='house' else 'light');door=48 if kind in ['house','shop'] else w//2-8;b(door+6,h-28,16,42,'dark');b(door+8,h-26,12,39,'wood');b(door+17,h-8,2,2,'cream')
  for x in [16,w-28]:b(x,51,22,21,'dark');b(x+2,53,18,17,'water');b(x+3,54,8,5,'#93c8ce');b(x+10,53,2,17,'cream');b(x+2,60,18,2,'cream')
  if kind=='house':b(w-18,0,11,22,'stone');b(w-19,0,13,3,'#52665e')
  if kind=='shop':
   for x in range(8,w,8):b(x,40,8,9,'coral' if x//8%2 else WHITE)
  if kind=='nursery':
   for x in range(12,w-12,16):b(x,17,13,17,'#93c8ce');b(x+5,17,2,17,'dark');b(x,25,13,1,'cream')
  if kind=='atelier':b(w-21,h-18,8,19,'#9270a1');b(w-15,h-24,2,25,'dark')
  if kind=='clinic':b(w//2-3,41,14,4,WHITE);b(w//2+2,36,4,14,WHITE)
 else:
  # Roof/wall occupy the existing two solid tile rows; pen remains open.
  p([(4,18),(w+8,18),(w+8,44),(4,44)],'wood');p([(0,18),(10,6),(w-4,6),(w+12,18)],roof);b(10,9,w-16,2,'cream');b(5,28,w+2,1,'dark');b(w//2,23,17,21,'dark');b(10,25,14,11,'cream');b(12,27,10,7,'water')
  if kind=='apiary':
   for x in [10,w-16]:b(x,30,12,16,'#c79b48');b(x,35,12,2,'dark');b(x+2,41,8,1,O)
  if kind in ['cheesemaker','loom']:b(7,30,w-2,12,'cream');b(13,32,8,6,'#c79b48' if kind=='cheesemaker' else 'coral')
 return im

def crop(kind,color,stage):
 im=Image.new('RGBA',(16,24));q=ImageDraw.Draw(im);q.rectangle((7,17-stage*3,8,22),fill='#687044');q.polygon([(7,19),(3,16-stage),(3,18-stage),(7,21)],fill='#a8b878')
 if stage>0:q.polygon([(8,18),(12,13-stage),(13,15-stage),(9,20)],fill='#87905d')
 if stage>1:
  if kind in ['milho','trigo']:q.rectangle((7,3,8,18),fill='#c79b48');[q.rectangle((4+(i%2)*4,4+i*2,7+(i%2)*4,5+i*2),fill='#e8c575')for i in range(5)]
  elif kind=='cenoura':q.polygon([(4,14),(12,14),(9,22),(7,23)],fill=color);q.line([(5,16),(9,16)],fill='#f3b471')
  elif kind in ['abobora','tomate','morango','nabo']:q.polygon([(4,14),(6,12),(11,12),(14,15),(13,21),(4,21),(2,18)],fill=color);q.line([(6,13),(6,20)],fill='#fff7e2' if kind=='nabo' else '#e9b88b');q.rectangle((7,10,9,13),fill='#687044')
  else:q.polygon([(2,17),(4,11),(7,13),(10,9),(13,14),(12,22),(4,22)],fill=color);q.rectangle((7,14,8,21),fill='#a8b878')
 if stage==3:q.point((13,5),fill=WHITE)
 return im

def build():
 m=json.loads((OUT/'atlas.json').read_text());wa=Atlas('world',(64,64),8);ba=Atlas('building',(160,128),4);ca=Atlas('crop',(16,24),16);m['world']={};m['buildings']={};m['crops']={}
 kinds=['tree','fruit_tree','rock','chair','rocking_chair','table','bench','workbench','water','trough','pond','lamp','flower','seedling','native_flower','mail','board','sign','upgrade','nest','catbed','platform','luggage','chest','bed','kitchen','gauge','sluice','filter','piece','glove','portrait']
 for k in kinds:
  m['world'][k]=[]
  for season in range(4 if k in ['tree','fruit_tree'] else 1):m['world'][k].append(wa.add(f'world.{k}.{season}',prop(k,season),[32,63]))
 dims={'house':(112,96),'shop':(96,96),'workshop':(128,80),'atelier':(96,80),'clinic':(128,80),'kitchen':(112,80),'nursery':(112,80),'coop':(96,80),'stable':(112,80),'pigpen':(112,80),'stall':(112,80),'rabbit_hutch':(80,80),'apiary':(64,64),'cheesemaker':(32,32),'loom':(32,32)}
 for k,(w,h) in dims.items():m['buildings'][k]=ba.add('building.'+k,building(k,w,h),[6,h+14])
 colors={'nabo':'#eee1db','cenoura':'#ee8a3a','abobora':'#c79b48','morango':'#cc7060','milho':'#c79b48','tomate':'#a94f3c','trigo':'#c79b48','espinafre':'#687044','couve':'#356f69'}
 for k,c in colors.items():m['crops'][k]=[ca.add(f'crop.{k}.{i}',crop(k,c,i),[8,23])for i in range(4)]
 for atlas in [wa,ba,ca]:m['frames'].update(atlas.map);m['atlases'][atlas.name]=atlas.write()
 (OUT/'atlas.json').write_text(json.dumps(m,separators=(',',':')))
 sample=Image.new('RGBA',(8*128,4*128),'#e9dfc3')
 for i,k in enumerate(kinds):sample.alpha_composite(prop(k).resize((128,128),Image.Resampling.NEAREST),((i%8)*128,(i//8)*128))
 sample.save(OUT/'preview-world.png');print(json.dumps(m['atlases'],indent=2))
if __name__=='__main__':build()
