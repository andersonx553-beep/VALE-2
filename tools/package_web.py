#!/usr/bin/env python3
"""Copy the reproducible single-file game to Capacitor's web directory."""
from pathlib import Path
from shutil import copy2
root=Path(__file__).resolve().parents[1]
web=root/'www'
web.mkdir(exist_ok=True)
copy2(root/'index.html',web/'index.html')
print(f'www/index.html: {(web/"index.html").stat().st_size:,} bytes')
