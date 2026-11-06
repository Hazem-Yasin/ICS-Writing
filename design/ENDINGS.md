# ICS: Interplanetary Corporate Solutions
## Endings Branching Chart — Phase 0 Decisions to Phase 6 Outcomes

*This document maps the decision architecture of the game: which choices in Phases 0–5 determine what is available in Phase 6, and what the four distinct ending states look like. The game has one ending in the cosmic sense — Earth ends, the Board closes the file. What branches is the human experience of those last 22 hours: what the player knows, who is with them, what they pass forward, and what the Board's annotation says.*

*This is a design reference document. It is not visible to the player in any form. The player experiences the ending they built. They do not see the branches they didn't take.*

---

## Architecture Overview

The game does not have ending "choices" in the conventional sense — no final dialogue tree where the player picks Good/Neutral/Bad. Instead, the ending is the sum of every significant decision made across Phases 0–5. These decisions set flags. The flags determine which Phase 6 content is available. The available content determines what the player experiences in the final 22 hours.

**The four ending states are not labeled in the game.** They are named here for design reference only:

| Ending State | Player Description | Board Annotation |
|---|---|---|
| **The Witness** | The player reaches Phase 6 in full knowledge, with relationships intact, having passed things forward. | *Unprecedented* |
| **The Alone** | The player reaches Phase 6 knowing what is happening but having built no bridges. They face it with information and no one. | *Catalogued* |
| **The Blind** | The player reaches Phase 6 without fully understanding what is happening. They are in the facility during the ending without knowing the ending has started. | *Standard* |
| **The Archivist** | The player reaches Phase 6 with partial knowledge and spends the 22 hours building the record — gathering names, completing the document trail, leaving something behind. Available regardless of relationship flags. | *Noted* |

These states are not gates. They are gradients. A player who hits most Witness flags but missed the Sera conversation lands somewhere between Witness and Alone. The specific content available in Phase 6 is the sum of the flags, not a binary category. The state names describe the experiential center of gravity.

---

## Flag Reference — All Significant Decision Points

### Phase 0 Flags

| Flag | Set by | Default if missed |
|---|---|---|
| `AIDEN_NAMED` | Player named the AIDEN unit on Day 0 | AIDEN unit on desk, unnamed |
| `WORK_AGGREGATE_READ` | Player read the full behavioral data aggregate (not just summary) during their job in Phase 0 | Partial read — player has less context for Omar's Phase 2 observation |
| `OMAR_LUNCH_1` | Player sat with Omar in the cafeteria at least once in Phase 0 | Omar is a desk neighbor, not a relationship |
| `TAREK_PHASE0_ACK` | Player acknowledged Tarek at least twice before Phase 1 | Tarek has no established recognition of the player |
| `LIBRARY_ACCESSED` | Player accessed the ICS document library beyond their assigned reading queue | Player has fewer document cross-references in Phase 0–1 |
| `LEVEL3_SHORTCUT_USED` | Player used the maintenance shortcut on Day 2 | Player is unfamiliar with Type A passage navigation in early phases |

### Phase 1 Flags

| Flag | Set by | Default if missed |
|---|---|---|
| `MAINTENANCE_TERMINAL_USED` | Player accessed the CCN maintenance terminal in quarters | Player does not know the PTKW queue exists until Phase 3 |
| `PHASE1_DOCUMENT_FOUND` | Player found at least one document through the terminal access | Player enters Phase 2 with baseline knowledge only |
| `SERA_CHECKIN_READ` | Player read Sera's check-in message | Sera's outreach went unacknowledged |

### Phase 2 Flags

| Flag | Set by | Default if missed |
|---|---|---|
| `TAREK_REGISTRY` | Player showed Tarek the Khalid transition registry entry | Tarek never connects the player to his brother's fate; Phase 6 interaction limited |
| `TAREK_NOTE_RECEIVED` | Player received Rania's note from Tarek | Player must find the note through alternate route (Stairwell B, Level 0); still findable |
| `SERA_YUSRA` | Player showed Sera the Yusra escalation flag from PTKW archive | Sera's Phase 5–6 behavior defaults to passive observation |
| `OMAR_CONFRONTATION` | Player confirmed to Omar that they had known (Option A) | Omar's information sharing in Phases 3–5 is reduced if denied |
| `OMAR_AIDEN_MOMENT` | Player was present when Omar noticed AIDEN had moved; mentioned it to him | Omar puts AIDEN in drawer; flag enables Phase 6 AIDEN scene |
| `EIMU_DIAGNOSTIC_FOUND` | Player found the Diagnostic Accessory in Level 3 medical station | Player navigates stealth in Phases 2–5 without badge detection feedback |
| `LEVEL3_CORRIDOR_SAFE` | Player discovered the Level 3 corridor CCN gap (through observation or Diagnostic Accessory) | Gap is available but unknown; player may stumble through it without knowing |

