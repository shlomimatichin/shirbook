# Illustrated-book consistency research and workflow

Researched 2026-11-19. Applies to this project's Comfy Desktop hosted `gpt-image-2` workflow. No Chapter 2 art generated in this research pass.

## Evidence and limitations

1. [OpenAI image prompting](https://developers.openai.com/api/docs/guides/image-prompting): recommends reusable character references for illustrated books, defining appearance/proportions/outfit and repeating defining details across scenes. Its sketch-to-render and targeted-edit examples support separating composition from final appearance. Current page also covers newer models; do not assume every example is specific to GPT Image 2.
2. [OpenAI image generation](https://developers.openai.com/api/docs/guides/image-generation): recurring-character consistency and precise placement remain limitations. GPT Image 2 processes references at high fidelity automatically; do not add unsupported `input_fidelity` tuning. Masks guide edits rather than guaranteeing a mathematically locked boundary. These facts rule out promising zero corrections.
3. [Official Comfy GPT Image 2 guide](https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-2): documents reference editing and multiple outputs. Its strong preservation claims are not an acceptance test; our door retries visibly changed geometry. Multiple independent API nodes in one workflow do not share scene memory. A batch count is not a proven connected multi-page story context. Verify installed node capabilities before using newer documentation examples.
4. [Brie's Lazy Character Control Suite, creator's community workflow](https://www.reddit.com/r/StableDiffusion/comments/1ol0a4h/bries_lazy_character_control_suite/): author separates character sheet, posed dummy and scene, then places/scales/rotates the dummy before rendering. This is firsthand Qwen/LoRA workflow evidence, NOT a GPT Image guarantee. Transfer the blocking principle, not its model-specific controls or success claims.
5. [Community discussion on book consistency](https://www.reddit.com/r/generativeAI/comments/1xoa85x/how_do_i_create_a_consistent_character_consistent/): practitioners discuss reference roles and loss of facial detail in crowded sheets. Anecdotal, not a controlled benchmark. Use separate high-resolution identity crops alongside a simple scale plate; do not rely on one overloaded collage.

## Installed-node findings
Inspected local `comfy_api_nodes/nodes_openai.py` on 2026-11-19. Existing workflows use `OpenAIGPTImage1` with model `gpt-image-2`. Its implementation sends image batches as separate image inputs, downsizes each to a pixel budget, and rejects a mask with multiple reference images. A same-size mask plus ONE edit target is supported. This means multi-reference scene creation and masked local repair are separate stages in this installation. No credentials were read. Seed fields alone do not establish character or geometric identity. ControlNet/IP-Adapter/LoRA recipes for local diffusion models cannot simply be connected to this hosted node.

## Project workflow (our synthesis, not vendor guarantees)

### Before the next art generation
- Preserve the no-art hold until owner authorizes Chapter 2 art. Prepare only written specifications now.
- Create one SHARED scale plate when authorized: Shir and hatchling on the same ground line, same depth, neutral side/front views, feet fully visible, no perspective enlargement. Add the egg and sandal as scale anchors. Keep the hatchling large enough to inspect; use separate detail crops for identity rather than shrinking the whole cast into a crowded sheet.
- Retain individual canonical Shir and hatchling references. Use only hatchling stage for Chapter 2, never all four dragon ages as a scene input. Later growth requires an explicit stage change and new joint plate with the SAME Shir scale.
- Establish interaction references: hatchling beside ankle, front paws resting on sandal with hind feet on ground, seated beside foot with partial contact, cradled in arms if later story calls for it. No full dragon balanced inside/on top of one shoe at current dimensions.
- Establish normal/camouflaged matched-pose reference pair. Same silhouette, scale, anatomy, markings placement; colour/contrast change only. No transparent ghost body. Camouflage is contextual blending, not automatic invisibility in every environment.
- Environment references: door closed/open from each side plus simple top-down hinge/swing diagram and figure position. Inspect geometry BEFORE accepting the sheet; generated sheets can themselves contradict physics.

### Scale lock
Existing drawing convention: Shir 130 cm; hatchling shoulder 18 cm (0.138 of Shir height), torso length excluding tail 30 cm (0.231 of Shir height). These are production conventions, not Shir's measured height. Shoulder height is not head height. Tail length/head height remain to be resolved from canonical hatchling design before creating scale plates; do not invent contradictory numbers per page.

Compare ratios only when subjects stand at similar depth on the same plane. For close-ups, seated poses or different depths, use a blocking reference/camera layout, not raw image bounding-box ratios. Proposed QA tolerance for comparable side-on neutral views: roughly ±10% around approved ratios, then visual judgment; this is a project check, not an AI guarantee. Never resize the dragon to fit a prop or text area. Revise pose/camera instead.

### Per-page production
1. Write a shot ledger: page, action, camera side/distance, character stage, scale reference, emotional/camouflage state, supporting feet/hands, background/door state, text band and controls band. Resolve ambiguous prose before rendering.
2. Prepare a rough composition/blocking image with deliberate subject sizes, ground contacts and perspective. Use simple 3D/blockout geometry for doors or difficult contact, not repeated verbal guesses. Any art/blockout creation waits for authorization.
3. Supply only relevant references, explicitly labelled by role: identity, shared scale, composition, style, environment. Do not feed a gate reference to unrelated garden shots. Do not assume files in a project folder are automatically passed to the model; confirm actual wired inputs.
4. Test three difficult pilots FIRST: sandal contact, fire reaction with both characters, camouflage matched to leaves. Review identity, size, paws/wings/tail, contact and page readability before a full chapter batch. Low/medium exploratory quality can reduce cost, but final-quality pilot must validate the intended look; a new high-quality render still needs checking.
5. Use the approved canonical pack afresh for each scene; avoid long edit chains that accumulate drift. Lock model/version, aspect, style paragraph, colour palette and reference IDs. Do not auto-upgrade models because docs list a newer option; compare on the same pilots if changing models.
6. Make small batches (2–3 pages), inspect at full resolution AND adjacent contact sheet AND phone reading size. Pass technical/story geometry before subjective polish. Record chosen/rejected versions honestly.
7. For an isolated defect, use one-target masked/local repair where supported. Verify unchanged areas afterward. After two unsuccessful attempts at the SAME geometric defect, stop blind retries: rebuild blocking or simplify composition, then retry. This is a change of method, not a demand for additional user permission.
8. Staging review remains mandatory before main publication; user explicitly approves the staged version. Keep published chapter assets isolated from staging so draft edits cannot silently alter released chapters.

## Chapter 2 prose/pose issue
Accepted lines “He climbs onto my sandal” and “He sits on my sandal” can incorrectly imply a shoe-sized dragon. Preserve accepted prose in chapter2.md for now; propose “He puts his little feet on my sandal” / “He sits with one foot on my sandal” before art. If unchanged, show PARTIAL contact with the rest of his body supported by ground. The story beat is attachment/obstruction, not miniaturization.

## What this improves
Shared scale + explicit blocking + early hard pilots should catch errors before expensive full-page production. References improve consistency but cannot guarantee it; human/agent visual checks remain essential. Previous mistakes came from accepting attractive images without checking geometry, not merely from weak prompt adjectives.
