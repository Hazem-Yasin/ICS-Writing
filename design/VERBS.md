# ICS — Rigged Sphere
## The Verb Sheet — What the Player Can Do

*Eight verbs. That is the whole game. Everything else in the design documents — the tools, the badge, the maintenance network, the Charter, the 22 hours — is something one of these eight verbs acts on. If a proposed feature does not need a ninth verb, it does not get one.*

*The player is a data analyst, not a soldier. Every verb below is written the way Kai Osei would perform it: deliberate, observant, a little too aware of being watched. None of them is a power fantasy. All of them have a cost.*

---

## How to read this sheet

Every line is tagged by where it comes from.

| Tag | Meaning |
|---|---|
| **Canon** | Stated in an existing design document. The source is named. Do not change without changing the source. |
| **[PROPOSAL]** | New. Written here to fill a gap the existing documents leave open. Needs sign-off before it becomes canon. |

`README.md` records that movement-related verbs were never defined. This sheet defines them as proposals and leaves everything else exactly as the systems documents already set it.

---

## The eight verbs at a glance

| # | Verb | What it is | Primary cost | Main risk | First taught (TUTORIAL beat) |
|---|---|---|---|---|---|
| 1 | **Move** | Walk, crouch, run | Noise | Acoustic and visual detection | Opening Sequence |
| 2 | **Read** | Documents, terminals, labels, floor plans | Time | CCN Anomaly Score on unauthorized terminals | Beats 2, 6 |
| 3 | **Badge** | Tap readers, open inventory, read vitals, remove it | Tone (3m) and a log entry | Manifest check; 4-minute gap-log | Beats 1, 7 |
| 4 | **Use** | Operate a tool at Tier 1, 2 or 3 | Noise, EIMU signature | Escalation to State 2 or 3 | Discovery tutorials, Phase 2+ |
| 5 | **Modify** | Rebuild a tool at a junction | Time and noise (no resources) | Scanner flag; noise reaching sensors | Phase 2, Junction A |
| 6 | **Speak** | Talk, show a document, say nothing | Whatever the answer costs later | Phase 6 consequences | Beat 5, Marcus (Phase 2) |
| 7 | **Slip** | Move through the maintenance network | Thermal, EIMU Coherence | Cold, narrow space, Omega-1 | Beat 4 |
| 8 | **Witness** | Sit, look, wait, listen, rest | The clock | None. This is the point. | Beat 8 |

---

## 1. MOVE

*Walk. Crouch. Run. There is no fourth thing.*

**Canon — what exists**

| Action | Sound radius | Notes (source: `design/STEALTH_DETECTION.md`) |
|---|---|---|
| Walk | 4m | Standard floor |
| Walk on maintenance grating | 7m | Metal carries vibration |
| Crouch-move | 1.5m | Standard floor |
| Run | 12m | Any surface. Always audible to a nearby enemy. Doubles visual detection speed. |
| Maintenance door | 6m | The hinge squeal is the same everywhere |

- A moving player is detected faster than a still one. Crouching shrinks the movement-detection radius.
- Corners attenuate sound: an 8m event heard around a corner reads as about 3m.
- Thermal vents mask up to 8m. The Level 3 HVAC unit masks 6m. Level 0's constant hum masks all acoustic events inside Level 0.
- Falls: minor Physical Integrity damage in Type B passages; none in standard corridors (`design/HEALTH_SURVIVAL.md`).
- Hypothermia slows movement and removes choices from the UI.
- Neurological damage degrades fine motor control (tools, modification), **not** gross motor control.

**How it feels**
Running is a mistake the player makes once. The cost is not a stamina bar. It is the sound of their own feet in a building that is otherwise very well soundproofed. The facility was designed to be quiet. The player is the loudest thing in it.

**[PROPOSAL] — to settle**
- No stamina meter. Running is limited by noise, not by breath.
- No jump. Ledges, railings and the Type B stoop do the job of obstacles.
- Reference speeds: walk ~1.4 m/s, crouch ~0.8 m/s, run ~3.5 m/s. These are placeholders chosen so the 4m / 1.5m / 12m radii read clearly against a 15m K-7 range.
- Crouch input should be hold-or-toggle, player's choice (see `design/DIFFICULTY_ACCESSIBILITY.md`).

---

## 2. READ

*The job was the tutorial. Reading is the job.*

