# ICS — Rigged Sphere
## Failure Loop — Death, Capture, Retry

*Failure in this game is a document. The player is never told "you died." They are told what the system has done with them: a status updated, an asset reclassified, a window closed. The loop is built so that the wording is the punishment and the return is fast.*

*The design argument: the cost of failure is not time. It is the player's knowledge of how the building sees them. A death that is a quick reload and a sentence of clinical language teaches more than a game-over screen, and it never makes the player stop caring about the people in the story.*

---

## How to read this sheet

| Tag | Meaning |
|---|---|
| **Canon** | Already stated in an existing document. The source is named. |
| **[PROPOSAL]** | New. Needs sign-off before it becomes canon. |

---

## 1. The three failure states

| State | Trigger | Screen | Return | Source |
|---|---|---|---|---|
| **Standard death** | Physical Integrity reaches zero | Black. Asset number. *"Productive capacity fully realized. Asset status updated to Schedule D completion."* | Last autosave | **Canon** — `HEALTH_SURVIVAL.md` |
| **CRD-7R overexposure** | Neurological failure | Black. *"Neurological failure. Asset Wellness record updated."* | Last autosave | **Canon** — `HEALTH_SURVIVAL.md` |
| **EOD capture** | Mode B or C ends in capture, or Day 21 | The look, black, then a PTKW reclassification document for E-05682, dated and signed. Held for **8 seconds**. | Last autosave | **Canon** — `SAVE_SYSTEM.md`, `HEALTH_SURVIVAL.md` |
| **Omega-1 capture / window closed** | Phase 6 only | Current time in the 22-hour countdown, number of Phase 6 actions completed, *"The 22-hour window closed."* | Latest Phase 6 autosave, or *"Day [X] — Last Entry"*. The clock is restored from the save. | **Canon** — `SAVE_SYSTEM.md`, `HEALTH_SURVIVAL.md`, `ENEMY_AI.md` |

Detection by PTKW is **not** a failure state by itself. It is a rise in alert state (0–3) that the player can escape. Failure follows only if the escape fails. (`STEALTH_DETECTION.md`)

---

## 2. The retry flow

**[PROPOSAL]** One path for every failure state, so the player always knows what the next ten seconds look like.

| Step | Time | What the player sees | Skippable? |
|---|---|---|---|
| 1. Cut | 0–1 s | Picture cuts to black. No music sting, no sound effect other than the room tone fading out. | No |
| 2. Document | 2–8 s | The status line or reclassification document. | Standard: not for the first reading of each type. After that, yes (see Part 5). |
| 3. Reload | ≤ 6 s | The autosave loads. A single line: the badge clock. | No |
| 4. Return | 0 s | The player is in control. Inventory, flags, world state exactly as of the autosave. | — |

**Total target from failure to control: ≤ 15 seconds** (≤ 10 s with the capture screen shortened — see `DIFFICULTY_ACCESSIBILITY.md`, "Capture screen length").

There is no "Continue / Load / Quit" menu on failure. The game returns the player directly. The pause menu is available as always (`UI_MENUS.md`).

---

## 3. What the player keeps and loses

**Canon:** The player returns with *"the same inventory, the same flags, the same world state as of the last autosave."* (`SAVE_SYSTEM.md`)

| Kept | Lost |
|---|---|
| Nothing of the failed attempt. | Anything the player did since the autosave. |
| **[PROPOSAL]** One piece of knowledge, not state: the badge's *Previous attempts* counter (see Part 4) increments. | — |

The autosave fires at room transitions, item pickups, document reads and conversation branches (`SAVE_SYSTEM.md`). The ceiling is 3 minutes of lost play. The conversation autosave means that no conversation outcome can be undone by a failure.

---

## 4. Target fail rate

**[PROPOSAL]** A single number per phase, so tuning has something to aim for. "Failure" here means any of the failure states in Part 1, per attempt at a section of roughly 10 minutes.

