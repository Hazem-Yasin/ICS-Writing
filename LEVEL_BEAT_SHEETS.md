# ICS — Rigged Sphere
## Level Beat Sheets — Template and Levels 0–14

*A level file says what a place is. A beat sheet says what happens in it, in what order, and what the player is meant to feel when they leave. The facility files are already good at the first. This sheet adds the second, and gives every future level the same skeleton so that pacing can be compared across the game.*

*The design argument: a level is a sequence of decisions about attention. Where does the player look first? What are they allowed to ignore? What does the room say when it thinks no one is listening? If those answers are not written down, they are made by accident.*

---

## How to use this sheet

1. Copy the template below.
2. Fill every field. A blank field is a decision not yet made.
3. Mark anything not in an existing document as **[PROPOSAL]**.
4. Cross-check against the level file, `STEALTH_DETECTION.md` and `TENSION_CURVE.md`.

Beat sheets are written for **one pass through a level at a specific phase**. A level visited in several phases gets one sheet per visit, or one sheet with a phase column. Level 4 uses a phase column. Level 0 is visited mainly in Phase 3 and so has a single main sheet plus return notes.

---

## The template

```
LEVEL ___ — name
Phases visited:
Detection zone(s):
Lighting / temperature / sound:
Safe spaces:
Tools relevant here:
Hidden information here:
Entry:
  how the player arrives, what they see first, what they hear first
Problem:
  what is in the way, and what it asks of the player
Escalation:
  how the pressure changes (more, closer, louder, quieter)
Reward:
  what the player gains (information, tool, access, a person)
Exit:
  how the player leaves, what they carry, what changed
Emotional target:
  one sentence
What must not happen:
  one sentence
Open questions:
```

**Field guide**

| Field | What it answers | Where to check |
|---|---|---|
| Phases visited | When is the level in play? | `DESIGN.md` |
| Detection zone | A, B, C or D? | `STEALTH_DETECTION.md` |
| Lighting / temp / sound | The BES triple (or its absence) | Level file, `facility/Overview.md` |
| Safe spaces | Where can the player stop? | `TENSION_CURVE.md` |
| Tools relevant | Which tools matter here? | `weapons/`, `SOLUTION_MATRIX.md` |
| Hidden information | What is there to read, hear or notice? | Level file, `internal-communications/` |
| Entry / Problem / Escalation / Reward / Exit | The five beats | This sheet |
| Emotional target | What the player should feel leaving | Author |
| What must not happen | The anti-goal | Author |

---

# LEVEL 0 — The Infrastructure Corridor

**Phases visited:** 3 (first and main visit), 4 (advance team sweeps the approach; Junction C), 5 (the device message), 6 (return as a choice)

**Detection zone:** **D** — no CCN, no PTKW monitoring. The badge still broadcasts but nothing is in range to receive. In Phase 6 Omega-1 carries portable arrays; Level 0 is not safe from them. (`STEALTH_DETECTION.md`)

**Lighting / temperature / sound**
- Lighting: emergency red, passive-power, steady, low, even. It has run since the facility was built.
- Temperature: ~12°C. No environmental management.
- Sound: pipes tick as hot water moves through the main. A very faint floor vibration. A constant low hum of unknown origin that masks all acoustic events inside Level 0.
- Smell: metal and stillness. No scent additive. (`facility/Level 0.md`, `scene-notes/Level 0.md`)

**Safe spaces:** The hatch handle at the south end (warm, first warm thing). The crawl. The sub-corridor shelf. All are cold; none is comfortable.

**Tools relevant:**
- Maintenance Bar T3 — pry the two glyph-marked panels (Phase 6 power coupling and data conduit).
- Junction C — Level 0 maintenance sub-corridor; certain modifications need materials found only here.
- ACS-9 Position 3 — set up before the Phase 4 sweep; the advance team files "environmental anomaly" and does not return.
- ICS-OLF-14 — the unmarked canister, found in Level 0.
- The maintenance jacket in the Level 0 supply recess (slows the cold; does not stop it).

**Hidden information:**
- The Board Governance Charter on the device (Document 2.23), read in full.
- The previous Branch Director's notebook, with its inside-cover addendum.
- The terminal in the sub-corridor (Document 2.42, the Board Terminal Message).
- Pre-ICS glyphs on two panels. The Charter notes: *"Certain structural elements predate ICS construction."*
- The faint lighter oval on the floor. The clean floor.

## Beat sheet — Phase 3, first visit

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | 02:00, Branch Time, Day 3 of Phase 3. Night cycle, corridor lights at 30%, broadcast silent. The Stairwell B door: grey, green seal, cold to the touch, a 2mm gap at the lower-left corner. The player pushes. It moves. | Slip (Move + Read). Approach through the service corridors or stairwell. Open the door. | Dread without threat. The door is *already* open to the player. |
| **Descent** | Two flights, ~4m each, to a landing, then ~4m more. Same non-slip surface, same right-hand rail. Cold gets real. The smell changes. | Move. Nothing else. | The frame comes off. No music, no scent. |
| **Arrival** | The 80m corridor. Raw metal, Cycle 1 notation on the pipes, red light. The floor is clean, and nothing is cleaning it. | Read the room: pipes, panels, the glyphs, the floor. | Wrongness that cannot be named. |
| **Problem** | Where to go, and what to touch. Nothing demands action. The cold ticks down Thermal Regulation, **-1 pip per 90 seconds** without insulation. | Choose: panels, sub-corridor, south end. | Pressure from the body, not an enemy. |
| **Escalation 1** | The false wall panel: 15m from the north end, third panel on the west wall, 3mm seam. Pressure at the upper right corner opens it. | Use (physical interaction). Find the device. | A small, quiet "yes." |
| **Escalation 2** | The device. Warm, silent, no seams. The Charter is open on the display. Sections 1–6, then Section 7 addressed to the player: *"You found this document. That means you are one of them — one of the 1.7%."* | Read. For as long as it takes. | The game's largest information beat. It arrives in silence. |
| **Escalation 3** | The sub-corridor (east wall, ~20m from north, 1.2m × 2.2m). Inspection reports, Cycles 291–293. The notebook in the gap. The terminal ~8m in, unconnected and on. | Read. The notebook's last entry: *"I want to keep reading."* | Company. Someone else was here and noticed. |
| **Reward** | The Charter, the notebook, the terminal message, the knowledge of the three grey dots and Section 7. Rania's kit is near the hatch (keycard, floor plans, the photograph of Leila). | Collect; decide what takes inventory slots (Charter physical copy = 2 slots). | Weight. The reward is a burden. |
| **Exit** | The south end. Rania's hatch: 60cm, warm to the touch, no lock. The crawl, ~12m to the water main junction, ~4 minutes. Emerges behind a removable panel in a Level 1 utility alcove. | Move + Slip. Thermal Regulation restores while moving. | The first warmth in the level. Relief with a taste. |
| **After** | 04:00, an empty corridor. The player returns to quarters and sits in the dark. | Witness. | They are no longer who they were when they went in. |

**Emotional target:** *The truth is not a monster. It is a cold room, a screen that has been left open for a very long time, and a notebook with room for one more entry.*

**What must not happen:** No enemy encounter on the first visit. No jump-scare. No music. If the floor is dirty, the sheet has failed.

## Beat sheet — Phase 4, the advance team

