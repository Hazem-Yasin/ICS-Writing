# ICS — Rigged Sphere
## Gating and Backtracking — What Opens, What Closes, What Can Be Revisited

*The game is a single building. The player can walk to almost anywhere they have a reason to. Gates are not walls; they are credentials, clocks and people. Backtracking is not penalised and is rarely rewarded with new content, except where the building has changed.*

*The design argument: a gate should tell the player something about the building. A door that does not open says what the player is. A door that opens says what someone left behind.*

---

## How to read this sheet

| Tag | Meaning |
|---|---|
| **Canon** | Already stated in an existing document. The source is named. |
| **[PROPOSAL]** | New. Needs sign-off before it becomes canon. |

---

## 1. The gate types

| Type | What blocks the player | Examples | Source |
|---|---|---|---|
| **Credential** | A badge tier or a special badge | Tier 3 for Level 7; PTKW-Clearance badge for the Level 5 wing; Branch Director badge for Levels 11–14 | **Canon** — `design/PROGRESSION.md` |
| **Clock** | A time window | Steam valve 2-J-7 (90 s); cafeteria service hours; the Phase 6 22-hour window | **Canon** — `canon/facility/Level 2.md`, `design/TIME_MODEL.md` |
| **Person** | A character who is or is not present | Rania's hatch (she knew it), Omar's 4-minute sweep gap, the Level 5 junction officer who lets the player pass | **Canon** — `design/PROGRESSION.md`, `design/TUTORIAL.md` |
| **Knowledge** | The player has to know it exists | The 2 mm gap at Stairwell B; the false wall panel on Level 0; Junction locations | **Canon** — `story/scene-notes/Stairwell B.md`, `canon/facility/Level 0.md` |
| **Tool** | A modification that has not yet been made | The Maintenance Bar T3 on the Level 0 glyph panels | **Canon** — `canon/weapons/MODIFICATIONS.md` |
| **Physical** | Something sealed | The Omega-1 docking bay (sealed), the Board Terminal on Level 0 (no badge system) | **Canon** — `design/PROGRESSION.md` |

---

## 2. The credential ladder

| Phase | Badge | Opens | Source |
|---|---|---|---|
| 0–1 | Tier 2 | Levels 1–6, Research Division, SOLCRED Canteen premium tier | **Canon** — `design/PROGRESSION.md` |
| 2 | Tier 3 | Levels 1–7, PTKW-adjacent corridors (reading access), Level 5 eastern perimeter with secondary authorization, Transit Coordination observation area | **Canon** — `design/PROGRESSION.md` |
| 3 | Stripped Tier 3 | Maintenance network, invisible movement, Level 0, Junctions B and C | **Canon** — `design/PROGRESSION.md` |
| 4 | PTKW-Clearance | Full PTKW wing, Levels 5 and 8 network, Level 7 transit corridor operational zone, Junction D | **Canon** — `design/PROGRESSION.md` |
| 5 | Branch Director | Every level, every archive; Levels 12–14 infrastructure; the Regional Sector Lead terminal (Documents 2.22, 2.44); transit docking | **Canon** — `design/PROGRESSION.md` |

**Never opened by any badge:** the Board Terminal on Level 0 (no badge system) and the Omega-1 arrival docking bay (physically sealed). (`design/PROGRESSION.md`)

---

## 3. The level graph

Which levels connect to which, and the gate on each connection. Gates marked **[PROPOSAL]** are not stated in a level file.

| From | To | By | Gate |
|---|---|---|---|
| 1 | 2 | Elevator, stairs | None |
| 2 | 3 | Elevator, stairs | None |
| 3 | 4 | Elevator, stairs | None |
| 4 | 5 | Stairwell A or elevator | Black card reader (**Canon**, `canon/facility/Level 5.md`). Tier 3 with secondary authorization for the eastern perimeter. |
| 5 | 6 | Stairs | None |
| 6 | 7 | Stairs | Tier 1 **[PROPOSAL]** |
| 7 | 8, 9, 10 | Stairs, staging corridor from Level 9 | PTKW-Clearance badge for Level 8 network |
| 10 | 14 | Board elevator | Branch Director badge **[PROPOSAL]** |
| 1 | 0 | Stairwell B (door at the bottom of the descent, in sub-Level 1) | Knowledge: the 2 mm gap and the cold. Open to the player's push. |
| 0 | 1 | Rania's hatch (south end, 60 cm, no lock) | One-way is not enforced; the hatch can be re-entered from Level 1 **[PROPOSAL]** |
| Any | Any | Maintenance network (Types A, B, C) | See `canon/facility/Maintenance Network.md` |

---

## 4. Backtracking rules

