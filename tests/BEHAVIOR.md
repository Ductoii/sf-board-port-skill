# Validation record

Checked 2026-10-27 using synthetic fixtures; no production script or media is bundled.

- **Without the skill:** an independent agent produced top-level `asset_library`, `reference_prompts`, and `videos`, plus a `.project` metadata file. This misses the observed SF Board import schema (a directory, `scenes[0].sfs`, `scenes[].shots`).
- **With the skill:** a fresh independent agent ported the same four-beat watch-repair task into a real `.project` directory: four 30s clips, six REF cards, exact original dialogue, completed prop transfers, silent edit handles and a matching ledger. The complex pocket watch/tool bag have AL cards; the plain glass does not. Validator passed with no errors/warnings, and no media was generated.
- **Real compatibility check:** read-only validation of the author's 111-clip/67-REF Furious project passed. That private script/media is deliberately not included.
- **Automated checks:** 13 standard-library unittest cases cover dialogue/escaping, missing IDs, stale usedBy, dependency cycles, timing vs diegetic dialogue, edit handles, previous-clip instructions, ledger transitions, export round trips/backups, installer idempotence/backups and symlink refusal. A runtime-cache idempotence failure was reproduced and fixed.
- **Skill metadata:** passed the Codex skill-creator quick validator; all bundled relative documentation links resolve.

These checks establish the tested import/prompt structure and package behavior. They do not establish rendered-video quality, complete semantic coverage on unseen films, or an official SF Board schema guarantee.

## Practical pacing guide follow-up

A fresh independent agent read the expanded guide and handled four decision cases: no automatic 65-word re-cut of an already running 111-clip film, action-heavy vs dialogue-heavy beat grouping, offscreen telephone speech and selective reuse of legacy prompt syntax. It correctly rejected clip-count/word quotas. A first single-shot response introduced an abbreviated header; the reference was clarified to distinguish a shot snippet from a complete clip and to keep source speaker labels. A follow-up produced a complete 30s phone clip with full header, quiet handles, BG/listener refs only and exact CALLER dialogue; validator/export passed without warnings. The visible listener keeps closed lips. Numeric overload thresholds and a minimum shot count remain deliberately unspecified: decisions depend on dramatic and physical load, not another quota.

The new reference includes measured aggregate statistics and small paraphrased lessons; no private source screenplay, transcript or production media was added to the repository.
