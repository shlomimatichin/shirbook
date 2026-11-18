# Shir’s Secret

A mobile-first illustrated book for beginning English readers.

**Read:** https://shlomimatichin.github.io/shirbook/

The cover turns to a single contents page. Chapter 1 is **Coming soon**; it will be written with the owner before any story pages are published. Use the page controls or left/right arrow keys. The animation respects reduced-motion preferences.

## Agent handoff

Start with [HANDOFF.md](HANDOFF.md) for current design decisions, canonical assets, ComfyUI lessons, release steps and the next task.

## Production

- `site/` — the only directory deployed to GitHub Pages; plain HTML, CSS and JavaScript, no build dependencies.
- `art/references/` — clean canonical Shir, Skitters growth stages and cover artwork.
- `art/scale-guide.md` — growth and anatomy continuity targets.
- `.agents/skills/shirbook-production/` — researched art, beginner-English and release instructions.
- `art/workflows/` and `art/briefs/` — ComfyUI production recipes and prompts. Load the appropriate private source images into named input slots; recipes do not bundle personal photographs.
- `art/status.json` — release readiness with review provenance. Owner design approval and agent technical review are distinguished.

Shir’s latest design: blue eyes, honey/dark-blonde hair in a loose bun at the scalp apex, lilac shirt, dusty-rose shorts, yellow backpack, pink patterned sport sandals with black soles and toe/ankle/heel straps. Skitters is light turquoise, with a yellow belly, apricot wing undersides and a golden forehead star. No dragon appears on the cover.

## Preview and publish

```sh
python3 -m http.server 8080 --bind 127.0.0.1 --directory site
python3 scripts/check_book.py --release
node --check site/book.js
```

Push reviewed changes, then run the **Publish book** GitHub Actions workflow manually. Only `site/` is uploaded. Chapter releases are deliberate editorial actions, not a timer.

The reader has a fitted leaf and page-turn navigation. It is checked at 320, 390 and 430 CSS pixels and in landscape. Enlarged accessibility text may overflow inside a leaf rather than being clipped. Keep future chapter text in HTML above the art, with 12–20 pages per chapter and approachable English rather than rigid line counts.

## Private working files

Original photographs live in ignored `private/`. Generated masters, rejected studies, source-selection material, QA screenshots, scripts and cost records live in ignored `work/`. Never publish raw ComfyUI outputs: they can include workflow metadata. Public derivatives are exported without EXIF or generation metadata.

Generation uses the owner’s local ComfyUI app with hosted partner nodes. Nano Banana Pro established the illustration direction; GPT Image 2 handled the successful targeted hairstyle, proportion and wardrobe corrections. This is project-specific experience, not a general model ranking. The initial hosted budget ceiling is $25.
