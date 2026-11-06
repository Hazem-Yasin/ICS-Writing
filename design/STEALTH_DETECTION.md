# ICS: Interplanetary Corporate Solutions
## Stealth & Detection Mechanics — Full System Design

*This document covers the complete detection architecture — how the player is found, how they avoid being found, and what the costs of each decision look like. design/ENEMY_AI.md covers the behavioral states of each enemy category. This document covers the underlying physics of the detection layer and the specific rules the player works within.*

*The core principle: the stealth system in this game should feel like operating inside a facility that was already surveilling you before you started trying to hide from it. There is no "entering stealth mode." The surveillance was always on.*

---

## The Three Detection Inputs — Detailed

### 1. Visual Detection

**Line of sight:** Binary. If an enemy can draw an unobstructed line to the player's position, visual detection is active. Obstructions include walls, doors, AIDEN units (ironically — their bulk blocks sightlines in corridors), maintenance equipment, and other NPCs.

**Lighting:** The facility has four ambient lighting states:
- **Standard** — white LED panels at full output. Detection distance: 18 meters.
- **Reduced** — maintenance dimming (common in off-hours, Phase 3 specifically). Detection distance: 11 meters.
- **Emergency** — red-spectrum alert lighting. Paradoxically increases player visibility but creates visual noise that extends the Curious period by 4 seconds before escalating.
- **Blackout** — total loss of main power. Detection distance: 2 meters (flashlight behavior). The player has a maintenance torch available from Phase 1 onward; enemies have handheld light units.

**Detection speed:** Not instant. An enemy who sees the player at distance builds detection over 1.5–3 seconds depending on range and lighting. The player's heads-up indicator (a faint amber pulse at the badge edge visible in the corner of the screen — not an intrusive UI element, just a warmth in the periphery) begins when this build starts. If the player breaks line of sight before the bar fills, detection resets.

The player learns this feel, not the bar. There is no detection meter UI. The amber pulse at the badge edge is the only feedback. Players who need the explicit meter can enable it in accessibility options — it is not the default.

**What enemies look for:** Movement first. A stationary player at distance is harder to detect than a moving player. Crouching reduces movement detection radius. Standard movement speed is always preferable to running within detection range — running doubles the visual detection speed and generates acoustic output that triggers EIMU acoustic logging.

---

### 2. EIMU Detection — The ICS Layer

This is the mechanic specific to this game. It makes the facility feel alive in a way no other first-person game's stealth layer does: the badge is a transmitter. The player has been broadcasting their location and emotional state for three years. The facility has been listening that whole time. None of this is new — only the player's awareness of it is new.

**How EIMU detection works:**

The badge continuously broadcasts a low-frequency compliance signal. Any authorized monitoring device — fixed CCN nodes, PTKW handheld K-7 monitors, or the Omega-1 scanner (which uses a different detection band) — can receive this signal and triangulate position to within approximately 1 meter.

**Range:** CCN fixed nodes have a range of 25 meters through standard facility walls. PTKW handheld K-7 monitors have a 15-meter range with the same wall penetration. The Omega-1 scanner range is not documented anywhere in the facility's accessible files.

**The key implication:** In standard phases, a player who is stationary in a maintenance passage is invisible to visual detection — but is still broadcasting their EIMU signature to every node within 25 meters. A PTKW officer with a K-7 walking the corridor outside can detect the player's presence and approximate location without ever opening the maintenance door.

**Countermeasures:**

