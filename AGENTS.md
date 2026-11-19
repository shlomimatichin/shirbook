# Shirbook

Start with `HANDOFF.md`, then read `.agents/skills/shirbook-production/SKILL.md` and its applicable references for art, writing and publishing. Use the local ComfyUI app, including authorized hosted nodes. Keep all byproducts in ignored `work/`, source photos in ignored `private/`. Never publish real photos or generation metadata.

## Current character direction

Shir: nine-year-old protagonist, blue eyes, recognizable happy smile, honey light-brown/dark-blonde loose topknot at the highest point of the scalp (not over the forehead), lilac T-shirt, dusty-rose shorts, mostly pink backpack with a KPop Demon Hunters print of the three HUNTR/X girls and pink patterned fabric sport sandals with black connectors, black soles and adjustable toe/ankle/heel straps. Owner accepted the revised smile direction. Canonical production sheet is `art/references/shir-reference.webp`; the forward-bun correction succeeded with GPT Image 2 in ComfyUI after Gemini repeatedly retained the old placement. Do not reuse the rejected rear-bun portraits.

Dragon name is **Skitters**, formerly Zinger. Owner approved its shape and accepted the light turquoise palette revision. Preserve ivory horns, yellow belly, apricot wing undersides, amber eyes, forehead star, four legs, two wings and one tail. Hatchling has tiny rounded horn buds. Use the stage-specific canonical sheet; growth scale targets are in `art/scale-guide.md`.

## Book and release

Title: **Shir's Secret**. No dragon on cover. Beginner English: small readable text blocks, usually above art; flexible line counts. Chapters 12–20 pages. Chapter 1 is being written with the owner in `chapters/chapter1.md`; finish the copy together before art and do not publish it prematurely. Launch contains cover → chapter selection → only Chapter 1, Coming soon.

Only `site/` is deployed to GitHub Pages. Validate with `python3 scripts/check_book.py --release`. Publish deliberate editorial updates, not scheduled unfinished content. The repository and Pages publication are already authorized. Do not invent further permission gates for routine implementation or QA. Record actual review provenance accurately in `art/status.json`.

Latest owner correction: in GPT sheet, left-view bun position is good but head appears too big; reduce left head about 10%. Side/rear buns are too far forward; place them at scalp apex. This supersedes earlier aggressive forward-over-forehead wording. Recheck cover against this correction.

Owner approved the balanced reference with “ok, shir looks good”. Use that sheet. Website must feel like a book: fitted leaves and turning animation; scrolling is not the primary navigation. Respect reduced motion and allow internal overflow only when accessibility text enlargement needs it.

Latest wardrobe correction is applied to both canonical reference and cover: hair lighter honey/dark blonde; dusty-rose shorts (not green); pink patterned fabric sport sandals with black connectors and black rubber soles, matching the owner-provided product photo. Preserve these consistently.

Latest owner footwear reference supersedes tan leather sandals: use pink patterned fabric sport sandals with black connectors and rubber soles, following private/sandal-reference.png. Apply consistently to cover and all reference views. Cover head reduced relative to unchanged body after owner review; preserve the corrected proportion.

Art layout update: cover and future reading pages are edge-to-edge (`data-layout="art"`), index remains framed. Bottom 7% of art is a control-safe band with no important details; allow device safe-area/touch-target minima. Preserve key content during responsive cropping.

Latest editorial direction: preserve occasional gentle humor and believable nine-year-old emotional conflicts. The 16-page Chapter 1 draft ends with “Then the egg moves.” The door is unnoticed by others; why it is special for Shir remains unknown. Backpack artwork still needs updating in both the canonical reference and cover, AFTER copy is finished; existing yellow-bag art is superseded on that detail only.

Latest owner review: middle side-profile reference head remains too large; reduce it relative to body while preserving scalp-apex bun. Cover must show only backpack side/straps with print occluded because Shir faces the viewer. Never force HUNTR/X print visible; respect bag geometry and occlusion in all art. Current pink reference/cover require these corrections.

## Chapter release approval — owner-required gate

1. Develop chapter text and art; commit coherent checkpoints periodically.
2. Deploy the chapter to `site/staging.html` and verify the live staging reader, including all text, art, page navigation and phone layout. Clearly label drafts and missing illustrations.
3. Send the owner the live staging URL and identify the version/commit for review.
4. Publish a chapter in the main book ONLY after the owner explicitly approves publication of that staged version. Earlier text approval, approval of individual images, generation authorization, credit purchases, or requests to push commits do not constitute chapter release approval.
5. Material changes to chapter content or art after approval require staging and renewed owner release approval. Keep the main book placeholder until the gate is satisfied.

Routine commits, pushes and staging deployments remain authorized and do not require repeated permission. This owner instruction supersedes earlier “publish when ready” wording. Current Chapter 1 is NOT approved for publication.

Latest release state (supersedes prior Chapter1 pending notes): owner approved staged 3c0bd32 for main publication on 2026-11-19. Chapter1 is now published with isolated assets; chapter2.md is saved text-only, with no art generation yet authorized. Use chapters/story-continuity.md and production skill references/consistency-workflow.md for subsequent chapters.
