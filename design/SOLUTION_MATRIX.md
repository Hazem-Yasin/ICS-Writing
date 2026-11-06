# ICS — Rigged Sphere
## The Solution Matrix — Many Ways Through, None of Them Clean

*Every obstacle in the facility has more than one answer. None of the answers is free, and none of them is "kill it." This sheet lists the obstacles the design documents already contain, the tools and verbs that answer each, and what each answer costs.*

*The design argument: the player should finish a hard moment thinking "I could have done that differently," not "I found the one thing the designers wanted." The cost column is what makes the choice real. A solution with no cost is not a solution. It is a shortcut, and shortcuts teach the player to stop reading.*

---

## How to read this sheet

- **Obstacle** — something in the way, taken from the existing enemy, detection, facility or NPC documents.
- **Answer** — a verb or tool the existing documents already give the player. Nothing here adds a tool.
- **Cost** — what the player pays. Costs use the game's real currencies: noise, EIMU signature, CCN Anomaly Score, time, inventory slots, and Phase 6 consequences.
- **Lethal?** — whether the answer can kill. Almost always no.
- **[PROPOSAL]** marks an answer or number that is not in the source documents.

Source documents: `design/ENEMY_AI.md`, `design/STEALTH_DETECTION.md`, `canon/weapons/`, `design/INVENTORY.md`, `design/NPC_COMPANIONS.md`, `canon/facility/`.

---

## The matrix at a glance

Rows are answers. Columns are obstacles. A filled cell means the answer works, and the letter shows how: **S** = stealth, **D** = diversion, **P** = power, **T** = talk, **K** = knowledge/information, **—** = does not work.

| Answer ↓ / Obstacle → | PTKW pair | PTKW triple + ACS-9 (Ph 4) | Advance team (Ph 4) | Badge-gated door | CCN node field | Patrol sweep | True Believer | Arrangement Class | Omega-1 | Manifest check |
|---|---|---|---|---|---|---|---|---|---|---|
| Crouch / shadow | S | S | S | — | — | S | S | S | — | — |
| Type B/C passage | S | S | S (stairwell: no) | S | S | S | S | S (Priti enters A) | C only | — |
| Stripped badge (4 min) | S | S | S | — | S | S | — | — | partial | — |
| EIMU-Jammer T1 | S | S | partial | — | S | S | — | — | partial | — |
| EIMU-Jammer T2 | D | D | partial | — | D | D | — | — | — | — |
| ACS-9 | D | D | felt only | — | — | D | — | D | minimal | — |
| CRD-7 T1/T2 | P | P (risk) | P (risk) | — | — | — | — | — | — | — |
| CRD-7 T3 | T/K | T/K | T/K | — | — | — | — | — | — | — |
| AMB-3 decoy | D | D | D | — | D | D | — | — | — | — |
| AIDEN decoy | D | D | D | — | D | D | — | — | — | — |
| Steam / pipes | D | D | D | — | — | D | — | — | — | — |
| Olfactory canister | D/S | D/S | D/S | — | — | D/S | — | — | — | — |
| CCN-Spoofer | — | — | — | — | K/D | K/D | — | — | — | — |
| Talk / show document | — | — | — | — | — | — | T | T | — | — |
| Maintenance Bar T2 | D | D | D | S (power cut) | — | D | — | — | — | — |
| Leave the item at home | — | — | — | — | — | — | — | — | — | S |

*The matrix is a design aid, not a promise. A cell marked "—" is a deliberate absence, not a gap.*

---

## Obstacle 1: A PTKW pair in a corridor (Phases 2, 3, 5)

**What it is:** Two officers on an 8-minute route. Walking, quiet talk, occasional pause at an AIDEN poster. State 1 sends one officer; State 2 sends both and locks the corridor doors to restricted mode. They do not enter Type B passages. (`design/ENEMY_AI.md`)

