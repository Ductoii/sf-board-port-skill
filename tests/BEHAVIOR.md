# Validation record

Checked 2026-10-27 using synthetic fixtures; no production script or media is bundled.

- **Without the skill:** an independent agent produced top-level `asset_library`, `reference_prompts`, and `videos`, plus a `.project` metadata file. This misses the observed SF Board import schema (a directory, `scenes[0].sfs`, `scenes[].shots`).
- **With the skill:** a fresh independent agent ported the same four-beat watch-repair task into a real `.project` directory: four 30s clips, six REF cards, exact original dialogue, completed prop transfers, silent edit handles and a matching ledger. The complex pocket watch/tool bag have AL cards; the plain glass does not. Validator passed with no errors/warnings, and no media was generated.
- **Real compatibility check:** read-only validation of the author's 111-clip/67-REF Furious project passed. That private script/media is deliberately not included.
- **Automated checks:** 13 standard-library unittest cases cover dialogue/escaping, missing IDs, stale usedBy, dependency cycles, timing vs diegetic dialogue, edit handles, previous-clip instructions, ledger transitions, export round trips/backups, installer idempotence/backups and symlink refusal. A runtime-cache idempotence failure was reproduced and fixed.
- **Skill metadata:** passed the Codex skill-creator quick validator; all bundled relative documentation links resolve.

These checks establish the tested import/prompt structure and package behavior. They do not establish rendered-video quality, complete semantic coverage on unseen films, or an official SF Board schema guarantee.

## Practical pacing guide follow-up

Independent application covered beat grouping, economical action coverage, offscreen telephone speech and selective reuse of legacy prompt syntax. A first single-shot response introduced an abbreviated header; the reference was clarified to distinguish a shot snippet from a complete clip and to keep source speaker labels. A follow-up produced a complete phone clip with full header, quiet handles, BG/listener refs only and exact CALLER dialogue; validator/export passed without warnings. The visible listener keeps closed lips.

The pacing guide now teaches directly through dramatic progression, connected exchanges, concise action coverage and motivated reactions/camera choices. Statistical comparisons and numerical pacing-policy discussions were removed at the user's request. No private source screenplay, transcript or production media was added to the repository.

A brisk-pacing check initially split a short records exchange into separate source clips for the reveal and response. The guide was revised to keep connected dialogue/action/immediate response together and use shot changes within that exchange. On a different radio-repair scenario, the agent then kept the complete short sequence together with economical action coverage, the reaction in the reply, a completed handoff and quiet edit handles.

## Standalone portability check

Runtime instructions were audited for references to the author's projects and sessions. Two instructions that told a new port to match project 83/prior projects were replaced with direct guidance for acting, coverage and pacing. New ports use the bundled full prompt, schema, references and synthetic example; current-task exemplars are optional.

A fresh agent read only an isolated copy of the skill package and a new shoe-repair scene. It created and exported a structurally valid project without external projects, sessions, network or media generation. The first run nevertheless copied the example's two-clip split onto a short connected exchange and implied an opening prop placement instead of showing it. The entrypoint was clarified: example boundaries illustrate data structure, while connected short exchanges and simple prop actions belong within one clip using shot changes.

A second fresh application still split the same short scene for editorial convenience, despite understanding the grouping guidance. The bundled example itself was therefore consolidated into one continuous clip, preserving its dialogue and prompting syntax. Its ledger/usedBy and the boundary regression fixture were updated accordingly.

With the revised package, a third fresh agent read only the isolated skill and planned the entire shoe-repair exchange in one clip with exact dialogue, completed shoe placement/slide/pickup, motivated speaker/reaction coverage and quiet handles. It reported no missing dependencies. This last check tested textual coverage planning; it did not render video or create another import artifact. The consolidated bundled JSON separately passes validation, and all 13 automated checks pass.

## Sequence and within-clip state review

A read-only comparison of two real ports reproduced the gap this revision addresses: a structurally valid project retained old positions in its header/set after a prop pickup, and called a restrained person free in its ending. Matching ledger entries did not expose these contradictions. The comparison also showed both unnecessary small clip boundaries and useful extra action coverage; reducing total clip count would not resolve both problems.

The revision adds a self-contained synthetic railway-storehouse source, coverage choices and state transitions. It teaches a sequence pass for fragmentation and overload, plus a whole-prompt state pass through header, action, subsequent poses/set and ending/next opening. Existing slash-tag/VO format, edit handles, ref rules and validator code are unchanged.

Five fresh agents then applied an isolated copy of the package to a different synthetic flooded-depot source and two existing prompt excerpts. All found the stale frame/set and restraint/set contradictions; one left the frame's unscoped header placement unchanged. The header check was clarified to include every conflicting occurrence while preserving the valid opening state and dialogue.

Five further fresh agents read only the final isolated package and raw task. All identified the conflicting header as well as both stale set descriptions, proposed local replacements, propagated the corrected ending into the next opening, and preserved the valid pre-restraint state. Their sequence plans kept the physical recovery, emotional recognition/playback and custody/departure readable as connected groups, with quiet handles and no separate clip just for confirmation or walking out. No run required private examples, external sessions, network or media generation.

This tests textual planning and minimal state repairs on the supplied cases. It does not prove generated acting or pacing, or that every unseen long port will make the same editorial decisions. The existing automated suite and bundled import example are checked separately.
