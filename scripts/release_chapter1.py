#!/usr/bin/env python3
"""Snapshot explicitly owner-approved Chapter 1, isolated from future staging edits."""
from pathlib import Path
import shutil,re,json
r=Path(__file__).resolve().parents[1];site=r/'site'
approval=json.loads((r/'chapters/chapter1-release.json').read_text())
assert approval['owner_approved'] and approval['staged_commit']=='3c0bd32'
s=(site/'staging.html').read_text()
assert s.count('data-state="illustrated"')==16
folder=site/'assets/published-chapter1';folder.mkdir(exist_ok=True)
for p in (site/'assets').glob('chapter1-*.webp'):shutil.copy2(p,folder/p.name)
s=s.replace('assets/chapter1-','assets/published-chapter1/chapter1-')
s=s.replace('<meta name="robots" content="noindex">','').replace('Draft Chapter 1 — Shir’s Secret staging','The Little Bell — Shir’s Secret').replace('Draft chapter reader','Chapter 1 reader').replace('Draft illustration','Illustration').replace('Draft page navigation','Page navigation')
s=re.sub(r'<header>.*?</header>','<header><a href="index.html#chapters">← Chapters</a><span>CHAPTER 1 · THE LITTLE BELL</span></header>',s)
s=re.sub(r'<p class="note" id="note">.*?</p>','',s)
s=re.sub(r'preview.css\?v=[a-z0-9]+','chapter1.css',s);s=re.sub(r'staging.js\?v=[a-z0-9]+','chapter1.js',s)
shutil.copy2(site/'preview.css',site/'chapter1.css')
js=(site/'staging.js').read_text();js=re.sub(r"document.querySelector\('#note'\)\.textContent=.*?;if\(push\)", 'if(push)',js)
(site/'chapter1.js').write_text(js);(site/'chapter1.html').write_text(s)
p=site/'index.html';s=p.read_text().replace('<p>The story is on its way.</p><span class="status">Coming soon</span>','<p>The Little Bell</p><a class="status" href="chapter1.html">Read Chapter 1 →</a>').replace('Chapter 1 is coming soon.','Read <a href="chapter1.html">Chapter 1</a>.');p.write_text(s)
print('Published Chapter 1 snapshot built.')
