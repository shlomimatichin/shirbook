# Research and model choice

Researched 2026-11-18. Distinguish documented capability from tested project quality. No blind rankings.

## Primary sources

- [ComfyUI workflow concepts](https://docs.comfy.org/basic-concepts/workflow): reusable JSON node graphs, dependencies and saved generation workflows.
- [BFL multi-reference guide](https://help.bfl.ai/articles/6546682167-what-is-multi-reference-editing): combine identity/style references; reference limits differ by model and endpoint.
- [FLUX.2 official repository](https://github.com/black-forest-labs/flux2): Klein supports local multi-reference editing; 4B uses Apache 2.0, 9B and dev have different licenses. Published GPU timings are not Apple MPS timings.
- [FLUX.2 Klein official ComfyUI guide](https://docs.comfy.org/tutorials/flux/flux-2-klein): compact local generation and reference editing. Suitable baseline to benchmark on a memory-constrained Mac, not a promise of final illustration quality.
- [FLUX.3 Klein official ComfyUI guide](https://docs.comfy.org/tutorials/flux/flux-3-klein.md): newer local candidate; documented minimum ComfyUI 0.41.0 and gated model downloads. Explicit indexed references; quantized model compatibility must be tested on MPS.
- [Qwen Image Edit 2511](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit-2511): documented identity and multi-person consistency improvements; a candidate for controlled illustration edits.
- [ComfyUI tutorial index](https://docs.comfy.org/_llms/en/tutorials.txt): discover current official workflows rather than following stale community setup instructions. Includes Qwen Image 2.1 and newer candidates; presence in an index is not a local compatibility test.
- [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages): deploy only the `site/` artifact with Pages permissions and the github-pages environment.

## Observed local setup

Apple M5, 24 GB unified RAM; Comfy Desktop 1.1.7, running local API at http://127.0.0.1:8188. `system_stats` reports ComfyUI 0.35.1 while the Desktop title displays 0.45.6: use actual API/node capabilities for compatibility, not the title. No checkpoint, diffusion or text-encoder weights are installed in the currently exposed loaders. Existing workflows must be preserved.

Available partner nodes include Nano Banana Pro (`GeminiImage2Node`), Nano Banana 2, FLUX.2 and Qwen. Nano Banana Pro accepts up to 14 batched image references per node documentation. Its installed price badge quotes approximately $0.1608 at 1K/2K and $0.288 at 4K; Nano Banana 2 quotes $0.1217 at 2K. These are estimates, not billing receipts. Recheck before use.

## Proposed selection method

Hosted Nano Banana Pro at 2K is the initial illustration candidate because it is already available through the user's ComfyUI and supports multiple image references. This is a practical starting choice, not a measured superiority claim. Compare it with another available high-quality model only if the initial output fails the rubric; use the same brief and canonical references. Judge drawing quality, face preservation, dragon anatomy, hands, palette and scene readability. Use 2K for studies and most mobile art; use 4K selectively when a detailed master actually benefits.

Do not equate a local app with local inference: partner nodes transmit inputs to providers. Do not extract browser/session tokens. Queue through the signed-in ComfyUI UI, or use a deliberately provisioned API credential through secure runtime input. Save sanitized JSON workflows.

## Published creative-production guidance → concrete practice

- [Google DeepMind: seven Nano Banana Pro prompt tips](https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/) identifies subject, composition, action, location and style as key controls, and recommends explicitly assigning roles to reference images. **Application:** label each reference as identity, pose, style or setting in the prompt; specify camera and action rather than piling on quality adjectives. The article acknowledges inconsistent character features and blend artifacts. **Review:** compare every generated face to the canonical drawing; never treat model output as automatically consistent.
- [Google Cloud: Gemini image generation best practices](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/gemini-image-generation-best-practices?hl=en) recommends purpose/context, specificity, iterative refinement and decomposing complex scenes. **Application:** separate likeness, environment and final composition; make narrow correction passes. Preserve conversation/thought context only when the selected ComfyUI node actually supports it; independent calls do not magically retain earlier images.
- [Google: AI storytelling guidance](https://blog.google/intl/en-africa/company-news/outreach-and-initiatives/empowering-the-next-generation-of-african-storytellers-with-generative-ai/) emphasizes creative direction, character consistency and local correction. **Application:** keep an intentional scene brief and repair a faulty hand instead of accepting it because the whole picture looks attractive.
- [Pixar: Toy Story 2 visual development](https://www.pixar.com/toy-story-2) describes color scripts as a sequence of small paintings establishing visual language and emotional movement. **Application (our adaptation to books):** build one contact sheet of all 12–20 page thumbnails and color keys before final rendering; vary shot scale and use light/color to reinforce story beats. This is a traditional production practice adapted here, not an AI-specific guarantee.

## Enforced project review sequence

Brief → character/wardrobe bible → likeness and four dragon-stage sheets → three stress-test scenes → 12–20 page beat sheet and thumbnail storyboard → chapter color script → selected final art → local corrections → typography → whole-chapter contact-sheet and phone QA → release.

Stress-test a canonical character in front/three-quarter, profile/action, and low light before committing a chapter. Keep identity failures and fixes in ignored work/qa-notes.md so lessons inform later prompts. If a model repeatedly fails a stable feature, compare another model with the same references; do not conceal the drift with increasingly ornate prose. These tests and release checks are project-specific design decisions, informed by the above sources.

- [Adobe: structure reference](https://www.adobe.com/learn/firefly/web/generative-ai-structure-reference-image) and [style reference](https://helpx.adobe.com/firefly/web/work-with-images/generate-images/reference-images-for-styling.html) distinguish composition guidance from appearance guidance. **Application:** our references have separate roles; do not expect a character portrait to determine the entire page layout. These Firefly controls are analogous guidance, not claims that ComfyUI's Gemini node exposes identical sliders.
- [British Council: learning English through picture books](https://learnenglishkids.britishcouncil.org/parents/helping-your-child/learning-english-through-picture-books) recommends familiar language with a little new language and useful everyday phrases. [Using storybooks](https://learnenglishkids.britishcouncil.org/parents/top-tips/using-storybooks) emphasizes illustrations, rereading and shared engagement. **Application:** allow repeated phrases, let illustrations carry meaning, and keep a page enjoyable to reread. No rigid sentence-length formula is implied by these sources.

## Verified credit conversion
[Comfy support: how credits work](https://support.comfy.org/articles/5846341390-how-credits-work-in-comfy), checked 2026-11-18, states USD 1 = 211 credits. Metered 35–37-credit Nano Banana Pro runs are approximately $0.17–$0.18; the observed 45.12-credit GPT Image 2 reference edit is approximately $0.21. Larger cover edits and image-reference tokens can cost more; use recorded run usage rather than the node estimate for accounting. Keep detailed session ledger under ignored work/session/.