| Answer | How | Cost | Lethal? |
|---|---|---|---|
| **Wait** | Read the route (Document 2.36), cross when they pass | Time | No |
| **Crouch past** | Crouch radius 1.5m; stay out of line of sight | Slowness; risk if the lighting is Standard (18m) | No |
| **Go around** | Type B passage or Level 3 service-corridor gap | Cold, EIMU Coherence if long | No |
| **EIMU-Jammer T1** | Broadcast "Compliance: High" | 8m click-and-hum; Phase 5+ officers recognize jammer interference | No |
| **ACS-9 Position 1** | Gradual discomfort; they drift away | Slow, gives a visible "wrong feeling"; may draw a third officer later | No |
| **Steam, valve 2-J-7** | Clears the corridor for 8s; seals adjacent doors for 90s | Noise; a second use in 24h raises a maintenance work order | No (moderate burn if close) |
| **CRD-7 contact** | 90s incapacitation | 20m noise; the officer's partner is awake; Physical and Neurological drain if misused | No |
| **CRD-7 T3** | Incapacitate, then ask questions | As above, plus the player must still leave | No |
| **Lethal mods** (CRD-7R, AMB-3F, BAR-FL) | Kills | Level 5 scanner flag; CCN score; the facility "noticed" | **Yes** |

**The design argument:** The cheapest answer is patience. The most expensive is violence. Everything in between trades noise for time.

---

## Obstacle 2: A PTKW triple with ACS-9 (Phase 4)

**What it is:** The most dangerous patrol before Phase 6. Three officers, ACS-9 carried, wider detection radius, tighter routes on Levels 3–5, CCN queue reviewed every 2 hours. (`design/ENEMY_AI.md`, `design/STEALTH_DETECTION.md`)

| Answer | How | Cost |
|---|---|---|
| **Stay out of Zone A** | Route through Type B/C and Zone C/D corridors | Time; thermal cost |
| **Stripped badge** | 4 minutes of EIMU invisibility | Closes badge doors; gap-log alert after 4 minutes |
| **Diversion** (EIMU-Jammer T2, AIDEN, AMB-3 decoy) | Pull them toward a false location | Each has an upkeep: jammer is audible to trained officers, AIDEN is a one-use position, AMB-3 needs a willing carrier |
| **Pressurized pipe, Junction 4** | Stall the freight elevator for 12 min; clears the Level 3 freight corridor | Maintenance technician comes after 12 min |
| **Olfactory OLF-11 reverse** | Flood Level 1 sweep with calm (Level 1 residential sweep only) | Level 1 only; 20 min; requires the unlabeled-conduit route |
| **Do not fight** | CRD-7 against three is a losing trade | — |

**[PROPOSAL]** — A triple has no single "stealth takedown" answer. The design intent is that the player cannot solve it by being strong. It is solved by being elsewhere.

---

## Obstacle 3: EOD's advance team (Phase 4)

**What it is:** Two Omega-adjacent assets. Task-specific route, issued verbally, so not in any document. Faster investigation windows. They **will** enter the Level 0 stairwell. One of them runs the badge manifest check. (`design/ENEMY_AI.md`, `design/INVENTORY.md`)

| Answer | How | Cost |
|---|---|---|
| **Pre-clear the badge** | Carry no contraband in the wrong slots | Fewer tools in the player's hand |
| **ACS-9 Position 3 at Level 0** (10+ minutes) | The team files "environmental anomaly — possible sensor interference" and does not return | Must be set up before Phase 4 starts; Position 3 cost (the player is also in range if near) |
| **Jammer** | Partial reduction only | Not decisive |
| **Hide in Type B/C** | They will not enter Type B/C in the field | Cold; Level 0 route is still Level 0 |
| **Do not meet them** | Everything else is secondary | — |

---

## Obstacle 4: A badge-gated door

| Answer | How | Cost |
|---|---|---|
| **Use the right badge** | Tier 2 / 3, PTKW (Phase 4), Director (Phase 5) | The badge is logged and each non-standard badge has its own problem (PTKW: visibly out of place) |
| **Go around via the network** | Type A/B/C passages | Cold; time |
| **Maintenance Bar T2** | Cut power to a floor section or trigger a local fire-door seal | Noise; local alarm |
| **Maintenance Bar T3** | Pry Level 0 panels | Level 0 only; Phase 6 use |
| **Tarek** | His keys; moving together lowers the anomaly weight | Needs the relationship built through Phases 2–3 |
| **Rania's keycard** | Opens the Level 1 utility alcove | One-purpose |
| **A dead employee's badge** | Does not work as a stolen badge | — |

---

## Obstacle 5: A CCN node field (Zones A and B)

**What it is:** Fixed nodes at 25m, 2m gaps in Zone A, 4–8m gaps in Zone B. The badge broadcasts position and stress signature throughout. (`design/STEALTH_DETECTION.md`)

