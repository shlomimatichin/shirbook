# Shir’s Secret — handoff

Updated 2026-11-18. Start here, then read `AGENTS.md` and `.agents/skills/shirbook-production/SKILL.md`.

## Current result

- Public repository: https://github.com/shlomimatichin/shirbook
- Live book: https://shlomimatichin.github.io/shirbook/
- Site is published and verified. It has a cover, animated turn to one contents leaf, and **Chapter 1 — Coming soon**. A 16-page collaborative text draft now exists in `chapters/chapter1.md`; it is not on the reading site.
- Latest art release: `cefa3c9`; Pages run `44351775977` succeeded. Live HTML and cover bytes matched the release.
- The owner is writing Chapter 1 **together** with the agent. Do not invent it or publish a chapter without that collaboration.

## Final character decisions

**Shir:** nine years old; recognizable cheerful smile; blue eyes; honey light-brown/dark-blonde hair; small loose bun at the **highest point of the scalp**. Not behind the head, and not over the forehead. Lilac T-shirt, dusty-rose shorts, mostly pink backpack with the three HUNTR/X girls from KPop Demon Hunters printed on it. Existing canonical art still has the superseded yellow bag; update the reference and cover after copy is finished.

The owner approved the balanced reference likeness/proportions with “ok, shir looks good”, then requested lighter hair, pink/rose rather than green shorts, and subsequently supplied a specific sandal photo. The newest changes were implemented and technically reviewed; do not describe them as a separate explicit owner approval.

**Current sandals:** pink patterned fabric sport sandals, pale-blue pattern flecks, black connectors/edging, black footbed and low rubber sole, adjustable toe and upper-foot/ankle straps, heel support. Match the canonical sheet. These supersede the earlier thin tan leather sandals. The product photo is private, not committed.

**Cover proportions:** owner said the head was still too big. Latest edit requests roughly 15% smaller head relative to unchanged body; visual QA confirms a visibly smaller head. Preserve this result rather than returning to an earlier large-head cover. A prompt percentage is not a pixel measurement.

**Skitters:** formerly named Zinger. Approved identity, subsequently changed to light turquoise. Yellow belly, apricot wing undersides, turquoise wing backs, amber eyes, ivory horns, golden star on forehead; four legs, two wings, one tail. Hatchling has tiny rounded horn buds. Four age stages have separate references. Adult body eventually becomes small-car sized so Shir can ride it. See `art/scale-guide.md`; the lineup compresses scale.

## Canonical assets — use these

- `art/references/shir-reference.webp` — latest three-view character sheet, including the exact sandal direction.
- `art/references/cover.webp` — latest clean cover master, smaller head and pink sport sandals.
- `art/references/skitters-hatchling.webp`
- `art/references/skitters-baby.webp`
- `art/references/skitters-adolescent.webp`
- `art/references/skitters-adult.webp`
- `art/references/skitters-lineup.webp` — identity overview, **not** a true scale chart.
- `art/status.json` — readiness and review provenance.

Do not use earlier raw portraits or sheets as identity references. The clean canonical artwork is sufficient for routine future illustrations; original photos are only needed when correcting likeness.

## Art workflow and lessons

Use the owner's **local Comfy Desktop app**, including authorized hosted partner nodes. Local app does not mean local inference. Do not extract session tokens. Run through the signed-in UI; save sanitized workflow JSON, prompts, reference roles and observed costs.

1. Write a specific shot brief: action, camera, composition, expression, wardrobe, stage, lighting, and text space. Assign each reference a clear role.
2. Use canonical drawings for identity, the appropriate single dragon stage, and explicit structure/style references when needed.
3. Generate a small candidate batch, inspect full size and phone size, then make narrow corrections.
4. Compare corrected assets with the originals for unintended face, proportion, hand, sandal, horn or wing changes. Check all three reference views, not only the first.
5. Export clean RGB WebP derivatives without EXIF, XMP or embedded workflow metadata. Keep text as HTML rather than baked into art.

Nano Banana Pro (`GeminiImage2Node`, model `gemini-3-pro-image-preview`, usually 2K) established the drawing style, dragon and cover composition. It repeatedly resisted bun repositioning, even with explicit prompts and a structure diagram. **GPT Image 2 (`OpenAIGPTImage1`, high quality) through ComfyUI succeeded** on targeted hair, head-size and wardrobe edits. This is observed project performance, not a general model ranking. Do not spend many retries on a failing model/feature pair.