| Beat | What happens | What the player does |
|---|---|---|
| **Warning** | Two Omega-adjacent assets sweep the Level 0 approach areas on a verbal route not in any document. They *will* enter the stairwell. | Read the signs: PTKW changes, Stairwell B closed, patrol shifts. |
| **Option A: avoid** | Stay out of Level 0 until the sweep ends. | Wait. Cost: time. |
| **Option B: prepare** | ACS-9 Position 3, aimed at the corridor for 10+ minutes beforehand. The team files "environmental anomaly — possible sensor interference" and does not return. | Use. **Cost:** setup time; the player must stay out of range. |
| **Option C: Junction C** | Modify in the sub-corridor (ACS-9RS, Ignition Canister). 20 minutes of noise and no EIMU coverage. | Modify. |
| **Failure** | Caught on the stairs. Capture is "processed": the reclassification document, the date, the asset number, then the last autosave. | — |

## Beat sheet — Phase 5, the message

| Beat | What happens |
|---|---|
| **Setup** | In quarters, EIMU-Jammer running, AIDEN placed elsewhere, ~02:00. The player holds the device in the dark. |
| **The cursor** | A single text field. No label. No prompt. No response. One message. |
| **Consequence** | Nothing visible. In Phase 6 one sweep arrives 12 minutes late to a specific corridor instead of 3. |

## Beat sheet — Phase 6, return

| Beat | What happens |
|---|---|
| **The choice** | Level 0 is one of the places the player *can* go. Red, cold, quiet. The notebook is still there. The device is still dark. |
| **What changes** | Nothing mechanical. The cold is still the cold. The inside cover still reads *"We are not the first. We will not be the last. But we were here, and we noticed, and that matters."* |
| **Tool use** | Maintenance Bar T3: pry the glyph panels. Behind the first, the power coupling. Behind the second, the Cycle 1 data conduit to the Board Terminal. |

**Open questions — Level 0**
1. ~~Device position.~~ **Resolved.** `facility/Level 0.md` now places the device in the 15m recess; the "lighter oval" 40m from the north wall is a separate, unexplained detail.
2. ~~Device state.~~ **Resolved.** `facility/Level 0.md` now describes the device as present on first visit, matching the scene notes.
3. **Hatch location.** `facility/Level 0.md` and the scene notes agree the hatch is at the south end. `weapons/found/Rania-Hatch-Kit.md` places the kit "in the Level 0 maintenance corridor, near the hatch." This sheet assumes the kit is by the hatch at the south end of the main corridor, not in the sub-corridor.
4. ~~Junction C Phase label.~~ **Resolved.** `weapons/MODIFICATIONS.md` and the Ignition-Canister file now read *available from Phase 3, first required in Phase 4*.
5. **Terminal.** `facility/Level 0.md` calls the terminal's content Document 2.42 and the device content the Charter. `scene-notes/Level 0.md` does not mention the terminal. This sheet treats both as separate objects.
6. **Day of entry.** This sheet says "Day 3 of Phase 3" (Day 13), `scene-notes/Stairwell B.md` says 02:00, `STORY.md` says Day 15 at 23:00. `TIME_MODEL.md` proposes the `STORY.md` timing.

---

# LEVEL 4 — Wellness / Cafeteria / Break Room

**Phases visited:** 0, 2, 3, 4, 5, 6 (not accessible in Phase 1)

**Detection zone:** **A** for the primary corridors (Levels 4–6: continuous CCN node coverage, no gaps over 2m); **B** for the cafeteria (`STEALTH_DETECTION.md` lists it under standard coverage). The Earth View Window corridor and the quiet room are the places where the player can stop without moving. **[PROPOSAL]** The window corridor and quiet room are not assigned a zone in any document; treat them as Zone A until decided.

**Lighting / temperature / sound**

| | Phase 0 | Phase 2 onward |
|---|---|---|
| Temperature | 21–22°C | −3°C at Day 4, −6°C by Phase 2 peak |
| Light | 2,700K warm | Same fixtures, same colour, no one under them |
| Sound | Vocal-only music; soft cafeteria ceiling; the 06:00 Ambient Update | Music off. No broadcast. The ceiling absorbs everything |
| Smell | Olfactory primer; coffee | Coffee; less of everything else |

**Safe spaces:** The quiet room (6m × 8m, eight seats, no Music Programme), the Earth View Window bench, the break room sofa corner.