| Answer | How | Cost |
|---|---|---|
| **Find the gap** | Level 3 service corridor gap; Diagnostic Accessory shows "---" when out of range | Time; needs the Accessory to see it |
| **Badge removal** | Signal stops | See Obstacle 2 |
| **EIMU-Jammer T1** | False compliance signal | Audible on the EIMU band |
| **Omar's 4-minute gap** | EIMU sweep grid on Level 3 drops to partial every 36 hours | Needs Omar's relationship from Phases 2–3 |
| **CCN-Spoofer (Ph 4+)** | Intercept, delay | Level 8 retrieval required |
| **Clear the review queue** | PTKW review terminal, Level 5, Phase 3+ | Unmarked room; PTKW access |

---

## Obstacle 6: A patrol sweep (Phase 6 Omega-1, or Phase 4 sweeps)

Omega-1 is covered in Obstacle 9. For standard sweeps:

| Answer | How | Cost |
|---|---|---|
| **Read the pattern from a Type C vantage** | Observe the edge of the sweep, time the move | Time; EIMU Coherence if prolonged |
| **Wait for the gap** | Phase 6: the 12-minute corridor gap if the Level 0 device message was sent in Phase 5 | Must have done the Phase 5 action |
| **Mask with sound** | Thermal vent (8m), HVAC (6m), cafeteria equipment (service hours), Level 1 water line vibration (10m; ends Phase 5) | Location-locked |

---

## Obstacle 7: A True Believer blocking a route (Phase 5)

True Believers are **not combat enemies.** They are dynamic obstacles with human behavior patterns. (`design/ENEMY_AI.md`)

| Who | Answers | What each costs |
|---|---|---|
| **Marcus** | Say nothing → he lets them go; lie → believes, but costs Phase 6 help; show the Charter section → arc moment | Phase 6 outcomes differ |
| **Cho** | "I'm just passing through." | Nothing |
| **Lani** | Not a blocker. Observe her on camera feeds. | — |
| **Violence** | No stealth, no conversation, no "solving" a person | Phase 6 consequences. **[PROPOSAL]** The game does not support attacking a True Believer. |

**The design argument:** A person who stands in the way is not a lock. The game does not offer a lockpick.

---

## Obstacle 8: Arrangement Class reporting (Phases 4–5)

Dayo and Priti have no aggressive state. They file reports. (`design/ENEMY_AI.md`)

| Who | Answer | Result |
|---|---|---|
| **Dayo** | Ignore → files a report; threaten → files immediately, PTKW alerted; tell him K-7 is under review → his arrangement loses its guarantor | Option 3 changes his Phase 6 behavior |
| **Priti** | Pass → flag in 3 minutes; EIMU-Jammer (ECT-4C) → confuses observation; ACS-9 → she wants to leave; tell her about her husband's open backlog → she sits with it | The honest answer is the only one that changes what she does next |

---

## Obstacle 9: Omega-1 (Phase 6 only)

**What it is:** Avoidance only. Full-spectrum detection plus an undocumented fourth mode. Geometric coverage sweeps. Caught means game over. (`design/ENEMY_AI.md`, `design/HEALTH_SURVIVAL.md` say no reload; `design/SAVE_SYSTEM.md` says reload to last autosave. See the open question in `design/DIFFICULTY_ACCESSIBILITY.md`.)