| Method | Effect | Trade-off |
|---|---|---|
| **Badge removal** | EIMU signal ceases immediately | Loss of all access-gated areas (badge readers won't open); cannot read EIMU on others; Physical Integrity track stops receiving passive healing inputs from facility health nodes |
| **EIMU-Jammer (canon/weapons/compliance/EIMU-Jammer — Emotional Interference Unit.md)** | Broadcasts a false compliance signal at a different location | Jammer is audible on the EIMU band — a PTKW officer with a K-7 who knows what a jammer sounds like (Phase 5+ officers do) will detect the interference rather than the player |
| **CCN-Spoofer (canon/weapons/compliance/CCN-Spoofer — Communications Node Spoofer.md)** | Spoofs the player's asset number to a different badge ID | High-risk; if the spoofed ID is a transitioned asset and the system flags the discrepancy, the alert is immediate and permanent until CCN reset |
| **Tier upgrade** | A Tier 4 badge is not detectable by standard K-7 monitors (designed for Tier 1–3 surveillance) | Tier 4 badges generate a different CCN-level signal that the PTKW monitoring team can see but field officers cannot query without authorization |

**EIMU coherence — the hidden stealth variable:**

The EIMU signal carries not just position but the player's emotional state — the four-track reading (Physical Integrity, Neurological Status, Thermal Regulation, EIMU Coherence) is what the facility reads from the badge. A player who is in high-stress states — running from pursuit, in low-oxygen maintenance passages, in cold Level 0 temperatures — broadcasts a stress signature that is distinct from a standard compliance reading.

PTKW officers are not trained to read EIMU stress signatures in real time. The K-7 does not flag stress signatures for field officers. However, the CCN backend processing does. If the player's stress signature is anomalous for more than 6 minutes, a passive automated flag is generated — not an immediate alert, but a logged anomaly that goes into the PTKW review queue. In Phase 4+, the review queue is actively monitored. Before Phase 4, it is checked in batch every 12 hours.

**The player does not see their own stress signature unless they have the EIMU Diagnostic Accessory** — a piece of equipment found in the Level 3 medical station that allows the badge to display its own output. Finding this changes how the player manages stealth from that point on.

---

### 3. Acoustic Detection

**Sound radius:** Every action the player takes generates a sound event with a defined radius. Enemies within that radius enter State 1 (Curious) if they are in State 0. Enemies already in State 1 or higher receive a position update.

**Sound radius by action:**

| Action | Radius | Notes |
|---|---|---|
| Normal walking | 4m | On standard floor surfaces |
| Walking on maintenance grating | 7m | Metal carries vibration further |
| Crouching movement | 1.5m | Standard floor |
| Running | 12m | Any surface; always audible to any nearby enemy |
| Tool activation (CRD-7) | 20m | Compliance tool discharge is loud by design |
| EIMU-Jammer activation | 8m | Mechanical click + hum |
| Maintenance door operation | 6m | Squeal of the hinges is consistent across the facility |
| Thermal venting (some maintenance passages) | Masks up to 8m | The player can use thermal vents as acoustic cover |
| Interacting with CCN badge reader | 3m | The accepted/denied tones carry |
| Dropping an object | 10m | Physics object — varies by surface |

**Sound propagation:** The facility's corridor geometry creates acoustic shadow zones. Perpendicular corridors attenuate sound sharply at the junction — a sound event at 8m radius around a corner reads as approximately 3m to an enemy at the same distance on the other side. The player can learn these geometry rules through observation or by reading the Maintenance Network Architecture file (canon/facility/Maintenance Network.md) which includes acoustic load data for structural reasons.

**Acoustic cover:** Specific persistent sounds in the facility create masking zones:
- The Level 3 HVAC unit (always on, produces a 6m masking zone in the adjacent corridor)
- The cafeteria food service equipment (during service hours — 06:30–08:30, 11:30–13:30, 17:30–19:30)
- The Phase 3 water line vibration in the Level 1 mechanical room (a fault; it produces a 10m masking zone that persists until Phase 5 when it is repaired)
- The Level 0 constant low hum (origin unknown; masks all acoustic events within Level 0 entirely)

---

## Detection Zones — Facility-Wide Map

The facility is divided into detection zones based on coverage density. The player cannot see this map directly — it exists in the PTKW monitoring room (Level 6, access Tier 4) as a standard operational document. The player who reaches Level 6 can read it. Until then, they learn coverage empirically.

**Zone A — High coverage** (Levels 4–6, primary corridors, transit wing): Continuous CCN node coverage, no gaps longer than 2 meters. PTKW patrols at standard density. These are the areas where movement requires planning.

**Zone B — Standard coverage** (Levels 2–3, secondary corridors, cafeteria): CCN coverage with standard node spacing (25-meter intervals). 4–8 meter gaps between nodes in some corridor junctions. One of these gaps is in the Level 3 service corridor — the player can identify it when their EIMU-Jammer stops reading the closest node (the jammer's UI shows local node signal strength as a secondary feature).

**Zone C — Sparse coverage** (Level 1, maintenance access corridors, residential): CCN nodes at 50-meter intervals. Designed for population that is assumed compliant. Used by maintenance staff (including Tarek) without concern. In Phase 2+, these corridors are technically under survey but practically unwatched.

**Zone D — No coverage** (Type B/C maintenance passages, Level 0): No CCN nodes. No PTKW monitoring. The facility infrastructure team knows these exist. PTKW knows they exist. Nobody thought to instrument them because nobody was supposed to be in them. The badge is still broadcasting — but there is nothing within range to receive the signal.

**Zone D exception:** In Phase 6, Omega-1 assets carry their own portable detection arrays. Type B passages are no longer safe from EIMU detection once Omega-1 begins their sweep. Type C crawlways remain outside their detection footprint — the crawlways are below minimum equipment clearance for Omega-1 deployment.

---

## The CCN Review Queue — Passive Detection That Accumulates

The game tracks a hidden value: **CCN Anomaly Score**. This is not displayed to the player.

Every action that generates a logged anomaly (unauthorized access attempts, stress signature flags, badge reads in unscheduled locations, Dayo's facilities reports, Priti's observation reports) adds to this score. The score decays slowly over time — routine compliance behavior, normal badge reads in expected locations, eating at scheduled mealtimes — reduces it.

**Score thresholds and consequences:**

| Score | Effect |
|---|---|
| 0–15 | No action. Player is logged. |
| 16–30 | PTKW review queue flag. Reviewed in next batch cycle (12 hours pre-Phase 4; 2 hours Phase 4+). If reviewed, patrol density in the player's most recent logged zone increases for 24 hours. |
| 31–50 | Active review flag. A PTKW officer is assigned to review the player's recent movement logs. Patrol route modification within 4 hours. |
| 51–80 | Direct surveillance order. One PTKW pair is tasked specifically to the player's area. This pair behaves differently — they are on assignment, not routine patrol, and will break standard routes. |
| 81+ | Emergency flag. EOD notification (Phase 2–4). In Phase 5+, the score cap means nothing — the system is already overwhelmed and anomaly queue processing has stopped. Phase 5 is a CCN score amnesty by default because the system cannot process the queue. |

The player can reduce their score by:
- Using the CCN-Spoofer to attribute their anomalous reads to a different badge
- Finding the PTKW review terminal on Level 5 and clearing specific queue entries (available Phase 3+, requires PTKW-level access)
- Simply being routinely compliant for 48+ hours — the decay rate is slow but consistent

The player cannot see their CCN Anomaly Score. They can infer it from environmental changes — additional patrols, a PTKW pair breaking its expected route, a locked door that was open yesterday.

---

## Maintenance Passages — Detailed Rules

The maintenance network is the player's primary stealth infrastructure. The rules for using it safely:

**Type A passages (tall enough to walk, accessible by maintenance staff):**
- CCN: no fixed nodes
- PTKW: will not enter in Phase 2–4 (not standard procedure; equipment not suited for narrow passage pursuit)
- Arrangement class: Priti enters one Type A passage in Phase 5 (by design — she is the specific exception)
- Omega-1: can enter, will enter in Phase 6
- Temperature: 4°C colder than adjacent rooms. Thermal Regulation track will degrade over extended time (20+ minutes continuous)

**Type B passages (stoop required; not all staff can access without a maintenance key):**
- CCN: no fixed nodes
- PTKW: will not enter under any Phase 2–5 protocol
- Arrangement class: no access
- Omega-1: can enter with difficulty; advance team will not enter; standard deployment will
- Temperature: 6–8°C below adjacent rooms; Thermal Regulation degrades faster

**Type C crawlways (hands and knees; maintenance keys plus small profile required):**
- CCN: no fixed nodes
- PTKW: no access (equipment clearance minimum not met)
- Arrangement class: no access
- Omega-1 deployment: no access (minimum equipment clearance not met)
- Temperature: 8–12°C below adjacent rooms; long exposure risks Physical Integrity track
- The player's EIMU Coherence track degrades in extended crawlway use — the passive wellness monitoring that stabilizes EIMU output is absent here; after 40+ minutes continuous, the EIMU Coherence track begins slow decline

**The maintenance network and Tarek:** Tarek has the full maintenance key set as Level 1–4 cleaning supervisor. He is the only NPC in the game who can access all Type A, B, and some Type C passages. In Phase 5, he is effectively immune to standard PTKW detection in the maintenance network because his presence there is authorized, routine, and expected. The player who moves with Tarek through the network reads as a colleague accompanying authorized maintenance staff — EIMU detection still applies, but a paired movement pattern triggers a lower anomaly weight than a single asset moving alone through a Zone D area.

---

## The EIMU Diagnostic Accessory — Learning the System

The EIMU Diagnostic Accessory is a badge attachment, available in the Level 3 medical station (Zone C, low patrol coverage). It is not presented as a key item — it is in a supply cabinet among standard wellness tools, labeled in ICS medical terminology. The player who reads the label carefully will understand what it does. The player who grabs it without reading gets the function with no explanation.

**What it adds to the player's information:**

When equipped, the badge monitor gains a secondary display mode: a small four-ring readout visible in the bottom corner of the screen (the same location as the badge health tracks) showing:
- Current EIMU broadcast signal strength (higher in Zone A, lower in Zone D)
- Nearest CCN node distance (in meters — when this reads "---", the player is in a Zone D area)
- Current stress signature status (Green: standard compliance read / Amber: elevated / Red: anomalous flagging)
- Nearest K-7 monitor signal (if a PTKW officer with a K-7 is within 30 meters, a faint pulse appears — the K-7 is itself an EIMU device and the Diagnostic Accessory can detect it)

The last item is the most operationally significant. The player who has the Diagnostic Accessory can detect the presence of a PTKW officer through a wall — not their position exactly, but whether one is nearby with a K-7 active. This inverts the surveillance relationship, briefly, on a single axis. It is the closest the game comes to giving the player a tool that the system was not designed for them to have.

---

## Summary: Detection by Phase

| Phase | Primary Threat | EIMU Sensitivity | CCN Score Consequences |
|---|---|---|---|
| Phase 0 | None (ambient surveillance only) | Low | None (queue checked every 24h) |
| Phase 1 | Confined quarters monitoring | Medium | Confined — movement is already tracked |
| Phase 2 | PTKW patrol (visual + EIMU) | High | Active (reviewed every 12h) |
| Phase 3 | Reduced PTKW, higher CCN automation | Medium-high | Active but sparse patrol response |
| Phase 4 | PTKW triple patrols + advance team | Maximum | Reviewed every 2h; 31+ = direct surveillance |
| Phase 5 | CCN overwhelmed; Arrangement Class reporting | Low for CCN; high for observation | Queue broken; Arrangement Class reports still reach PTKW manually |
| Phase 6 | Omega-1 full-spectrum | Full-spectrum | Irrelevant — Omega-1 does not use CCN queue |

---

*→ See: design/ENEMY_AI.md — the behavioral states that activate when detection thresholds are crossed.*
*→ See: canon/weapons/compliance/ — the tools available for managing EIMU detection.*
*→ See: design/NPC_COMPANIONS.md — how Tarek and Omar provide specific navigational intelligence.*
*→ See: canon/facility/Maintenance Network.md — the physical layout of Type A, B, and C passages.*
