#!/usr/bin/env python3
"""Build the public draft reader from approved copy and available clean art."""
from pathlib import Path
import hashlib,html,re
ROOT=Path(__file__).resolve().parents[1]
site=ROOT/'site';source=(ROOT/'chapters/chapter1.md').read_text();leaves=[]
for n in range(1,17):
    copy=source.split(f'## Page {n}\n',1)[1].split('\n## ',1)[0].split('\n---',1)[0].strip()
    copy=re.sub(r'\*(.*?)\*',r'<em>\1</em>',html.escape(copy)).replace('\n\n','\n').replace('\n','<br>')
    asset=site/f'assets/chapter1-{n:02d}.webp'
    if asset.exists():
        url=f'assets/{asset.name}?v={hashlib.sha256(asset.read_bytes()).hexdigest()[:10]}'
        art=f'<img src="{url}" width="960" height="1431" alt="Draft illustration for chapter 1 page {n}" loading="{ "eager" if n==1 else "lazy"}">'
        style=f' style="background-image:url({url})"';state='illustrated'
    else:
        art='<div class="placeholder">Illustration in progress</div>';style='';state='pending'
    leaves.append(f'<section class="leaf" id="page{n}" data-state="{state}"{style} {"" if n==1 else "hidden"}>{art}<div class="copy"><p>{copy}</p></div></section>')
css=hashlib.sha256((site/'preview.css').read_bytes()).hexdigest()[:10]
js=hashlib.sha256((site/'staging.js').read_bytes()).hexdigest()[:10]
(site/'staging.html').write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>Draft Chapter 1 — Shir’s Secret staging</title>'''+f'<link rel="stylesheet" href="preview.css?v={css}"><script src="staging.js?v={js}" defer></script>'+'''<style>.placeholder{position:absolute;inset:42% 10% 18%;display:grid;place-items:center;border:1px dashed #9f9a86;color:#747d6a;font-family:Georgia,serif;font-style:italic}header select{max-width:45vw;font:inherit;background:#fff9ed;color:inherit;border:1px solid #bdb6a5;border-radius:8px;padding:6px}.copy{top:max(68px,8%);max-height:30%;overflow:auto}header{align-items:center}#page8 .copy,#page13 .copy{background:#fff8eeed;border-radius:14px;padding:10px 12px;box-shadow:0 3px 18px #453b2520}</style></head><body><main aria-label="Draft chapter reader"><header><a href="index.html">← Published book</a><label>DRAFT <select aria-label="Draft chapter"><option>Chapter 1 · The Little Bell</option></select></label></header>'''+''.join(leaves)+'''<nav aria-label="Draft page navigation"><button id="prev" disabled>← Previous</button><span id="position" aria-live="polite">Page 1 of 16</span><button id="next">Next →</button></nav><p class="note" id="note">Draft chapter · awaiting owner release approval</p></main></body></html>''')
print('Built 16-page staging reader.')