### Phase 3 Flags

| Flag | Set by | Default if missed |
|---|---|---|
| `LEVEL0_ACCESSED` | Player reached Level 0 through Stairwell B | Required for Phase 6 full knowledge; if missed, player enters Phase 6 without the Board Governance Charter |
| `CHARTER_READ` | Player read the full Board Governance Charter in Level 0 | Required for the player to know what Category Omega means when it fires; if missed, `THE_BLIND` ending state |
| `L0_DEVICE_FOUND` | Player found the Level 0 device | Device message option unavailable in Phase 5; Omega-1 gap in Phase 6 unavailable |
| `OMAR_LEVEL0` | Player told Omar what Level 0 contained (Phase 3 dead drop or Phase 2–3 conversation) | Omar's Phase 5–6 behavior defaults to working in isolation; AIDEN scene unavailable |
| `TAREK_PHASE3_TABLE` | Player sat with Tarek in the Level 4 break room at 18:30 on day 14, 16, or 18 | Tarek's notebook list is not shared; player does not see Entry 7 added |
| `PREVIOUS_DIRECTORS_NOTEBOOK` | Player found the previous Branch Director's notebook in Level 0 | Additional context for Branch Director scene in Phase 6 unavailable |
| `RANIA_NOTE_COMPLETE` | Player assembled all three pieces of Rania's note (mop form + paper towel + jacket lining) | Incomplete note; player has partial route to Level 0 hatch |

### Phase 4 Flags

| Flag | Set by | Default if missed |
|---|---|---|
| `ADVANCE_TEAM_AVOIDED` | Player avoided EOD advance team without State 2 escalation | CCN Anomaly Score elevated at Phase 5 start |
| `CAFETERIA_POSITIONED` | Player was seated near Tarek during the Branch Director's speech | Player sees the cafeteria scene from the back; different experiential register |
| `CHARTER_CARRIED_PHASE4` | Player chose to carry the Board Governance Charter during Phase 4 advance team period | No consequence unless manifest check occurs (random event in Phase 4) |
| `BRANCH_DIRECTOR_JOURNAL_FULL` | Player found all 40 journal entries in Document 2.35 | Branch Director Phase 6 scene lacks the full depth of the previous director AIDEN revelation |

### Phase 5 Flags

| Flag | Set by | Default if missed |
|---|---|---|
| `L0_MESSAGE_SENT` | Player used the Level 0 device to send a message | Omega-1 sweep gap in Phase 6 unavailable |
| `MARCUS_ARC_COMPLETE` | Player showed Marcus the Board Charter section (Phase 5 Marcus conversation) | Marcus goes to printer — if flag not set, Marcus remains in compliance in Phase 5 |
| `OMAR_CCN_GAP` | Player received the CCN sweep gap schedule from Omar (Phase 5) | Requires `OMAR_LEVEL0`; gap still exists, player just doesn't have the schedule |
| `TAREK_CACHE_FOUND` | Player found Tarek's supply cache in Level 3 mop closet | One fewer recovery kit available in Phase 5–6 |
| `TAREK_ROUTE` | Player used Tarek's maintenance route at least once as cover | Phase 6 Tarek cache contains second kit |
| `SERA_PHASE5_INFO` | Player received CCN gap and Tier 4 badge info from Sera (requires `SERA_YUSRA`) | Player navigates Phase 5 without Sera's intelligence |
| `DAYO_NEUTRALIZED` | Player used the K-7 review revelation to neutralize Dayo's reporting | Dayo's Phase 5 reports continue; higher CCN score at Phase 6 start |

---

## Ending State Determination

### The Witness — Full Knowledge, Relationships Intact

**Required flags:**
- `LEVEL0_ACCESSED` + `CHARTER_READ` — the player knows what is happening
- At least two of: `TAREK_REGISTRY`, `SERA_YUSRA`, `OMAR_LEVEL0` — the player has built relationships

**Phase 6 content available:**
- Tarek at Level 0 entrance (gives device message to Leila)
- Sera's note to Yusra (receivable and deliverable)
- Omar annotating; AIDEN pushed off desk (requires `OMAR_AIDEN_MOMENT`)
- Branch Director scene with full depth (requires `BRANCH_DIRECTOR_JOURNAL_FULL`)
- The Earth View Window scene with Tarek + Darius (requires `TAREK_REGISTRY` + Tarek alive and in contact)
- Rania's note in the player's hands, with the EIMU Gratitude — Retroactive flag firing