**[PROPOSAL]** Principle: *the player can return to any place they have already been, subject to the clock and the people.*

| Rule | Detail |
|---|---|
| **Nothing is lost by going back.** | Documents, tools, inventory and flags are not removed by a return trip. |
| **The place may have changed.** | A returning player finds the Phase's state, not the old one. Level 4 in Phase 2 is cold and silent; in Phase 0 it was warm. |
| **Content that closes.** | Some content is bound to its time, not its place. See the table below. |
| **No "last chance before X" warnings.** | The game never says "you cannot return after this." |
| **Fast travel.** | None. The maintenance network is the shortcut system. |

### What closes

| Content | Closes | Why | Source |
|---|---|---|---|
| Medical Centre supplies | Phase 3 | The Medical Centre goes to restricted access | **Canon** — `design/HEALTH_SURVIVAL.md` |
| Canteen wellness items | Before Phase 3 (sale); prices still shown later | Prices persist on the display board in Phase 5; stock does not | **Canon** — `design/HEALTH_SURVIVAL.md` |
| Omar's 4-minute sweep gap | If the relationship was not built in Phases 2–3 | A person gate | **Canon** — `design/TUTORIAL.md` |
| Atrium act (Day 21) | Day 21, 08:17 | An event, not a place | **Canon** — `design/TIME_MODEL.md` |
| The speech (Day 22, 08:00) | Day 22 | Irreversible | **Canon** — `design/SAVE_SYSTEM.md` |
| Level 7 transit node | Phase 6 | The Level 1 hatch exit remains; the transit bay becomes a choice | **[PROPOSAL]** |
| Phase 0 content | Phase 1 | "Not accessible in Phase 1" for Level 4 | **Canon** — `canon/facility/Level 4.md` |

### What never closes

- Level 0, in every phase. Red, cold, quiet. The device may be dark.
- The Earth View Window, in Phases 4–6.
- Quarters 17C, and the quarters safe interface for manual saving.
- The Level 4 quiet room.

---

## 5. Level availability by phase

**[PROPOSAL]** `✓` open, `~` partly or conditionally, `—` closed.

| Level | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| 0 | — | — | — | ✓ | ✓ | ✓ | ✓ |
| 1 | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 3 | ✓ | ✓ (quarters) | ✓ | ✓ | ✓ | ✓ | ✓ |
| 4 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| 5 | — | — | — | ~ | ✓ | ✓ | ✓ |
| 6 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| 7 | — | — | ~ | ~ | ✓ | ✓ | ✓ |
| 8–10 | — | — | — | — | ✓ | ✓ | ✓ |
| 11–14 | — | — | — | — | — | ~ | ✓ |

Notes: Level 4 is "not accessible in Phase 1" (**Canon**). Level 5 in Phase 3 is the PTKW monitoring room and review terminal (**Canon**, `design/TUTORIAL.md`).

---

## 6. Sequence breaks

**[PROPOSAL]** The game accepts several, because the world is one building.

| Break | How | Consequence |
|---|---|---|
| Reach Level 0 before Phase 3 | Stairwell B via the maintenance network | The first visit does not exist in a vacuum; nothing stops the player, but the device message is Phase 5. |
| Take the Branch Director badge early | Not possible; the badge appears only in Phase 5 | — |
| Skip Junction A | Do not modify | Tools remain at the base state; the SOLUTION_MATRIX lists non-modified answers. |
| Skip Omar | Never talk to him | The 4-minute sweep gap is lost, and the player uses avoidance. |
| Skip Level 7 | Do not go | Phase 6 transit ending requires it. |

---

## 7. Open questions

1. **Level 6 → 7 and 8–10 gates.** Resolved: Level 6 → 7 requires Tier 1. Levels 8–10 require PTKW-Clearance badge.
2. **Branch Director badge timing.** Resolved: she left it when she went to deliver the Phase 5 address (Day 22 morning speech). Badge available from Phase 5 start.
3. **Level 7 Tier 1 vs PTKW badge.** `design/PROGRESSION.md` says Tier 1 reaches Level 7 observation area; the PTKW badge reaches the operational zone.
4. **Does the hatch re-enter?** Rania's hatch is described from Level 0 up; no document says the player can go down.

---

*→ See: design/PROGRESSION.md — the badges and what they open.*
*→ See: design/TIME_MODEL.md — the clocks.*
*→ See: canon/facility/Overview.md — the building structure.*
*→ See: canon/facility/Maintenance Network.md — the shortcut system.*
*→ See: design/HEALTH_SURVIVAL.md — the Medical Centre restriction.*
*→ See: design/LEVEL_BEAT_SHEETS.md — what each level asks.*
*→ See: design/PLAYER_GUIDANCE.md — how the player learns what is open.*
