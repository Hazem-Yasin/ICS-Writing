# ICS: Interplanetary Corporate Solutions
## Enemy AI — Behavioral States & Detection Design

*This document covers how every enemy category behaves in the game — patrol patterns, alert states, pursuit logic, and how the player interacts with detection. The design must be consistent with who these enemies are: compliance officers, grieving loyalists, and interplanetary enforcers — not generic guards.*

---

## Core Detection Architecture

Every enemy has three detection inputs, all tied to existing world systems:

**1. Visual detection** — line of sight, lighting level, distance. Standard.

**2. EIMU detection** — the facility's ambient sensor network reads badge EIMU signals. An enemy with a monitoring device (K-7 equivalent in the field, or a PTKW officer with a handheld monitor) can detect the player's EIMU signature even without visual contact — if the player's badge sensor is active, they are detectable through walls. This is the ICS-specific stealth layer. A stripped badge eliminates this entirely. An EIMU-Jammer broadcasting false compliance eliminates it differently.

**3. Sound** — footsteps, tool noise, steam releases, badge reader activations. Each action has a radius. Standard stealth game acoustic model.

### The Alert State Ladder

All enemy categories share the same four-state alert system, with different *responses* per category:

**State 0 — Unaware.** Normal behavior. Not searching.

**State 1 — Curious.** Something triggered a minor detection input. The enemy investigates the last known position. If nothing is found in 20 seconds, returns to State 0.

**State 2 — Alert.** Confirmed detection of the player or a significant anomaly. Calls for backup (CCN ping — meaning K-7/K-12 monitoring receive the flag and log it). Pursues. Does not return to State 0 until the player is either caught or breaks line of sight for 45+ seconds in an unmonitored zone.

**State 3 — Pursuit.** Active chase. Calls for additional personnel. This state does not resolve until the player is caught, the enemy is incapacitated, or the player reaches a Type B/C maintenance passage (which security personnel do not enter in Phases 2–4 — they are not equipped or trained for it).

---

## Category 1 — PTKW Security Division

### Phase 2 (EOD active)

**Patrol behavior:** Two-person pairs. Fixed routes on Levels 2–6, timed to 8-minute cycles. The routes are in Document 2.36 (Floor Plans) — the player can find the schedule if they read the maintenance overlap notes carefully. Routes favor main corridors; they do not enter maintenance network Type B passages.

**Detection:** EIMU-primary at long range (badge sensor through walls, up to 15 meters). Visual primary at close range. ACS-9 units are not carried in Phase 2 — the compliance atmosphere is managed at the behavioral level.

**State 0 behavior:** Walking the route. Occasionally pausing at AIDEN posters (the AIDEN units report to them, not the reverse — but they check the status lights). Talking quietly to their patrol partner in a language the player cannot understand.

**State 1 behavior:** One officer investigates. The other holds position and watches the corridor behind them.

**State 2 behavior:** Both officers converge on last known position. CCN ping generated. Corridor doors in that zone go to restricted mode (badge reads become logged, wellness integration doors lock).

**State 3 behavior:** Calls additional pair. CRD-7 drawn. Does not enter Type B passages. If the player is cornered: CRD-7 contact, not lethal force — still in compliance mode.

**Phase 3 (silence period):** Reduced presence, slower routes, longer pauses. The 10-day pressure period means security officers are themselves in an unusual emotional state — EIMU readings on security personnel during Phase 3 show elevated Anticipation: Vigilance. They are not comfortable. Some of them linger at windows.

**Phase 5 (revolution):** Patrol discipline breaks down. Some officers maintain routes mechanically. Some have abandoned routes and are holding fixed positions near key corridors (Level 5 entrance, transit wing). Some are visibly doing nothing — standing at their post, not responding to non-critical CCN pings. The player can identify which officers are still operational by their body language and position relative to their scheduled route.

### Phase 4 (Return) — High-Intensity Configuration

Security pairs become security triples. ACS-9 units are now carried. Detection radius increases. Routes are tightened to cover more of the Level 3–5 zone. This is the most dangerous patrol configuration the player faces before Phase 6.

**EOD's advance team** (Phase 4 specifically): Not standard security. Two Omega-adjacent assets deployed ahead of EOD's public reappearance to sweep specific locations including Level 0 approach areas. They do not follow the standard patrol pattern. They are on a task-specific route that the player cannot find in any document — it was issued verbally. They are detectable through standard methods but are faster-moving, have shorter investigation windows before escalating to State 2, and will enter the Level 0 stairwell (unlike standard security).

---

## Category 2 — True Believers (Marcus, Lani, Cho)

True Believers are **not combat enemies**. They are dynamic obstacles with human behavior patterns.

### Marcus (Phase 5 forward)

**Movement:** Marcus moves between his regular locations — cafeteria, Level 4 work floor, Level 4 Earth View Window. His movement schedule is partially predictable (he eats at the same time, goes to the window in the morning) and partially not (Phase 5 disrupts his routine — he appears in unexpected locations, including the Level 3 maintenance corridor entrance, at unpredictable times).

**Detection:** Line of sight only. No EIMU monitoring capability. No radio. He cannot call security.

**State 0:** Moving between locations, head down, clearly processing something. Not looking for the player.

**State 1:** He sees the player somewhere unexpected. He stops. He makes eye contact. He does not immediately pursue — he stands there, working out what he's seeing and what it means.

**State 2:** He follows the player and attempts to speak to them. This is not an attack. It is a conversation trigger. If the player stops: the Marcus conversation scene activates. If the player keeps moving: he follows for approximately 60 seconds before stopping and watching them go.

