#!/usr/bin/env python3
from make_art import Atlas,OUT,O,WHITE
from PIL import Image,ImageDraw
import json
GRASS=[['#66a459','#5b994e'],['#8ba85b','#7e9b4e'],['#b49b5f','#a58a52'],['#d5e2de','#c8d8d4']]
def tile(kind,v=0,mask=0,frame=0):
 base=GRASS[int(kind[-1])][v%2] if kind.startswith('grass')else {'path':'#b69c6d','stone':'#bfae8b','sand':'#e1cea2','soil_dry':'#76593e','soil_wet':'#574130','snow':'#d5e2de','wood':'#bfae8b','water':'#497f92'}[kind];im=Image.new('RGBA',(16,16),base);q=ImageDraw.Draw(im)
 if kind.startswith('grass'):
  for x,y in [(3+v,9),(11,4+v)]:q.line([(x,y+2),(x,y),(x+1,y+3),(x+2,y+1)],fill='#eef4ec'if kind=='grass3'else'#4c7747'if kind!='grass2'else'#c79b48')
 elif kind=='water':
  q.line([(2+frame,6),(6+frame,6)],fill='#93c8ce');q.line([(9-frame,12),(13-frame,12)],fill='#639dad')
  for bit,box in [(1,(0,0,15,1)),(2,(14,0,15,15)),(4,(0,14,15,15)),(8,(0,0,1,15))]:
   if mask&bit:q.rectangle(box,fill='#c2ddd3')
 elif kind in ['soil_dry','soil_wet']:q.line([(1,4),(14,4)],fill='#68462a');q.line([(1,10),(14,10)],fill='#68462a');q.line([(0,0),(15,0)],fill='#4a3824')
 elif kind in ['stone','wood']:q.line([(0,14),(15,14)],fill='#967145');q.line([(7,0),(7,14)],fill='#a09173')
 else:q.point((3+v,5),fill='#967145');q.line([(10,12),(12,12)],fill='#c79b48')
 return im

def effect(kind,f):
 im=Image.new('RGBA',(16,16));q=ImageDraw.Draw(im);phase=f-1
 if kind=='heart':q.polygon([(5,6),(6,5),(8,6),(10,5),(11,6),(11,8),(8,11),(5,8)],fill='#cc7060');q.point((6,6),fill='#e9b88b')
 elif kind in ['leaf','harvest']:q.polygon([(5+phase,8),(7+phase,5),(10+phase,6),(9+phase,9),(6+phase,10)],fill='#a8b878'if kind=='leaf'else'#e8c575');q.line([(6+phase,9),(9+phase,6)],fill='#687044')
 elif kind=='water':q.line([(8,4+f),(6,8+f),(8,10+f),(10,8+f),(8,4+f)],fill='#93c8ce');q.point((8,7+f),fill='#c2ddd3')
 elif kind=='soil':q.rectangle((5+f,7,7+f,9),fill='#967145');q.point((10-f,5+f),fill='#68462a')
 elif kind=='smoke':q.polygon([(5,8),(6,5),(9,5),(11,8),(10,10),(6,11)],fill='#c0d1ca');q.point((7,6),fill='#dae3d8')
 elif kind=='rain':q.line([(8,5),(7,10)],fill='#93c8ce')
 elif kind=='snow':q.line([(5,8),(10,8)],fill=WHITE);q.line([(8,5),(8,10)],fill=WHITE)
 elif kind=='firefly':q.rectangle((7,7,8,8),fill='#e8c575'if f%2 else'#a8b878')
 elif kind=='footstep':q.rectangle((6,8,7,9),fill='#a09173');q.point((8,10),fill='#bfae8b')
 else:q.line([(4+f,7),(9+f,7)],fill='#93c8ce'if kind=='clear'else'#a09173');q.line([(7-f,10),(12-f,10)],fill='#497f92'if kind=='clear'else'#967145')
 return im

def build():
 m=json.loads((OUT/'atlas.json').read_text());a=Atlas('tile',(16,16),16);fx=Atlas('effect',(16,16),16);m['tiles']={};m['effects']={}
 for kind in ['grass0','grass1','grass2','grass3','path','stone','sand','soil_dry','soil_wet','snow','wood']:m['tiles'][kind]=[a.add(f'tile.{kind}.{v}',tile(kind,v),[0,0])for v in range(4)]
 m['tiles']['water']={str(mask):[a.add(f'tile.water.{mask}.{f}',tile('water',mask=mask,frame=f),[0,0])for f in range(4)]for mask in range(16)}
 for kind in ['heart','leaf','harvest','water','soil','smoke','rain','snow','firefly','footstep','clear','turbid']:m['effects'][kind]=[fx.add(f'effect.{kind}.{f}',effect(kind,f),[8,8])for f in range(4)]
 for atlas in [a,fx]:m['frames'].update(atlas.map);m['atlases'][atlas.name]=atlas.write()
 (OUT/'atlas.json').write_text(json.dumps(m,separators=(',',':')))
if __name__=='__main__':build()
