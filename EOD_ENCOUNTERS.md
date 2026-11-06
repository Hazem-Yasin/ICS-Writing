# ICS — Rigged Sphere
## EOD Encounter Design

*He cannot be fought, he cannot be outrun, and he is not a boss. He is a condition of the building that sometimes takes a shape. This sheet says when that shape is on the screen, what the player can do about it, and what it costs when they can't.*

*The design argument: EOD frightens the player in proportion to how little the game does with him. Each scene below is built to give him less to do than a normal enemy, not more. Every encounter is about who is in the room with him, not about him.*

---

## How to read this sheet

- **Canon** is tagged with its source. **[PROPOSAL]** marks anything new.
- Dates follow `TIME_MODEL.md`. He is on the floor Days 4–10 and Day 21 only.
- "Encounter" means the player and EOD are in the same space or the player can see him. A report that he has been somewhere is not an encounter.

---

## 1. What canon fixes

| Fact | Source |
|---|---|
| Not an employee. No badge. Looks human, tall, modified senior-management attire. | `characters/EOD.md` |
| Cannot be defeated in combat. A lore decision. | `weapons/OVERVIEW.md` |
| Cruelty is deliberate, excessive and visible. | `characters/EOD.md` |
| First appears on a Level 2 corridor. No announcement. | `DESIGN.md`, `characters/EOD.md` |
| Arrives Day 4. Enters via Level 7 → 10 → Board elevator, quartered on Level 13. | `facility/Levels 11-14.md` |
| ACS-9 affects him: he understands the mechanism and still feels it. | `weapons/compliance/ACS-9 — Acoustic Compliance System.md` |
| Capture is "processed," not death: a PTKW reclassification document for E-05682, dated, signed. | `HEALTH_SURVIVAL.md`, `SAVE_SYSTEM.md` |
| Capture screen is shown for 8 seconds, then the last autosave loads. | `SAVE_SYSTEM.md` |
| Sweeps Level 0 in Phase 4, dwell time anomalous, 11 minutes alone. | `weapons/modifications/ACS-9RS — Resonance Shell.md` |
| Atrium act on Day 21 at 08:17. Yaw. | `STORY.md` §III |
| Sent back to the docking bay at 14:30. | `STORY.md` §III |
| Score 81+ on the CCN anomaly scale triggers EOD notification in Phases 2–4. | `STEALTH_DETECTION.md` |

---

## 2. The three modes **[PROPOSAL]**

EOD behaves in exactly one of three modes. The game never mixes them. Each one is a different kind of dread.

| Mode | What it is | Phases | Where the player is |
|---|---|---|---|
| **A. Demonstration** | He does something to someone else, in public. The player watches. | 2 (Days 4–10), 4 (Day 21) | A bystander, 15–40 m away |
| **B. Pressure** | He is not seen. The facility behaves as if he is. | 3 | Anywhere |
| **C. Pursuit** | He is looking for the player specifically. | 2, 4 | A target, in a scripted set piece |

*There is no free-roaming EOD. A roaming threat would turn him into an enemy. He would become the thing the player learns to out-pattern. Canon says he can't be learned.*

---

## 3. Phase 2 — Days 4–10

### 3.1 What the player is doing

Phase 2 is confinement-adjacent. The player has the quarters panel and the maintenance network. They are not in the open facility on their own errands. They are watching.

### 3.2 The encounter structure

Four fixed beats and two optional ones. The beats are tied to Days, not to player progress; the game offers the slice and the player chooses whether to be present.

| Day | Beat | Mode | Location | The player's role |
|---|---|---|---|---|
| 4 | **First sight** | A | Level 2 corridor | Seen from the end of the corridor, or via the live feed through the maintenance panel. He walks past a manager office. Nothing happens. A manager's glass goes from clear to frost. |
| 5 | **The corridor** | A | Level 3 main corridor | He stops beside a work-floor door and waits. A person inside is called out by name. The player hears it from a pod. |
| 6 | **The reflection** | A | Level 4 window corridor | Darius sees him in the glass (`scene-notes/Earth View Window.md`). The player may be on the bench. |
| 8 | **The officer** | A | Level 2 | Marcus tries to speak to a PTKW officer. EOD is in the background and never turns his head. |
| 9 | **The panel** *(optional)* | C | Level 3 service corridor | He walks the maintenance corridor entrance once, slowly, with a PTKW pair. The player is in the passage. |
| 10 | **The exit** *(optional)* | A | Level 5 → Level 2 elevator | Last sighting. He is going up. |