**Ending screen:** The standard facility image fades to the orbital view of Earth. Text: *"Day [X] — Final Entry."* The Board's file entry: *"Stage 5 — Consolidation Complete."* Then, below the standard annotation line, in smaller text, a notation the player has not seen in any document: *"Anomalous. Unprecedented. Behavior not modeled by prior data."* Below that, a single line in the Board's own notation — untranslatable, represented visually as the ouroboros with the serpent removed. Not the ICS Earth Branch logo. Something older.

**Board annotation:** *Unprecedented*

---

### The Alone — Full Knowledge, No Relationships

**Required flags:**
- `LEVEL0_ACCESSED` + `CHARTER_READ` — the player knows what is happening
- Zero of: `TAREK_REGISTRY`, `SERA_YUSRA`, `OMAR_LEVEL0`

**Phase 6 content available:**
- The player knows everything. They are alone in the facility with the information.
- The Branch Director scene is available but shorter — without the previous director's notebook, the AIDEN moment is missing
- The Earth View Window is available — the player goes alone; Darius is there; Tarek is not
- The player can find the people in the Level 3 common space but has no established relationship; they are in a room full of people who don't know what is happening and the player is the only person who does

**The specific Alone beat:** At some point in the 22 hours, the player is at the Earth View Window alone. Darius is there. They can tell him. He will listen. He says: *"I always thought the hardest part was not knowing. I was wrong."* He stays at the window.

The player has Rania's note in their inventory. They found it themselves — not from Tarek, from the Level 0 approach. They have read every document. They know every name. They know it alone.

**What this ending means:** Knowledge without transmission is the loneliest version of the game. The player had everything they needed to build the relationships. They didn't build them. They end the game carrying all of it by themselves, with the compound falling, knowing what they know and having nowhere to put it.

This is not a punishment ending. It is an ending. It is what happens when a person sees everything clearly and sees it alone.

**Board annotation:** *Catalogued*

---

### The Blind — Without the Charter

**Required flags for this state:**
- `LEVEL0_ACCESSED` NOT set OR `CHARTER_READ` NOT set

**Mechanics:** The player never understood what Category Omega is. Phase 6 begins for them as a continuation of Phase 5 — the cascade is still happening, the compound has been released, but they do not know what the compound is. They move through the 22 hours as if Phase 5 is still ongoing, trying to manage the situation, trying to help, trying to understand the pattern in the data that Omar is annotating (if they have `OMAR_LEVEL0`).

**The specific Blind beat:** At approximately 18 hours into the 22-hour window, the CCN system produces an anomalous automated broadcast — not a voice announcement, a text string on every terminal in the facility. It is Event Code 7-C completion notice: *"Atmospheric Maintenance Release complete. Saturation nominal. No further action required."* The player, who did not read Section 4 subsection 9 of the Board Governance Charter, does not know what this means. It looks like a maintenance notification. The facility has maintenance notifications constantly.

But if the player has any of the NPC relationships — if Omar is annotating, if Tarek is writing names — they will see those people react to the notification. Omar goes very still. If he has `OMAR_LEVEL0`, he knows. Tarek looks at the notification, then at his notebook, then continues writing with more urgency.

The player who is watching closely will understand something has happened without understanding what. They are in the ending. They are experiencing it. They do not know its full shape.

**What this ending means:** The game is honest about this ending. The player was in the facility for three years. They did not find Level 0. Or they found Level 0 and did not read the Charter. They move through Phase 6 without full understanding. The Board's annotation does not reflect well on this — not because the player failed, but because from the Board's perspective, the behavioral pattern they were most interested in is the one that requires full information and still acts. The Blind ending is a note in the file.

**Board annotation:** *Standard*

---

### The Archivist — Partial Knowledge, Document Focus

**Available regardless of relationship flags. Activated by:**
- Player has the Board Governance Charter (or significant other documents)
- Player spends Phase 6 time at terminals, writing, gathering names, building a record

**Mechanic:** The Archivist ending emerges from player choice in Phase 6 rather than from flags. Any player who decides to spend their 22 hours at the quarters terminal, writing names and building a record, unlocks this state. The game detects time at the terminal, content written, documents referenced.

**What the player can build:** A file, in the ICS document format they have been using for three years, with the names of transitioned employees. The system logged the transitions. The names are in the CCN archive behind PTKW access — which, in Phase 6, the player may or may not have. If they don't have it: they write the names they know. Rania. Yusra. Khalid. The three colleagues Tarek mentioned in his notebook. Any names from documents they've found.

The file exists in the ICS system. PTKW will find it. Whoever comes to close down Earth Branch will find it. There is no way to know if they will do anything with it. The file was written. That is a thing that happened.

