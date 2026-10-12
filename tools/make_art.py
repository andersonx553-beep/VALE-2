#!/usr/bin/env python3
"""Autoria raster de sprites em coordenadas inteiras. As pranchas não são recortadas.
As silhuetas, cabelos, roupas e expressões abaixo seguem os conceitos em design/arte.
Pillow é uma ferramenta de produção; o HTML final usa somente Canvas e PNG inline.
"""
from pathlib import Path
from PIL import Image,ImageDraw
import json,math
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'assets';OUT.mkdir(exist_ok=True)
O='#251b17';WHITE='#fff7e2';BOOT='#68462a'
PEOPLE={
'player':dict(skin='#d59a69',light='#efbb87',hair='#292324',hairlight='#514442',cloth='#f5e8cf',shade='#c6b68f',pants='#39333b',style='jacket',head='split'),
'rainara':dict(skin='#c88b5e',light='#e9b88b',hair='#4a2c1d',hairlight='#805133',cloth='#cc7060',shade='#a94f3c',pants='#a94f3c',style='skirt',head='waves'),
'marta':dict(skin='#cc9064',light='#efbd91',hair='#aca09a',hairlight='#dbd1bd',cloth='#cc7060',shade='#944746',pants='#73393c',style='apron',head='bun'),
'tiao':dict(skin='#ad7048',light='#d59a69',hair='#b6ada0',hairlight='#e3d5bc',cloth='#527d9b',shade='#355169',pants='#687044',style='shirt',head='hat'),
'luna':dict(skin='#74442e',light='#b87548',hair='#32251f',hairlight='#5e4030',cloth='#f5e8cf',shade='#b5a788',pants='#9270a1',style='overalls',head='curls'),
'celina':dict(skin='#74442e',light='#ad7048',hair='#33231d',hairlight='#654631',cloth='#356f69',shade='#234e4a',pants='#76593e',style='vest',head='braids'),
'augusto':dict(skin='#b87548',light='#d59a69',hair='#76695f',hairlight='#b7a996',cloth='#a94f3c',shade='#71372c',pants='#504c49',style='work',head='beard'),
'iara':dict(skin='#b87548',light='#e9b88b',hair='#49301f',hairlight='#80553a',cloth='#c79b48',shade='#977330',pants='#687044',style='apron',head='braid')}
DIRS=['down','up','left','right'];STATES={'idle':2,'walk':6,'talk':2,'run':6,'hoe':6,'water':6,'axe':6,'fish':6,'plant':6,'harvest':6,'pet':4,'note':4,'wave':4,'feed':6,'sit':2}

