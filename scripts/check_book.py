#!/usr/bin/env python3
"""Validate static assets, chapter scope and release readiness without dependencies."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.ids=set();self.images=[];self.chapters=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        if tag=='article' and 'chapter-card' in a.get('class','').split():self.chapters+=1
        for key in ('src','href'):
            if a.get(key):self.links.append(a[key])
        if a.get('srcset'):
            self.links.extend(v.strip().split()[0] for v in a['srcset'].split(','))
        if tag=='img':self.images.append(a)

parser=argparse.ArgumentParser();parser.add_argument('--release',action='store_true');args=parser.parse_args()
errors=[]
for path in SITE.rglob('*.html'):
    page=Page();page.feed(path.read_text())
    for link in page.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        target=(path.parent/unquote(u.path)).resolve() if u.path else path
        if not target.is_relative_to(SITE.resolve()):errors.append(f'Asset outside site: {link}')
        elif not target.is_file():errors.append(f'Missing asset: {link}')
        if not u.path and u.fragment and u.fragment not in page.ids:errors.append(f'Missing anchor: {link}')
    for img in page.images:
        if not all(img.get(k) for k in ('alt','width','height')):errors.append(f'Image missing alt/dimensions in {path.name}')
    if path.name=='index.html' and page.chapters!=1:errors.append('Launch must show exactly one chapter card.')
for f in SITE.rglob('*'):
    if f.is_symlink():errors.append(f'Symlink in public artifact: {f.name}')
    elif f.is_file() and f.suffix.lower() not in ('.html','.css','.js','.webp','.avif','.svg','.ico',''):
        errors.append(f'Unexpected public artifact: {f.relative_to(ROOT)}')
if args.release:
    for name,item in json.loads((ROOT/'art/status.json').read_text()).items():
        if not item['approved'] or not item.get('path') or not (ROOT/item['path']).is_file():
            errors.append(f'Not release-ready: {name}')
if errors:raise SystemExit('\n'.join(errors))
print('Book checks passed.'+(' Release assets ready.' if args.release else ' Draft checks only.'))
