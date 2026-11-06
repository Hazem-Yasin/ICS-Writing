# ICS — Rigged Sphere
## Player Guidance — How the Game Says "Go There"

*The game has no quest marker, no task log and no glowing path. In Phase 6 that is canon: "no objective marker, no task log." This sheet decides how the player knows where to go in Phases 0 to 5, using only things that exist in the facility: people, documents, signs, light and sound.*

*The design argument: guidance is a tone of voice. In Phase 0 the building is helpful and says exactly where to go. In Phase 5 it says nothing and the people say it for it. By Phase 6 the player is finding their own way, and the removal of help is a story event, not a design omission.*

---

## How to read this sheet

| Tag | Meaning |
|---|---|
| **Canon** | Already stated in an existing document. The source is named. |
| **[PROPOSAL]** | New. Needs sign-off before it becomes canon. |

---

## 1. The rule

**Every place the player must go is named by someone or something in the world before they need it.** Never by an overlay. If a place cannot be introduced in the world, it should not be required.

**Canon:** Phase 6 has no objective marker and no task log. (`scene-notes/Phase 6 Final 22 Hours.md`, `DIFFICULTY_ACCESSIBILITY.md`)

---

## 2. The five channels

| Channel | What it does | Examples |
|---|---|---|
| **People** | Say where to go, or where not to | Sera's messages; Tarek's route; Omar's 4-minute sweep gap; Rania's note |
| **Documents** | Name a place, a time, a code | Floor plans (Document 2.36), the work order archive, the Charter |
| **The badge** | The clock, tier, reader colours, the Diagnostic readout once found | Reader says "Access Granted, Tier 2"; a red reader says "no" |
| **Environment** | Light, sound, temperature, smell | The cold from the Stairwell B gap; the low sound near Level 7 |
| **The building's own signage** | Directional signs, level numbers | Corridor signs follow the ICS sign system |

---

## 3. Guidance by phase

| Phase | How the game guides | Source of "next" | Failure to follow means |
|---|---|---|---|
| **0** | The job is the guide. A work memo, a wellness alert, a message from Sera. Tutorial Beats 1–8. | Supervisor memo; schedule; the badge | Nothing. The player cannot get lost. |
| **1** | Confinement is the guide. The quarters panel, the CCN terminal, the PTKW pass every 4 hours. | The badge clock | Nothing yet; an anomaly flag is delayed. |
| **2** | People and notes. Yusra's cache, Marcus as a human detector, the first Junction A. | Notes; EOD's visits | Missed tools. Recoverable. |
| **3** | The building itself. The cold in the gap, the glyphs on the panels, the notebook. No one is there to tell the player. | Environment; the notebook's last entry | A missed room, not a failed run. |
| **4** | Rania's note, Tarek's name, the speech. Others now say where things are. | People; word of mouth | Missed information. |
| **5** | NPC obstacles and allies: Marcus, Lani, Cho, Dayo, Priti, Omar, Tarek. Two or three possible next places at any time. | Conversation | Narrower route; later endings. |
| **6** | **None.** The player has seen every kind of guidance and now has none. | The player | Not failure — the ending is chosen. |

---

## 4. Specific moments

| Moment | The question the player asks | How the world answers **[PROPOSAL]** |
|---|---|---|
| Phase 1 — "Where does the panel go?" | Can I leave my room? | The Type A passage is the only visible change. Sound beyond the grate is the draw. |
| Phase 2 — "Where is Junction A?" | Where can I make things? | Level 3 service corridor; a note in the maintenance log; a bench with scratched-in dates. |
| Phase 3 — "Where do I go at night?" | Is there something below? | The cold in Stairwell B, a 2 mm gap at the lower-left corner of the grey door. |
| Phase 3 — "What do I do on Level 0?" | What am I here for? | The clean floor. The 15m recess. The sub-corridor door. |
| Phase 4 — "Who can I trust?" | Is anyone like me? | Tarek stands. His name for Rania's note. |
| Phase 5 — "What can I stop?" | Is there anything I can change? | The 11,000-event queue on Level 5; three grey dots on the HQ Response ladder. |
| Phase 6 — "What do I do?" | Where do I spend 22 hours? | Seven options in `scene-notes/Phase 6 Final 22 Hours.md`, none marked. |

---

## 5. Guidance that never appears

**[PROPOSAL]** Things the game does not do, to keep the building's voice honest.

- No waypoint, quest marker or compass. 
- No "press X to see objective." (The optional *Objective reminder* in `DIFFICULTY_ACCESSIBILITY.md` is a single line for the last thing done, off by default, and unavailable in Phase 6.)
- No NPC who says "go to Level 5 and find the terminal."
- No colour-coded paths. The one colour is the reader: green, red.
- No fade or mark on doors the player has not entered.

The facility can say *"Access Denied"* but never *"you should go to…"* — except the people.

---

## 6. When the player is lost

**[PROPOSAL]**

| Stuck for | What happens |
|---|---|
| ~10 minutes in Phases 0–2 | A message arrives (Sera, a work memo, an alert) that points back at the current thread. |
| ~10 minutes in Phases 3–5 | AIDEN (the player's own) says nothing. A nearby NPC walks past. A document in the room becomes lit by a lamp that was already there. |
| Phase 6 | Nothing. The 22 hours are the 22 hours. |

The player may re-read any document at any time; the badge holds it. (`INVENTORY.md`)

---

## Open questions

1. **Is the "lamp lights the document" nudge acceptable?** It is a diegetic hint but still a hint. Without it, Phase 3 players may stall.
2. **Phase 2 guidance.** The Phase 2 tutorial is "situational" (`TUTORIAL.md`). It needs at least one reliable first pointer to Junction A.
3. **Do the optional "Objective reminder" and "Patrol route overlay" count as guidance?** They are accessibility options and default off.

---

*→ See: TUTORIAL.md — the Phase 0–1 teaching beats.*
*→ See: DIFFICULTY_ACCESSIBILITY.md — the optional reminders.*
*→ See: VERBS.md — the eight verbs the guidance leads to.*
*→ See: SOLUTION_MATRIX.md — the obstacles guidance must make findable.*
*→ See: LEVEL_BEAT_SHEETS.md — per-level entry and problem beats.*
*→ See: GATING_BACKTRACKING.md — what locks and unlocks.*
*→ See: scene-notes/Phase 6 Final 22 Hours.md — the unguided phase.*
