# Seedance prompting and cinematic pacing

## Video format — preserve this shape

Every video prompt is one paragraph on one line. The following illustrates syntax; substitute the actual cast/location, never leave placeholders in a deliverable.

```text
Scene 001: REF BG1a, CHAR1a, CHAR2a, AL1a: /filmlook: /softbox: photorealistic 35mm film quality, ARRI ALEXA aesthetic, authentic Kodak color science, visible 35mm film grain, soft highlight halation, transform all referenced subjects into real live-action humans with raw unretouched matte skin micro-texture, visible skin pores, fine peach fuzz, subtle natural skin imperfections and physical fabric weave, warm window light, 30fps, widescreen 16:9 frame, clear dialogue up front, no background music score, only soft natural ambience, every spoken line is in natural English, each referenced character appears once only in the live scene, every background extra is a different stranger in muted clothes, reference-sheet panels and captions never appear in the live-action frame, BG1a = the one location for every live-action shot: a small records office with one wooden desk between two chairs and a window at rear, CHAR1a = Maya, a brown-skinned woman of 30 in a blue cotton shirt and grey trousers, hair in a low bun, neutral expression, realistic unretouched matte skin with visible pores, physical fabric weave, must match exactly, CHAR2a = Elias, a fair-skinned man of 45 in a brown wool jacket and cream shirt, short dark hair and clean-shaven face, realistic unretouched matte skin with visible pores, physical fabric weave, must match exactly, AL1a = one dark navy leather binder with a brass clasp | shot 1: /midpoint: static 40mm medium shot, CHAR1a standing left holding closed AL1a in both hands; CHAR2a standing right with empty hands, lips closed | shot 2: /closecrop: static three-quarter 75mm close-up on the single CHAR1a, holding closed AL1a, VO: "Here is the record." lips in sync, others keep lips still | shot 3: /dropdetail: close shot of CHAR1a offering AL1a; CHAR2a grips it with both hands, CHAR1a releases completely and withdraws empty hands | shot 4: /closecrop: static slightly low-angle 50mm close-up on the single CHAR2a, holding AL1a in both hands, VO: "Thank you. I can read it now." lips in sync, others keep lips still | shot 5: /dropdetail: close shot of CHAR2a setting AL1a on the desk and releasing it, both hands withdrawing empty | shot 6: /midpoint: static 40mm medium shot, CHAR1a standing left, empty hands; CHAR2a standing right, empty hands; closed AL1a rests on the desk, lips closed, hold
```

For a new port, use the full header, tag spelling, separators and voice convention demonstrated above and in the bundled example. For a revision, preserve the existing project's working format. Change only content/definitions needed for the current story. Lighting tone tags vary with the scene. English is this workflow's default, not permission to translate an existing non-English script without instruction.

- First and last shots: explicit present positions/postures/props, quiet closed lips; last `lips closed, hold`. No technical second counts. These handles are intentional editing room; do not remove them to claim faster pacing.
- Middle shots: a close shot of the one speaker per turn, `VO: "..." lips in sync, others keep lips still`. Separate consequential hand actions into readable inserts; do not hide a six-step prop exchange behind a reaction close-up.
- If the source explicitly has an offscreen phone caller or narrator, keep that voice offscreen: show the visible listener with closed lips, identify the offscreen speaker, and do not put `lips in sync` on the listener. Match the turn in `shots[].text`; do not spawn the caller in the room. If a clip contains another spoken language explicitly required by the source, scope the header language rule accordingly rather than silently translating it or contradicting it with “every line in English”.
- An over-the-shoulder shot keeps the foreground listener's face hidden and respects the established dialogue axis. Reaction shots show a different narrative response, not interchangeable filler.
- Ground visible writing on the actual paper/phone/sign. Phone screens face the person; use an over-the-shoulder insert for readable screen information. Archival evidence plays only within the physical display, without spawning its people in the live room.
- The header must agree with state changes. A character wearing WITHOUT an apron after removal cannot also have a header definition locking the apron on. A glass filled during the scene is not perpetually described as empty.

