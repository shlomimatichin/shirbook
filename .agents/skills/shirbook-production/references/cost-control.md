# Image production cost audit — 2026-11-19

## Findings from this project
Credit top-ups are prepaid balance, not chapter invoices. Comfy converts211credits/USD. Before Chapter2 batchA balance595; while running365; after explicitly authorized$25 purchase5640. Exact historical total cannot be reconstructed from incomplete per-node ledger; do not claim all purchased credit was spent on this book. Comfy balance can fund other workflows too. Full receipts are not archived.

Previous default was GPT Image2 high at1696x2528 (4.29MP), then downsampled to960x1431 (1.37MP). Multiple reference, cover, door and framing retries multiply cost. High output resolution did not prevent geometry mistakes. This default was unnecessarily expensive for unreviewed mobile-first drafts.

Installed nodes_openai.py preset estimates for1024x1536 output: GPT Image2 low$0.0057, medium$0.0494, high$0.1976. Four image inputs estimated another$0.0392–0.0588 total, plus text. These are estimates, not observed invoices. At medium this suggests about$0.09–0.12 per attempted page;16 first passes roughly$1.5–2, before retries. High at previous custom resolution has observed node charges around77–90credits ($0.36–0.43). One-pass16page illustration cost roughly$6–7, not$50; repeated design/refinement contributes substantially.

## Official documentation
- [Comfy credit conversion](https://support.comfy.org/articles/1982697177-partner-nodes-pricing):211credits=$1, shared paid-feature balance.
- [Comfy partner pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing): Seedream4.5 8.44credits/image (~$0.04); FLUX2pro charges output and reference megapixels; adding many large references is not free. Confirm live node quote and installed model before selecting.
- [OpenAI image generation](https://developers.openai.com/api/docs/guides/image-generation): GPT Image2 supports low/medium/high, explicit dimensions, reference inputs always high fidelity. Quality and size affect output cost. Cached image rates do not apply to direct Images API edits; repeated references are not automatically free. Existing Comfy node exposes quality, not reasoning_effort.
- [Google pricing](https://ai.google.dev/gemini-api/docs/pricing): Nano Banana2 developer API output$0.067 at1K,$0.101 at2K plus inputs; these are direct-provider rates, not guaranteed Comfy charges. Batch discount is a separate asynchronous API product, NOT several nodes running together.

## Community evidence (firsthand anecdotes, not controlled guarantees)
- [GPT Image2 quality comparison](https://www.reddit.com/r/nightcafe/comments/1tk0ff5/gpt_2_low_vs_medium_vs_high_comparison/): same-prompt low/medium/high comparison; useful method, platform-specific economics.
- [GPT2.5 API experiments](https://www.reddit.com/r/comfyui/comments/1whzw2s/gpt_image_25_api_in_practice_the_five_settings/): author reports quality-dependent timings; supports testing settings rather than assuming maximum always necessary. Not evidence for our character likeness.
- [Storybook maker's SDXL workflow](https://www.reddit.com/r/StableDiffusion/comments/1av02st/six_months_ago_i_quit_my_job_to_work_on_a_small/): reusable style/character LoRAs, pose controls, selective compositing and2xupscaling. Older workflow; hardware rental prices are historical. Training/local models entail setup and QA and do not guarantee Shir/Skitters consistency.

## Adopted production policy
1. Default first attempt GPT Image2 medium1024x1536, one candidate per page. Validate first batch at phone/export size against approved references before extending.
2. Keep accepted medium render as final if it meets identity/anatomy/scale/layout/style requirements. Do not automatically regenerate high after approval: rerender can change geometry.
3. High quality or larger master only for a demonstrated defect, cover/print need, or failed medium comparison. Low is for rough composition only after a trial; do not assume identity detail survives.
4. Match delivered resolution first.1024x1536 already exceeds current960x1431 website export; no upscale needed for phone delivery. For future print, test conservative non-generative upscaling on accepted master. Generative upscalers can alter faces/scales; never use them as anatomy repair.
5. Keep necessary identity/shared-scale references. Avoid redundant full sheets; crop/select relevant views only after checking preservation. Cost per ACCEPTED page includes retries, inputs and finishing.
6. Benchmark cheaper model on one existing hard scene (sandal contact or camouflage), not all pages. Seedream/FLUX/Nano Banana are candidates; previous Nano Banana bun corrections failed, so price alone cannot justify switching.
7. Track actual node charge when available, estimated vs observed separately, all rejected attempts, and topups separately. Report batch and chapter usage, never imply a topup equals chapter cost.
8. After two failed fixes of one defect, change blocking/method instead of blind reruns. Preserve accepted artwork and correct only the fault.

Current Chapter2 batchesB–E changed to medium1024x1536. BatchA finished under prior high setting; page1 backpack print and page2/3 framing/scale require QA before selection. Main release remains unapproved.

Additional official source: [Comfy upscaling tutorial](https://docs.comfy.org/tutorials/basic/upscale) documents model-based ESRGAN upscaling and recommends comparing models by image type. This is an option for future print masters, not necessary for current mobile exports.

First medium batchB completed in34.87seconds per UI job, versus batchA99.49seconds. Images5/6/7 inspected and retained for staging QA; no formal same-scene A/B has been completed, so do not claim equivalent quality or an exact savings percentage. Balance afterB5381credits; earlier595→365 was a pending reservation, not final cost. Use settled per-job receipts for future exact accounting.