**Canon — what exists**
- Documents have up to three layers (Global, PTKW, Board). Most of the player's early reading shows only the Global layer.
- Reading is how Tier 3 tool knowledge is found. "You have to read the safety spec to know how to defeat it" (`canon/weapons/MODIFICATIONS.md`).
- Reading is how the player finds patrol schedules (Document 2.36, 8-minute cycles) and Tarek's route schedule (work order archive).
- The EIMU Diagnostic Accessory is not explained. Its label is written in medical terminology. "Reading comprehension is the tutorial."
- Unauthorized terminal access adds to the hidden CCN Anomaly Score. In Phase 1 the player fires an anomaly flag without knowing it (Tutorial Beat 9).
- Documents are items. They take inventory slots. The Board Governance Charter takes two.
- Phase 6 has no objective marker and no task log.

**How it feels**
Quiet and slightly illicit. The Global layer is warm and well written. The player has to read past it. Nothing pops up to say "knowledge gained." The player either noticed or did not.

**[PROPOSAL] — to settle**
- Documents do not auto-summarize. The player's memory is the codex. (An *optional* in-world notebook is proposed as an accessibility assist, not a default. See `design/DIFFICULTY_ACCESSIBILITY.md`.)
- Long documents (Schedule D, Yusra's document, the Branch Director's address) are readable in sittings. The clock pauses while a document is open in Phases 0–5. In Phase 6 it does not.

---

## 3. BADGE

*Badge equals identity equals currency equals access equals inventory equals health. One object. One verb.*

**Canon — what exists**
- **Tap:** badge readers open doors. The accepted or denied tone carries 3m. Every read is logged.
- **Open inventory:** press the badge face. A grid of ten squares appears. Two items take two slots (the Charter, the Omega-1 countermeasure).
- **Read vitals:** look down at the lanyard. Four LED strips: Physical Integrity, Neurological Status, Thermal Regulation, EIMU Coherence.
- **Remove:** the EIMU signal stops. Gap-log alert after 4 minutes. Costs: no access-gated doors, no EIMU reading of others, no passive healing from facility nodes.
- **Swap:** Tier 1–3 badges; dead employees' badges (cannot be used as stolen badges); PTKW clearance badge (Phase 4); Director's badge (Phase 5); the stripped badge.
- **Manifest check:** once, in Phase 4. An advance-team officer reads the badge manifest of any non-PTKW staff. The wrong items in the wrong slots cause an immediate State 2 alert, with no prior visual detection.

**How it feels**
The badge is the one object the player can never put down without consequence. Every interaction is small and domestic: a tone, a green light, a door. The horror is that the verb that opens doors is the same verb that reports on you.

**[PROPOSAL] — to settle**
- Opening the inventory does **not** pause the world in the default mode. The badge is worn, not paused. A pause-on-open option is provided for accessibility.
- Item selection is from the badge grid. No weapon wheel.

---

## 4. USE

*Every tool refuses to behave like a weapon. That is what the player is exploiting.*

**Canon — what exists** (full specs in `canon/weapons/compliance/`, `canon/weapons/improvised/`, `canon/weapons/found/`)