## Offscreen speech — snippet versus complete clip

For a requested **single shot**, return only its `shot N: ...` body and corresponding role line; do not invent a shortened Scene/header and present it as an importable full clip. A complete video still needs the full standard header plus quiet first/last shots.

Use the source's actual speaker label when known (for example RENATA), otherwise a stable label such as CALLER. Do not replace the caller label with the listener's name. A middle-shot example, where CHAR1a is the visible listener and the caller has no visible body:

```text
text turn: CALLER: Please check page four.
shot 3: /closecrop: static 50mm close-up on CHAR1a standing at the left, her right hand holding a black phone against her ear; the OFFSCREEN CALLER is heard through the phone, VO: "Please check page four." offscreen voice only; CHAR1a listens with lips closed and does not answer, the caller is not visible in the room
```

The visible CHAR1a and current BG must already be defined/attached in the full clip. Do not attach an unused visible character image just to represent this phone voice. Check the clip's global English/on-screen-character wording does not contradict a specified offscreen or other-language turn.

## Pacing and camera

Read [pacing-and-lessons.md](pacing-and-lessons.md) for practical beat grouping and lessons from previous ports. Build a clear, engaging flow: connected exchanges move naturally, action remains readable, and revelations get a meaningful response. Keep the important story turns and causal links in the user's prompting style.

- Establish geography when a location changes. Then stay with the unfolding exchange, using medium, three-quarter, over-the-shoulder, low angle, off-centre negative space, reaction and hand/evidence inserts where they contribute. 32–40mm suits space; 50–85mm suits dialogue/detail.
- Give each camera choice a dramatic job. Track an actor crossing space, pan to a new piece of information, or use a restrained push-in when a decision changes the scene. Static compositions let performance carry the moment. Keep moves clear and physically motivated.
- Keep replies close to their questions and consequences close to their causes within the ongoing clip. A short reveal, its immediate reaction and the reply can be told through successive shot choices. Group connected small actions into readable coverage and let a speaker close-up carry the reaction when possible; cover routine handling economically.
- Preserve quiet source handles for editing. The edit can trim these buffers while retaining the meaningful pause or response. Judge pacing across the sequence: progression, impact and a clean move into the next beat.
- Review shot bodies for actual camera direction and narrative function. Remove duplicated explanations, repeated entrances and interchangeable reaction filler; preserve the requested source dialogue and structure when revising an existing port.

Local templates avoid: `everyone holding still`, `the whole room frozen`, `no plastic`, `black face patches`, `subsurface scattering`, `3D wireframe`, `skin sheen`, `jib-arm crane`, `30-degree orbital arc`. Use concrete positive descriptions of real skin/fabric and simple camera placement. These are workflow conventions, not proven universal claims about a model's internals.

## CHAR reference — one step, four views

Use a single photorealistic landscape 16:9 white-studio sheet with FOUR vertical panels in one row: FACE CLOSE-UP, FRONT, BACK, SIDE. The sharp front head-and-shoulders close-up takes 30 percent; the remaining three panels divide 70 percent equally and show full bodies from head to soles, aligned feet and clear margins. Thin grey dividers; the four exact labels in the footer. Same face/body/outfit/accessories across panels, neutral relaxed posture/expression, arms naturally at sides, empty hands, even studio light, real skin pores and fabric weave. Append the individual face anatomy, hair, age, skin tone and outfit. Use original fictional faces, no celebrity imitation.

Costume variants attach the base CHAR directly; no separate vertical BASE portrait stage. Keep transient handheld props off sheets. Hats/jewellery may remain when habitual; removed/wet/carried variants are ordinarily handled in video text.

## BG reference — four views of one empty place

One landscape 16:9 reference sheet in a 2×2 grid of four equal panels, thin white dividers. Main view / left view / right view / useful spatial detail, all of the same architecture, furniture, light and weather. No people, portraits, captions or panel numbers. Real believable materials and 35mm photography. Different persistent day/night conditions may use linked variants. Do not put the entire story cast or stage a dramatic action in the BG sheet.
