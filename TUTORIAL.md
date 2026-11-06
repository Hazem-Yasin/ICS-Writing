# ICS — Rigged Sphere
## Tutorial Integration — The Job Is The Tutorial

*The game teaches the player how to play it by giving them a job. There is no tutorial level, no tutorial room, no guardian NPC who says "here's how the badge reader works." The player is E-05682, a behavioral data analyst with three years of experience at ICS Earth Branch. They know how the badge reader works. The game's job is to make the player feel like they already know how everything works — and then begin revealing that they don't know what it means.*

---

## Design Principle: Competence First, Horror Later

The tutorial is designed in two registers:

**Register 1 — The Competent Employee.** Phase 0 teaches the player all the mechanics by putting them in situations where using those mechanics is their normal job. The badge reader is introduced because the player has to badge into their work floor. The EIMU Coherence track is introduced because the player receives a wellness message about it from Sera. The maintenance passages are introduced because a shortcut between Levels 2 and 3 is something any Tier 3 employee knows about. The player learns everything before they know they will need it for something other than work.

**Register 2 — The Revelation.** When the game reveals what these mechanics mean in context — the badge EIMU as a surveillance instrument, the CCN as a harvest preparation tool, the EIMU Coherence track as a compliance score rather than a health score — the player already knows how to operate them. The tutorial already happened. What shifts is the meaning of everything they've learned.

---

## Mechanic Introduction Schedule

### Weeks 1–52 (Phase 0, Pre-Exposure)

The player has been at ICS for three years. The tutorial for Phase 0 covers only the mechanics the player needs right now — discovering that things are not what they seem. The mechanical skills are assumed.

**Opening sequence (see: scene-notes/Opening Sequence.md):**

The first thing the player does is badge into their quarters door. The badge reader is the first input. The badge display is the first UI element. No explanation is given. The badge read worked. The door opened. That's how this works.

**Tutorial Beat 1 — Badge Reader Proficiency (Day 0)**
*Mechanic introduced:* Badge reader interaction, Tier access levels
*Context:* The player's morning routine. They badge into quarters → corridor → Level 3 work floor. Three readers, three doors. The third is their work floor — the reader says "Access Granted, Tier 2" in small text. Most players will not read the tier number. Some will notice it says Tier 2, not Tier 3, and wonder what Tier 3 requires. The game does not explain. The answer is in the Badge Technical Specification (Document 2.46), discoverable in the library terminal.

**Tutorial Beat 2 — Behavioral Data Interface (Day 0)**
*Mechanic introduced:* The work terminal, document reading, the behavioral aggregate
*Context:* The player sits at their desk and opens their active work file. This is a real work task — they are reviewing a behavioral data set for anomalies and flagging items for review. The task is explained in a brief work memo from their supervisor. The player does the job. While doing the job, they are learning: how to read documents, how the data aggregate is structured, what normal compliance numbers look like. They are also — without knowing it — doing exactly what ICS needs them to do.

**Tutorial Beat 3 — AIDEN Unit (Day 0 evening)**
*Mechanic introduced:* AIDEN interaction; EIMU collection mechanic (hidden)
*Context:* AIDEN is in the player's quarters, returned to position overnight (see Opening Sequence). The player can interact with it. They can feed it data inputs as requested. They can move it. They can name it, or leave it unnamed. Every interaction with AIDEN is logged. The tutorial for AIDEN is: it is a companion, warmly designed, responsive. The tutorial for AIDEN's second function is: it does not exist yet. That comes in Phase 2.

**Tutorial Beat 4 — Maintenance Passage Navigation (Day 2)**
*Mechanic introduced:* Maintenance doors, Type A passage navigation, acoustic awareness
*Context:* The Level 3 service corridor is the shortcut between the behavioral data work floor and the medical station. The player has reason to go to the medical station — a wellness check scheduled as part of their Tier 2 status review. The shortcut is shorter. The maintenance door requires the maintenance key (clipped to the work floor key rack — the player can take it; nobody questions this; it is a normal key for normal use). The first time through the maintenance corridor, the player hears the temperature drop and the sound difference from the main corridors. Nothing else. The mechanic is: this passage exists, you can use it, it is different from the main corridors.

**Tutorial Beat 5 — Internal Communications (Day 3)**
*Mechanic introduced:* Message terminal, internal communications reading
*Context:* The player receives three messages: a message from Sera ("saw you took the service corridor, good shortcut right?"), a work scheduling update, and a Comfort machine alert from the Level 3 dispenser. Reading messages is the tutorial. The message from Sera is also the tutorial for: Sera exists, she notices things, she sends messages.

**Tutorial Beat 6 — Document Discovery (Day 4–10)**
*Mechanic introduced:* Discoverable documents, cross-references, three-tier structure
*Context:* The player, doing their normal work, accesses the ICS document library through the work terminal. Several documents are in their reading queue as recommended professional development (Document 2.01, the Charter; Document 2.18, the Psychology Report — flagged for behavioral analysts). The player reads them for work. They are excellent documents by the Global Access standard. The three-tier structure is not visible yet — the Global Access layer is all the player can see. The tutorial is: documents exist, reading them is how you understand things, some documents have more layers than the page count suggests.

**Tutorial Beat 7 — SOLCRED Economy (Day 5)**
*Mechanic introduced:* SOLCRED, facility purchases, badge as currency
*Context:* The player is hungry. The cafeteria machine requires SOLCRED. The badge IS the SOLCRED wallet — it was loaded when the player started, automatically, from their salary deposit. The player buys lunch. The mechanic is: badge = identity = currency = access, all the same device, all the same system.