| Tool | Tier 1 (standard) | Tier 2 (operational) | Tier 3 (full) | Noise |
|---|---|---|---|---|
| CRD-7 | Contact discharge, 90s incapacitation | Directed field ≤3m, 40s | Target stays aware: interrogate | 20m |
| ACS-9 | Position 1: gradual discomfort, guards leave | Position 2: distress, unpredictable | Position 3, 10+ minutes: the "frequency of presence" | n/a (infrasound) |
| EIMU-Jammer (ECT-4) | Broadcast false state at own location | Broadcast distress at a chosen location (diversion) | "Vigilance — Sustained": 4-minute Level 8 window | 8m |
| AMB-3 baton | Strike, incapacitate | Carry it elsewhere as a false location | Hand it to Tarek or Omar as a decoy | none |
| CCN-Spoofer | Intercept | Delay (40-min gap in EOD's reported position) | Spoof (two Phase 6 messages) | none |
| AIDEN unit | Place elsewhere: PTKW reads you stationary | Ghost AIDENs flood Level 5 for 30 min | Open it: listen to the archive **or** destroy it | none |
| Olfactory canisters | Release a primer | OLF-11 on a floor's intake | OLF-14: all subjects "Engagement — Maximum" for 8 min | n/a |
| Pressurized pipe | Steam, valve 2-J-7 | Hydraulic stall, Junction 4 (12 min) | Reverse OLF-11 conduit, Level 1 | n/a |
| Maintenance Bar | Strike | Cut power / steam / seal a fire door | Pry Level 0 panels | none |

- Combat is a failure mode. Violence is never the primary solution (`canon/weapons/OVERVIEW.md`).
- EOD cannot be beaten. Capture is "processed," not death.
- Tool tiers are knowledge, not upgrades. The tool does not change. The player does.

**How it feels**
Each tool has a different unwillingness. The CRD-7 glows amber and then red. The ACS-9 does nothing the player can hear. The EIMU-Jammer asks which of 47 emotions to perform. Using a tool well feels like understanding a procurement document better than its author did.

**[PROPOSAL] — to settle**
- Tool use is one input (hold to aim, release to act). No reload, no ammo count, no aim-down-sights.
- Tool UI lives on the tool, not on the HUD: the CRD-7 indicator, the ACS-9 slider, the ECT-4 dial.

---

## 5. MODIFY

*There is no workbench. There are junctions. The cost is time and noise, never resources.*

**Canon — what exists** (`canon/weapons/MODIFICATIONS.md`)

| Junction | Location | Opens |
|---|---|---|
| A | Level 3 service corridor | Phase 2 |
| B | Level 1 sub-level room, with workbench and vice | Phase 3 |
| C | Level 0 maintenance sub-corridor | Phase 3 (index) / Phase 4 (individual files) |
| D | Level 5 east perimeter, PTKW zone | Phase 4 |

- Three categories: Amplification, Conversion, Lethalization. Lethalization means understanding the safety spec well enough to invert it.
- Modified tools are visible. They flag on the Level 5 scanner because their electromagnetic profile no longer matches the registered spec.
- 20 minutes at a junction is 20 minutes outside EIMU coverage and 20 minutes of noise that may reach adjacent habitable areas.

**How it feels**
Slow and ugly. Insulation tape. Housings wedged with a pipe bracket. The modified tool looks like the opposite of the facility: no warmth, no soft edge, no "Asset Welfare Series."

**[PROPOSAL] — to settle**
- Modification is a short sequence of physical steps (3–5), one component per step, each with a name and a place. No timing minigame and no skill check.
- The player may carry a clean version and a modified version of the same tool, at the cost of a slot, to pass the Level 5 scanner.

---

## 6. SPEAK

*The hardest verb in the game is saying nothing.*

**Canon — what exists**
- NPCs follow the *unannounced relationship* principle. There are no relationship meters (`design/NPC_COMPANIONS.md`).
- **Marcus** (conversation trigger, State 2): say nothing, lie (costs him in Phase 6), or show him the Charter section (his arc moment).
- **Cho**: one calm exchange, "I'm just passing through."
- **Dayo**: ignore, threaten, or tell him K-7 is under review.
- **Priti**: pass, jam, ACS-9, or tell her about the open backlog on her husband's review.
- **Tarek** in Phase 6: two questions ("How do you know?" and "How much time?"), then "Does Rania's note still matter?"
- **CRD-7 Tier 3:** speak to an incapacitated officer. Several late-game facts can only be obtained this way.
- **CCN-Spoofer:** speak by proxy. Two spoofed messages in Phase 6.
- In Phase 6 the last choices "are not presented as options. They are available."

**How it feels**
There is no dialogue wheel announcing which line is kind. The player says a thing, and the person across from them changes by a degree they might not see until Phase 6.

**[PROPOSAL] — to settle**
- Spoken options appear as the line itself, in the player's voice, with no tone label and no colour code.
- No conversation has a timer. A silence option exists in every conversation that has a state-2 trigger.
- No visible approval, trust or relationship value anywhere in the UI.

---

## 7. SLIP

*The maintenance network is the player's body. The rest of the facility is the system's.*

**Canon — what exists** (`canon/facility/Maintenance Network.md`, `design/STEALTH_DETECTION.md`)

| Type | Posture | CCN | PTKW | Omega-1 | Temperature |
|---|---|---|---|---|---|
| A | Walking height | none | won't enter (Phases 2–4); Priti enters once | enters in Phase 6 | −4°C; Thermal degrades after 20+ min |
| B | Stoop | none | won't enter (Phases 2–5) | can enter, with difficulty | −6 to −8°C |
| C | Hands and knees | none | no access | no access | −8 to −12°C; EIMU Coherence declines after 40+ min |

- Entry is by quarters panel, pressure-point panels (Level 0: upper right corner), maintenance keys and quarter-turn valves.
- Tarek has the full key set. Moving with him lowers the anomaly weight.
- Rania's hatch: a warm crawl. The only passive healing in the game.

**How it feels**
Colder, tighter, louder than the corridors, and the first place the player feels in charge. Safe, but not comfortable. The cost of safety is the body.

**[PROPOSAL] — to settle**
- Passage type changes the camera: Type A is standing height, Type B lowers the camera, Type C locks it low with a narrower head-turn.
- No fast-travel through the network. Distance is the cost.

---

## 8. WITNESS

*The only verb with no failure state. It is also the one the whole ending is built on.*

**Canon — what exists**
- Sit at the Earth View Window. What the window shows changes every phase (`story/scene-notes/Earth View Window.md`).
- Wait. Listen. Sit with Tarek for the full 40 minutes while he writes names.
- Rest. Quarters heal all four tracks slowly and flag nothing. The Wellness Hub restores Neurological and Thermal. The hatch crawl restores Thermal.
- Watch: Lani's group on the camera feeds. The K-7 pulse via the Diagnostic Accessory.
- Nothing requires the player to do any of it. "The player may sit here. Nothing requires them to."
- Reading a note at the right moment produces an EIMU state the system has no name for: *Gratitude — Retroactive*.

**How it feels**
Stillness the game gives back. The player is watched in every other verb. Here the watching changes character: the window looks back, and what it sees is a person.

**[PROPOSAL] — to settle**
- "Sit" is one input, held. The player does not choose a pose. They stay.
- No achievement, popup or tracked stat for any Witness behavior.

---

## Where verbs combine

| Combination | Result | Source |
|---|---|---|
| Read → Use | Reading the PTKW manual unlocks Tier 3 | `canon/weapons/OVERVIEW.md` |
| Badge → Slip | Badge off for 4 minutes plus Zone D movement means near-total invisibility | `design/PROGRESSION.md` |
| Use → Speak | CRD-7 Tier 3: an enemy who must answer | CRD-7 file |
| Modify → Badge | Modified tools flag the Level 5 scanner and the Phase 4 manifest check | `MODIFICATIONS.md`, `design/INVENTORY.md` |
| Speak → Witness | Telling Tarek, then sitting while he writes | `Phase 6 Final 22 Hours.md` |
| Slip → Witness | The hatch crawl heals as the player moves | `design/HEALTH_SURVIVAL.md` |

---

## What the player cannot do

**[PROPOSAL]** — confirm before treating these as final.

- Jump. Block or parry. Snap to cover. Perform takedown animations.
- Fast-travel. See a minimap. Follow an objective marker.
- Open a crafting menu. Spend points on a skill tree.
- Loot every container. Pick up everything. The inventory is ten squares.
- Win a fight with EOD or with Omega-1.

---

## Open questions

1. Is there a sprint speed separate from run? (Proposed: no.)
2. Does the world pause while the inventory is open? (Proposed: no, with an accessibility option.)
3. Can the player drop an item on purpose to make noise? (`design/STEALTH_DETECTION.md` lists "Dropping an object: 10m." The input is not defined.)
4. Camera: field of view default and range. (Handed to `design/DIFFICULTY_ACCESSIBILITY.md`.)

---

*→ See: design/STEALTH_DETECTION.md — the sound radii and detection inputs behind Move.*
*→ See: design/INVENTORY.md — the ten-slot badge grid.*
*→ See: design/HEALTH_SURVIVAL.md — the four vitals tracks.*
*→ See: design/TUTORIAL.md — where each verb is first introduced.*
*→ See: design/NPC_COMPANIONS.md — the Speak verb's recipients.*
*→ See: design/SOLUTION_MATRIX.md — which verbs solve which obstacles.*
*→ See: design/DIFFICULTY_ACCESSIBILITY.md — hold/toggle, remapping, pause behavior.*
*→ See: canon/weapons/OVERVIEW.md — the three-tier tool knowledge system.*