For multi-reference edits, `LoadImage` nodes feed `BatchImagesNode`, then the image model and `SaveImage`. The latest recipe is `art/workflows/sport-sandals-proportions.json`; exact prompts are in `art/briefs/sport-sandals-proportions.txt`. Other retained recipes document the dragon/reference and cover-composition steps. Their input filenames are transport placeholders: replace them with the intended source images in the local Comfy input directory. The JSON does not contain the source photos.

In the setup used here, new images had to be placed in the **root** Comfy input folder; subfolders did not appear in LoadImage choices. Refresh the app after adding inputs, then open the saved workflow through the Workflows sidebar. Re-read current UI state; accessibility element IDs are not stable. Refresh the workflow list if a new JSON file is missing. Verify output files and visual quality, not just an empty queue.

The initial hosted budget was **$25 total**, not a recurring allowance. Detailed records are in ignored `work/session/cost-ledger.json`; some per-run costs were not captured, so do not claim an exact total. Official conversion verified on 2026-11-18: 211 credits per USD. Reference the linked source in the skill research notes and recheck current prices before new substantial spending.

## Reading and website decisions

- Beginner English; small approachable text blocks, generally above the art. The initial 5–7 lines was guidance, **not a hard numerical limit**.
- Each chapter: 12–20 pages. Build a beat sheet, thumbnails and color script before final illustration. Run consistency tests before generating a whole chapter.
- The website must **feel like a book**. Fitted leaves, page-turn animation and explicit controls; long scrolling is not primary navigation. Respect reduced motion. Internal overflow is an accessibility fallback for enlarged text.
- Cover title: **Shir’s Secret**. **No dragon, egg reveal or dragon silhouette on the cover.**
- Current implementation: plain HTML/CSS/JS, no build dependencies. Arrow keys and controls turn pages; focus moves to the new heading. Browser Back during a turn cancels the pending animation safely.

## Editing and release

Only `site/` deploys to Pages. Photos and intermediate files never belong there.

```sh
python3 scripts/check_book.py --release
node --check site/book.js
```

For UI changes, check 320/390/430 CSS-pixel widths, landscape, keyboard/focus, reduced motion and enlarged text. Previous checks found no ordinary phone-page scrolling or horizontal overflow; enlarged text can scroll inside the leaf. Reduced-motion code was reviewed without changing the owner's OS preference.

After replacing the cover, export 480/960/1600px WebPs and update the image version query in `site/index.html` so existing viewers receive the new art. Check image metadata and the staged file list. Commit and push reviewed changes, then manually run **Publish book** (`pages.yml`). Wait for success and verify the live assets. Publication and routine updates to this repository/site are already authorized; do not invent a new approval gate.

## Working files and next step

All byproducts stay under ignored `work/`; source photos/reference material under ignored `private/`. Comfy input/output copies are transport, not the canonical archive. Rejected workflows and prior sheets are in `work/archive/`. Raw generated masters are in `work/raw/`. QA evidence is in `work/qa/`. These are available in the owner's local checkout but intentionally absent from a fresh public clone.

The current creative task is to finish the 16-page Chapter 1 copy **with the owner**, then update the backpack in the Shir reference and cover before chapter illustration. Preserve the launch placeholder until that content and its illustrations are ready. No automatic chapter publishing schedule has been authorized.

## Edge-to-edge art and control safe area
Owner requested cover and story pages to use the screen without exterior margins. The chapter index is the exception and remains framed. Mark cover/story sections `data-layout="art"`; use the shared `.page-art` image treatment and the existing page controls. Keep page-turn navigation.

Reserve the **bottom 7% of every illustration** for overlay buttons: no faces, feet, hands, essential props, lettering or other important details there. Show only expendable background in that band. Account for device safe-area insets and minimum 44px touch targets on short screens; these can require a slightly taller control area. Keep reading text as HTML above the art.

For tall phones, art fills the viewport with central horizontal cropping; keep critical action away from lateral edges and test the crop. On wide screens, preserve the full figure and extend the illustration background to fill the sides rather than cropping heads/feet or adding beige margins. The current cover uses a softly blurred artwork backdrop. Future pages should supply the corresponding page's background, never the cover's.