**Tutorial Beat 8 — EIMU Coherence (Day 7)**
*Mechanic introduced:* EIMU Coherence track, wellness monitoring
*Context:* The player receives an automated wellness alert from the EIMU system — their EIMU Coherence track has dipped to a level that triggers the standard low-wellness notification. The notification says: *"Your behavioral coherence is reading slightly below preferred range. This is normal during adjustment periods. Your wellness team recommends 20 minutes in a designated relaxation space."* The player can go to a relaxation space (the Earth View Window, the cafeteria during quiet hours, the Level 4 quiet room). Their Coherence track recovers. The tutorial is: EIMU Coherence is a health metric, it goes up when you're in compliant spaces, it recovers in the places the facility provides. The second tutorial — that it is a surveillance score, not a wellness metric — comes later.

---

### Phase 1 — Confinement as Forced Tutorial

Phase 1 is a deliberate restriction that forces the player to use the one skill they were introduced to but may not have fully developed: reading.

The maintenance access panel in the player's quarters is the only non-standard element available. The panel opens to a Type A maintenance passage. The passage connects to adjacent ventilation infrastructure. The player cannot leave their residential zone this way — not yet — but they can hear things, observe things through grates, and access one wall-mounted CCN terminal that was not deactivated when the quarters were locked down (a maintenance oversight; the terminal is documented in the PTKW maintenance log as a known gap that was never prioritized).

**Tutorial Beat 9 — CCN Terminal Unauthorized Access (Phase 1)**
*Mechanic introduced:* Unauthorized access, CCN Anomaly Score, PTKW queue behavior
*Context:* The maintenance terminal gives the player access to a limited set of documents behind a Tier 3 access point that the terminal's old credentials still satisfy. The player accesses them. An anomaly flag fires. They don't know it fired. The tutorial for CCN Anomaly Score is: it exists, it fired, and they will not learn this until they find the PTKW monitoring room in Phase 3. By which point their Phase 1 anomaly score is already in the queue. This is the tutorial for consequence delay.

**Tutorial Beat 10 — Confinement Clock (Phase 1)**
*Mechanic introduced:* In-world time tracking, the badge clock
*Context:* The player is confined for Days 1–3 post-exposure. The badge display shows Branch Time. The player learns, through necessity, to track time — when the PTKW officer makes their monitoring pass (every 4 hours, regular as the badge told them), when the maintenance passage is safe to move in, when the anomaly queue is checked. The tutorial is: time is a resource in this game. The badge clock is your primary tool for managing it.

---

### Phase 2 Onward — Discovery Tutorials

After Phase 2, the tutorial system becomes situational. Each new mechanic is introduced through encounter, not through scheduled beats.

| Mechanic | When introduced | How introduced |
|---|---|---|
| EIMU-Jammer | Phase 2 — Yusra's cache (if found) | Player finds it. No instructions. Activating it produces a sound and the K-7 interference effect becomes visible if the player has the Diagnostic Accessory. |
| EIMU Diagnostic Accessory | Phase 2–3 — Level 3 medical station | Player finds it in a supply cabinet. The label describes its function in medical terminology. Reading comprehension is the tutorial. |
| CCN Anomaly Score (revealed) | Phase 3 — PTKW monitoring room | Player reads the monitoring queue and finds their own Phase 1 anomaly flag. The tutorial for the queue is: it exists. The tutorial for their own behavior: they were already in it. |
| Stealth via body language | Phase 2 — Marcus encounter mechanic | Marcus does not detect through EIMU. He detects through observation. The tutorial for human-detection (different from EIMU-detection) is Marcus. |
| Omega-1 full-spectrum detection | Phase 6 — First Omega-1 sweep | The player runs the playbook they've learned. It works less well. The Diagnostic Accessory shows the K-7 ping from Omega-1 as different from a standard K-7 signal — the frequency ring is larger. The tutorial is: pay attention to things that are different from what you've learned to expect. |

---

## What Is Never Explicitly Taught

These mechanics exist in the game and are discoverable. The game does not teach them. Players who find them are ahead. Players who don't still complete the game, more slowly or more narrowly.

- **The CCN Anomaly Score decay mechanic** — spending 48 hours in compliant behavior reduces the score. Many players never discover this and manage detection through avoidance instead.
- **Using thermal vents as acoustic masking** — the maintenance network knowledge file mentions acoustic load data. Most players don't read maintenance engineering documents.
- **The PTKW review terminal** (Phase 3+, Level 5) — allows manual clearing of queue entries. Requires PTKW access and finding the room. The room is not marked.
- **Tarek's maintenance route schedule** — in the work order archive. Allows the player to time their maintenance network transit to move with Tarek as cover. Most players encounter Tarek as a surprise. Some encounter him as a planned route.
- **The 4-minute CCN sweep gap** (from Omar in Phase 5) — requires building the relationship with Omar through Phase 2–3. Players who skipped Omar's conversations don't have this.

**The design argument:** A game that teaches everything is a game that tells you exactly what to do. The tutorial-as-job design works because the player's job teaches them the skills. What the job can't teach them is how to use those skills against the system they're embedded in. That knowledge comes from paying attention to the people around them and reading documents they weren't necessarily assigned. The player who finishes Phase 6 having had the best experience is not the player who executed every mechanic optimally. It is the player who noticed Tarek. Who read Rania's note carefully. Who stayed at their desk in Phase 2 long enough to have the conversation with Omar.

The tutorial is: be curious. The game does not tell you this. It is the thing you are either doing or you are not.

---

*→ See: scene-notes/Opening Sequence.md — the first seven beats that open Phase 0.*
*→ See: STEALTH_DETECTION.md — the full mechanics that the tutorial prepares the player to use.*
*→ See: NPC_COMPANIONS.md — the relationship system that the tutorial beats begin building.*
