# Practical prop continuity and AL decisions

## Which objects get image references?

Ask two independent questions: **will the viewer need to recognise this specific design/content**, and **does reuse make drift consequential**?

| Object | Treatment |
|---|---|
| White cloth napkin, plain water glass, plate of bread, generic paper cup, candy, blanket, takeout carton | A short stable phrase in video text; no AL just because it appears in four clips. |
| Generic black tablet/laptop, keyboard, reading glasses, plain crossword or invoice stack | Usually short plain text; exact model/grid/line contents are unimportant. |
| A repeatedly used distinctive bag, complex coffee-service set, identifiable device/tool with a particular construction | AL if changing shape would make it look like two different objects. Reuse in more than three clips strengthens the case. |
| Handwritten clue on a napkin, a specific ownership page, settlement offer, framed magazine headline, evidence screen | AL/KU when the physical layout or essential text carries the reveal; can merit a ref even in fewer clips. This is not the ordinary-napkin rule. |
| Hat/badge/apron/jewellery already part of CHAR | Describe on/off/wet/carried state in the video. Do not multiply character sheets for small transient changes. |
| Table/chair/fixed room fixtures | Normally covered by BG. |

Count **visible physical appearances**, including a prop that persists on the table in continuous coverage. Do not count dialogue mentions of a cup left in another room, hidden items in a bag, imagined objects or archival-only content as new live props. Different newspapers/letters with conflicting story content remain distinct, even if their materials match.

AL ref prompts: one single-line photorealistic landscape 16:9 product/reference photograph, neutral background, clear material/construction, no people/hands. Give just enough shape, material, colour and distinctive content to keep identity. Small ensembles can be one kit when they travel together. Evidence images can attach the appropriate CHAR/BG identities; never attach an old thumbnail as a person reference. Ref IDs need not be renumbered after deletions.

## Four state checks

For each continuous clip boundary, compare actual shot text and the ledger:

1. **Body accessories:** if a hat was removed, the next clip's character definition is bareheaded. If an apron is left on a cart inside, it is absent on the actor outside. Do not reintroduce it via the copied header.
2. **Object identity/state:** retain one physical noun phrase; paper cups do not become ceramic mugs. A poured bowl is empty/overturned, a torn document stays in two halves, an opened jar is open until closed. Ref photos establish design; shot text establishes current state.
3. **Holder and position:** track owner/hand, left/right, sitting/standing, side of barriers and who is offscreen. Do not repeat an entrance or an action already completed. A phone resting on the desk cannot simultaneously be gripped in a copied speaker pose.
4. **Completed transfer:** receiver grips, giver releases, giver's hands withdraw empty before the next shot. Complex sequences need enough coverage to show essential state changes without over-choreographing every finger.

Each prompt states its own opening state. Never use “same as previous video”, “continue from the last clip”, “opens on the exact final frame of the previous clip”, or similar generation-memory instructions. Intentional scene/time jumps are not continuity failures.

## Revision scope

Fix the smallest conflicting phrase in the header/action/speaker pose; preserve working structure, dialogue, shot order, edit handles and cast refs. Keep source-to-prompt coverage pragmatic: protect the core dramatic meaning, accept harmless background variation within generation limits. Do not turn an approximate fidelity preference into a mechanically claimed percentage score.

A bad generated take alone does not prove the text is wrong. For requested video audits, view the video directly where supported. Separate an observed output failure from a demonstrated textual contradiction; do not promise a ref deletion or more detailed prompt will fix random muting or model variance. Queue/API troubleshooting is a separate task, and application-private files must not be edited for prompt-port work.