### 3.3 Rules for Mode A (Demonstration)

- **The player is never the target.** In Phase 2, EOD uses people the player has met or could meet. The cruelty falls on others. This is canon (`characters/EOD.md`: "it costs the people around the resistors, not just the resistors themselves").
- **The player can stay or leave.** The camera does not lock. Leaving is always possible and costs nothing in the system.
- **The player can intervene only by not being seen.** Throwing a tool or using the ACS-9 makes things worse. The ACS-9 effect, if used from a distance, makes EOD slow for 3 seconds and look toward the source. If the player's position is not in cover, that is Pursuit.
- **No countdowns.** There is no timer. The scene ends when it ends.

### 3.4 Rules for Mode C (Pursuit) in Phase 2

Two optional beats only (Day 9, Day 10). They are **scripted evasions, not chases.**

- EOD walks a **fixed route** at a fixed pace (walking, never running). He stops at three points.
- The player's job is to be somewhere else. Routes: a Type B passage (he does not enter, canon: `STEALTH_DETECTION.md`), a Type C crawlway, or a locked room with a closed door.
- If the player is **seen**, there is a 4-second beat where he looks at them. If the player holds still, the beat ends. If the player runs, **capture** (§6).
- If the player is **not seen**, nothing happens. No success message.
- Max one Pursuit encounter per slice. No Pursuit within 20 minutes of play of another high-tension beat (`TENSION_CURVE.md`).

### 3.5 The CCN trigger

At anomaly score **81+** EOD is notified (`STEALTH_DETECTION.md`). In Phase 2 this converts the next Mode A beat into Mode C: the same location, but he is looking. This is the only way score matters to him.

---

## 4. Phase 3 — Days 11–20: silence

He is gone. That is the design.

- **No encounter.** Not one.
- **Pressure only (Mode B).** The facility carries him: PTKW patrols are slower and linger at windows (`ENEMY_AI.md`). EIMU readings show distributed Anticipation: Vigilance.
- **One rumour per slice [PROPOSAL].** A cleaner mentions the Level 13 elevator light. A manager stands still in a corridor. A dropped cup. No dialogue about him.
- **Player-readable evidence:** the Level 7 → 10 elevator log; the Level 13 quartering note in `facility/Levels 11-14.md`.
- **Level 0 (Day 15–16).** EOD's Phase 4 sweep has not happened yet. Level 0 is clean and cold and untouched.

*The design argument: if he is absent for ten days, the player learns the facility is EOD. The silence is the encounter.*

