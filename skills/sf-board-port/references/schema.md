# SF Board import/export contract

This is the concrete local JSON format observed in working SF Board projects; it is not an official universal interchange standard. Retain unknown fields when editing an existing board.

## Files

```text
Title.project/
  sf-board.json
  SOURCE.txt                  # Original source if available as plain text
  CONTINUITY-MAP.json          # Story/physical state ledger, authored by Codex
  PROMPT_VIDEO.txt             # Derived, one prompt per line
  BANGTRA.tsv                 # Derived clip table
  REF/
    prompts.json              # Exact scenes[0].sfs array
    CHAR1a.prompt.txt          # One prompt per actual REF card
    BG1a.prompt.txt
    AL1a.prompt.txt
    THUMB1.prompt.txt
```

`assets/`, `versions/`, and `videos/` contain real generated media only. Do not fabricate a selected filename or a placeholder image. Empty directories are optional in a prompt-only port. Do not ship duplicate copies under old/new project names.

## Board

Required root: `film` (title), `updated_at` (local saved time), `kind: "phim"`, `scenes`.

First scene:

```json
{"id":"REF","name":"REF — Nhân vật, bối cảnh, đạo cụ, thumbnail","sfs":[],"shots":[],"script":"Ghi chú ref và phong cách."}
```

Production scene:

```json
{"id":"S01","name":"S01 — Địa điểm — thời điểm","sfs":[],"shots":[],"script":"Nội dung và thoại của cụm cảnh."}
```

REF card:

```json
{"id":"CHAR1a","label":"CHAR1a — Maya — work clothes","desc":"Maya — work clothes","prompt":"ONE SINGLE-LINE IMAGE PROMPT","status":"draft","notes":"Tạo trực tiếp một bước; chỉ prompt.","usedBy":["CHAR1b","V-001"],"refs":{"chars":[],"bg":null},"picked":""}
```

The `usedBy` above is illustrative: only include IDs that actually exist and refer to this card. Derive it by traversing library dependencies first, then video headers in clip order. `refs.chars` lists dependent identity/image refs; `refs.bg` is a BG ID or null. A costume variant CHAR1b normally has `refs.chars=["CHAR1a"]`. BG variants can attach the base BG via `refs.bg`. Avoid dependency cycles. Separate CHAR1a and CHAR1b are never two actors in one live shot.

Clip:

```json
{"sf":"BG1a","dur":30,"vstatus":"","ai_request":"","notes":"Seedance · S01 · REF (3): BG1a, CHAR1a, AL1a · 4 shot","text":"MAYA: Here is the record.","prompt":"SINGLE-LINE VIDEO PROMPT","music":null,"id":"V-001","label":"001 — Here is the record.","goc":"4 shot","vpicked":""}
```

- `sf` is the actual location BG card, also the first REF in the prompt header.
- Sequence clips `V-001..V-NNN` and prompt prefixes `Scene 001..NNN` across production scenes.
- `dur` is numeric seconds. Use 30 by default; never put production timing instructions in the prompt. Diegetic dialogue such as “You have thirty seconds” is dialogue and remains intact.
- `text` is one `ROLE: exact spoken words` line per turn, in the same order as `VO: "..."` strings in the prompt. Escape quotes with JSON rules. Silent clips use empty text and no VO. For offscreen speech, keep the caller/narrator role from the source (or a stable CALLER label if unnamed), not the visible listener; clarify offscreen delivery in the shot body.
- REF headers list only attached cards, normally BG, CHAR by number/variant, then AL/KU. THUMB cards are not video inputs.
- New prompt-only cards use `status="draft"`, `picked=""`; video `vpicked=""`. For existing real selections, preserve their files/fields. Selected REF assets normally resolve to `assets/<ID>.png` and `versions/<picked>`; video choices follow the existing project's conventions.
- Notes' REF count/list, `sfs[].usedBy`, and exported lists must agree with the prompt header. Gaps in AL numbering after removing obsolete cards are harmless; avoid renumbering working refs.

## Continuity ledger

Use a list of entries, e.g.:

```json
[{"id":"V-001","scene":"S01","source_scene":1,"dur":30,"refs":["BG1a","CHAR1a","CHAR2a","AL1a"],"opening":{"left":"Maya standing left holding the closed binder with both hands","right":"Elias standing right, empty hands"},"ending":{"left":"Maya standing left, empty hands","right":"Elias standing right holding the closed binder with both hands"}}]
```

Include source events/lines when practical. Within a continuous scene, the next opening equals the last ending. Scene/time jumps may change state when the story accounts for the change. The ledger is a planning check, not evidence that a generated video obeyed the prompt.

## Scripts

`python3 scripts/project.py Title.project` checks only; `--export` also writes derived exports, backing up changed existing export files under `.snapshots/`. The helper does not rewrite prompts, set usedBy automatically, generate media, or repair story continuity. Fix the authoritative JSON yourself, then rerun. Review errors before publishing; warnings flag missing editorial ledgers or picked-media mismatches without guessing the application's media-selection semantics.

The helper report’s `camera` field counts `/followshot:` and `/pushin:` tags only; it is not a complete motion/framing audit. Inspect shot bodies for pan/tilt, meaningful static compositions and the actual reason for each move.
