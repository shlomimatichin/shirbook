#!/usr/bin/env python3
"""Build draft readers from chapter Markdown and available clean illustration exports."""
from pathlib import Path
import hashlib,html,re
ROOT=Path(__file__).resolve().parents[1]
site=ROOT/'site'
chapters=[(1,'The Little Bell','staging.html'),(2,'I Am Not Your Mama!','staging-chapter2.html')]
for chapter,title,filename in chapters:
    source=(ROOT/f'chapters/chapter{chapter}.md').read_text()
    blocks=re.findall(r'^## Page (\d+)\n(.*?)(?=^## Page |^---|\Z)',source,re.M|re.S)
    assert [int(n) for n,_ in blocks]==list(range(1,17)),f'Chapter {chapter}: expected pages 1–16'
    leaves=[];illustrated=[]
    for number,text in blocks:
        n=int(number)
        copy=re.sub(r'\*(.*?)\*',r'<em>\1</em>',html.escape(text.strip())).replace('\n\n','\n').replace('\n','<br>')
        asset=site/f'assets/chapter{chapter}-{n:02d}.webp'
        if asset.exists():
            url=f'assets/{asset.name}?v={hashlib.sha256(asset.read_bytes()).hexdigest()[:10]}'
            art=f'<img src="{url}" width="960" height="1431" alt="Draft illustration for chapter {chapter} page {n}" loading="eager" decoding="async">'
            style=f' style="background-image:url({url})"';state='illustrated';illustrated.append(n)
        else:
            art='<div class="placeholder">Illustration in progress</div>';style='';state='pending'
        leaves.append(f'<section class="leaf" id="page{n}" aria-label="Page {n}" data-state="{state}"{style} {"" if n==1 else "hidden"}>{art}<div class="copy"><p>{copy}</p></div></section>')
    css=hashlib.sha256((site/'preview.css').read_bytes()).hexdigest()[:10]
    js=hashlib.sha256((site/'staging.js').read_bytes()).hexdigest()[:10]
    options=''.join(f'<option value="{file}" {"selected" if num==chapter else ""}>Chapter {num} · {html.escape(name)}</option>' for num,name,file in chapters)
    samples='<div class="sample-links" aria-label="Illustrated samples">Samples: '+ ' · '.join(f'<a href="#page{n}">Page {n}</a>' for n in illustrated)+'</div>' if chapter==2 else ''
    (site/filename).write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'''+f'<title>Draft Chapter {chapter} — Shir’s Secret staging</title><link rel="stylesheet" href="preview.css?v={css}"><script src="staging.js?v={js}" defer></script>'+'''<style>
.placeholder{position:absolute;inset:42% 10% 18%;display:grid;place-items:center;border:1px dashed #9f9a86;color:#747d6a;font-family:Georgia,serif;font-style:italic}
header select{max-width:51vw;font:inherit;background:#fff9ed;color:inherit;border:1px solid #bdb6a5;border-radius:8px;padding:6px;min-height:32px}
.copy{top:max(92px,9%);max-height:29%;overflow:auto}header{align-items:center;flex-wrap:wrap;row-gap:5px}.sample-links{width:100%;text-align:center;font-size:11px}.sample-links a{display:inline-block;padding:3px 6px;font-size:12px}
#page8 .copy,#page14 .copy{background:#fff8eeed;border-radius:14px;padding:10px 12px;box-shadow:0 3px 18px #453b2520}
@media(max-height:650px){.copy{font-size:16px;line-height:1.35}}
@media(max-height:500px){header{padding:5px 10px}.copy{top:76px;max-height:38%;font-size:17px}.note{bottom:54px}nav{bottom:5px}}
</style></head><body><main aria-label="Draft chapter reader"><header><a href="index.html">← Book</a><label>DRAFT <select id="chapter" aria-label="Draft chapter">'''+options+'</select></label>'+samples+'</header>'+''.join(leaves)+'''<nav aria-label="Draft page navigation"><button id="prev" disabled>← Previous</button><span id="position" aria-live="polite">Page 1 of 16</span><button id="next">Next →</button></nav><p class="note" id="note">Draft chapter · awaiting owner release approval</p></main></body></html>''')
    print(f'Built chapter {chapter}: {len(illustrated)} illustrations / 16 pages → {filename}')
