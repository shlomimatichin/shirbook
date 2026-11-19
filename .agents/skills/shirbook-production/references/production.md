# Editorial and visual production

## Reading

Use concrete everyday words, short active sentences, clear referents and repeated useful vocabulary. Start with present-tense narration unless the story needs otherwise. One visible action or emotional beat per page. Let the picture explain unfamiliar nouns; avoid idioms, long clauses and dense description. Read aloud at a beginner's pace. Aim for a small handful of sentences, often 5–7 lines; allow fewer on a dramatic page and more when comfortable. Do not use automated word counts as a substitute for editorial judgment. At 320–430px wide and enlarged text, wrapping must remain readable without clipping.

Plan 12–20 pages as a beat sheet before illustration. For each page record text, action, setting, characters and age stage, wardrobe, props, composition and continuity from adjacent pages. The first chapter is being drafted collaboratively in `chapters/chapter1.md`; finish the copy with the owner before illustration.

## Art bible

Proposed direction: premium digital drawing with expressive contours, layered gouache-like brushwork, restrained paper texture, luminous light and clear silhouettes. Teal/moss, apricot, warm cream and midnight blue. Intentional edges and quiet areas; no plastic 3D finish. Proposal remains editable until reviewed.

Shir: BLUE eyes, brown hair in a high topknot at the scalp apex, its tallest point (not over the forehead and not behind the head), pink patterned fabric sport sandals with black connectors, black soles and adjustable toe/ankle/heel straps. These are explicit owner corrections; do not infer brown eyes from photos or reuse sneakers. For future missing-reference requests, request 3–5 clear photos (front, three-quarter, profile, and optionally full-body), ordinary clothes and natural light. Derive only visible appearance. First create a portrait and full-body drawing; have the user choose the likeness and costume. Then generate separate front, side, back and three-quarter views plus happy, curious, worried, determined and surprised expressions. Assemble a labeled sheet from reviewed drawings; don't assume a generated turnaround is geometrically consistent. Preserve age-appropriate proportions. Keep photos private.