## Urban gate and stable turns — latest owner direction
The owner likes the gate cover and requests a modern Israeli urban neighborhood: tall apartment buildings, a modern building facade around the inexplicable old gate, ordinary pavement in front, and a secret garden only beyond the opening. Preserve approved Shir proportions, likeness, wardrobe and bun. Workflow: `art/workflows/urban-gate.json`; prompt: `art/briefs/urban-gate.txt`.

Keep the animation stage full viewport at all times. Size the contents leaf independently inside it; changing the active layout may change control colors, never leaf or stage geometry. This prevents the end-of-turn jump between framed and edge-to-edge layouts.

Final urban cover uses `urban-safe.json` after the initial urban edit; it adds clear pavement below the sandals for controls. Clean master and responsive site assets replace the previous garden-exterior cover. Both raw passes are archived in ignored `work/raw/`.

## Chapter 1 copy — latest owner decisions

Draft: `chapters/chapter1.md`. Pink backpack, crosswalk instead of shop, door unnoticed by other people, birthday joke retained, danger plus being-late conflict, final line “Then the egg moves.” The door is special for Shir but its cause is unknown; do not make the birthday a confirmed trigger. Preserve gentle humor and age-nine emotional conflicts in future chapters. Owner explicitly says copy first, graphics afterward; the reference-sheet and cover backpack updates remain queued. Site remains Coming soon.

## Chapter art authorized
Owner approved Chapter 1 text and requested `chapters/chapter1.md`. Copy is now locked; begin backpack corrections and all 16 page illustrations. Publish when finished and verified. Prior copy-first hold is satisfied.

## Active generation session
Backpack jobs submitted through signed-in ComfyUI: Shirbook_Backpack_Reference running, Shirbook_Backpack_Cover queued. Hosted GPT Image 2 high. Server unusually slow (over 11 minutes, no error or output as of last check); do not resubmit blindly. Expected outputs in shared output/shirbook/Backpack_Reference* and Backpack_Cover*. Archive raw results to work/raw, inspect before replacing canonical assets. Three pilots prepared in art/workflows/ch01-page{02,12,16}-pilot.json and Comfy workflow list as Shirbook_Pilot_02/12/16. They require corrected images copied to shared input/shirbook_pink_reference.png and shirbook_pink_cover.png; not submitted yet. Scripts under work/session/backpack_workflow.py and pilot_workflows.py.

Recovery: cancelled stalled reference after ~38 minutes; local queue verified 0 running/0 pending. Cover surfaced Sign In Required to Use API Nodes. Comfy Desktop login screen opened; awaiting owner sign-in. No backpack outputs found, no pilots submitted. Do not treat prior queued jobs as active. Resume with backpack reference after authentication restored.

Recovery succeeded after owner signed in: backpack reference completed in 73s (45.02 credits), cover in 79s (76.69 credits). Both visually reviewed and installed as clean canonical assets; site cover derivatives updated locally. Three pilots 02/12/16 now submitted through ComfyUI. Owner requests periodic commits; checkpoint coherent reviewed changes, keep unfinished chapter off Pages.

Latest checkpoint: ComfyUI insufficient-credit dialog stopped pilot16; no output found. Page02/page12 drafts archived and saved in art/chapter1, not approved for release. Page02 exit correction workflow prepared in local ComfyUI list. Need fix page12 gaze/safe-area. Owner asked for periodic commits; checkpoint 04ea2e2 contains text/backpack corrections. Awaiting explicit $10 top-up authorization (skill disallows automatic purchase).

Owner feedback is now recorded in the production reference and chapter art plan: independently check middle-view head proportions, and enforce backpack panel visibility by torso/camera angle. Cover/egg are explicit negative examples. Targeted correction workflows prepared; reference correction queued. Owner authorized and purchased $25 top-up (5,275 credits); no recurring purchase authorization.

Latest selected samples: art/chapter1/page02.webp, page12.webp, page16.webp. All three generated and visually reviewed. Cover_Bag_Geometry and Reference_Head_Only installed as canonical; rejected Reference_Proportion shrank whole middle figure, archived only. Egg_Bag_Geometry fixes print visibility. User feedback retained in skill production reference. Hosted credit top-up $25 completed by explicit authorization. Remaining chapter art/integration not complete; no Pages deployment this session.

Owner requested a separate public draft reader: site/staging.html shows approved Chapter 1 copy for all 16 pages with available drafts at 2/12/16 and explicit illustration-pending placeholders elsewhere. Keep main index Coming soon until complete. Update staging as art develops; page12 scale correction pending to match cover.