def human(who,direction,state,frame):
 c=PEOPLE[who];im=Image.new('RGBA',(32,48));q=ImageDraw.Draw(im);phase=[0,1,2,0,-1,-2][frame%6];walk=state in ['walk','run'];bob=-1 if walk and frame%3 else 0
 def poly(points,color,outline=O):q.polygon([(x,y+bob)for x,y in points],fill=color);q.line([(x,y+bob)for x,y in points]+[(points[0][0],points[0][1]+bob)],fill=outline,width=1)
 def box(x,y,w,h,color):q.rectangle((x,y+bob,x+w-1,y+bob+h-1),fill=color)
 def dots(points,color):
  for x,y in points:q.point((x,y+bob),fill=color)
 side=direction in ['left','right'];back=direction=='up';sign=-1 if direction=='left' else 1;hx=16+(-2 if direction=='left' else 2 if direction=='right' else 0)
 # Hair behind shoulders: each character has its own silhouette.
 if c['head']=='waves':
  poly([(12,5),(21,5),(25,7),(28,11),(27,17),(29,21),(27,24),(30,28),(27,32),(28,36),(24,40),(21,38),(10,39),(6,40),(3,36),(5,32),(2,28),(5,24),(3,20),(4,14),(6,9)],c['hair'])
  for x,y in [(6,15),(24,14),(5,25),(25,24),(7,33),(24,33)]:box(x,y,3,2,c['hairlight']);box(x+1,y+2,2,2,'#624029')
 elif c['head'] in ['braid','braids']:
  poly([(8,7),(23,6),(27,12),(26,23),(24,28),(25,35),(22,40),(18,36),(19,25),(7,27),(5,20),(5,13)],c['hair'])
  braidx=6 if c['head']=='braid' else 24
  for y in range(22,39,4):box(braidx,y,4,3,c['hairlight']);box(braidx+1,y+2,3,2,c['hair'])
 # Boots/legs are separate pixel poses, not translations of a static sprite.
 leg=phase if walk else 0
 for x,dy in [(10,leg),(19,-leg)]:
  box(x,37,4,7,c['pants']);box(x,42+dy//2,5,4,BOOT);box(x-1,45+dy//2,7,2,O);box(x,43+dy//2,3,1,'#a07949')
 # Distinct clothing and arm silhouettes.
 if c['style'] in ['skirt','apron']:
  wide=2 if who=='marta' else 0
  poly([(10-wide,25),(22+wide,25),(24,30),(26+wide,39),(22,42),(9,42),(6-wide,39),(8,30)],c['pants'])
  for x in [10,16,22]:box(x,34,2,6,c['shade'] if who=='rainara' else '#a27b68' if who=='iara' else '#944746')
  poly([(9,25),(22,25),(24,29),(21,33),(10,33),(7,29)],c['cloth'])
  if c['style']=='apron':
   poly([(11,26),(21,26),(22,39),(10,39)],'#eee1bf' if who=='iara' else '#73393c')
   box(12,34,4,3,'#687044' if who=='iara' else '#bd8865');box(18,34,3,3,'#c79b48')
 else:
  poly([(10,25),(22,25),(24,30),(21,37),(10,37),(8,30)],c['cloth'])
  if c['style']=='jacket':box(14,25,5,12,WHITE);box(11,28,2,7,c['shade']);box(20,28,2,7,c['shade']);box(13,27,1,10,O);box(19,27,1,10,O)
  if c['style']=='overalls':box(12,28,9,9,c['pants']);box(11,25,2,7,c['pants']);box(20,25,2,7,c['pants']);box(15,31,4,3,'#b498bc')
  if c['style']=='vest':box(14,25,4,11,WHITE);box(10,29,3,5,c['shade']);box(20,28,3,6,c['shade']);box(10,30,2,1,'#8aa699')
  if c['style']=='work':box(10,27,13,12,c['pants']);box(12,25,2,6,'#a07949');box(20,25,2,6,'#a07949');box(10,36,14,2,'#967145')
  box(10,37,12,1,O)
 if who=='augusto':
  for x in [8,10,23]:box(x,28,2,2,'#df9370');box(x,32,2,2,'#71372c')
 # Sleeves and hands. Action poses actually extend toward the subject.
 reach=state in ['hoe','water','axe','plant','harvest','feed','pet','note','wave','fish'];motion=phase if walk else 0
 for x,dy in [(6,motion),(23,-motion)]:
  box(x,27+dy,4,6,c['cloth']);box(x,32+dy,4,4,c['skin']);box(x+1,33+dy,2,2,c['light']);dots([(x,32+dy),(x+3,35+dy)],O)
 if reach:
  contact=math.sin(frame/max(1,STATES[state]-1)*math.pi)
  yy=29-int(contact*7) if state in ['wave','hoe','axe'] else 31+int(contact*3)
  xx=6 if direction=='left' else 23 if direction=='right' else 9 if back else 21
  box(xx,yy,5,4,c['skin']);box(xx+1,yy,3,2,c['light'])
  if state=='note':box(20,29,7,8,'#e1cea2');box(21,30,5,1,'#687044');box(21,33,4,1,'#967145')
  if state=='feed':box(23,33,4,5,'#687044');box(24,34,2,1,'#c3cc81')
 if who=='rainara':
  bagx=5 if back else 23 if not side else 21 if direction=='left' else 23
  box(bagx-1,27,2,10,'#404c30');box(bagx-2,34,7,7,'#687044');box(bagx-1,35,5,4,'#87905d');box(bagx,36,3,1,'#b3bc81');box(10,33,13,2,'#4a3824');box(16,33,2,2,'#d6bb76')
 if who=='celina':box(22,33,7,6,'#637347');box(24,34,1,3,WHITE);box(23,35,3,1,WHITE)
 if who=='luna':box(24,31,6,9,'#efdfba');box(25,33,4,1,'#687044');box(25,36,3,1,'#9270a1')
 if who=='tiao':box(9,36,14,2,'#4d452c');box(15,36,2,2,'#d1b876')
 # Neck, head, and brows.
 box(hx-3,23,7,5,c['skin']);box(hx-2,24,5,2,c['light'])
 if not back:
  face=[(hx-7,10),(hx+6,10),(hx+9,13),(hx+9,21),(hx+5,25),(hx-4,25),(hx-8,22),(hx-9,15)] if not side else [(hx-6,10),(hx+6,10),(hx+7,20),(hx+5,24),(hx-4,24),(hx-8,20),(hx-8,14)]
  poly(face,c['skin']);poly([(hx-5,12),(hx+5,12),(hx+7,15),(hx+6,21),(hx+3,24),(hx-3,24),(hx-6,20)],c['light'],c['light'])
  box(hx-10,16,3,4,c['skin']);box(hx+8,16,3,4,c['skin'])
  eyeXs=[hx-6,hx+3] if not side else [hx-6 if sign<0 else hx+3]
  for ex in eyeXs:
   if state=='idle' and frame==1 or state=='talk' and frame==1:
    box(ex,18,5,1,O);box(ex,17,1,1,O)
   else:
    box(ex+1,16,3,6,O);box(ex,17,5,4,O);box(ex+1,17,3,4,'#593922');box(ex+1,17,1,3,WHITE);box(ex+3,17,1,1,WHITE);box(ex+2,20,2,1,'#95663b')
   box(ex,14,5,1,c['hair'])
  box(hx-1,22,2,1,'#b2794d');box(hx-1,24,3,1,'#995d47')
  if c['head']=='beard':poly([(hx-6,22),(hx+6,22),(hx+5,26),(hx,28),(hx-5,26)],c['hair']);box(hx-4,22,8,2,c['hairlight']);box(hx-1,24,2,1,O)
  if who=='tiao':box(hx-5,22,11,2,'#d3c6b0');box(hx-3,24,7,1,c['hair']);box(hx-1,23,3,1,O)
  if who=='marta':
   for ex in eyeXs:q.rectangle((ex-1,15+bob,ex+5,22+bob),outline='#76533b');box(hx-1,18,3,1,'#76533b')
 # Hair crown, deliberately unique shapes.
 if back:
  poly([(7,10),(10,6),(16,4),(23,6),(27,11),(27,21),(23,25),(9,25),(5,21),(5,14)],c['hair']);box(9,8,6,2,c['hairlight']);box(20,11,3,7,c['hairlight'])
 elif c['head']=='split':
  poly([(6,13),(6,9),(9,9),(10,5),(14,5),(15,7),(17,5),(22,5),(25,9),(27,9),(27,17),(23,16),(21,10),(18,14),(16,17),(14,16),(13,10),(10,13),(8,17),(6,17)],c['hair']);box(9,8,5,2,c['hairlight']);box(19,8,4,2,c['hairlight']);box(17,11,2,2,c['hairlight'])
 elif c['head']=='curls':
  poly([(4,13),(4,9),(7,9),(7,6),(11,6),(13,4),(17,5),(21,4),(24,7),(28,8),(29,12),(27,14),(28,17),(25,18),(23,13),(19,12),(17,14),(14,11),(11,13),(8,17),(5,17)],c['hair']);box(8,8,3,2,c['hairlight']);box(19,7,3,2,c['hairlight']);box(24,11,2,2,c['hairlight'])
 elif c['head']=='bun':
  poly([(6,14),(6,10),(10,7),(22,7),(27,12),(26,17),(23,13),(19,10),(14,13),(8,15)],c['hair']);poly([(12,6),(12,3),(15,1),(20,2),(23,5),(21,8)],c['hair']);box(14,3,5,2,c['hairlight']);box(9,10,6,2,c['hairlight'])
 else:
  poly([(5,15),(6,10),(10,7),(17,5),(23,7),(27,11),(26,17),(23,15),(21,11),(16,10),(12,13),(8,16)],c['hair']);box(10,8,5,2,c['hairlight']);box(21,10,3,2,c['hairlight'])
 if c['head']=='hat':poly([(2,11),(6,8),(9,7),(10,3),(22,3),(24,7),(28,9),(30,12),(26,14),(6,14)],'#c79b48');box(11,5,10,2,'#e9c779');box(8,9,17,2,'#967145');box(5,12,22,1,'#e9c779')
 # Asymmetric accessories are drawn for each direction, never mirrored.
 if who=='rainara':
  ax=7 if back else 24 if direction=='down' else 12 if direction=='left' else 24
  box(ax,10,2,5,'#687044');box(ax-2,9,3,2,'#87905d');box(ax+1,12,3,2,'#a8b878');dots([(ax,10),(ax+2,13)],'#c4d599')
 if who=='luna':box(25 if not back else 7,12,3,3,'#c79b48');box(26 if not back else 8,13,1,1,WHITE)
 if state=='sit':
  # Compress the lower pose by moving actual knee/boot pixels onto the seat.
  cut=im.crop((0,35,32,48));im.paste((0,0,0,0),(0,35,32,48));im.alpha_composite(cut,(0,31));
 return im

def portrait(who,expression):
 # Portraits are authored from the same head, then expression pixels are changed.
 face=human(who,'down','idle',0).crop((1,0,31,28)).resize((90,84),Image.Resampling.NEAREST)
 im=Image.new('RGBA',(96,96));im.alpha_composite(face,(3,5));q=ImageDraw.Draw(im)
 # Repaint eye zones on a logical portrait grid so expressions are real poses.
 c=PEOPLE[who]
 def r(x,y,w,h,col):q.rectangle((x*3+3,y*3+5,(x+w)*3+2,(y+h)*3+4),fill=col)
 if expression=='joy':
  for x in [9,18]:r(x,16,5,6,c['light']);r(x,18,5,1,O);r(x+1,17,3,1,O)
  r(13,23,6,2,'#7c4335');r(14,23,4,1,WHITE)
 elif expression in ['worry','determination']:
  for x in [9,18]:r(x,14,5,2,c['light']);r(x,15 if expression=='worry' else 14,4,1,c['hair']);r(x+3,14 if expression=='worry' else 15,2,1,c['hair'])
  r(13,24,5,1,'#995d47');r(14,23 if expression=='worry' else 25,3,1,'#995d47')
 elif expression=='curiosity':r(15,23,2,3,'#995d47');r(17,25,5,2,c['skin'])
 elif expression=='affection':
  r(18,16,5,6,c['light']);r(18,18,5,1,O);r(19,17,3,1,O);r(7,22,3,1,'#cc7060');r(22,22,3,1,'#cc7060')
 return im

class Atlas:
 def __init__(self,name,cell,columns):self.name=name;self.cell=cell;self.columns=columns;self.frames=[];self.map={}
 def add(self,key,im,anchor):
  assert im.mode=='RGBA';idx=len(self.frames);w,h=self.cell;x=(idx%self.columns)*(w+2)+1;y=(idx//self.columns)*(h+2)+1
  f={'atlas':self.name,'x':x,'y':y,'w':im.width,'h':im.height,'anchor':anchor};self.frames.append((im,x,y));self.map[key]=f;return key
 def write(self):
  w,h=self.cell;rows=math.ceil(len(self.frames)/self.columns);canvas=Image.new('RGBA',((w+2)*self.columns,(h+2)*rows));
  for im,x,y in self.frames:canvas.alpha_composite(im,(x,y))
  canvas.save(OUT/(self.name+'.png'),optimize=True);return {'width':canvas.width,'height':canvas.height,'bytes_rgba':canvas.width*canvas.height*4,'frames':len(self.frames)}

def build():
 humanAtlas=Atlas('human',(32,48),24);portraits=Atlas('portrait',(96,96),8);manifest={'frames':{},'actors':{},'portraits':{},'atlases':{},'directions':DIRS,'status':'authored_raster_production'}
 for who in PEOPLE:
  manifest['actors'][who]={}
  for state,count in STATES.items():
   manifest['actors'][who][state]={}
   for direction in DIRS:
    keys=[]
    for f in range(count):keys.append(humanAtlas.add(f'{who}.{state}.{direction}.{f}',human(who,direction,state,f),[16,47]))
    manifest['actors'][who][state][direction]=keys
  manifest['portraits'][who]={}
  for expression in ['calm','joy','curiosity','worry','determination','affection']:manifest['portraits'][who][expression]=portraits.add(f'{who}.portrait.{expression}',portrait(who,expression),[48,96])
 for atlas in [humanAtlas,portraits]:manifest['frames'].update(atlas.map);manifest['atlases'][atlas.name]=atlas.write()
 (OUT/'atlas.json').write_text(json.dumps(manifest,separators=(',',':')))
 sample=Image.new('RGBA',(8*96,160),'#e9dfc3')
 for i,who in enumerate(PEOPLE):sample.alpha_composite(human(who,'down','idle',0).resize((96,144),Image.Resampling.NEAREST),(i*96,8))
 sample.save(OUT/'preview-cast.png')
 print(json.dumps(manifest['atlases'],indent=2))
if __name__=='__main__':build()