**The conversation (State 2 trigger):** The hardest conversation in the game. Marcus is not an enemy in the conventional sense. He is someone trying to understand what the player is doing. The conversation can end three ways: the player explains nothing (he lets them go, files a mental note he doesn't act on), the player lies to him (he believes it, he lets them go, the lie costs something in Phase 6 — Marcus's willingness to help is reduced), or the player shows him the Board Governance Charter section they've read (the Marcus arc moment — he goes to the atrium with the document).

**Blocking behavior (Phase 5, specific locations):** At the Level 3 maintenance corridor entrance and near the transit corridor, Marcus positions himself without knowing why. He is an obstacle the player must route around or engage.

### Lani (Phase 5) and Cho (Phase 5)

**Lani:** Counter-group organizer. Stays in the cafeteria. Does not pursue. Does not block routes. Is a presence — her group eating lunch while the revolution builds around them is visible on camera feeds the player can observe. She is not a threat. She is a reminder of what the compliance architecture made.

**Cho:** Waits near the PTKW floor entrance in Phase 5. If the player approaches: he tries to talk to them, asks if they have PTKW access. He wants to volunteer. He is not hostile. He is in the way. A single calm exchange ("I'm just passing through") resolves him — he accepts this, returns to waiting.

---

## Category 3 — Arrangement Class

### Dayo (Phase 4–5)

Dayo is the hardest to avoid because he has **no aggressive state**. He does not pursue, does not call security directly, does not physically obstruct. He observes and files reports.

**Detection method:** Dayo is always in places he has a reason to be. He files facilities reports about things he notices. The player is not aware of his reports until they read the PTKW intercept archive — by which point the reports are already filed.

**How the player identifies him:** PTKW intercepts in the archive show a pattern — a Level 4 Operations employee filing detailed facilities observations at unusual times. The player connects the pattern to the man they've seen in the same corridors. It is never announced. The player has to read it.

**Confrontation mechanic:** If the player gets within conversation range of Dayo and initiates contact, a unique interaction triggers. Dayo is nervous. He knows who the player is — his files on K-7 told him. The player can: (a) ignore him (he files a report), (b) threaten him (he files a report immediately and PTKW is alerted), (c) tell him K-7 has received a conduct notation and is under review (his arrangement loses its guarantor — he sits with this information for a long time). Option (c) changes his Phase 6 behavior.

### Priti (Phase 5)

Priti operates in the maintenance network specifically. She knows the player uses it — her facilities reports showed the warm panel patterns. In Phase 5, she enters the maintenance network on the Level 3-to-Level 1 route to file a direct observation report.

**The encounter:** The player and Priti meet in the Type A maintenance corridor — a space too narrow to pass without acknowledging each other. Priti doesn't have a weapon. She has a personal device on which she is actively typing a report.

**Resolution options:** The player can pass her without confrontation (she completes the report — a PTKW flag triggers in 3 minutes), use the EIMU-Jammer to flood the area with a false compliance reading that confuses her about what she's seeing, use the ACS-9 to produce the presence-feeling that makes her want to leave the corridor, or — simply speak to her. Priti is protecting her husband. The player knows this from the archive. They can tell her that her husband's review has been in the open backlog for two years and has no active reviewer assigned to it. Her arrangement may already be hollow. She takes that information and sits with it, mid-corridor.

---

## Category 4 — Omega-1 Assets (Phase 6 only)

Omega-1 are not designed for encounter. They are designed for avoidance.

**Detection:** Full-spectrum. Visual, EIMU, acoustic, and a fourth detection mode the player has no documentation for — it is the first thing in the game that the compliance architecture documents don't cover. They find the player even with a stripped badge, even with the EIMU-Jammer running, if the player stays in range long enough. The detection is not magic — it is technology the player has no counterintelligence for.

**Behavior:** They move in structured sweeps. Not patrol routes — geometric coverage patterns that clear a defined area completely before moving to the next. The player can observe the edge of a sweep from a Type C crawlway and time the movement to the next zone.

**The one gap:** If the player used the Level 0 device in Phase 5 and sent a message, one Omega-1 sweep is 12 minutes late to a specific corridor. This is the only window the game provides for direct Omega-1 avoidance. The player must have done the thing in Phase 5 to have access to the gap in Phase 6.

**What happens if caught:** Not health damage. The run-ending capture screen: the reclassification document, the date, the asset number — the same screen as EOD capture. The player then reloads the latest Phase 6 autosave or the *"Last Entry"* save (see design/SAVE_SYSTEM.md and design/HEALTH_SURVIVAL.md).

---

## Stealth Rules Summary

| Enemy | Primary Detection | Maintenance Network | EIMU Jamming Effect | ACS-9 Effect |
|---|---|---|---|---|
| PTKW Security | Visual + badge EIMU | Won't enter (Phases 2–4) | Hides player from EIMU scan | Produces discomfort, shorter patrol stays |
| EOD advance | Visual + badge EIMU | Will enter stairwell | Partial reduction | Felt, acknowledged, not decisive |
| True Believers | Visual only | Won't enter | No effect | No effect |
| Arrangement Class | Observation + reporting | Priti will enter | ECT-4C confuses observation | Produces desire to leave area |
| Omega-1 | Full-spectrum + unknown | Can enter all passages | Partial reduction only | Minimal |

---

*→ See: canon/weapons/compliance/ — the tools used against each enemy category.*
*→ See: canon/enemies/ — the full lore profile for each category.*
*→ See: design/HEALTH_SURVIVAL.md — what happens when detection results in direct damage.*
