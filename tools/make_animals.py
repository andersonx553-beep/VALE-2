#!/usr/bin/env python3
from pathlib import Path
from PIL import Image,ImageDraw
import json,math
from make_art import Atlas,O,ROOT,OUT,DIRS,WHITE
SPECIES={'chicken':('#dca35b','#f4d494',24,24),'cow':('#f5e8cf','#b99a70',48,40),'goat':('#b87548','#e9b88b',40,32),'sheep':('#f5e8cf','#c6b99b',40,32),'duck':('#f5e8cf','#c6cfb8',24,24),'pig':('#e6a184','#f2c4a3',40,32),'horse':('#a06b3c','#cd955c',48,40),'donkey':('#9b9485','#c5bdab',48,40),'rabbit':('#f5e8cf','#c6b99b',24,24),'bee':('#c79b48','#e9c779',24,24),'bento':('#b87548','#e9b88b',32,32),'amora':('#352c29','#eee3cc',32,32)}
STATES={'idle':2,'walk':6,'eat':4,'rest':2,'pet':4,'special':4}
def animal(kind,d,state,f,young=False):
 base,light,W,H=SPECIES[kind];im=Image.new('RGBA',(W,H));q=ImageDraw.Draw(im);side=d in ['left','right'];front=d=='down';back=d=='up';sign=-1 if d=='left'else 1;phase=[0,1,2,0,-1,-2][f%6] if state=='walk' else 0;eat=state=='eat' or state=='special' and kind in ['chicken','pig','rabbit','horse'];rest=state=='rest';cx=W//2;feet=H-2
 def poly(p,col):q.polygon(p,fill=col);q.line(p+[p[0]],fill=O,width=1)
 def box(x,y,w,h,col):q.rectangle((x,y,x+w-1,y+h-1),fill=col)
 def oval(b,col,outline=O):q.ellipse(b,fill=col,outline=outline,width=1)
 if kind=='bee':
  for i,(x,y)in enumerate([(5,9),(14,14),(16,6)]):
   oval((x-3,y-3,x+4,y+3),base);box(x,y-2,2,5,O);oval((x-3,y-7-(f%2),x,y-2),light);oval((x+1,y-7+(f%2),x+4,y-2),light);box(x+3,y-1,1,1,O)
  return im
 big=kind in ['cow','horse','donkey','goat','sheep','pig'];bodyW=int(W*.64)if big else int(W*.58);bodyH=int(H*.45)if big else int(H*.43);by=feet-bodyH-5+(3+f%2 if rest else 0)
 if side:oval((cx-bodyW//2-4,by,cx+bodyW//2-3,by+bodyH),base)
 else:oval((cx-bodyW//2,by-1,cx+bodyW//2,by+bodyH),base)
 # Pés e patas com poses alternadas.
 if not rest:
  xs=[cx-11,cx-5,cx+6,cx+12] if big and side else [cx-9,cx+3] if big else [cx-5,cx+3]
  for i,x in enumerate(xs):
   yy=feet-5+(phase if i%2==0 else -phase)//2;box(x,yy,3 if big else 2,5,base);box(x,feet+(phase if i%2==0 else -phase)//2,4 if big else 3,2,'#76593e'if kind in ['chicken','duck']else O)
 # Cauda: espécie e direção determinam a forma.
 if side:
  tx=cx-bodyW//2-5 if sign>0 else cx+bodyW//2
  if kind in ['bento','amora','horse','donkey']:poly([(tx,by+7),(tx-2*sign,by+3),(tx-2*sign,by),(tx+2*sign,by+3),(tx+3*sign,by+10)],'#49301f'if kind in ['horse','donkey']else base)
  if kind=='pig':oval((tx-2,by+4,tx+2,by+8),base);box(tx,by+5,1,2,O)
 if kind=='sheep':
  for x,y in [(cx-11,by+3),(cx-5,by),(cx+2,by),(cx+9,by+3),(cx-9,by+11),(cx-2,by+14),(cx+7,by+11)]:oval((x-4,y-3,x+4,y+4),light,light)
 if kind=='cow':
  poly([(cx-10,by+6),(cx-5,by+3),(cx-1,by+7),(cx-4,by+13),(cx-10,by+11)],'#68462a');poly([(cx+4,by+9),(cx+9,by+7),(cx+12,by+10),(cx+9,by+15),(cx+3,by+14)],'#967145')
 if kind=='duck':poly([(cx-5,by+5),(cx+3,by+4),(cx+6,by+8),(cx,by+12),(cx-5,by+10)],'#356f69')
 if kind=='pig':box(cx-7,by+12,4,2,'#b87548');box(cx+4,by+9,3,2,'#b87548')
 # Face expressive, with a stepped outline and eyes lit from the left.
 hw=14 if big else 12 if kind in ['bento','amora']else 10;hh=13 if big else 11;hx=cx+sign*(bodyW//2-2)if side else cx;hy=by-3+(3+(f%3) if eat else 0);hx=max(hw//2+1,min(W-hw//2-2,hx));hy=max(5,hy)
 if kind in ['rabbit','amora']:ears=[(hx-5,hy-8),(hx+3,hy-8)]
 elif kind in ['bento']:ears=[(hx-7,hy-1),(hx+5,hy-1)]
 else:ears=[(hx-6,hy-2),(hx+4,hy-2)]
 for i,(x,y)in enumerate(ears):
  if kind=='rabbit':poly([(x,y-1),(x+1,y-7),(x+3,y-8),(x+4,y),(x+2,y+3)],base);box(x+2,y-5,1,6,'#cc7060')
  elif kind=='amora':poly([(x,y+2),(x,y-4),(x+5,y+1)],base);box(x+2,y-1,1,2,'#cc7060')
  elif kind=='bento':poly([(x,y),(x-2,y+2),(x-2,y+9),(x+1,y+11),(x+4,y+8),(x+4,y+1)],'#967145')
  elif kind=='donkey':poly([(x,y+2),(x,y-7),(x+2,y-9),(x+4,y+2)],base);box(x+1,y-5,2,5,'#cc7060')
  elif kind in ['cow','goat']:poly([(x,y+2),(x-3,y),(x-2,y-2),(x+3,y-1),(x+4,y+2)],base);poly([(x+1,y-2),(x,y-6),(x+2,y-7),(x+3,y-2)],'#c6b99b')
  elif kind=='pig':poly([(x,y+2),(x-1,y-3),(x+4,y-2),(x+4,y+3)],base)
  elif kind=='horse':poly([(x,y+2),(x,y-3),(x+3,y-4),(x+4,y+2)],base)
 oval((hx-hw//2,hy,hx+hw//2,hy+hh),light if kind not in ['amora','sheep']else '#352c29')
 if kind=='horse':poly([(hx-6,hy+4),(hx-5,hy-2),(hx,hy-4),(hx+5,hy-1),(hx+4,hy+4),(hx+1,hy+2),(hx-2,hy+4)],'#49301f');box(hx,hy+2,2,4,WHITE)
 if kind=='donkey':box(hx-4,hy,8,2,'#49301f')
 if kind=='cow':poly([(hx-5,hy+2),(hx,hy-2),(hx+4,hy+1),(hx+2,hy+4),(hx-3,hy+5)],base)
 if kind in ['chicken']:poly([(hx-2,hy),(hx-2,hy-3),(hx,hy-4),(hx+1,hy-2),(hx+3,hy-3),(hx+3,hy+1)],'#cc7060')
 eyes=[hx-4,hx+2]if not side else [hx-4 if sign<0 else hx+2]
 if not back:
  for ex in eyes:
   if rest or state=='idle' and f==1:box(ex,hy+5,3,1,O)
   else:box(ex,hy+3,3,5,O);box(ex,hy+4,1,2,WHITE);box(ex+2,hy+6,1,1,'#68462a')
  if kind in ['cow','pig']:oval((hx-5,hy+8,hx+5,hy+13),'#cc8a75');box(hx-2,hy+10,1,1,O);box(hx+2,hy+10,1,1,O)
  elif kind in ['chicken','duck']:poly([(hx+sign*3,hy+8),(hx+sign*7,hy+9),(hx+sign*4,hy+11)],'#c79b48')
  else:box(hx-2,hy+9,4,2,O);box(hx,hy+11,1,2,'#68462a')
 if kind=='amora':poly([(hx-1,hy+7),(hx+4,hy+9),(hx+3,hy+12),(hx-2,hy+12)],WHITE);poly([(cx-3,by+6),(cx+3,by+6),(cx+4,by+12),(cx-3,by+15)],WHITE)
 if kind=='bento':poly([(hx-1,hy+1),(hx+2,hy+2),(hx+1,hy+8),(hx-2,hy+7)],WHITE);poly([(hx-6,hy+12),(hx+6,hy+12),(hx,hy+17)],'#527d9b')
 if kind=='cow':box(hx-1,hy+14,3,4,'#c79b48');box(hx,hy+15,1,1,WHITE)
 if state=='special' and kind=='duck':
  box(cx-7,feet-3,14,2,'#93c8ce');box(cx-4+f%3,feet-5,8,1,'#c2ddd3')
 if state=='special' and kind=='goat':
  box(cx-8,feet-6-f%2,4,6,base);box(cx+4,feet-8+f%2,4,4,base)
 if state=='special' and kind=='bento':
  box(2+f%3,by+3,3,6,base)
 if state=='special' and kind=='sheep':
  box(cx-5+f%3,by+5,8,3,'#fff7e2')
 if state=='pet':box(hx-6,hy+9,2,1,'#cc7060');box(hx+5,hy+9,2,1,'#cc7060')
 if young:im=im.resize((max(12,W//2),max(12,H//2)),Image.Resampling.NEAREST)
 return im

def build_animals():
 manifest=json.loads((OUT/'atlas.json').read_text());atlas=Atlas('animal',(48,40),24);manifest['animals']={};manifest['young']={}
 for kind in SPECIES:
  for young in [False,True]if kind not in ['bee','bento','amora']else [False]:
   target=manifest['young']if young else manifest['animals'];target[kind]={}
   for state,count in STATES.items():
    target[kind][state]={}
    for d in DIRS:
     target[kind][state][d]=[atlas.add(f'{kind}.{young}.{state}.{d}.{f}',animal(kind,d,state,f,young),[animal(kind,d,state,f,young).width//2,animal(kind,d,state,f,young).height-1])for f in range(count)]
 manifest['frames'].update(atlas.map);manifest['atlases']['animal']=atlas.write();(OUT/'atlas.json').write_text(json.dumps(manifest,separators=(',',':')))
 preview=Image.new('RGBA',(6*96,2*96),'#e9dfc3')
 for i,kind in enumerate(SPECIES):
  image=animal(kind,'down','idle',0);preview.alpha_composite(image.resize((image.width*2,image.height*2),Image.Resampling.NEAREST),(i%6*96+12,i//6*96+10))
 preview.save(OUT/'preview-animals.png');print('Animal atlas:',manifest['atlases']['animal'])
VARIANTS=[{'#dca35b':'#c89b74','#f4d494':'#f5e8cf','#a06b3c':'#805133','#cd955c':'#b87548','#b87548':'#9b6f52','#e9b88b':'#dba575','#9b9485':'#b3ab99','#c5bdab':'#ded6c4','#e6a184':'#cb9279','#f2c4a3':'#e8b79c'}, {'#dca35b':'#c79b48','#f4d494':'#e9c779','#a06b3c':'#68462a','#cd955c':'#a07949','#b87548':'#cc9064','#e9b88b':'#f0c79e','#9b9485':'#7f8680','#c5bdab':'#b8c0b8','#e6a184':'#e9b88b','#f2c4a3':'#f5d6b1','#f5e8cf':'#e9dfc3','#c6b99b':'#a9997d'}]
def recolor(im,palette):
 from PIL import ImageColor
 mapping={ImageColor.getrgb(a)+(255,):ImageColor.getrgb(b)+(255,)for a,b in palette.items()};out=im.copy();out.putdata([mapping.get(c,c)for c in (im.get_flattened_data() if hasattr(im,'get_flattened_data') else im.getdata())]);return out
def build_variants():
 manifest=json.loads((OUT/'atlas.json').read_text());adult=Atlas('animal_variant',(48,40),24);baby=Atlas('young_variant',(24,20),24);manifest['animal_variants']={};manifest['young_variants']={}
 for kind in SPECIES:
  if kind in ['bee','bento','amora']:continue
  for young,atlas,group in [(False,adult,'animal_variants'),(True,baby,'young_variants')]:
   manifest[group][kind]={}
   for v,palette in enumerate(VARIANTS,1):
    manifest[group][kind][str(v)]={}
    for state,count in STATES.items():
     manifest[group][kind][str(v)][state]={}
     for d in DIRS:
      frames=[]
      for f in range(count):
       im=recolor(animal(kind,d,state,f,young),palette);frames.append(atlas.add(f'{kind}.v{v}.{young}.{state}.{d}.{f}',im,[im.width//2,im.height-1]))
      manifest[group][kind][str(v)][state][d]=frames
 for atlas in [adult,baby]:manifest['frames'].update(atlas.map);manifest['atlases'][atlas.name]=atlas.write()
 (OUT/'atlas.json').write_text(json.dumps(manifest,separators=(',',':')))
if __name__=='__main__':build_animals();build_variants()
