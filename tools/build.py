#!/usr/bin/env python3
"""Empacota o jogo e assets locais em um único HTML, sem dependências no navegador."""
from pathlib import Path
import base64,json
ROOT=Path(__file__).resolve().parents[1]
def build():
    source=(ROOT/'src/game.html').read_text()
    for name in ('historia','sistemas'):
        data=json.loads((ROOT/f'design/conteudo/{name}.json').read_text())
        source=source.replace(f'/*__{name.upper()}__*/',json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
    for marker,path in [('ASSET_DATA','assets/atlas.png'),('ASSET_MAP','assets/atlas.json')]:
        if f'/*__{marker}__*/' in source:
            data=json.dumps('data:image/png;base64,'+base64.b64encode((ROOT/path).read_bytes()).decode()) if marker=='ASSET_DATA' else (ROOT/path).read_text()
            source=source.replace(f'/*__{marker}__*/',data)
    if '/*__' in source: raise ValueError('Marcador não resolvido')
    (ROOT/'index.html').write_text(source)
    print(f'index.html: {len(source.encode()):,} bytes')
if __name__=='__main__':build()