| Answer | How | Cost |
|---|---|---|
| **Type C crawlways** | Omega-1 cannot enter (equipment clearance) | Cold, EIMU Coherence decline after 40 min |
| **Observe, then move** | Read the sweep from a crawlway, time the jump to the next zone | Time |
| **Level 0 device gap** | One sweep arrives 12 minutes late | Requires the Phase 5 action |
| **Omega-1 countermeasure** (Rania's kit) | Two inventory slots | The player must decide if it is worth the slots |
| **Jammer** | Partial reduction only | — |
| **CCN-Spoofer Tier 3** | Spoof "stand down Level 5 lockdown" → opens docking route | Two spoofs total in Phase 6 |
| **Do not stay in range** | Even a stripped badge fails if the player stays | — |

---

## Obstacle 10: The manifest check (Phase 4, once)

An advance-team officer reads the badge manifest of any non-PTKW staff. The wrong items in the wrong slots cause an immediate State 2 alert without any prior visual detection. (`design/INVENTORY.md`)

| Answer | Cost |
|---|---|
| **Carry no contraband in that sweep area** | Fewer tools; planning needed before Phase 4 |
| **Carry clean versions of tools; leave modified ones elsewhere** | A slot for each version; a hiding place |
| **Avoid the officer** | The sweep is a single moment |
| **Hand the dangerous item to Tarek / Omar** | Relationship required |

The one moment in the game where the inventory screen is also the threat.

---

## Obstacle 11: A locked system or a sealed Level 0 panel

| Answer | How | Cost |
|---|---|---|
| **Maintenance Bar T3** | Pry the two glyph-marked panels | Level 0; Phase 6 use |
| **EIMU-Jammer T3** | "Vigilance — Sustained" opens a 4-minute unmonitored Level 8 window | Once (Phase 5 use); needs Yusra's map |
| **CCN-Spoofer T3** | Spoof a standing-down order | See Obstacle 9 |
| **Reading the engineering files** | Partial PTKW network access shows the conduit layout | Needs the file; time |

---

## Cross-cutting costs

| Cost | Where it shows up | Source |
|---|---|---|
| **Noise radius** | Every action on a surface; CRD-7 20m, jammer 8m, door 6m | `design/STEALTH_DETECTION.md` |
| **EIMU signature** | Badge always broadcasts; stress adds a signature | `design/STEALTH_DETECTION.md` |
| **CCN Anomaly Score** | Unauthorized access, odd badge reads, Arrangement Class reports | `design/STEALTH_DETECTION.md` |
| **Time** | Modifications, waiting, sweeps, junction work (20 min) | `canon/weapons/MODIFICATIONS.md` |
| **Cold** | Type A −4°C, B −6 to −8°C, C −8 to −12°C, Level 0 12°C | `design/STEALTH_DETECTION.md`, `design/HEALTH_SURVIVAL.md` |
| **Inventory slots** | 10 slots; Charter takes 2; countermeasure takes 2 | `design/INVENTORY.md` |
| **Phase 6 consequences** | Lying to Marcus, ignoring Dayo, skipping Omar, skipping the Phase 5 message | `design/ENEMY_AI.md`, `design/NPC_COMPANIONS.md`, `canon/weapons/found/Level-0-Device.md` |
| **Scanner flag** | Modified tools at Level 5 | `canon/weapons/MODIFICATIONS.md` |

---

## Where the matrix is intentionally thin

- **Violence against True Believers, Arrangement Class and NPCs** — no answer. **[PROPOSAL]** None provided on purpose.
- **Beating EOD** — no answer. The only answers are not being there and the 22-hour window.
- **Lockpicking** — no tool exists. Doors are solved by badges, power, passages, other people or time.
- **Brute-forcing the CCN** — the CCN is never "hacked." It is intercepted, delayed or spoofed, one function at a time.

---

## Coverage check

An obstacle is under-designed if the player has fewer than three non-lethal answers. Current count (non-lethal answers listed above):

| Obstacle | Non-lethal answers | Status |
|---|---|---|
| PTKW pair | 7 | Strong |
| PTKW triple | 5 | OK |
| Advance team | 4 | OK |
| Badge-gated door | 5 | OK |
| CCN node field | 6 | Strong |
| Patrol sweep | 3 | Minimum |
| True Believer | 3 | Minimum (talk-only by design) |
| Arrangement Class | 4 each | OK |
| Omega-1 | 5 | OK |
| Manifest check | 4 | OK |
| Locked system | 4 | OK |

**[PROPOSAL]** — The patrol sweep is thin because the existing documents describe Omega-1 sweeps better than standard sweeps. The next design task is a second answer family for standard Phase 4 sweeps that does not depend on Type C access.

---

*→ See: design/VERBS.md — the eight verbs these answers are built from.*
*→ See: design/ENEMY_AI.md — the obstacle behaviors.*
*→ See: design/STEALTH_DETECTION.md — noise, EIMU and CCN costs.*
*→ See: canon/weapons/OVERVIEW.md — the three-tier tool knowledge system.*
*→ See: canon/weapons/MODIFICATIONS.md — the junctions and modification costs.*
*→ See: design/INVENTORY.md — the manifest check and the slot limit.*
*→ See: design/NPC_COMPANIONS.md — Tarek, Omar and Sera as part of the answer set.*
*→ See: design/TENSION_CURVE.md — how often each obstacle appears across the phases.*
