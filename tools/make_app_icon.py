#!/usr/bin/env python3
"""Render Android launcher assets from the game's original pixel sprites."""
from pathlib import Path
from PIL import Image,ImageDraw
import json
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'assets/atlas.json').read_text())
human=Image.open(root/'assets/human.png').convert('RGBA')
base=Image.new('RGBA',(512,512),'#356f69')
d=ImageDraw.Draw(base)
for y in range(0,512,32):
 color='#527d76' if y<190 else '#687044' if y<350 else '#497f92'
 d.rectangle((0,y,512,y+31),fill=color)
for x in range(0,512,48):d.rectangle((x,346+(x//48%3)*7,x+20,359+(x//48%3)*7),fill='#c79b48')
d.rectangle((0,405,512,438),fill='#93c8ce');d.rectangle((0,438,512,512),fill='#356f69')
foreground=Image.new('RGBA',(512,512))
for uid,x in [('player',134),('rainara',250)]:
 key=manifest['actors'][uid]['idle']['down'][0]
 f=manifest['frames'][key]
 sprite=human.crop((f['x'],f['y'],f['x']+f['w'],f['y']+f['h'])).resize((128,192),Image.Resampling.NEAREST)
 foreground.alpha_composite(sprite,(x,160))
base.alpha_composite(foreground)
for name,size in [('mdpi',48),('hdpi',72),('xhdpi',96),('xxhdpi',144),('xxxhdpi',192)]:
 folder=root/'android/app/src/main/res'/('mipmap-'+name)
 icon=base.resize((size,size),Image.Resampling.NEAREST)
 icon.save(folder/'ic_launcher.png')
 round_icon=icon.copy();mask=Image.new('L',(size,size));ImageDraw.Draw(mask).ellipse((0,0,size-1,size-1),fill=255);round_icon.putalpha(mask);round_icon.save(folder/'ic_launcher_round.png')
 fg=foreground.resize((size*108//48,size*108//48),Image.Resampling.NEAREST)
 fg.save(folder/'ic_launcher_foreground.png')
base.save(root/'design/app-icon.png')
print('Android launcher icon generated from player and Rainara sprites')
