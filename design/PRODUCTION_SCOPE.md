# ICS: Interplanetary Corporate Solutions
## Production Scope

*Nothing in the design documents decides how the game is built, by whom, in what engine, or for which platform. This sheet does not decide those things either. It lists every production question the design leaves open, states what the existing documents imply, and puts a clearly marked placeholder where a decision is needed.*

*The design argument: scope is a design decision. A game with ten inventory slots, one manual save and no combat has already chosen to be small in some ways and expensive in others. Writing those choices down is how they stay choices.*

---

## How to read this sheet

| Tag | Meaning |
|---|---|
| **Canon** | Already stated in an existing document. The source is named. |
| **[PROPOSAL]** | New. A placeholder, not a decision. **No figure in this sheet is canon unless tagged so.** |

---

## 1. What the design already fixes

| Fact | Implication for production | Source |
|---|---|---|
| First person narrative horror, "in the style of BioShock" | A first-person engine, hand-authored levels, no open world | Project brief |
| Playtime: 8–15 hours to reach Phase 6 | A single-player campaign of that length | **Canon** — `design/SAVE_SYSTEM.md` |
| 15 levels (0–14) in one building | One connected map with no loading between levels where possible | **Canon** — `canon/facility/Overview.md` |
| Seven phases (0–6) | Seven states of the same space | **Canon** — `design/DESIGN.md` |
| Eleven voiced characters; Swahili and Arabic recordings | A voice cast and a translation pass | **Canon** — `design/AUDIO_VOICE.md` |
| Four endings | Four end states from one save | **Canon** — `design/ENDINGS.md` |
| Ten inventory slots | A small, simple inventory system | **Canon** — `design/INVENTORY.md` |
| One manual save, plus autosave | A simple save system | **Canon** — `design/SAVE_SYSTEM.md` |
| 61 documents, hundreds of messages | A large in-engine text corpus | **Canon** — `canon/documents/`, `canon/internal-communications/` |
| No combat as a primary system | No combat animation, damage or ballistics | **Canon** — `canon/weapons/OVERVIEW.md` |
| EOD cannot be beaten | One scripted threat, not a boss AI | **Canon** |
| Omega-1: structured sweeps, full-spectrum detection | One patrol AI with a stronger perception model | **Canon** — `design/ENEMY_AI.md` |

---

## 2. Scope drivers

| Driver | What makes it big or small |
|---|---|
| **Level count** | Fifteen levels is large. Levels 8–14 are staged, mostly corridors and rooms; Levels 3–4 are the large spaces. |
| **Phase variants** | Each level needs a version per phase it is visited. Level 4 has six. |
| **Text** | The documents and messages are already written. Implementing them as readable objects is the cost. |
| **Voice** | Eleven voices; some with limited lines. |
| **NPCs** | Named NPCs are few; most "people" are absent, which reduces animation cost. |
| **Combat** | Near zero. |
| **Stealth AI** | One patrol model (PTKW), one threat model (EOD), one perception model (Omega-1). |

---

## 3. Phase variants by level

**[PROPOSAL]** Counting how many distinct states of each level must be built. This is the main scope driver.

| Level | Phases visited | Distinct visual states **[PROPOSAL]** |
|---|---|---|
| 0 | 3–6 | 2 (before and after the device message) |
| 1 | 0, 3–6 | 3 |
| 2 | 0, 2, 4–6 | 3 |
| 3 | 0–6 | 4 (populated, empty, restored, last night) |
| 4 | 0, 2–6 | 4 |
| 5 | 4–6 | 2 |
| 6 | 0–6 | 3 |
| 7 | 4–6 | 2 |
| 8–10 | 4–6 | 1 each |
| 11–14 | 5–6 | 1 each |

*Distinct states are lighting, population and prop passes, not new geometry.*

---

## 4. Team, budget, schedule

**[PROPOSAL]** No team, budget or schedule exists in any document. The repository shows a writing team and an artist (the Blender work). Everything below is a question.

| Question | Placeholder |
|---|---|
| Team size | Unknown |
| Roles needed | Level design, 3D environment art, character art (few), animation (few), narrative implementation, audio, programming, QA |
| Budget | Unknown |
| Schedule | Unknown |
| Vertical slice | **[PROPOSAL]** Level 4 in Phase 0 and Phase 2 (the warm and cold versions of the same space), plus the Stairwell B descent to Level 0. |
| Why that slice | It tests the central idea (the same room, different meaning), the narrative tone, the lighting and the cold, and uses assets that already exist (`BreakArea.blend`). |