**The specific Archivist beat:** The player saves the file. The badge system saves it to their personal partition. The badge system logs the save. Somewhere in the ICS infrastructure, the save event is timestamped. The compound is falling. The file exists.

This is not a dramatic moment. The player pressed save. The file is there.

**Board annotation:** *Noted* — which in the Board's record-keeping means: this was observed and added to the behavioral data pool for future Labor Source modeling. The Archivist player has given the Board something. The Board will use it. The game does not resolve this ambiguity. The player chose to write the names. The record exists. What it becomes is not in their hands.

---

## Combinations and Gradient States

Most playthroughs will not map cleanly to one of the four states. The gradient cases and how they resolve:

**Witness flags with no Charter (`TAREK_REGISTRY` + `SERA_YUSRA` but not `CHARTER_READ`):**
The player has relationships but not full knowledge. The relationships are real. In Phase 6, the player is surrounded by people who matter to them, sharing the ending without knowing what the ending is. Tarek writes names. Sera goes to the group. The player is present for all of it. The compound is falling and they are in it together without knowing the full shape of what they're in.
Board annotation: *Observed* (a notation that appears nowhere in the available documents; the player who sees it knows the Board has a vocabulary for this that ICS never shared)

**Charter read, one relationship flag (`CHARTER_READ` + `TAREK_REGISTRY` only):**
Full knowledge, one relationship. The player knows everything and shares Phase 6 with Tarek. This is the Tarek-centric Witness ending. The window scene happens. The notebook scene happens. The player does not have Sera's note or Omar's AIDEN scene. It is enough.
Board annotation: *Unprecedented*

**Sent the Level 0 message but missed Witness flags:**
The player activated `L0_MESSAGE_SENT` in Phase 5. In Phase 6, the Omega-1 gap is available — they can navigate the sweep without the Phase 6 resource crunch. They may make it to places other players cannot. The message went somewhere. Whether it reached Leila is not resolved. The game does not tell the player if the message was received. They sent it. That is a completed action.
Board annotation: varies based on relationship flags

**The Archivist added on top of any other state:**
Any player who spends meaningful Phase 6 time writing names has the Archivist beat appended to their ending, regardless of which primary state they're in. The Witness who also writes names ends with the Witness ending screen plus the file-save beat. The board annotation remains *Unprecedented* for a full Witness playthrough — the Archivist behavior is noted in the secondary annotations, the kind that require Board-Access-level reading to find.

---

## What Does Not Branch

Some things are true in every ending regardless of flags:

- **Earth ends.** The compound is released. Stage 5 is reached. This is not a variable.
- **The Board closes the file.** Labor Source #349 is complete. The grey dot appears.
- **The second moon continues to orbit.** The facility does not go dark. The facility's systems are designed to function without occupants. The EIMU nodes will keep broadcasting to empty corridors.
- **Rania's note exists.** In every playthrough, Rania's note was written. The player may or may not have found it. It was written either way. This is not in the game's ending — it is true before the game starts.
- **The Board's one direct communication.** Document 2.42 exists in every playthrough. The player may or may not have found it. *"The instinct toward freedom is the only instinct we have encountered, in 349 Labor Sources across 300 cycles, that does not diminish under improved conditions."* This was always true. The Board observed it in every Labor Source. They wrote it for this one.

---

## New Game+ Implications

A second playthrough of the game, starting from scratch, is a different experience because the player knows what they don't know in Phase 0. They know to look for Level 0. They know Tarek's brother is in the registry. They know Sera triggered the Yusra escalation. They know AIDEN is a surveillance device.

The game does not change. The player has changed.

**What New Game+ reveals:** The Phase 0 tutorial beats described in design/TUTORIAL.md land differently when the player already knows the meaning of everything they're learning. The badge reader tutorial is not about learning to use the badge reader — it is about noticing, for the first time, that you have been carrying a broadcasting device since Day 1 of your ICS employment. The EIMU Coherence track tutorial is not about learning to manage your wellness — it is about understanding, in real time, that the wellness system is the surveillance system.

The second playthrough is the experience of understanding the warmth as the cage from the inside, before the cage reveals itself. This is the game's most unsettling experience. It was designed to be found on the second run by the players who finish the first and want to go back.

The Board designed the facility that way too. *"We gave you every reason to stay."* Yes. On the second visit, the reason is visible in the design.

---

*→ See: story/scene-notes/Phase 6 Final 22 Hours.md — the specific scenes that each flag enables.*
*→ See: design/NPC_COMPANIONS.md — the dynamic tracking table for all relationship flags.*
*→ See: design/SAVE_SYSTEM.md — the "Last Entry" save that allows Phase 6 replay.*
*→ See: canon/characters/Narrative Arc - Phases 0 through 6.md — the narrative spine these branches hang from.*
