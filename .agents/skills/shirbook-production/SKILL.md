---
name: shirbook-production
description: Create consistent illustrated characters, covers and beginner-English chapters for Shir's Secret using the owner's ComfyUI app, and maintain its mobile GitHub Pages book. Use for this book's art, editorial and publishing work.
---

# Shir's Secret production

Read the repository-root `HANDOFF.md` for current state and latest owner decisions. Then read `references/production.md` for visual continuity, reading level, art QA and publishing. Read `references/research.md` when choosing models or changing the ComfyUI workflow. Project root is three directories above this folder.

## Established brief

A mobile-first illustrated serial for Shir, a nine-year-old beginning English reader. Digital drawing, exceptional art direction and consistent characters. Chapters are 12–20 pages. Short text, usually above a generous illustration; 5–7 short lines is a useful starting point, not a hard constraint. The user explicitly prioritizes approachable English over numerical limits. Write chapter one with the user when ready; do not invent and publish it in advance.

Shir is the protagonist; derive her illustrated likeness from user-provided photographs. Skitters is an original friendly dragon with hatchling, baby, adolescent and adult reference designs; adult body grows to small-car size and eventually carries Shir. Cover title is exactly **Shir's Secret**. No dragon on the cover, including silhouettes or dragon-shaped shadows.

## Art and authority

Use the local Comfy Desktop app for generation, including hosted partner models when authorized. Initial-session hosted budget is at most USD 25 total, not a recurring allowance or spending target. Track estimated and observed costs; typically begin with 2–4 candidates, review, then refine. Do not automatically buy credits. Never claim a model is best without a comparative test on this project's style and identity needs.

Original photographs, rejected work, image metadata containing private filenames, and credentials stay outside the public tree. Use ignored `private/` for photographs and `work/` for intermediate output. Publish clean derivatives deliberately, not an entire ComfyUI output folder. Hosted generation of identifiable reference photos requires a clear destination and authorization; the general hosted-model budget does not substitute for that decision.

Create canonical drawings before scene production. Reference those drawings in every subsequent image; a repeated seed is not a character lock. Keep consistent identity features, costume, dragon anatomy and relative scale. Refer back to canonical art rather than repeatedly editing the previous page. Save the workflow JSON, model/version, prompt, reference IDs, settings and seed when supported. Never include authentication state in exported workflow files.

## Repository and release

Repository: `shlomimatichin/shirbook`; desired checkout: `~/personal/shirbook`; public host: GitHub Pages under `/shirbook/`. Use relative asset URLs. Keep first release to cover → chapter selection → only Chapter 1 (Coming soon until collaboratively written). No fabricated pages or extra chapter cards.

The user conditioned site publication on having the cover and character references. Build and test the shell now; publish the site after these assets are ready. Repository creation itself is authorized. `scripts/check_book.py --release` enforces asset readiness. GitHub Actions is manual until first release. After launch, publish chapters deliberately every few days or weekly as agreed; no timer should release unfinished work.

## Chapter release approval — owner-required gate

1. Develop chapter text and art; commit coherent checkpoints periodically.
2. Deploy the chapter to `site/staging.html` and verify the live staging reader, including all text, art, page navigation and phone layout. Clearly label drafts and missing illustrations.
3. Send the owner the live staging URL and identify the version/commit for review.
4. Publish a chapter in the main book ONLY after the owner explicitly approves publication of that staged version. Earlier text approval, approval of individual images, generation authorization, credit purchases, or requests to push commits do not constitute chapter release approval.
5. Material changes to chapter content or art after approval require staging and renewed owner release approval. Keep the main book placeholder until the gate is satisfied.

Routine commits, pushes and staging deployments remain authorized and do not require repeated permission. This owner instruction supersedes earlier “publish when ready” wording. Current Chapter 1 is NOT approved for publication.
