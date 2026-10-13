#!/usr/bin/env python3
from make_art import Atlas,OUT,O,WHITE
from make_world import crop
from PIL import Image,ImageDraw
import json
CROPS={'nabo':'#eee1db','cenoura':'#ee8a3a','abobora':'#c79b48','morango':'#cc7060','tomate':'#a94f3c','milho':'#c79b48','trigo':'#c79b48','espinafre':'#687044'}
KEYS=list(CROPS)+['s'+str(i)for i in range(8)]+['lambari','carpa','bagre','truta','tilapia','dourado','peixe_gelo','peixe','madeira','pedra','racao','water','ovo','leite','leite_cabra','la','ovo_pato','composto','raiz','pelo_escovado','mel','queijo','queijo_cabra','tecido','erva','sopa','peixe_assado','torta','omelete','pao_milho','pao_mel','ensopado','cha','muda_flor','escova','tesoura','almofada','fruta','isca_simples','hoe','wateringcan','seed','bag','journal','axe','rod','coin','calendar','rain','sun','snow','dialogue','heart','task','food','clean','lantern']
def icon(k):
 im=Image.new('RGBA',(24,24));q=ImageDraw.Draw(im)
 def b(x,y,w,h,c):q.rectangle((x,y,x+w-1,y+h-1),fill=c)
 def p(pts,c):q.polygon(pts,fill=c);q.line(pts+[pts[0]],fill=O)
 if k in CROPS:im.alpha_composite(crop(k,CROPS[k],3),(4,0));return im
 if k.startswith('s') and k[1:].isdigit() or k=='seed':p([(6,6),(17,6),(18,19),(5,19)],'#e1cea2');b(7,8,9,2,'#687044');b(9,12,5,4,list(CROPS.values())[int(k[1:])%8]if k!='seed'else'#87905d')
 elif k in ['lambari','carpa','bagre','truta','tilapia','dourado','peixe_gelo','peixe','peixe_assado']:
  colors=['#93c8ce','#c79b48','#849089','#527d9b','#356f69','#e8c575','#dae3d8','#527d9b','#b87548'];color=colors[['lambari','carpa','bagre','truta','tilapia','dourado','peixe_gelo','peixe','peixe_assado'].index(k)];p([(5,12),(7,7),(13,5),(18,8),(19,12),(16,17),(7,17)],color);p([(5,12),(2,8),(2,16)],color);b(16,9,2,2,O);b(8,9,4,2,WHITE)
 elif k in ['ovo','ovo_pato']:p([(9,5),(14,4),(17,9),(19,15),(16,19),(8,19),(5,15),(6,9)],'#f5e8cf'if k=='ovo'else'#e1cea2');b(9,7,2,5,WHITE)
 elif k in ['leite','leite_cabra','water','wateringcan']:p([(7,7),(16,7),(18,11),(18,19),(6,19),(6,11)],'#527d9b'if k in ['water','wateringcan']else'#e1cea2');b(9,4,5,4,'#849089');b(9,10,6,6,'#93c8ce'if k in ['water','wateringcan']else WHITE);b(10,12,3,2,'#cc7060'if k=='leite_cabra'else'#356f69')
 elif k in ['la','pelo_escovado']:p([(5,9),(9,5),(16,6),(19,11),(18,17),(13,20),(6,17)],'#e1cea2');b(7,10,9,1,WHITE);b(8,14,8,1,'#967145')
 elif k in ['queijo','queijo_cabra']:p([(4,13),(16,6),(20,14),(18,19),(4,19)],'#c79b48'if k=='queijo'else'#e1cea2');b(8,14,2,2,'#a07949');b(15,12,2,2,'#a07949')
 elif k in ['sopa','ensopado','omelete','cha','food']:p([(3,10),(21,10),(19,18),(15,21),(8,21),(4,17)],'#e1cea2');b(5,11,14,3,'#c79b48'if k=='omelete'else'#687044'if k=='cha'else'#a94f3c');b(7,12,3,1,WHITE);b(9,4,1,3,'#849089');b(14,3,1,4,'#849089')
 elif k in ['pao_milho','pao_mel','torta']:p([(4,10),(7,6),(16,5),(20,10),(20,18),(4,18)],'#c79b48');b(7,8,2,7,'#e1cea2');b(12,7,2,7,'#e1cea2');b(17,9,1,5,'#e1cea2');b(5,17,14,2,'#68462a');
 elif k in ['madeira','axe','hoe','rod','escova','tesoura']:b(10,6,3,15,'#967145');b(11,8,1,10,'#e1cea2');p([(5,4),(17,4),(18,9),(5,9)],'#849089'if k in ['axe','hoe','tesoura']else'#68462a');b(7,5,9,1,'#c0d1ca');
 elif k=='pedra':p([(4,18),(4,12),(8,6),(14,5),(20,11),(21,18),(14,20)],'#849089');p([(6,12),(10,7),(15,8),(12,13)],'#c0d1ca')
 elif k in ['bag','journal','calendar','task','dialogue']:p([(4,6),(20,6),(20,19),(4,19)],'#cc7060'if k=='bag'else'#e1cea2');b(7,4,10,3,'#68462a');b(7,10,10,1,'#687044');b(7,14,8,1,'#967145');b(7,17,6,1,'#967145')
 elif k in ['coin','sun']:p([(9,3),(16,4),(20,9),(19,16),(14,21),(7,19),(3,13),(4,6)],'#c79b48');b(8,7,2,10,'#e8c575');b(10,7,5,2,'#e8c575')
 elif k=='heart':p([(3,7),(6,4),(10,5),(12,8),(15,4),(19,5),(21,9),(18,14),(12,20),(5,14)],'#cc7060');b(6,6,3,2,'#e9b88b')
 elif k in ['rain','snow']:p([(4,6),(9,4),(13,5),(17,4),(20,8),(19,11),(3,11)],'#c0d1ca');[b(x,14,2,3 if k=='rain'else 2,'#93c8ce'if k=='rain'else WHITE)for x in [5,11,17]]
 elif k in ['tecido','almofada']:p([(5,6),(19,6),(21,18),(5,20),(3,14)],'#9270a1');b(6,9,12,1,'#e1cea2');b(8,7,1,10,'#b6a1bf');b(6,17,12,1,'#68462a')
 elif k=='lantern':b(11,2,2,4,'#68462a');p([(6,5),(18,5),(19,17),(17,21),(7,21),(5,17)],'#c79b48');b(9,7,6,11,'#e8c575');b(11,7,2,11,WHITE)
 elif k in ['mel','clean']:p([(6,7),(17,7),(19,12),(17,20),(6,20),(4,12)],'#c79b48'if k=='mel'else'#356f69');b(6,5,11,3,'#68462a');b(8,10,7,6,'#e8c575'if k=='mel'else'#93c8ce')
 else:
  p([(4,16),(8,9),(16,8),(20,14),(17,20),(6,20)],'#967145'if k in ['composto','raiz']else'#687044');b(11,5,2,11,'#87905d');p([(11,9),(5,4),(5,8)],'#a8b878');p([(13,11),(20,5),(19,9)],'#a8b878')
  if k in ['muda_flor','fruta']:b(8,5,8,5,'#cc7060'if k=='muda_flor'else'#c79b48');b(11,6,2,2,'#e1cea2')
 return im

def build():
 m=json.loads((OUT/'atlas.json').read_text());a=Atlas('icon',(24,24),16);m['icons']={}
 for k in KEYS:m['icons'][k]=a.add('icon.'+k,icon(k),[12,23])
 m['frames'].update(a.map);m['atlases']['icon']=a.write();(OUT/'atlas.json').write_text(json.dumps(m,separators=(',',':')))
 sample=Image.new('RGBA',(16*48,5*48),'#e9dfc3')
 for i,k in enumerate(KEYS):sample.alpha_composite(icon(k).resize((48,48),Image.Resampling.NEAREST),(i%16*48,i//16*48))
 sample.save(OUT/'preview-icons.png')
if __name__=='__main__':build()