**Tools relevant:**
- Olfactory canisters (Level 4 environmental systems closet behind a ventilation panel near the cafeteria; Hana's lab bench notes).
- AIDEN plush (break room, east wall, 30cm; the social AIDEN, not the player's).
- The four coffee machines (Comfort descriptions as EIMU primers).
- Wellness Hub extension: neurological and thermal restore, logged and flagged above a certain phase.

**Hidden information:**
- The BES design intent for the level (Mosaic Dependency, Default Mode Threat, the Curiosity Policy, harvest goals).
- AIDEN's laminated cards, rotated monthly.
- Tarek's moving of the AIDEN at night; its return by morning.
- Rania's paper-towel note history on this level; the third stall.

## Beat sheet — by phase

| Phase | Entry | Problem | Escalation | Reward | Exit | Feeling |
|---|---|---|---|---|---|---|
| **0** | Lunch, break, the window at 06:00 | None. Pick a table. | The AIDEN card, the coffee description, the wellness alert (Beat 8) | Belonging; the 06:00 broadcast | Back to work | Warmth. The player loves it. |
| **2** | Level 4 is cold, silent and empty. No queue at the coffee machine. | Reach the window past PTKW pairs | Music and Ambient Update gone; Darius at the window on Day 6 | The view; the silence made visible | Back down | The cage without the warmth. |
| **3** | Night cycle. Window corridor. Coffee ring on the left of the bench. | None. | 03:40: the player's city appears for ~12 minutes | The city | Down to Stairwell B | Grief with no name. |
| **4** | After the speech. | Room full of people who heard it. | Tarek stands up. | A name that "goes everywhere" | The window | Quiet as an event. |
| **5** | A cafeteria that is not emptying on schedule. | Marcus, Cho, Lani. | Day 31: Darius comes back. | *"I used to think the view was a gift."* | Wherever the player goes | Something is changing. |
| **6** | The Level 4 floor at 03:00 has people on it. | None. | 06:00, six hours to saturation. Darius, Tarek, the player. | Names read. Earth, unchanged. | Wherever the player goes | The room holds the weight. |

## Beat sheet — key scenes

### The cafeteria (south face, ~5,000 m²)

| Beat | Detail |
|---|---|
| **Entry** | Round tables, eight seats each. Three service periods (06:30–08:30, 11:30–13:30, 17:30–19:30) plus continuous light service. |
| **Problem** | Phase 0: none. Phase 4: the speech. Phase 5: it is not emptying. |
| **Sound** | The ceiling absorbs voice differentiation and passes a low warm rumble. When Tarek stands in Phase 4, the room goes quiet more suddenly than a hard space would. His voice is the only thing that carries. |
| **Reward** | Phase 4: Rania's note read aloud. Her name, "when he says it, goes everywhere." |
| **Tools** | None. Service-hour equipment gives masking in the corridor. |

### The break room (east face, ~800 m²)

| Beat | Detail |
|---|---|
| **Entry** | Sofas, low tables, bookshelf, two game tables, a screen with the Earth feed. |
| **The AIDEN plush** | 30cm, east wall, at standing eye height, facing the room. Laminated monthly card. Approval 87%. |
| **Problem** | Tarek finds the cards unsettling and has never filed a PWRP about it. |
| **Reward** | The player may move the AIDEN. By morning it is back. |
| **Tools** | AIDEN T1 (the player's own). |

### The Wellness Hub extension and quiet room (west face)

| Beat | Detail |
|---|---|
| **Entry** | Two private rooms, one larger quiet room (6m × 8m, one west window, eight seats with low dividers). |
| **Problem** | None. Designed so the player will not go to Stairwell B. "It is partially effective." |
| **Reward** | Rest. Neurological and Thermal restore. Logged and flagged above a certain phase. |
| **Tools** | None. |

### The Earth View Window (north face)

| Beat | Detail |
|---|---|
| **Entry** | A 15m corridor, slightly wider than the corridors around it. At the end, a 3m × 2.5m composite panel. A bench bolted to the floor, worn on the right. |
| **What it shows** | Large Earth. Roughly 19 of every 24 hours. Terminator line at 06:00. Shadow-side city lights; the player's city (Accra) appears ~03:40 for ~12 minutes. |
| **Problem** | None. This is not a puzzle. |
| **Reward** | Stillness. Darius. The sense that something is looking back. |
| **Rule** | Always accessible in Phases 4, 5, 6. The bench never has a task attached. |
| **Tools** | None. |

### The restrooms and third stall

| Beat | Detail |
|---|---|
| **Entry** | Two clusters, near the cafeteria and the break room. |
| **Problem** | Sera's PWRP report goes nowhere. |
| **Reward** | The cleaned floor. Whoever cleans it now does it the way Rania did. |

**Emotional target:** *You had a life here. That is the problem.*

**What must not happen:** No combat on Level 4. No spectacle. No score. Any threat on Level 4 should come from someone the player knows.

**Open questions — Level 4**
1. ~~Break room window.~~ **Resolved.** `facility/Level 4.md` now notes that "break room window" is the colloquial name for the Level 4 Earth view; the window is on the north face and the break room has a screen.
2. ~~Garden atrium.~~ **Resolved.** `TUTORIAL.md` Beat 8 now names the Level 4 quiet room.
3. Where exactly does Sera submit her PWRP report? `facility/Level 4.md` says "the Level 4 terminal"; no terminal location is given. **[PROPOSAL]** one terminal in the restroom-side alcove near the cafeteria entrance.
4. Rania's shift ended "six months before this scene" (restroom). She was transitioned in Cycle 300 Q2 (`facility/Level 5.md`). Consistent with Phase 1 if the scene is Cycle 300 Q4.

---

*Levels 1, 2, 3 and 5–14 below. Header fields (areas, hours, temperatures, tool numbers, junction placements) come from the level files. The beat tables are **[PROPOSAL]** throughout: they sequence canon facts into beats but have not been checked line by line against every scene note. Treat each row as a draft until its level file is revised to match.*

---


# LEVEL 3 — Work Floors / Medical Centre / Quarters

**Phases visited:** 0–6. This is the level the player lives on. *Everything else is a trip away from it.* (`facility/Level 3.md`)

**Detection zone:** **A** on the work floors and main corridors; **B** in quarters corridors. **[PROPOSAL]** The player's own quarters (17C) are Zone B with a *sound-only* hazard: neighbours hear loud actions, nothing records them.

**Lighting / temperature / sound:** 2,700K amber, 21–22°C in Phase 0. The Medical Centre is the exception: 3,000K, a cooler white. After the Phase 2 shutdown the work floors keep the lights and lose the people. The pool is 28°C and is the last warm place on the level.

**Safe spaces:** Quarters 17C (door closed), the gym's west window, the pool. **[PROPOSAL]** The pool is a Phase 2–3 safe space: PTKW does not enter, and the water masks noise.

**Tools relevant here:** Junction A (Phase 2: first modifications). CRD-7 bench materials. The Medical Centre supplies for the Thermal and Neurological restores. Work Floor C, the player's desk (two desks from the right, facing the interior glass wall; Omar directly to the left).

**Hidden information:** the player's own workstation (the Reports they were hired to review). Omar Khalil on the floor. The AIDEN desk cards. Yusra's note in the Level 2 restroom stall (see Level 2 below) is not on this level but is found while moving through it.

## Beat sheet — Phase 0: the first morning

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Shift start, 07:00, Work Floor C. The floor is busy — all four floors visible through the glass, all occupied. The chair is noticeably good. The AIDEN desk card reads *"You Belong Here."* | Sit. Read the reports queue. | The job feels like competence. |
| **The desk** | The first Review: an aggregate of emotional data, anonymized to the population level. The numbers are clean. The pattern detection metrics are in the green. The AIDEN card is face-up. | Review. Flag. File. | Pride. The work is real. |
| **Omar** | Omar Khalil, directly to the left: night-shift facilities, day-shift analyst. He makes koshari from cafeteria ingredients. He always makes too much. He puts a portion on the player's desk without being asked. | Eat, or don't. The portion is there on the next visit either way. | A colleague. The start of something. |
| **The report that doesn't resolve** | One aggregate, mid-afternoon, contains a discrepancy that the standard reporting framework has no category for. It is small. It is probably nothing. | Flag as "anomalous — see note." | A question the job didn't ask. |
| **Exit** | The evening service. Cafeteria. The floor empties at 21:00. | Move. | The day was good. |

## Beat sheet — Phase 1: the interrogation days

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Day 1 morning. The floor is normal. Two desks are empty that were full yesterday. Nobody mentions them. | Go to the desk. Sit. | The floor likes them. That is worse. |
| **The monitoring pass** | Every four hours, a PTKW pair passes the work floor door. Their route is visible through the glass wall. They do not enter. They are always there. | Work. Do not look up too much. | Being watched by a room that likes you. |
| **Quarters 17C** | After 21:00, the floor closes. Quarters are the only space that is theirs. The badge broadcasts but the neighbours are not security. | Close the door. | The first breath they have taken all day. |
| **Days 2–3** | Confinement lifts on Day 3 night. The rhythm: floor, desk, cafeteria, quarters. No deviation possible yet. | Wait. | Patience as a skill. |

## Beat sheet — Phase 2: Junction A and the first tools

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Day 4. Empty floor. The BES warmth is on but the people are not. The AIDEN posters are still there. | Enter the work floor alone. | Wrongness that takes a moment to name. |
| **The patrols** | PTKW pairs on 8-minute cycles. The maintenance corridor behind Junction A is in the east service passage, accessible via the quarters stairwell panel. The pairs pass the Level 3 corridor entrance at minute 3 and minute 11 of each cycle. | Time the patrol window (5 minutes clear). | The building as a puzzle. |
| **Junction A** | The bench behind the east service panel: materials, a cleared workspace, no EIMU node within 4 m. First modification possible here. | Modify. The cost is time and noise. | Ownership. This space is ours. |
| **Day 6 — the pair outside quarters** | A PTKW pair stops outside the quarters corridor. They stand for 11 minutes. They do not knock. They leave. | Stay still. | Cold without cold. |
| **The pool** | Phase 2 safe space. Water masks acoustic events. PTKW does not enter. 28°C against the 21°C corridors. | Swim. Or just sit at the edge. | The body still works. |
| **Exit** | Back to quarters with the first crafted tool. | Return. | The cage is real and they are inside it and they made something inside it. |

## Beat sheet — Phase 3: the museum

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Days 11–20. The floor is empty. The lights are still on. The AIDEN cards are still on the desks. Tarek has been straightening them. | Walk the floor. | Isolation as a place. |
| **Tarek** | Days 14, 16, 18 at 18:30: he is at the Level 4 break-room corner table. He does not initiate. If the player sits nearby, he is present. | Be near him or not. | Company measured in proximity. |
| **The Medical Centre** | Open. Staffed. The 3,000K warmth. Thermal and Neurological restores available. The only non-empty room with staff. | Enter. | Care that is still warm. |
| **Materials** | The Medical Centre supplies, the CRD-7 bench at Junction A, the Level 3 service corridor for the maintenance network. | Collect. | Agency in an empty building. |
| **Level 0 approach** | Day 15, 23:00 (`STORY.md` §II). The access path runs: quarters → stairwell panel → service corridor → Level 1 janitorial station → sub-level → Stairwell B door. | Move carefully. Night cycle, 30% light. | The decision has been made already. |

## Beat sheet — Phase 4: named

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Day 22, 08:00, after the speech. The floor is full. Something has changed — people are not louder, but they are different loud. | Enter the crowd. | Two kinds of fear: of them, and of what you carry. |
| **Tarek's name** | Three colleagues who were in the cafeteria for the speech know Tarek's name now. They say it in corridors. It is not a dangerous word yet. | Listen. | The beginning of something that cannot be undone. |
| **Ally contact** | Tarek is back on his maintenance route (Level 3 corridor, 14:00–16:00). If the player has the jacket, or the Charter, or both: a moment of near-contact, without words. He straightens a desk card near the player's. He does not look up. | Be there. | Trust without language. |
| **Exit** | Anywhere. The floor is theirs and theirs and theirs and theirs. | Leave whenever. | The room holds more now. |

## Beat sheet — Phase 5: trust and its cost

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Day 22–60. The floor is active. Marcus, Lani, Cho, Dayo, Priti are all on it. Some of them have heard things. Some have not. The data still comes in every morning. | Work, and watch. | Belonging, now with stakes. |
| **The Q3 Baseline Archive** | The fourteen-month secondary analysis — the pattern that cannot be unseen — becomes legible in Phase 5. It names colleagues approaching the harvest threshold. It names the player as the instrument that found them. | Read it, or file it. | The work was always this. |
| **An NPC reports a conversation** | One of the Phase 5 NPCs submits a PWRP report about something the player did or said. The player finds out when a manager asks a careful question. No accusation. A careful question. | Answer carefully. | Trust, retroactively wrong. |
| **Day 44** | The cascade becomes self-sustaining. The floor is different in a way that has no single cause — like a room where someone has rearranged the furniture one centimetre in every direction. | Notice. | Something is changing. |

## Beat sheet — Phase 6: 03:00

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | 03:00, Day 62. Six hours left. The floor has people on it who are not supposed to be there. | Enter. | The room holds the weight. |
| **Goodbyes** | The work floor is the right place for them: not a gesture, just the space where time passed. Omar's koshari tin is on the counter. Tarek's desk cards are straight. | Say what there is to say. | Not enough time and also exactly enough. |
| **Exit** | Wherever the player goes next. The window. Level 0. The transit node. | Choose. | — |

**Emotional target:** *This was home, and it was never yours.*

**What must not happen:** No set-piece. Level 3 does not host the worst thing that happens in the game; it hosts the thing that makes the worst thing hurt. The AIDEN cards on the empty desks in Phase 2–3 are never commented on. They just keep being there.

**Open questions — Level 3**
1. Is the pool a safe space? **[PROPOSAL]** yes, Phases 2–4.
2. Medical Bay vs Medical Centre naming. **Resolved:** "Medical Centre" is used everywhere.
3. Omar's level (Level 3 floor) vs scenes elsewhere. Keep him on Level 3.

---

# LEVEL 1 — Arrival / Janitorial / Sub-Level

**Phases visited:** 0 (arrival), 3 (Stairwell B bottom, Junction B), 4–5 (hatch exit, supply route), 6 (transit node).

**Detection zone:** **A** in the public lobby; **B** in service corridors; the sub-Level 1 section and the Type C crawlway are **D** (no security entry in Phases 2–4, `ENEMY_AI.md`).

**Lighting / temperature / sound:** Phase 0 is the most welcoming space in the building: 23°C (warmer than the facility standard, BES-deliberate), 2,700K amber on a slow warm gradient from the shuttle corridor. The scrolling text: *"You made it. You're here. Welcome to something different."* The sub-level is dry, cold and quiet; the Stairwell B door sits at the *bottom* of the descent, visible from below for the first time when the player comes up from the sub-level in Phase 3.

**Safe spaces:** The janitorial station (15 m², near the north face), the sub-level shelf.

**Tools relevant here:** Junction B (Phase 3). The maintenance panel in the janitorial station's back wall (entry to the Maintenance Network). Rania's hatch exit.

**Hidden information:** the cleaning log in the janitorial station. Rania's handwriting on the supply shelf ("*Shelf 3 — mop heads, supply request submitted 14.09.300*"). The biometric calibration room (Phase 0 only): the pleasant images, the Earth music, the two blank minutes.

## Beat sheet — Phase 0: Day One

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **The shuttle corridor** | 40 m, 23°C, gradual amber light. The scrolling text. Three ICS employees visible through the terminal glass waiting for the next group. | Walk. Read the walls. | Warmth before thinking. |
| **The arrival hall** | Thirty meters, soft ceiling, wooden floor. A welcome desk with two staff. Three AIDEN plushes visible before the player has been introduced to AIDEN. The desk is lower than expected — no counter, no glass, no barrier. | Walk toward the desk. | Chosen. Not processed. |
| **Biometric processing** | "Wellness Baseline Assessment," 15 minutes of pleasant images and Earth music (the only place in the facility where full-instrumented music plays). Then 2 minutes of blank screen. The player does not choose the images. Their body produces the data. | Sit. Watch. | Peace, and the strange absence of effort. |
| **The badge and the AIDEN plush** | The badge is on. The AIDEN plush is in their hands — familiar, because they saw three of them in the room before receiving this one. | Hold it. | Meeting someone they have already met. |
| **Elevator to Level 3** | The atrium lobby, open upward. Plants. The circular seating, chairs facing outward. The first sight of the facility as a community rather than a building. | Look up. | The right choice, confirmed. |

## Beat sheet — Phase 3: the sub-level

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Night cycle. Maintenance panel in the janitorial station's back wall. The panel opens without resistance. The service corridor beyond it is dry and cool. | Slip (Move + Use). | They have been here before. This is the first time they noticed. |
| **The janitorial station** | Rania's handwriting on the supply shelf, in the same careful print as on the supply forms in Level 5's archive. The cleaning log, open at the last entry: her name, her shift, a note about the Level 5 acoustic anomaly. | Read. | She was here. She noticed too. |
| **The sub-level** | Below the station, through the back panel: dry corridor, cooler, the same industrial ceiling notation as Level 0 above. The Stairwell B door is visible from below — grey, the same green seal. From this angle the seal looks like an eye. | Descend. | Recognition: it was here all along. |
| **Junction B** | [PROPOSAL] A pipe junction in the sub-level corridor, 8 m from the bottom landing. The first modification here unlocks a Type B passage that connects the sub-level to the maintenance network. | Find. | Arrival is the reward. |
| **Stairwell B** | The bottom of the Stairwell B descent. The sealed door, the 2mm gap, the cold air. | Ascend. | Two flights up and the world changes. |

## Beat sheet — Phases 4–5: the return

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Rania's hatch: ~12 m crawl from the water main junction (Level 0) to the removable panel behind a Level 1 utility alcove, north face. Emerges at 04:00 or later. The corridor is on the 30% night cycle. | Crawl. Emerge. | The first warmth since Level 0. |
| **The patrol gap** | After the Phase 4 speech, patrol timing around Level 1 tightens. The utility alcove is 40 m from the nearest PTKW pair route — safe if the player moves within 3 minutes of emerging. | Move now. | Relief with a cost. |
| **Supply route** | In Phase 5: the Level 1 janitorial station is a transit point for materials coming down from the maintenance network. Tarek's morning arrival (07:15) is the earliest the station is occupied; the overnight window is open. | Use. | The route is theirs. |

## Beat sheet — Phase 6: the transit node

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Day 62, six hours left. The Level 1 lobby is quieter than it should be. The atrium plants are still being watered by the automatic system. | Enter. | Familiar and wrong. |
| **The arrival hall, reversed** | The welcome desk is empty. The circular seating is there. The chairs still face outward. | Sit, or don't. | The welcome, without the welcomed. |
| **The transit node** | The Level 7 connection is through here. The player can go up. Omega-1's main force is on the way. There is also nothing requiring them to leave. | Choose. | The door is real. What matters is whether they go through it. |

**Emotional target:** *The way in and the way out are the same door.*

**What must not happen:** The janitorial station is never a place where the player is caught. It belongs to Rania. The AIDEN plushes in the arrival hall are never noted as sinister in any caption or narrator text — they are just there, familiar, doing what they were designed to do.

**Open questions — Level 1**
1. Hatch exit location: "transit docking area" vs "utility alcove". **[PROPOSAL]** utility alcove; the dock is Level 7.
2. Junction B placement within the sub-level. Not specified; placed here as 8 m from the bottom landing, a natural bottleneck.
3. Is the Level 1 biometric room accessible after Phase 0? **[PROPOSAL]** No. The door reads "Employee Processing — Authorised." The player's badge does not open it.

---

# LEVEL 2 — Mezzanine / HR / Branch Director

**Phases visited:** 0 (onboarding at HR), 2 (steam valve 2-J-7, EOD's first appearance), 4 (atrium act on Day 21), 5–6 (Branch Director suite).

**Detection zone:** **A** on the mezzanine and manager corridor; **A+** at the Branch Director suite (access requires Tier 1 or appointment, guarded during hours). The lost property office is **B**. The HR meeting rooms have EIMU monitoring not disclosed to visitors — the space feels private; it is not.

**Lighting / temperature / sound:** Warm mezzanine light, the same 2,700K amber as the lower levels, slightly elevated Music Programme volume in the HR suite ("slightly louder than elsewhere" — the BES spec, `facility/Level 2.md`). The Branch Director's inner office is 8 m × 7 m; the AIDEN plush on the left of the desk faces the room.

**Safe spaces:** None in the public zones. The lost property office after hours (north quadrant, near Stairwell B access, Zone B). **[PROPOSAL]** The steam-valve pipe gallery (the 90-second window between valve activation and the automated reset): the only protected space when the mezzanine is occupied.

**Tools relevant here:** Steam valve 2-J-7 (90-second clear window on the Level 2 service corridor). Rania's jacket (lost property, north quadrant). The PWRP terminals in HR (three stations; the leftmost is Sera's). The manager corridor glass wall (clear by default; frost indicates a meeting in progress — and cover).

**Hidden information:** Yusra's writing on the inside of the second stall door in the south restroom ("*I was here. I was here. I was here.*" — partial name below, first two letters: *Yo*). The fourth drawer of the Branch Director's filing cabinet ("Archived Catering Schedules": Document 2.14). The Earth photograph on the outer office wall, taken at orbital apogee — Earth in the frame, both poles visible, smaller than it looks from Level 4.

## Beat sheet — Phase 0: onboarding

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | HR & Wellness, south quadrant. Softer lighting, slightly warmer ambient music. The waiting area chairs are better than the corridor. | Sit and wait, briefly. | Welcomed. |
| **The onboarding meeting** | A private room, 3 m × 4 m. Warm. The HR staff member is trained in "active listening posture." The EIMU cameras are in the ceiling. The meeting is genuine care and high-resolution monitoring simultaneously. | Answer. | The institution is paying attention. That is the point. |
| **A friendly question** | Near the end of the meeting, one question about family. Not asked for HR records — those are already on file. Asked to establish a Belonging anchor, which the HR handbook calls "grounding inquiry." | Answer or redirect. | The question that felt personal was not personal. It was perfect. |
| **The badge and the exit** | The badge is live. The tier is assigned: Tier 3. *Your Tier 3 employee badge is your key to the facility.* The elevator is right there. | Leave. | Named. |

## Beat sheet — Phase 2: the valve

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Day 4–10. The mezzanine is empty except for PTKW pairs doing corridor sweeps. The manager offices are mostly clear: glass walls transparent, a few managers at desks, some frosted. | Enter from Stairwell B or elevator. | The building is quiet in the wrong way. |
| **EOD on the rail** | Day 4, first sighting (`EOD_ENCOUNTERS.md` §3.2). EOD walks past a manager office on the Level 2 corridor. The manager's glass goes from clear to frost. He is seen from the end of the corridor or through the maintenance panel live feed. He does not look toward the player. | Witness. | The glass going frost is the thing. |
| **Steam valve 2-J-7** | The service corridor behind the north face panel. The valve controls a secondary steam line; when manually activated it produces a 90-second gap in the PTKW pair route through the mezzanine corridor (the pair detours to the service ramp). The valve is a physical lever, warm to the touch. It makes a sound. Not a loud sound. | Time it. Activate. Move in the 90-second window. | Precision as survival. |
| **Access to lower service space** | Through the north face panel, past the pipe gallery, to a Type A corridor that connects down to the Level 1 sub-level service passage. | Use the window. | The building can be read. |
| **The Yusra stall** | The south restroom, second stall from the left. *I was here.* The partial name. Two letters. | Read. | Company across Cycles. |

## Beat sheet — Phase 4: Day 21

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Vantage choice** | Day 21, 08:17. Four vantage points for the atrium act (`EOD_ENCOUNTERS.md` §5.1): mezzanine rail (above, visible to EOD if leaning), atrium floor (in the crowd, can't leave quickly), HR glass wall (safe, through glass), maintenance feed (no emotional presence, allowed). | Choose before 08:17. | Complicity in the choice of witness. |
| **The act** | Canon (`STORY.md` §III): the badge reader activates on the pillar, Yaw reads his classification, EOD waits, speaks in a voice only Yaw hears, Yaw leaves with him. The letter stays on the chair. | Watch. There is nothing else. | The silence where an intervention would be. |
| **Marcus and the letter** | If the player is on the floor, Marcus picks up the letter after. If they speak to him he says nothing. | Approach, or stay back. | Grief that found a proxy. |
| **The afternoon** | 14:30: EOD sent back to the docking bay. The player can see the corridor to the Level 7 bay from Level 1 below. Level 2 empties. The Branch Director's light is on in the inner office at 23:00. | See the light, or don't. | The building breathing out. |

## Beat sheet — Phase 5–6: the Director's suite

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **The outer office** | The framed charter. The apogee photograph, Earth small, centered, both poles. The reception desk empty after hours. | Look at the photograph. | The window on Level 4 shows Earth large. This shows it true. |
| **The inner office** | Phase 5: access requires Tier 1 or an appointment the player will not receive. **[PROPOSAL]** The Phase 6 door is unlocked — the Branch Director is inside, as she has been for hours. The AIDEN plush on the desk faces the room. She is holding one. | Enter or knock. | Authority, sitting still. |
| **The conversation** | She knows. Not everything — not the Vantage transmission history, not what the player has built in the Q3 Baseline Archive. She knows that something irreversible has been set in motion and that she wrote the speech that gave it language. The conversation cannot be won: she is not wrong, and neither is the player. | Speak. | The face of accountability, and it is a real face. |
| **Rania's jacket** | In Phase 5–6, the lost property office can be reached from the north quadrant, after hours. The jacket on the wire rack. Her name is not on it. Her asset number is not on it. The note is in the lining. | Take it, or read it there. | The note was always going to be found. |

**Emotional target:** *Authority that looks like care — and the care is real, and so is the authority, and they are the same thing.*

**What must not happen:** The Branch Director is never a villain monologue. She does not confess or explain. The fourth drawer of the filing cabinet does not require a key; it opens when the player opens a drawer. The horror is that it was never hidden.

---

# LEVEL 5 — PTKW Operations / EIMU Centre / Reclassification

**Phases visited:** 4–6. Reached only by Stairwell A (black card reader at the Level 5 access door, 120cm height, black rather than white) or the PTKW elevator (separate elevator bank, east face of Level 5).

**Detection zone:** **A** throughout; the CCN intercept station and the reclassification workflow cluster are **A+** (any non-PTKW badge presence within 6 m triggers an immediate flag).

**Lighting / temperature / sound:** the same 2,700K amber as the employee levels — a deliberate choice, because Level 5 that looks different would communicate its difference (`facility/Level 5.md`). Faint hum from the EIMU processing racks, audible only in the quiet between patrols. By Phase 5 the review queue reaches **11,000 events**.

**Safe spaces:** None. **[PROPOSAL]** One janitorial recess, north face, 3 m × 2 m — the only space on Level 5 without an EIMU node. Rania waited here once, between 01:47 and 02:10, before the acoustic insulation was repaired. The cleaning log records her route.

**Tools relevant here:** Junction D (Phase 4), on Level 5. The review terminal (standard workstation, visible through the operations center glass). EIMU-Jammer (8-minute battery). CCN-Spoofer (3 sessions, found in the Level 8 network closet).

**Hidden information:** the reclassification workflow form ("Transition — Productive Capacity Realization"), the queue at 11,000 events, the file naming the player (E-05682, Phase 4 end). The Level 5 restroom wellness cards — the PTKW staff can read them too.

## Beat sheet — Phase 4: the operations floor

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Black card reader, Stairwell A. The door opens. The corridor looks like Level 3. Same temperature, same lighting, same AIDEN poster. The difference is the silence of people who know things. | Enter. | The building seeing itself. |
| **Reaching the terminal** | The PTKW triples — tighter spacing than pairs, ACS-9 route pattern — move on 6-minute cycles. The review terminal is visible through the operations center glass wall, 30 m from the stairwell door. Three patrol gaps: 90 seconds each, offset by 2 minutes. | Time two gaps. Reach the terminal. | Patience with a consequence. |
| **The review terminal** | The EIMU event queue. The player's own file is in there: the CCN transmission history, fourteen months of flagged behavioral data, the exposure event and its date. The file is accurate. The player did what it says. | Read it. | The cage, from the inside of its own record. |
| **Junction D** | [PROPOSAL] The Level 5 service junction, accessible through a panel behind the northern EIMU processing racks. First materials here unlock the CCN intercept work (`SOLUTION_MATRIX.md`). | Modify. | Tool as argument. |
| **Exit** | Stairwell A, back down. | Move. | They know what the building knows about them. |

## Beat sheet — Phase 5: the queue

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | The queue is at 11,000. The operations floor is running but not processing — the automated response system has been suspended to prevent cascade errors. Flags accumulate. Nobody is being sent anywhere. | Enter in a gap between shifts. | The machinery of care, stopped. |
| **A colleague's file** | One of the names in the queue is someone the player knows. Not a minor character — someone whose face the player has seen in the cafeteria, whose desk is near theirs. Their file: compliance score, deviation curve, harvest readiness index. | Read it, or close it. | Complicity, in the player's hands. |
| **The choice** | The CCN-Spoofer creates a 40-minute gap in the position report for one file. The flag is not cleared — it is deferred. Time. | Use it, or don't. | The system can be slowed. It cannot be stopped. |
| **Exit** | The queue is still 11,000. | Leave. | Everything is exactly where they left it. |

## Beat sheet — Phase 6: no one in a hurry

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Day 62, six hours left. The PTKW staff are still here. They are doing their jobs. Nobody looks up. | Walk through. | The machinery is still running. That is the most frightening thing. |
| **The last log** | The EIMU archive access terminal, east side: the full behavioral record of every employee who has ever been in the facility, back to Cycle 290. The player's own record ends — the last entry is today. It is not a death. It is the last data point. | Access it. | The record is complete. |
| **Omega-1** | An Omega-1 sweep is scheduled for Level 5 at Hour 4 of the window. The time is visible on the duty roster, which is a standard document, not hidden. | Leave before Hour 4, or find a way to stay. | The schedule is public. The schedule is the threat. |

**Emotional target:** *The machinery of the thing is boring, and that is what is terrible.*

**What must not happen:** No lecture. The workflow speaks for itself. The wellness card in the Level 5 restroom reads the same text as every other level. Do not add irony to it.

**Open questions — Level 5**
1. Is Junction D on Level 5 or reached from it? **[PROPOSAL]** on Level 5, behind the EIMU processing racks.

---

# LEVEL 6 — Research & Learning / Library

**Phases visited:** 0–6. The division home; quarterly reports are *reviewed* here. The player's desk is on Level 3 Work Floor C.

**Detection zone:** **B** throughout. CCN monitoring frequency is calibrated upward on Level 6 to compensate for reduced ambient social pressure (`facility/Level 6.md`). The east restroom utility closet is unmonitored: the access panel is the entry to the maintenance corridor network.

**Lighting / temperature / sound:** quieter than Level 3 — the work selects for a population that spends more time looking at screens and thinking. 2,700K, 8 m double-height ceilings in the library. The secondary bar (07:00–20:00) is in the center corridor. The tally marks are under the bar overhang — seven groups of four, different hands, different tools, first noted by Tarek in Cycle 295.

**Safe spaces:** The library alcoves (soft chairs, two per table, low lamp — the player can stop here without purpose). The east restroom utility closet (maintenance panel).

**Tools relevant here:** The maintenance panel in the east restroom closet (Phase 0 discovery, month four: the player's first access to the maintenance network). The library archive (physical Global Access documents; PTKW-level documents not present — no gap on the shelf, simply absent). The CCN-Spoofer is found on Level 8; the path there runs through Level 6's north face terminal room.

**Hidden information:** the tally marks under the bar; Yusra's preferred table (second from the back, left side, facing the entrance — a detail in her document, which is Document 2.39); the Q3 Baseline Archive on the player's Level 3 desk, but the pattern it contains was first visible through Work Floor H data on this level; the behavioral data aggregate that flows through Level 6 every day.

## Beat sheet — Phase 0–1: the division home

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Quarterly report review day. Level 6, Work Floor H, 34 desks, most occupied. The data aggregate comes in every morning. | Sit. Review the quarter. | Competence in the right direction. |
| **A review that doesn't match** | The aggregate from the Level 3 EIMU data, processed through Work Floor H, contains a pattern that the reporting framework has no category for. Same pattern as the Level 3 Phase 0 anomaly, now larger. | Flag it, or file it without a note. | The question follows the player home. |
| **Yusra's table** | Phase 1: the library is accessible after work hours. Second table from the back, left side, facing the entrance. The light. The chairs. Books don't change based on who's reading them. | Read, or sit. | The most honest space in the building. |
| **The maintenance panel** | The east restroom utility closet, month four. The panel is labeled. The authorization level is not specified. The player opens it. | Open it. | A route into the building that the building did not offer. |

## Beat sheet — Phase 3–5: reading as work

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | The library is open. No one is checking what the player reads. The cameras are in the corridor, not the stacks. | Enter. | Safety of a specific and unusual kind. |
| **The archive** | Physical binders, all Global Access documents, filed by number. The gaps are not visible — the PTKW documents are simply absent, like pages removed from a book before it was bound. | Read what is there. Notice what is not. | A library that has been curated. |
| **The tally marks** | Under the bar overhang, visible only from a stool. Seven groups of four. Different tools, different depths. The marks have been there since at least Cycle 295 (`facility/Level 6.md`). Nobody knows what they count. | Find them, or don't. | Something was being counted. |
| **The Q3 Baseline Archive** | The data on Work Floor H, in Phase 5, becomes the second entry point to the fourteen-month secondary analysis — the pattern is the same pattern that was anomalous in Phase 0, now resolved into something legible. | Recognize it. | The job produced this. |
| **Exit via the panel** | The maintenance panel in the east restroom closet opens to the service corridor network, the fastest route to Levels 5 and 8. | Use. | The building has routes the building doesn't advertise. |

## Beat sheet — Phase 6: the last reading

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | The library, quiet. Day 62, hours left. Yusra's table is empty. The chairs are where she left them. | Enter. | Peace with consequences. |
| **A last document** | The player may leave a document on the table. Any document — the Charter, the notebook, the Q3 analysis. It will still be here when the archive closes. | Leave something, or not. | The act of having read. |
| **Exit** | The maintenance panel, or the corridor. | Go. | — |

**Emotional target:** *Reading as resistance — not because it changes anything, but because it insists.*

**What must not happen:** Reading is never a chore. The library never gives the player a "find the document" prompt with a map marker. If they are in the stacks it is because they chose to be.

**Open questions — Level 6**
1. Reports reviewed here vs the desk on Level 3: **Resolved** in `facility/Level 6.md`.
2. Can the player access Work Floor H data to advance the Q3 Baseline Archive analysis, or is all the work done from the Level 3 desk? **[PROPOSAL]** both — Level 3 is the synthesis desk; Level 6 Work Floor H is where the raw aggregate comes in.

---

# LEVEL 7 — Transit Coordination

**Phases visited:** 4–6. Tier 1 badge required.

**Detection zone:** **A** throughout. Lighting: clean, neutral white — the only level in the standard-access range deliberately not given the BES warmth treatment (`facility/Level 7.md`). Sound: the shuttle bay status board, a restrained hum, and from the adjacent corridor — a low sound, not mechanical, not voice. The corridor the 847 used.

**Safe spaces:** The restroom stall with "94" scratched into the door. The wellness card was never replaced — the stall door has no card, just the number.

**Tools relevant here:** Form ICS-T8 (departure request, one page, real). The transit scheduling desk reception (a real desk, a real process, an outcome of nine cases that is not disclosed). The adjacent corridor (not on any floor plan, connects to the Level 9 staging area).

**Hidden information:** The nine voluntary departures that did not produce departure. The 847 operational transfers that use a different corridor. The number 94 on the stall door — just the number.

## Beat sheet — Phase 4: the waiting room

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Tier 1 badge, elevator or Stairwell A. The transit commons. Sixteen chairs. No BES warmth. A coffee point with two options. The shuttle schedule display. | Enter. | A place between places. Without the warmth. |
| **The form** | ICS-T8, departure request form, available at the transit desk reception. One page. It asks for reason, anticipated date, and acknowledgment of Schedule D. The form is real. The player can take it. | Pick it up. Read it. | The form says you can leave. The form is telling the truth. |
| **The adjacent corridor** | 40 m long, 3 m wide, not on the floor plan. Same functional white light as Level 9. Nothing in it. A sound — low, continuous, not mechanical. | Stand at the entrance. Listen. | The sound before a sentence is read. |
| **The 847** | The transit log, accessible on the scheduling terminal with a Tier 1 badge: 847 "operational transfer" movements, labeled as logistics. Nine entries labeled "voluntary departure." The nine did not depart. | Read the log. | The form was always going to go in the file. |
| **The stall** | The restroom stall door: "94." No card. | Read it. | Someone was counting. |

## Beat sheet — Phase 6: the transit node

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Day 62, six hours left. The transit commons is quieter than it was. The shuttle schedule shows one inbound flight. It is not a shuttle for departing employees. | Enter. | Familiar and wrong. |
| **The form** | ICS-T8 is still in the rack at the desk. The player may have one already. The player can fill it out and leave it on the desk. It will be in the file by morning. | Fill it out, or not. | The act has no practical consequence. The act has weight. |
| **The corridor** | The adjacent corridor. The sound is the same. Omega-1 will come this way. The player can wait here, or go. | Choose. | A door that opens inward. |

**Emotional target:** *A door that does not open outward — and the door was always the point.*

**What must not happen:** No chase on Level 7. The Omega-1 threat is a time pressure, not a pursuit. The departure form is never shown to be impossible — it is simply never sufficient. The neutral-functional design is never commented on by any NPC.

**Open questions — Level 7**
1. Does the transit bay physically connect to Level 1 and to the dock? **[PROPOSAL]** yes — Level 7 is the operational dock; Level 1 is the arrival experience; both are shuttle access but different architecture.
2. The 94 scratched into the door: is it a person, a year, a count? **[PROPOSAL]** Leave it unanswered.

---

# LEVELS 8–10 — EIMU / Reclassification / Infrastructure

**Phases visited:** 4–6. Accessible only from the PTKW elevator or Stairwell A with PTKW clearance.

**Detection zone:** Level 8 — **A** (continuous real-time EIMU monitoring, 22 workstations). Level 9 — **A+** (reclassification workflow; any non-PTKW presence triggers immediate escalation). Level 10 — **A** (infrastructure staff; Zone 00-ENV unmonitored because it was never commissioned).

**Lighting / temperature / sound:** Level 8 and 9 — cool functional, no BES warmth. Level 8 wellness cards were removed on PTKW request (no reason given). Level 9 has no AIDEN posters — they were simply never ordered (`facility/Levels 8-10.md`). Level 10 has the Facilities team second door on the left, and a wellness card with a handwritten addition: *"Also the Facilities team is here. Second door on the left. We have coffee."* It is still there.

**Safe spaces:** Level 10 only: Zone 00-ENV (the unconnected environmental loop, never commissioned, no monitoring). Cold — for the same reason Level 0 is cold. The engineering staff do not enter it.

**Tools relevant here:** CCN-Spoofer (Level 8 network closet, Phase 4). The EIMU archive terminal (Level 8 east side, full behavioral record of all employees since Cycle 290). The Category Omega release mechanism (Level 10, south wall of the primary mechanical room, 40 × 40 × 60 cm, grey, no label, dual-key release).

**Hidden information:** The 11,000-event queue overflow (Level 8, Phase 5). The Level 9 staging corridor sound. The AIDEN absence on Level 9. The Level 10 engineer's handwritten note. Zone 00-ENV.

## Beat sheet — Level 8: behavioral monitoring

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Phase 4, PTKW clearance. The monitoring center: 22 workstations, one room, 600 m², three shifts. The "8s" are the people the Level 6 employees see at the secondary bar. | Enter during a shift change gap. | The face of the machine that watches. |
| **The network closet** | East side, behind a standard infrastructure panel. The CCN-Spoofer is on the second shelf. It is not locked. It is not labeled. It was left here by someone who is no longer in the facility. | Find it. | This was always going to be here. Someone made sure. |
| **The archive terminal** | Full behavioral record, Cycle 290 to present. Every employee who has ever been in the facility. The player's own record ends today. | Read the player's own record, or someone else's. | A building seeing itself, and the player seeing the building seeing them. |
| **Phase 5** | The queue at 11,000. The workstations are running. Nobody is keeping up. | Pass through. | The machinery is overwhelmed and still running. |

## Beat sheet — Level 9: reclassification

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Phase 4–5. Offices, workstations, document printers, a secure data room. No AIDEN posters. The absence is the kind you only notice if you have been on every other level first. | Enter. | A building that forgot to complete one thing. Or chose not to. |
| **The form** | "Transition — Productive Capacity Realization." A standard ICS form, precise and thorough. The player's own reclassification form, pre-populated with E-05682, is in the pending queue — dated the day of the Phase 4 exposure, held because the asset is still producing data. | Read it. | The paperwork was always ahead of the player. |
| **The corridor** | The staging corridor, south end, 40 m long. Connects to the Level 7 shuttle bay. It is clean. It is lit. Nothing is in it. It has a sound. Not mechanical, not voice. Low, continuous, present since the corridor was built. | Stand in it. | The sound before a sentence is read. |

## Beat sheet — Level 10: infrastructure

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Phase 4 or 6. The mechanical floor. Real systems, real staff, real engineering. The Facilities team has coffee. | Enter. | The building keeps itself alive, and it does it well. |
| **Zone 00-ENV** | The unconnected environmental loop, designated Cycle 1. A sealed section of the mechanical floor, unlit, ~12°C. Not entered by the engineering staff. No EIMU node. The same cold as Level 0 for the same reason: the loop was never connected. | Enter through the engineering access hatch. | Level 0, explained. And somehow worse. |
| **The release mechanism** | South wall of the primary mechanical room. 40 × 40 × 60 cm, painted facility grey, no label. A panel. Two key slots. Both keys must be inserted simultaneously. The Branch Director holds one. The Level 9 senior officer holds the other. | Find it. | It does not look like what it is. That was the design. |
| **Phase 6: the Omega** | At 14:00 Day 61, the panel was opened, the release initiated, the panel closed. The mechanism did its job and returned to looking like nothing. Event Code 7-C. | Read the maintenance log. | The thing that ended the world is a maintenance note. |

**Emotional target:** *The sound before a sentence is read — and the sentence has already been read.*

**What must not happen:** The release mechanism is never a boss fight, a puzzle requiring both keys, or a dramatic confrontation. It was activated before the player knew it existed. The drama is in the date on the maintenance log.

**Open questions — Levels 8–10**
1. Does the player ever carry the second key? **[PROPOSAL]** No. The dual-key rule is the point. The player can find the mechanism but cannot reverse what it did.
2. Is Zone 00-ENV accessible from Level 10, or only from the Level 0 infrastructure approach? **[PROPOSAL]** Both — they are the same loop. The hatch on Level 10 and the Level 0 end are two access points to the same unlit, unconditioned space.

---

# LEVELS 11–14 — Board / IOS / EOD

**Phases visited:** 5–6 (the Board elevator from Level 10 to 14, accessible from the infrastructure room via a Board-level authorization door).

**Detection zone:** **A+** throughout — or more precisely, not detection in the facility sense. There is no EIMU here. The monitoring on these levels is not the PTKW system. It is older. 17°C, cleaner light than the employee levels. Not cold like Level 0: a preference, a set point, a choice.

**Lighting / temperature / sound:** Below the acoustic isolation threshold for the employee levels. Quiet. Not the silence of an empty building — the silence of something that has no need to produce sound. In Stairwell B above Level 10, between Level 10 and the locked door to Level 11, something can be heard if the stairwell is quiet and the player is still. Not a voice. Not mechanical. *"The sound of something that has been thinking for a very long time."* (`facility/Levels 11-14.md`)

**Safe spaces:** None. This is not a space the player was designed to enter.

**Tools relevant here:** None are effective here. The EIMU-Jammer jams the PTKW monitoring system; this is not that system. The CCN-Spoofer has no function. The ACS-9 has no effect on the non-human IOS staff.

**Hidden information:** What Level 11–14 actually looks like — not fully documented even at Board level. The Board Governance Charter's section on ICS staff is brief. The Branch Director asked once and was told: *"They are comfortable and appropriate for the staff who live there. You don't need to see them."* (`facility/Levels 11-14.md`, `documents/2.35`) The player sees it. There is no document for what they see.

## Beat sheet — Phase 5: ascent

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **The Board elevator** | Level 10 infrastructure room, the unmarked door requiring Board-level authorization. The player's Tier 1 badge does not open it. **[PROPOSAL]** In Phase 5, the door has been left on proximity latch — an IOS staff member used it and the latch did not reset, the mechanical failure mode that appears in the Level 10 maintenance log as an unresolved work order. | Try the door. It opens. | They were not supposed to be here. The building made a mistake. |
| **The ascent** | The elevator goes from Level 10 to Level 14 without stopping. The number does not count up in the display. The display is blank. | Ride. | The space between knowing and having seen. |
| **The upper floor** | 17°C. Cleaner light. The IOS staff move through the corridors. They are not hostile — they are at work. They have work to do. They do not react to the player with alarm. They react, if at all, as one might react to a person who has walked into the wrong meeting: inconvenient, briefly, then resumed. | Move through the space without purpose. | Executives are staff. The Board is administration. |
| **EOD's door** | Level 13, the quartering floor. A standard door, same as the employee quarters. The elevator access logs show his arrivals and departures. He is not here now. The door is closed and unlocked. | Open it, or don't. | He lives somewhere. That is the detail that lands. |
| **The Board's plain face** | Level 14, the Board communication relay. A room of instruments and terminals. The instruments are running. The Board does not appear. There is no dramatic reveal. The relay is on, is connected, is receiving, is transmitting. It has been doing this since the facility opened. | Stand in it. | Management, not malice. The horror is how ordinary the scale is. |

## Beat sheet — Phase 6: the Archive

| Beat | What happens | What the player does | Feeling target |
|---|---|---|---|
| **Entry** | Day 62, six hours left. The IOS staff have begun their departure protocol. The upper floors are less occupied than they were. Omega-1 has not reached here. | Ascend. | An ending that is also a departure. |
| **The Archive** | Somewhere on Levels 11–14 — the location is not specified in any document, because it was not a human project — the Board's archive of the Earth Branch is stored: every EIMU data file, the behavioral record, the harvest readiness progression, the schedule, the notes. Not in a room that looks like a library. In a format the player can access through one of the relay terminals, in one session, before the connection closes. | Read as much as there is time to read. | A place with no answers, only records. And then records are answers. |
| **Omega-1** | At 12:00, the main force arrives. The upper floors are not the target. But the elevator will not go down. | Stay, or find another way. | The ending that was always in the maintenance log. |

**Emotional target:** *Management, not malice — and the management was always indifferent to the difference.*

**What must not happen:** The Board never shows up on screen to explain itself. EOD is not encountered here in Phase 6 — he is gone, deployed elsewhere, the facility is no longer his responsibility. The IOS staff on Levels 11–14 do not speak to the player, do not chase the player, and are not frightening in any conventional sense. They are ICS staff, doing their jobs.

**Open questions — Levels 11–14**
1. Are Levels 11–14 optional in Phase 5? **[PROPOSAL]** yes — the door being unlocked is a rare mechanical failure, not a designed gate.
2. What does the upper floor actually look like? **[PROPOSAL]** Write it only when the art direction is decided; leave this sheet at functional description for now.
3. Is the Archive encounter timed, or does the player simply read until they choose to leave or Omega-1 arrives? **[PROPOSAL]** timed — the relay connection closes at Hour 22. The player may read for up to 4 real minutes if they reach Level 14 before Hour 18.

---

*→ See: facility/Level 0.md — the level description.*
*→ See: facility/Level 4.md — the level description.*
*→ See: facility/Level 1.md, Level 2.md, Level 3.md, Level 5.md, Level 6.md, Level 7.md, Levels 8-10.md, Levels 11-14.md — the remaining level descriptions.*
*→ See: TIME_MODEL.md — the day-by-day ledger these sheets assume.*
*→ See: EOD_ENCOUNTERS.md — the Level 2 and Level 3 encounters.*
*→ See: scene-notes/Level 0.md — the full discovery sequence and the Charter.*
*→ See: scene-notes/Earth View Window.md — the window by phase.*
*→ See: scene-notes/Stairwell B.md — the approach to Level 0.*
*→ See: weapons/found/Level-0-Device.md — the Phase 5 message.*
*→ See: weapons/found/Rania-Hatch-Kit.md — the kit near the hatch.*
*→ See: TENSION_CURVE.md — where these levels sit in the pacing.*
*→ See: SOLUTION_MATRIX.md — the obstacles and answers used here.*
*→ See: STEALTH_DETECTION.md — the detection zones.*