**Off-facility event [PROPOSAL, no encounter].** On Day 16 (Thursday, 00:20) EOD carries out his own demonstration against a host-nation special-operations unit (Blue Harrow Team, Sudbury; one of the six assault teams of the Harrow, Document 2.47). The player is never present. The player may find it afterwards as evidence only: C-19 (the Branch Manager's update, the Research Team's field report and the survivor's transcript). It is a Phase 3 find, not a Phase 3 scene. The silence stays intact; the player learns what the silence cost somebody else. Source for the Day 16 date: `internal-communications/branch-director/C-19`.

**Second off-facility event [PROPOSAL, no encounter].** On Day 18 (Saturday, 03:09–03:21) a Gyrfalcon Wing pilot has twelve minutes of radio contact (Gyrfalcon One of a four-aircraft flight; Document 2.48) with something that does not identify itself. There are no casualties and no violence. The player finds it only as the cockpit and radio transcript in `internal-communications/branch-director/C-20`, which also corrects C-19: this one was not ARM-27's, and the Research Team's interest reading for it was baseline.

**Third off-facility event [PROPOSAL, no encounter, and a break in the silence].** On Day 21 (Tuesday, 02:44–03:59 local, over open water and at Hallvik) both Gyrfalcon alert flights, eight aircraft, engage EOD and ARM-27. All eight pilots die. The air engagement is in `internal-communications/branch-director/C-21`. The tower scene that follows — EOD and ARM-27 standing on the apron, EOD entering the cab and speaking plainly to Colonel Leif Aronsen (`characters/Colonel Leif Aronsen.md`), whose son Captain Eirik Aronsen (`characters/Captain Eirik Aronsen.md`) is Gyrfalcon Seven — is in `internal-communications/branch-director/C-22`. The player is never present for either. They find them only as recordings. Two things about the tower scene break the rules this sheet sets for him:
- **He explains.** Sudbury and Day 18 gave the witness nothing to repeat. Hallvik gives the witness a statement ("downsizing", "branch sunsetting"). C-21 itself notes that this contradicts the method of Section 2.10. Open ruling 25 in `HANDOFF_CARTOGRAPHER.md`.
- **He is working on the morning he returns.** The tower scene ends at 03:59 local. The atrium act begins at 08:17 Branch Time. The Branch Manager notes the gap and offers no mechanism.
The player-facing effect is unchanged: the silence in the facility is intact, and the cost is carried by a stranger.

**One human answers him [PROPOSAL].** On the air engagement recording, Captain Eirik Aronsen (Gyrfalcon Seven) tells his father that the contact is coming back and that he is dead and knows it, then tells the species to be afraid and to proceed despite being afraid (`internal-communications/branch-director/C-21`, 03:33:53 and 03:33:57). The Research Division's study of fear (Document 2.18, Section 2.10) predicted a sudden and unquestioned surrender. It was refused once, on tape. After his return EOD tells the Research Team that the Captain smiled while he was taken to the sea, and that he does not think humans can be controlled. Why was he smiling? The Team seals the question in Document 2.49, "The Study of Eirik's Smile", readable only by the Research Team, the Earth Branch Manager and EOD, and tells PTKW the mission was complete. The player finds all of it as text only, and only in the sealed files. Open ruling 25 in `HANDOFF_CARTOGRAPHER.md`.

---

## 5. Phase 4 — Day 21: the atrium

### 5.1 The morning (Mode A, the longest set piece)

The player is present for the atrium act from a position of their choosing. **[PROPOSAL]** The game offers four vantage points.

| Vantage | Where | What the player sees | What it costs |
|---|---|---|---|
| Mezzanine rail | Level 2 | The whole act from above, 14 m | Visible to EOD if they lean over |
| Atrium floor | Level 1/2 | Yaw's face, the badge reader | In the crowd; cannot leave quickly |
| HR glass wall | Level 2 | The PWRP terminals in foreground | Safe, but only see through glass |
| Feed only | Maintenance panel | The room as the live feed shows it | No emotional presence, but allowed |

- **What happens is canon** (`STORY.md` §III): the badge reader on the pillar activates, Yaw reads his classification, EOD waits, speaks in a voice only Yaw hears, Yaw leaves with him. The letter stays on the chair.
- **The player cannot change it.** There is no branch. No tool works. The ACS-9 has no effect on the outcome; used, it makes Yaw look at the player.
- **Marcus and the letter.** If the player is on the floor, Marcus picks up the letter after. If they speak to him he says nothing. The printer beat follows in the afternoon.
- **Everything is on the live feed.** Even a player in the feed-only vantage sees it. The act is for the audience.

### 5.2 The afternoon (Mode B → C)

- **14:30:** EOD is sent back to the docking bay by the Branch Director (`STORY.md`). The player can see the corridor to the bay from Level 1.
- **The advance team (Phase 4)** is the only pursuit-like element on Day 21. Two Omega-adjacent assets sweep Level 0 approach areas (`ENEMY_AI.md`). **They are not EOD.** They are EOD's hand and the player's real problem.
- **Level 0.** EOD himself enters Level 0 *alone* after the sweep and stays 11 minutes (`ACS-9RS` file). **[PROPOSAL]** The player can hear this from Type C crawlway under the grating. They cannot see it. They hear a voice. They do not hear what it says.

*The 11 minutes on Level 0 are the closest he gets to the player.*

### 5.3 Day 22, 08:00

The speech. He is not present. The Branch Director is.

---

## 6. Capture — the processing flow

### 6.1 What triggers it

| Trigger | Phase | Notes |
|---|---|---|
| Seen and ran during a Mode C beat | 2, 4 | Run = admission |
| Seen in a Mode A beat from a bad vantage and the player acts | 2, 4 | E.g. ACS-9 thrown at him |
| Entered Level 0 while the advance team is present and not hidden | 4 | The advance team is the enforcer; EOD is the sign |
| Caught by a PTKW triple after score 81+ in Phase 4 | 4 | Caught by security; delivered to him |

### 6.2 The sequence

1. **The look.** EOD turns to face the player. No music. Silence.
2. **The nothing.** He does not speak. He does not move closer. Four seconds.
3. **The fade to black.** No sound.
4. **The document.** A PTKW reclassification document for E-05682, dated, signed, in the facility's standard format. Eight seconds (`SAVE_SYSTEM.md`).
5. **The reload.** The last autosave loads. The player's inventory, flags and world state are as at that save.

### 6.3 What is not in the flow

- **No health bar damage.** Capture is not a death state (`HEALTH_SURVIVAL.md`).
- **No cutscene of violence.** The document is the scene.
- **No "tips" screen.** The document is the tip.
- **No penalty.** The wait is the cost.

### 6.4 Failure rate target **[PROPOSAL]**

| Beat | Target capture rate (first attempt, median player) |
|---|---|
| Phase 2 Day 9 pursuit | 25% |
| Phase 2 Day 10 pursuit | 15% |
| Phase 4 advance team sweep | 35% |
| Phase 4 Level 0 sequence | 30% |

*See `FAILURE_LOOP.md` for the retry rules and the overall fail-rate budget.*

---

## 7. Tools vs. EOD

| Tool | Effect | Cost |
|---|---|---|
| ACS-9 | Slows him for 3 s at 8 m; he turns toward the source | Reveals position |
| ACS-9D | 25° beam, 22 m range, same effect | Same |
| ACS-9RS | Charges a space for 40–60 min; he feels watched in it. He spends 11 min where he would have spent 7. | Needs Junction C and 50 min |
| EIMU-Jammer | He is not tracked by badge. Jammer affects only the advance team's monitor. | None |
| CCN-Spoofer | Spoofs a position report; creates a 40-minute gap in the reported location | 1 spoof session |
| Olfactory Canister (OLF-14) | EIMU Maximum for 8 min, **including EOD** (canon: `weapons/improvised/Olfactory-Canister.md`) | Single canister, found at Level 0 |
| CRD-7 / AMB-3 / Fragment Launcher | **No effect.** | The attempt is a capture trigger |

*OLF-14 is the only item canon says reaches him. **[PROPOSAL]** If used, he stops for 8 minutes in the middle of a corridor, face blank, then resumes without comment. The player is not captured. The player is the only one who saw.*

---

## 8. What must not happen

- No health bar or visible HP on EOD.
- No "cannot be seen" cheat. He is always on screen when he is on screen.
- No chase music. If there is music at all, it is the facility's absent music.
- No boss fight, no phase two, no final confrontation. The 22 hours are the last thing between them (`weapons/OVERVIEW.md`).
- No EOD in Phase 5. In Phase 5 he is absent. The system has no enforcer left; that is the point.
- No EOD in Phase 6. Omega-1 replaces him.

---

## 9. Open questions

1. Does Mode C (Pursuit) belong in Phase 2 at all, or is Mode A enough? **[PROPOSAL]** Keep two optional beats; remove if playtests show the player is relieved rather than frightened.
2. Is there an EOD scene in Phase 5 Day 44 (the cascade)? **[PROPOSAL]** No. Silence.
3. Can the player see his face? Canon says he looks human. **[PROPOSAL]** Seen at distance and in reflection only. No close-up until the end of the game, if at all.
4. Is the Level 0 11 minutes shown from the crawlway, or not at all?

---

*→ See: characters/EOD.md — profile.*
*→ See: internal-communications/branch-director/C-21 — the open water air engagement, Day 21.*
*→ See: internal-communications/branch-director/C-22 — the Hallvik tower report, Day 21.*
*→ See: weapons/OVERVIEW.md — "cannot be defeated."*
*→ See: ENEMY_AI.md — advance team, patrol configurations.*
*→ See: STEALTH_DETECTION.md — anomaly scores and zones.*
*→ See: SOLUTION_MATRIX.md — Obstacle 3, the advance team.*
*→ See: TENSION_CURVE.md — Phase 2–4 intensity.*
*→ See: TIME_MODEL.md — the Day 4–10 / Day 21 timeline.*
*→ See: HEALTH_SURVIVAL.md — the capture state.*
*→ See: SAVE_SYSTEM.md — the reload.*
*→ See: FAILURE_LOOP.md — retry flow.*
*→ See: STORY.md — the Day 21 atrium.*
