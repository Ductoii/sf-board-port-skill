---
name: sf-board-port
description: Use when porting a screenplay into SF Board sf-board.json/.project, or reviewing its Seedance video prompts, reference prompts, pacing, thumbnails, and prop continuity.
---

# SF Board Port

Port the user's story into a usable SF Board project. Default to **prompts only**; generating reference images, thumbnails, or videos requires a request for those media. Answer briefly in the user's language.

## Start with the right contract

Read [schema.md](references/schema.md) and [prompting.md](references/prompting.md). The bundled [example](assets/example.project/sf-board.json) supplies the actual import shape: `scenes[0].sfs` is the REF library; production clips live in `scenes[].shots`. Its clip boundaries demonstrate data structure, not a pacing template to copy onto a new story. A `.project` is a **directory**, not a metadata file. Do not invent `asset_library`, `reference_prompts`, or a top-level `videos` schema.

Use the user's existing project as the authority for a revision. Inspect its latest saved contents and preserve picked media, statuses, unknown fields, and manual edits. Snapshot before changing it. For a new port, use this skill's bundled schema, prompting instructions, pacing guide and example as the complete baseline. Additional examples supplied in the current task are optional context. All required instructions are inside this skill; proceed without searching for the author's projects, sessions or applications.

## Port

1. Read the complete source. Identify story turns, dialogue, locations, costumes, recurring distinctive objects, and the title's thumbnail situation. Keep a source copy. Resolve only consequential contradictions; preserve dialogue unless rewriting is requested.
2. For a new port or a pacing review, read [pacing-and-lessons.md](references/pacing-and-lessons.md) for practical beat grouping, camera functions and lessons from previous ports. Build a brisk, coherent dramatic flow: keep connected dialogue, action and the immediate response together. A clip can contain several connected beats: cover a short exchange and simple prop handling in one clip, using shot changes for listening and reactions. Let a reveal change the coverage within the ongoing exchange; create a new clip when the sequence actually needs one. Give every shot a storytelling purpose. Use performance-led drama coverage: clear opening geography, focused speaker close-ups, meaningful listening reactions, inserts for consequential actions, and a settled ending for editing. Leave natural room for breathing, listening, hesitation and emotional reaction; keep connected exchanges flowing. Check the sequence for both fragmented exchanges and overloaded clips using the [worked sequence](references/worked-sequence.md). Apply the prompting conventions written in this package. Default `dur=30` in metadata unless the user specifies otherwise. Preserve quiet opening/ending edit handles.
3. Draft CHAR/BG reference prompts using the layouts in [prompting.md](references/prompting.md). Costume variants link directly to the base CHAR. Keep neutral expressions and empty hands in character sheets.
4. Use the AL decision rule in [continuity.md](references/continuity.md): frequency alone does not justify a ref. Simple cups/napkins/plates stay short plain-text descriptions; distinctive designs and plot-bearing evidence merit AL. A handwritten clue is different from an ordinary napkin. Handle minor prop changes in video text, not extra character variants.
5. Write single-line video prompts with the exact slash-tag/shot format. Make each clip self-contained. Preserve the existing format on revisions. Track openings/endings in a small continuity ledger. Follow each consequential state change through the actual header, action, speaker pose and ending before updating the ledger; use the [within-clip state review](references/continuity.md#review-the-whole-prompt-after-a-state-change).
6. Plan cinematic framing and motivated movement per [prompting.md](references/prompting.md). Choose economical static and moving coverage around the action and emotional turn; use framing and movement to reveal information rather than stretching a beat.
7. If thumbnail prompts are requested, place THUMB cards in REF using [thumbnails.md](references/thumbnails.md). Make a readable story moment, not a poster. Prompt-only delivery includes no generated image or fake `picked` value.

## Package and verify

Create `<title>.project/sf-board.json` in the requested SF Board folder; infer a sensible local output directory if unspecified. Preserve source, supply a concise source-to-clip/continuity map, and finish the files yourself.

Run through the interpreter, from this skill folder:

```sh
python3 scripts/project.py /absolute/path/Title.project --export
```

This checks structural integrity and writes derived REF/prompt/table exports. Separately review the actual prompt sequence for readable action, room for performance, useful clip boundaries and consistent state changes. Matching ledger strings are supporting data, not an independent semantic check: a stale state can be copied into both the ledger and prompt. Fix demonstrated contradictions in the smallest relevant phrases and recheck affected neighbours. If asked to audit actual generated video, watch it directly when playback is available and state any limitation. Text checks cannot establish rendered acting or pacing; do not invent a cause for a random generation failure.

Deliver the project link, clip/REF counts, meaningful minimal fixes, and honest validation scope. Never generate assets, mutate an application's private storage, or operate a render queue just to complete a prompt port.