| Phase | Target failures per section (first-time player, default preset) | Intent |
|---|---|---|
| 0 | 0 | There is no failure in Phase 0. |
| 1 | 0 | Confinement. The PTKW pass is a clock, not a threat. |
| 2 | 0–1 | The first reclassification screen should be rare enough to be a shock. |
| 3 | 0–1 | The Level 0 first visit has no enemy. The cold is the only cost. |
| 4 | 1–2 | Learning to treat PTKW triples as geometry. |
| 5 | 1–2 | NPC obstacles are social, not lethal. Most failures are EOD or Level 5. |
| 6 | 1–3 | The 22-hour window allows for reloads, because the clock is restored from the save. |

**Hard ceiling:** if a player fails the same section **four times in a row**, the game offers help (Part 5). It never lowers the difficulty silently.

---

## 5. When the player is stuck

**[PROPOSAL]** Help escalates through information, not through power. This follows the principle in `DIFFICULTY_ACCESSIBILITY.md`: the game tells the player more, it does not weaken the world.

| Failure count (same section) | What happens |
|---|---|
| 1–2 | Nothing. |
| 3 | The badge's *Previous attempts* line shows the count. No suggestion. |
| 4 | A one-line prompt on the next return: *"Detection overlay available in Accessibility."* A link to the setting, not the setting itself. |
| 5+ | **Capture screen shortened** is offered once. If accepted, it stays on. |

**Never done:** no "skip this section," no invincibility, no checkpoint-nearer option, no hint that names the solution. The Solution Matrix exists so that designers know the answer; the player finds it. (`SOLUTION_MATRIX.md`)

EOD cannot be beaten at any setting. Failure against him is not a skill check. Capture rates are in `EOD_ENCOUNTERS.md`.

---

## 6. Where failure must not happen

| Place | Rule |
|---|---|
| Level 0, first visit | No enemy. No failure state is reachable except the cold. If Thermal Regulation reaches zero, the player is carried to the hatch warmth and loses time, not progress. **[PROPOSAL]** |
| Level 4, any phase | No combat. The only threats are people the player knows. |
| The conversation autosave | No failure inside a conversation. |
| The window at 06:00 in Phase 6 | The Earth View Window is not a trap. |
| Tutorial Beats 1–8 | No failure state exists before Phase 1. |

---

## 7. The reload and the narrative

The reclassification document uses the player's real asset number (E-05682) and the real date in Branch Time. The date after Day 61 is the Phase 6 date. In Phase 6, the screen on Omega-1 capture changes: *"The 22-hour window closed."* instead of the reclassification language. (`HEALTH_SURVIVAL.md`)

**[PROPOSAL]** After the third reclassification screen of a playthrough, the wording varies slightly: the *date* changes to whatever Branch Time was at capture. The player begins to read it as a log of their own attempts. The building has a record of every one.

---

## Open questions

1. **Failure count persistence.** Should *Previous attempts* survive a quit-to-menu? **[PROPOSAL]** yes within a session; reset on a new load.
2. **Phase 6 reload and the 22-hour clock.** Canon says the clock is restored from the save. Does a failure still cost the player *real* time, as `SAVE_SYSTEM.md` implies? **[PROPOSAL]** yes: real time spent is the cost; the in-fiction clock does not advance.
3. **Capture screen first-time skipping.** The 8-second hold is canon. Should it be skippable on the second view of the *same* document? **[PROPOSAL]** yes, after the first full reading.
4. **Numerical fail rates** are placeholders. They need playtest data.

---

*→ See: HEALTH_SURVIVAL.md — the death states and the four tracks.*
*→ See: SAVE_SYSTEM.md — autosave triggers, the 8-second screen, Last Entry.*
*→ See: ENEMY_AI.md — Omega-1 and PTKW behavior.*
*→ See: EOD_ENCOUNTERS.md — capture flow and target capture rates.*
*→ See: DIFFICULTY_ACCESSIBILITY.md — the options this sheet offers.*
*→ See: UI_MENUS.md — the pause and load screens.*
*→ See: TENSION_CURVE.md — how failure sits in the pacing.*