Skitters: owner-approved identity is light turquoise scales (approximately #86DAD4), butter-yellow belly, apricot wing membranes, amber eyes, two rounded ivory horns and a small golden forehead star scale. Four legs plus two wings and one tail. The owner approved the four-stage design on 2026-11-18. Stage-specific references: hatchling with horn buds/winglets and oversized head; playful baby; lankier adolescent with larger wings; calm powerful adult with rideable shoulders. Produce each stage independently using the selected design as reference, then make front/side/three-quarter views. Add a true scale chart beside the same Shir silhouette; initial all-stage concept sheets may compress scale and are not scale references. Adult roughly small-car body size; exact dimensions are design choices to establish before riding scenes. Preserve markings as anatomy grows.

Cover proposal: Shir at a half-open garden gate at blue hour, warm secret light beyond, leafy framing, calm dark upper area for the title. No dragon, dragon silhouette or egg reveal. Until photos arrive, an environment study can establish palette and composition but is not a finished likeness cover. Typeset title separately in HTML/CSS for the website; create a composed export only when needed.

## Reference-driven scene workflow

1. Use the approved character portrait/full-body, correct Skitters stage, and one approved style keyframe. Reference images have explicit roles; avoid contradictory or excessive references.
2. Prompt the finished scene: subject and action, camera, environment, composition, light, palette, must-preserve identity and anatomical constraints. Reserve quiet upper space when text overlays; prefer a cream text panel above art for beginner reading.
3. Generate a small batch. Inspect at full resolution and phone size. Choose the strongest composition, not the most detailed image.
4. Fix local faults with targeted editing/inpainting while preserving accepted faces and poses. If identity drifts, return to canonical references. Upscaling cannot repair bad anatomy or composition.
5. Review across adjacent pages. Lock accepted art with a reference version, prompt/workflow and cost entry. Replacing canonical art requires consciously reviewing affected pages.

## Acceptance rubric

Reject: identity drift; wrong dragon stage; unexplained costume/prop changes; missing/extra limbs; merged fingers or wings; unreadable action; accidental lettering; unsettling faces; overbusy page; clipped subjects. Look for deliberate brushwork, balanced focal hierarchy, inviting mood, consistent lighting, enough visual variety and composition that supports the sentence being learned. Compare all four dragon stages together. Inspect cover at thumbnail size and on a phone.

## Web delivery

Keep text real HTML, not baked into illustrations. Use semantic headings, large touch targets, visible focus, good contrast, no forced animation, and a simple cover → chapters flow. A reader should have previous/next controls, page count and access back to chapters; keyboard navigation and local reading progress are useful when chapters exist. Don't add empty controls before content exists.

Serve responsive WebP/AVIF derivatives with dimensions to avoid layout shift; keep original masters private. Never crop a character's head to fill a fixed phone screen. Let small screens scroll; don't force everything into 100vh. Test 320, 390 and 430px widths, landscape, 200% text zoom, keyboard and broken-image fallback. Only `site/` goes to Pages.

Publish no real photos, EXIF location, session credentials or arbitrary ComfyUI metadata. Gitignore is a guard, not proof: inspect the staged list and image metadata. Keep rejected/generated drafts out of the release artifact. Initial publication waits for the cover and reference set, as requested. Chapter one may be Coming soon until written together. Release cadence is editorial, not an automatic publishing schedule.

## Before a full chapter

Create thumbnail storyboards and a color script; review all pages together for visual rhythm (wide / medium / close), continuity, repetitive compositions and text density. Run a small reference-consistency pilot before mass generation. Record corrections and failures in `work/qa-notes.md`. Use a clean approved reference pack rather than feeding every prior image into the next request.

All byproducts belong under the project's ignored `work/` directory; personal source photographs belong in ignored `private/`. Archive ComfyUI task outputs into `work/raw/` and keep browser screenshots, scripts, logs and contact sheets under `work/`. App-managed temporary input/output copies are working transport only, not the canonical archive. Do not leave task byproducts scattered across chat directories.

## Learned from this production
Before selecting identity photos, inspect the whole collection and compare promising images at full resolution. Document each selected image’s role and limitation. Favor clear recent face views; add complementary hairstyle and body views. Do not repeatedly repair a weak initial likeness or use a generic generated face as identity truth. First obtain one faithful likeness pilot, then expand to expressions and turnarounds. Owner corrections override ambiguous photographic color or inferred appearance.

## Current canonical references
Use `art/references/shir-reference.webp` for Shir; `skitters-hatchling.webp`, `skitters-baby.webp`, `skitters-adolescent.webp`, or `skitters-adult.webp` for the correct dragon age. Full paths are under `art/references/` at the repository root. The lineup compresses growth scale; use `art/scale-guide.md` for scale targets.

When repeated edits cling to an incorrect feature, stop repeating the prompt. Crop identity references to exclude that feature, supply a separate structure guide, then compare another available model. In this production, GPT Image 2 corrected forward bun placement that repeated Nano Banana Pro edits did not. This is one observed task result, not a universal model ranking. Retain the successful workflow and QA against the original face.

## Book interaction
Owner requires the site to feel like a book: a fitted leaf, cover-to-contents page-turn animation and explicit page controls, not a long scrolling webpage. Respect reduced motion. Keep normal phone layouts to one leaf; internal overflow is an accessibility fallback for enlarged text. The current first release has only a Chapter 1 Coming soon entry.

## Edge-to-edge art and control safe area
Owner requested cover and story pages to use the screen without exterior margins. The chapter index is the exception and remains framed. Mark cover/story sections `data-layout="art"`; use the shared `.page-art` image treatment and the existing page controls. Keep page-turn navigation.

Reserve the **bottom 7% of every illustration** for overlay buttons: no faces, feet, hands, essential props, lettering or other important details there. Show only expendable background in that band. Account for device safe-area insets and minimum 44px touch targets on short screens; these can require a slightly taller control area. Keep reading text as HTML above the art.

For tall phones, art fills the viewport with central horizontal cropping; keep critical action away from lateral edges and test the crop. On wide screens, preserve the full figure and extend the illustration background to fill the sides rather than cropping heads/feet or adding beige margins. The current cover uses a softly blurred artwork backdrop. Future pages should supply the corresponding page's background, never the cover's.

## Urban gate and stable turns — latest owner direction
The owner likes the gate cover and requests a modern Israeli urban neighborhood: tall apartment buildings, a modern building facade around the inexplicable old gate, ordinary pavement in front, and a secret garden only beyond the opening. Preserve approved Shir proportions, likeness, wardrobe and bun. Workflow: `art/workflows/urban-gate.json`; prompt: `art/briefs/urban-gate.txt`.

Keep the animation stage full viewport at all times. Size the contents leaf independently inside it; changing the active layout may change control colors, never leaf or stage geometry. This prevents the end-of-turn jump between framed and edge-to-edge layouts.

Final urban cover uses `urban-safe.json` after the initial urban edit; it adds clear pavement below the sandals for controls. Clean master and responsive site assets replace the previous garden-exterior cover. Both raw passes are archived in ignored `work/raw/`.

## Continuing editorial voice and backpack correction

Use occasional gentle, character-driven humor like Shir’s “Well… happy birthday to me” when the door will not open. Do not force a joke on every page. Include believable nine-year-old emotional conflicts in simple language: curiosity versus danger, wanting independence versus needing help, and worries about being late or keeping a promise. Chapter 1 combines danger and lateness without a lecture.

Shir’s backpack is mostly pink with a KPop Demon Hunters print showing the three HUNTR/X girls, superseding yellow. Existing reference and cover need a narrow backpack-only edit AFTER copy is finished. Preserve all other approved visual features. Other people do not notice the door; do not assert invisibility or a birthday activation rule. Why it is special for Shir remains unresolved. Chapter 1 ends “Then the egg moves.”

Backpack continuity means consistent construction and perspective, not showing the print in every image. When Shir faces camera, show side/straps only; rear artwork is occluded. Check side-profile head scale separately from front/rear in reference sheets.

## Owner feedback: proportions and backpack perspective

- Check Shir’s head-to-body proportion independently in EVERY reference view. The middle side-profile head was too large even when front/rear were acceptable. Correct the head locally; keep bun at scalp apex and preserve recognizable face.
- A consistent backpack does not mean visible HUNTR/X artwork in every shot. The print exists ONLY on its broad outer rear panel. Preserve bag construction, color, straps and panel placement across views.
- When Shir’s chest/belly faces camera, the backpack is behind her torso: show straps and at most a narrow plain-pink side/pocket. The printed back panel faces away and must be occluded. Do not swivel, flatten or wrap that panel around the side to advertise the print.
- When Shir’s back faces camera, the rear print may be visible; head turning back does not change torso/bag orientation.
- Cover and first egg pilot both incorrectly showed a printed rear panel with a front-facing torso. Reject this geometry and correct it before release. Use these as explicit regression checks, not visual references to imitate.
- Inspect spatial storytelling too: farewell must read as leaving home toward school, with Dad inside; garden discovery should direct Shir’s attention into the garden. Keep bottom control band free of feet and important objects.
- Prompt reference roles precisely. A reference sheet defines identity and object construction, not a requirement to expose every identifying feature in every scene. Check occlusion before accepting output.

Door continuity: owner selects COVER proportions as canonical for Shir relative to doorway and door width/height. Page12 initial reveal made her too small and gate too wide. Match cover geometry across all door scenes, independent of framing or pose; never enlarge doorway to manufacture text/control space.

## Chapter release approval — owner-required gate

1. Develop chapter text and art; commit coherent checkpoints periodically.
2. Deploy the chapter to `site/staging.html` and verify the live staging reader, including all text, art, page navigation and phone layout. Clearly label drafts and missing illustrations.
3. Send the owner the live staging URL and identify the version/commit for review.
4. Publish a chapter in the main book ONLY after the owner explicitly approves publication of that staged version. Earlier text approval, approval of individual images, generation authorization, credit purchases, or requests to push commits do not constitute chapter release approval.
5. Material changes to chapter content or art after approval require staging and renewed owner release approval. Keep the main book placeholder until the gate is satisfied.

Routine commits, pushes and staging deployments remain authorized and do not require repeated permission. This owner instruction supersedes earlier “publish when ready” wording. Current Chapter 1 is NOT approved for publication.

## Reference leakage learned during Chapter 1
Do not supply the gate environment as a visual reference for home, ordinary-street or garden-interior shots: it can introduce the secret gate before its reveal or repeat the threshold in unrelated scenes. Use identity-only references for these shots and describe their distinct location explicitly. For a correct composition with a local wardrobe error, prefer a narrow edit of that image; broad regeneration can change door geometry, expression and text space. Inspect the actual rendered page with HTML text on a small phone; add a subtle local text backing where the illustration lacks sufficient contrast.

## Persistent environment continuity
Treat recurring locations/props like characters: generate a canonical multi-view door sheet before scene batches. Lock hinge axis, free edge, paired handles, inward/outward swing, wall fixtures, dimensions and camera side. A garden reverse shot must reverse physical handedness, not copy the street facade. Track open/closed state across pages and match hand contact to the actual free edge. Check adjacent page pairs for action chronology, adult/child scale and consistent object dimensions. See `art/chapter1/continuity-review.md` for the owner-requested correction pass.