---

## 5. Platform and engine

**[PROPOSAL]** Not decided. The Blender files export to `.fbx` and `.glb`, which both major engines accept.

| Option | Pros | Cons |
|---|---|---|
| Unreal Engine | Strong lighting, suited to the BES light-as-narrative approach | Larger team footprint |
| Unity | Familiar for small teams | Lighting needs more work for this look |
| Godot | Open, light | Less proven for first-person realtime lighting at this fidelity |

**Platform:** PC first. Console later, if at all. Input: keyboard and mouse plus controller from the start (`design/DIFFICULTY_ACCESSIBILITY.md`, Part 6).

---

## 6. Localization

| Item | Status |
|---|---|
| Source language | English |
| In-game non-English | Swahili (Rania), Arabic (Tarek), EOD (non-human). Subtitled. **Canon** — `design/AUDIO_VOICE.md` |
| Other languages | **[PROPOSAL]** Out of scope for the first release. Plan the text pipeline so they can be added. |
| Names | Many characters come from Nairobi, Alexandria, Accra. Names and places must not be anglicised. |

---

## 7. Ratings and content

| Item | Detail |
|---|---|
| Content | Institutional coercion; planetary-scale death; separation of a mother and child; psychological manipulation. **Canon** — `design/DIFFICULTY_ACCESSIBILITY.md`, Part 4 |
| Violence | No gore. Limited depictions. |
| **[PROPOSAL]** Expected rating | Teen to Mature. Not determined. |

---

## 8. QA

**[PROPOSAL]**

| Area | Why it needs care |
|---|---|
| **Time model** | Branch Time, NPC schedules, 22-hour clock (`design/TIME_MODEL.md`) |
| **Save and reload** | Autosave triggers, Last Entry, Omega-1 reload (`design/SAVE_SYSTEM.md`) |
| **Flags** | NPC relationships are unannounced, so flag bugs are invisible. Needs a flag viewer. |
| **Phase transitions** | Level states change; props must swap cleanly |
| **Photosensitivity** | ACS-9 effects must be reviewed before any build is shared |
| **Accessibility options** | Every option in `design/DIFFICULTY_ACCESSIBILITY.md` needs a pass |

---

## 9. Save format

**[PROPOSAL]** Not described in any document beyond behavior.

| Item | Detail |
|---|---|
| Autosave | Silent; ≤3 minutes of loss |
| Manual save | One slot, quarters only |
| Last Entry | Permanent at the start of Phase 6 |
| Stored | World state, flags, inventory, Branch Time, Phase 6 clock |
| Not stored | Screenshots, thumbnails (see `design/UI_MENUS.md`) |

---

## 10. Pre-production checklist

| # | Item | Status |
|---|---|---|
| 1 | Decide engine and platform | Open |
| 2 | Confirm vertical slice | **[PROPOSAL]** Level 4 + Stairwell B |
| 3 | Rulings on the open design questions | See each sheet's *Open questions* |
| 4 | Map the Blender work to levels | Open (see `design/ENVIRONMENTAL_STORYTELLING.md`) |
| 5 | Decide the Props/Shotgun | Open |
| 6 | Voice cast and Swahili/Arabic translators | Open |
| 7 | Photosensitivity safe mode | **Required** |
| 8 | Budget and schedule | Open |

---

## Open questions

1. **Engine.** No decision.
2. **Team.** None recorded.
3. **Platform.** PC first is an assumption.
4. **Is the 88-minute Phase 6 target acceptable?** `design/TIME_MODEL.md`.
5. **Does the game ship with all four endings or add them post-launch?** The design needs all four.

---

*→ See: design/DESIGN.md — the overall design.*
*→ See: design/LEVEL_BEAT_SHEETS.md — the level work.*
*→ See: design/ENVIRONMENTAL_STORYTELLING.md — props and the Blender link.*
*→ See: design/ART_DIRECTION.md — the visual target.*
*→ See: design/DIFFICULTY_ACCESSIBILITY.md — accessibility and input.*
*→ See: design/SAVE_SYSTEM.md — saves.*
*→ See: design/AUDIO_VOICE.md — voice cast.*
*→ See: design/TIME_MODEL.md — time.*
*→ See: design/TOOL_TUNING.md — numbers.*
