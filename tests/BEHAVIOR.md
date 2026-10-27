# Validation record

Checked 2026-10-27 using synthetic fixtures; no production script or media is bundled.

- **Without the skill:** an independent agent produced top-level `asset_library`, `reference_prompts`, and `videos`, plus a `.project` metadata file. This misses the observed SF Board import schema (a directory, `scenes[0].sfs`, `scenes[].shots`).
- **With the skill:** a fresh independent agent ported the same four-beat watch-repair task into a real `.project` directory: four 30s clips, six REF cards, exact original dialogue, completed prop transfers, silent edit handles and a matching ledger. The complex pocket watch/tool bag have AL cards; the plain glass does not. Validator passed with no errors/warnings, and no media was generated.
- **Real compatibility check:** read-only validation of the author's 111-clip/67-REF Furious project passed. That private script/media is deliberately not included.
- **Automated checks:** 13 standard-library unittest cases cover dialogue/escaping, missing IDs, stale usedBy, dependency cycles, timing vs diegetic dialogue, edit handles, previous-clip instructions, ledger transitions, export round trips/backups, installer idempotence/backups and symlink refusal. A runtime-cache idempotence failure was reproduced and fixed.
- **Skill metadata:** passed the Codex skill-creator quick validator; all bundled relative documentation links resolve.

These checks establish the tested import/prompt structure and package behavior. They do not establish rendered-video quality, complete semantic coverage on unseen films, or an official SF Board schema guarantee.
