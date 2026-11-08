# ICS: Interplanetary Corporate Solutions

**A first-person narrative game in the style of BioShock.** The player is a human employee inside the ICS Earth Branch — a corporate facility shaped like a second moon in orbit above Earth. ICS is an alien-run planetary labor company. The warmth is real. The cage is real. The horror is that you cannot point to the moment it goes wrong, because it was always this.

---

## Layout

```
canon/      What is true in the world. Source of truth for lore.
  documents/  characters/  facility/  enemies/  weapons/
  internal-communications/   (A employee, B PTKW, C Branch Director, D design team)
story/      What the player experiences, written as prose.
  STORY.md  EXTENDED.md  trailers.md
  scenes/ (new scenes, 1.1-1.13)  scene-notes/  trailers/
design/     How the game works: systems, pacing, production. Mostly [PROPOSAL].
meta/       How we work: STYLE_GUIDE, CANON_DECISIONS, HANDOFF_CARTOGRAPHER.
reference/  Generated snapshot of the whole corpus. Read-only.
```

If two files disagree, `canon/` wins over `story/`, and `story/` wins over `design/`.

### Repository

This is one git repository. Every file keeps its path, so links and the lookup tools work unchanged. The master reference in the reference folder is generated and not tracked: run `python3 tools/ics.py build` after cloning to create it, and again after changing content to refresh `meta/` and `reference/`. To rebuild and check on every commit, run `python3 tools/ics.py install-hooks`.

---

## Files

### Canon & Narrative

| File | Contents |
|---|---|
| `canon/documents/` | **The canon.** All 62 in-world documents (2.1–2.62), one file each, including the Glossary (2.29). The source of truth for lore, access tiers, and cross-references. The two old compiled files (WORLD and ICS - Rigged Sphere) were retired; their unique text lives in the master reference below. |
| `reference/` | **Master reference (generated snapshot).** One large read-only file with the writing files verbatim, plus Appendix A (Game Overview, the earlier Doc 2.32 version, recovered variants). It duplicates the other files and will drift; don't edit it. The script that regenerated it was in the retired writing map. |
| [`design/DESIGN.md`](design/DESIGN.md) | **The blueprint.** Characters, narrative arc (Phases 0–6), scene notes, and Document 2.41 (EOD's perspective). This is where the game lives. |
| [`story/STORY.md`](story/STORY.md) | **The story itself.** Six scenes written as experienced narrative: the interrogation, what happened in the atrium on Day 21, the Level 0 descent and Section 7, Tarek standing up, Maren Voss in the final hours, and the ending. |
| [`story/scenes/`](story/scenes/) | **New scenes.** Thirteen short scenes that sit in the gaps of the canon: EOD at Labor Source #312 and on Earth, Omar, Sera, Tarek, Yusra, James, Kai's shift, the atrium and the folder, the Director's Entry 37, a Monday coffee queue, and K-7's forty minutes. All [PROPOSAL]. |
| [`meta/STYLE_GUIDE.md`](meta/STYLE_GUIDE.md) | **One-page style guide.** Voice, motifs to keep, tics to retire, canon rules for scenes. |
| [`meta/CANON_DECISIONS.md`](meta/CANON_DECISIONS.md) | **Rulings for the author.** The real contradictions with proposed defaults, and a triage of the [PROPOSAL] material. |
| [`story/scene-notes/The Review Room.md`](story/scene-notes/The Review Room.md) | **Scene note.** The Step 1 conversation in Level 2 Room 3: a good tea, a clock two minutes fast, and a fact the player can only see from outside. **[PROPOSAL]** |
| [`story/EXTENDED.md`](story/EXTENDED.md) | **The long reads.** Schedule D pages 1–6, Yusra's full resistance document, and the Branch Director's address — the three documents the player finds and must read completely. |
| [`story/trailers.md`](story/trailers.md) | **Seven trailer/ad scripts.** "The Crack," "The Offer" (revised), "The Contract," "The Archive" (post-release, Board POV), the 30-second in-world TV spot "Something Better," and "The Envoy" (EOD, told across Global, PTKW and Board access). Four are also split into `story/trailers/`; the TV spot lives only in `story/trailers.md`; "The Envoy" lives only in `story/trailers/Trailer 5 - The Envoy.md`. "The File" (Trailer 6) is a tag that can close any trailer: the sound of the Folio file opening, then the EOD card; its Name field is left for the author (`story/trailers/Trailer 6 - The File.md`). |

### Game Design Systems

| File | Contents |
|---|---|
| [`design/PROGRESSION.md`](design/PROGRESSION.md) | **Badge tier system.** The badge IS the character sheet. Tier 1–5 unlock mechanics, 847 undeactivated badges in the system, the badge as the game's primary progression mechanic. |
| [`design/PLAN_SYSTEM.md`](design/PLAN_SYSTEM.md) | **The Plan system.** Cover story against real reason, the five information layers, Support Steps 1–5, the Perception Alignment layer, the hidden Plan meter and the NPC arcs. **[PROPOSAL]** |
| [`design/HEALTH_SURVIVAL.md`](design/HEALTH_SURVIVAL.md) | **Four-track vitals system.** Physical Integrity, Neurological Status, Thermal Regulation, EIMU Coherence — each track, its sources of damage and recovery, and what flat-lining each one looks like. |
| [`design/ENEMY_AI.md`](design/ENEMY_AI.md) | **Behavioral states for all 5 enemy categories.** PTKW Security, True Believers (Marcus/Lani/Cho), Arrangement Class (Dayo/Priti), Omega-1, and EOD advance team. Four-state alert ladder. |
| [`design/STEALTH_DETECTION.md`](design/STEALTH_DETECTION.md) | **Full detection architecture.** Visual, EIMU, and acoustic detection inputs. Zone coverage map. CCN Anomaly Score. Maintenance passage rules. EIMU Diagnostic Accessory. Phase-by-phase detection summary. |
| [`design/NPC_COMPANIONS.md`](design/NPC_COMPANIONS.md) | **Tarek, Omar, Sera — dynamic interaction.** Phase-by-phase behavior for each NPC. Specific conversation options, flags, and Phase 6 outcomes. The unannounced relationship design principle. |
| [`design/INVENTORY.md`](design/INVENTORY.md) | **10-slot inventory system.** Badge-as-interface design. Item categories (documents, tools, recovery, key items). Inventory pressure in Phase 5. The Phase 4 manifest check. |
| [`design/AUDIO_VOICE.md`](design/AUDIO_VOICE.md) | **11 voices, full audio log design.** Who speaks, what they say, why audio vs. text, performance notes. Includes Rania's single recording and the Senior Analyst's 11-second log. Ambient audio by phase. |
| [`design/SAVE_SYSTEM.md`](design/SAVE_SYSTEM.md) | **Save architecture.** Continuous autosave, one manual save slot (quarters only), irreversible events list, death save behavior, and the "Last Entry" Phase 6 permanent save. |
| [`design/TUTORIAL.md`](design/TUTORIAL.md) | **Tutorial-as-job design.** 10 mechanic introduction beats across Phase 0–1. Discovery tutorial schedule for Phases 2+. What is never explicitly taught and why. |
| [`design/ENDINGS.md`](design/ENDINGS.md) | **Endings branching chart.** Full flag reference (Phases 0–5). Four ending states: The Witness, The Alone, The Blind, The Archivist. Gradient states. What does not branch. New Game+ implications. |
| [`design/VERBS.md`](design/VERBS.md) | **The verb sheet.** The eight things the player can do (Move, Read, Badge, Use, Modify, Speak, Slip, Witness), how each feels, and what each costs. Canon and proposals tagged separately. |
| [`design/SOLUTION_MATRIX.md`](design/SOLUTION_MATRIX.md) | **Obstacles × answers.** Every obstacle in the facility with the non-lethal answers the existing tools and verbs give, and what each answer costs. |
| [`design/TENSION_CURVE.md`](design/TENSION_CURVE.md) | **Pacing across Phases 0–6.** Intensity targets, peaks, valleys, safe-space ledger, pacing rules, playtime split. |
| [`design/LEVEL_BEAT_SHEETS.md`](design/LEVEL_BEAT_SHEETS.md) | **Level beat-sheet template**, filled in for Levels 0–14 (Levels 0 and 4 in detail; the rest are draft tables). Includes inconsistencies found between level files. |
| [`design/DISCOVERY_SEQUENCE.md`](design/DISCOVERY_SEQUENCE.md) | **Discovery sequence & narrative spine.** Single ordered path across Phases 0–6, room-by-room trajectory, key document pickups, and full staging of named set pieces (Rania's 3-part note, Level 0 Charter retrieval, Atrium confrontation, Cafeteria stand, PTKW backlog). |
| [`design/TIME_MODEL.md`](design/TIME_MODEL.md) | **Time model.** Weekday anchor, phase boundaries, day-by-day ledger, Phase 6 arithmetic, NPC schedules, real-time rates, action time costs. |
| [`design/EOD_ENCOUNTERS.md`](design/EOD_ENCOUNTERS.md) | **EOD, encounter by encounter.** Modes A/B/C, Phase 2 beats, Day 21 atrium, capture flow, tools versus him. |
| [`design/PLAYER_GUIDANCE.md`](design/PLAYER_GUIDANCE.md) | **How the game says "go there."** Five channels, guidance by phase, what never appears, Phase 6 as unguided. |
| [`design/GATING_BACKTRACKING.md`](design/GATING_BACKTRACKING.md) | **Gates and backtracking.** Credential ladder, level graph, what closes, what never closes, sequence breaks. |
| [`design/FAILURE_LOOP.md`](design/FAILURE_LOOP.md) | **Death, capture and retry.** The failure states, the retry flow, target fail rates, when the player is stuck. |
| [`design/UI_MENUS.md`](design/UI_MENUS.md) | **HUD, badge, menus.** What is on screen, the badge tabs, boot, pause, save/load, settings, credits. |
| [`design/SOLCRED_ECONOMY.md`](design/SOLCRED_ECONOMY.md) | **SOLCRED as a mechanic.** Canon prices, where it appears, what it is for, detection flags. |
| [`design/TOOL_TUNING.md`](design/TOOL_TUNING.md) | **Tool numbers in one place.** Charges, durations, ranges, build times, enemy parameters, playtest targets. |
| [`design/LOGO.md`](design/LOGO.md) | **The Earth Branch mark.** Construction, colour, the wordmark, minimum sizes, the readings by access layer, where the mark is deliberately absent, and open questions. Generated files are in `design/brand/` (SVG and PNG). **[PROPOSAL]** |
| [`design/ART_DIRECTION.md`](design/ART_DIRECTION.md) | **Visual direction.** Brand colours, light by place and phase, materials, mascots, camera. |
| [`design/BADGES_AND_UNIFORMS.md`](design/BADGES_AND_UNIFORMS.md) | **Badges and attire.** Tier cards, department glyphs, per-character badge sheet, PTKW/Director/stripped badges, uniforms for every group. Canon vs [PROPOSAL] marked. |
| [`design/ENVIRONMENTAL_STORYTELLING.md`](design/ENVIRONMENTAL_STORYTELLING.md) | **Placement rules and prop manifest per level.** The Blender files it once linked to were removed from this repo. |
| [`design/PRODUCTION_SCOPE.md`](design/PRODUCTION_SCOPE.md) | **Production questions.** What the design fixes, scope drivers, vertical slice, engine, localization, QA. All figures are placeholders. |
| [`design/JOBS_AND_CAREER.md`](design/JOBS_AND_CAREER.md) | **Jobs and the career ladder.** What the player's job produces, why the department is fixed, second jobs through acquired badges, tier versus role, and what a rung pays besides access. All [PROPOSAL]. |
| [`design/DIFFICULTY_ACCESSIBILITY.md`](design/DIFFICULTY_ACCESSIBILITY.md) | **Difficulty as information, not damage.** Presets, individual options, vision/hearing/motor/cognitive/photosensitivity accessibility, controls. |
| [`meta/HANDOFF_CARTOGRAPHER.md`](meta/HANDOFF_CARTOGRAPHER.md) | **Handoff brief: Archivist → Cartographer.** What exists, what is missing, canon not to break, working rules, and the open rulings to resolve with the user. |



### Facility

| File | Contents |
|---|---|
| [`canon/facility/Overview.md`](canon/facility/Overview.md) | The full facility — orbital position, BES design philosophy, level structure, what it smells like. |
| [`canon/facility/TV_SCREENS.md`](canon/facility/TV_SCREENS.md) | **The Broadcast Display System.** 200+ screens, the advertising characters (SONA, BRIK, the Wellness Pair), all products, SOLCRED pricing, and what the BDS looks like when the warmth is gone. |
| `canon/facility/Level 0.md` through `canon/facility/Levels 11-14.md` | Individual level files. |
| `canon/facility/Maintenance Network.md` | The parallel map — Type A, B, C passages. |

### Internal Communications

| File | Contents |
|---|---|
| `canon/internal-communications/README.md` | Index of all recovered correspondence: A (employees), B (PTKW), C (Branch Director / HQ), D (design team). |
| [`design/HEARTH.md`](design/HEARTH.md) | **Hearth, the ICS Earth Branch internal messaging system.** The in-world name, the design (Deep Blue and Warm Gold, three panes), the folders (delivered, drafts, held by CCN, sealed, found notes), and how the viewer is built from the messages and kept current by the writing map. **[PROPOSAL]** |
| [`design/ICS_OS.md`](design/ICS_OS.md) | **ICS-OS (version 0.1), the ICS Earth Branch operating system.** Boot, sign-in and desktop; three windowed apps (Hearth mail, ICS Cloud Drive, Folio document viewer); cloud-only files with no local save; clearance by whole file and by layered section; and the Branch Director's retained copies of Staff and PTKW mail. Lives in its own folder, ICS-OS, beside the writing map. **[PROPOSAL]** |
| [`design/DEVICES.md`](design/DEVICES.md) | **Devices and addresses.** The invented mail domain (`.ics`, never ics.org), department and staff mailboxes, the device map (Manager, K-7, Director, a Work Floor B desk, found notes), where each slice of the 95 messages lives, and the passwords (`smiling-man`). **[PROPOSAL]** |
| [`tools/`](tools/) | **Scripts.** `mail_index.py` counts messages per mailbox; `add_addresses.py` appends `<address>` to From/To/Cc (dry run by default); `export_mail.py` writes `mail.json` (95 messages and the four device slices) for the game. Run with `python3 -I`. **Lookup:** `build_index.py` rebuilds `meta/INDEX.md`, `ENTITIES.md`, `LINKS.md`, `FACTS.md` and `graph.html` (also `--who EOD`, `--links C-24`, `--find text`); names and numbers it tracks are in `entities.json` and `facts.json`. **One command:** `python3 tools/ics.py build` rebuilds everything generated (also `check`, `impact C-24`, `who EOD`, `install-hooks`); `build_extras.py` writes `meta/THREADS.md`, `OPEN.md`, `ACCESS.md`, `TIMELINE.md`; start at `meta/LOOKUP.md`. `build_master.py` rebuilds the master reference snapshot. `make_logo.py` draws the ICS mark into `design/brand/` (`--png` also renders PNGs). `fix_encoding.py` repairs mojibake. **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-18 — EOD Research Team - Deployment 287 Field Report Update Request.md` | The EOD Research Team asks the Earth Branch Manager for findings on Deployment Order 287; the Branch replies that it cannot place EOD at any point in the ten days. **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-19 — EOD Research Team - Deployment 287 Field Report Update - Team Blue Harrow - Last Survivor Interview.md` | **Newest.** Day 22: the Branch Manager's update to C-18. It places EOD at Sudbury on Day 16, explains the ten days and reproduces the Blue Harrow survivor's transcript; the Research Team replies. Split out of C-18. **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-20 — EOD Research Team - Deployment 287 Field Report Update - Team Gyrfalcon Wing - Incident Report.md` | The Branch Manager corrects C-19: the second demonstration (Gyrfalcon Wing, Day 18) was not ARM-27's. A cockpit and radio transcript, no casualties; the Research Team replies. **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-21 — EOD Research Team - Deployment 287 Field Report Update - Team Gyrfalcon Wing - Open Water Combat Report.md` | Day 21: the air engagement — HAWK patrol spots EOD on the surface, Gyrfalcon Wing scrambles, one pilot breaks formation and his face is pressed flat against his own canopy by an open hand before weapons release; the other seven engage for 36 minutes with no hits. One of them, Captain Eirik Aronsen (Gyrfalcon Seven), is flown by hand by the contact, ordered to eject by his father, and killed in the sea after his father says "son", the contact turns back and the parachute is cut. On the way he tells his father he is dead and knows it, and tells humans to be afraid and to proceed despite being afraid. Eight pilots dead total; seven aircraft land, one empty. ARM-27's first active sortie since the Show of Force. Sealed with C-23 and Doc 2.49; the question of why the Captain was smiling is first raised in a board note. **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-22 — EOD Research Team - Deployment 287 Field Report Update - Team Gyrfalcon Senior Officer - Hallvik Tower Conversation Report.md` | Day 21 (continues C-21): EOD and ARM-27 stand at the Hallvik tower; the Wing's commander shoots at him through bullet-proof glass and EOD speaks plainly ("downsizing", "branch sunsetting"). The tower cab recording, the Branch Manager's conclusions and the Research Team's reply. **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-23 — EOD Research Team - Deployment 287 Field Report Update - Master Summary.md` | **Newest.** Day 28: the Branch Manager's master summary of all four Deployment 287 events (C-19 through C-22), drawing the through-line — four demonstrations, four audiences, one argument. The Research Team replies at length: its human-psychology study (Doc 2.18) succeeded and fear is a useful instrument; what it expected of humans facing EOD; Eirik's refusal and his message to the species, and Gyrfalcon Three's inverted pass, which it did not expect and will study further; and EOD's own debrief statement, that humans who smile at certain death cannot be controlled. Sealed: readers are the Research Team, the Earth Branch Manager and EOD, not PTKW. **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-24 — EOD Research Team - The Discussion of EOD Sunsetting.md` | **Newest.** Day 29: the Research Team to the Earth Branch Manager, two readers only (one level above Doc 2.49; EOD is excluded). The words EOD said about Eirik must never be said or heard in any branch or asset planet, given ICS's record of never failing. The Team asks the Manager to watch EOD closely, or to sunset him: the Journey Completion Directorate (fourteen of its members held ready, from a larger roster) will arrive disguised as a rival company's force, he will fight it, and the analysis says 100 percent. Failure to report puts the whole Branch before the Board and the Directorate. He will be announced as a hero who died defending ICS, and the humans must never question it. The Team asks the Branch for the location, the damage costs and the repair time, and supplies the public statement ("After more than 300 years…"). **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-25 — Earth Branch Manager - Reply to The Discussion of EOD Sunsetting.md` | **Newest.** Day 30: the Earth Branch Manager's reply to C-24, two readers only. It opens to EOD by his full name and "my dear friend" (a line he will never read), then argues seven reasons to hold the sunset order, proposes the first option under his own hand, and prepares the entire Level 7 floor for EOD's farewell and the fight, "the least he can do for an old friend" (Day 38, 02:00 Branch Time). He says he will comply if the Team insists, and asks that EOD be told the attackers are real and have come to destroy the Branch, so that he dies believing he protected the ICS he served. **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-25 — HQ Host Force Monitoring Instruction.md` | **Newest.** PTKW Oversight tells Level 5 to monitor the Harrow and Gyrfalcon Wing by open sources only, and not to tell Branch Operations. **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-26 — Incident Report ICS-IR3 - Restricted Designation Heard and Document Recovered.md` | Day 32: PTKW Level 5 duty officer to K-7 and TOR-9. A human asset (E-03615, Operations Division, Work Floor B) is heard saying "[Subjugator]" at his desk, and a print of a scan of the Doc 2.15 designation block is found in his drawer, with "Executioner of Despair" highlighted and, above it, his own written reaction. Form ICS-IR3 and the seven-part source investigation; the asset is retained, not released and not reclassified, because he is the only trace. The handling note records that PTKW officers have now read names that are not for PTKW use. **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-26 — Earth Branch Manager - EOD First Arrival at Labor Source 312 - Cycle 292 Thread.md` | **Newest.** Cycle 292 Q2 (an earlier planet, off the game timeline): the Manager of Labor Source #312 writes to HQ about a man with no badge who smiles and waves at everyone, and whom he finds hard to look at; HQ copies the EOD Research Team and tells it to explain; the Team sends the eight-section handling manual that comes with EOD, with a cropped one-page scan of his profile as section 7. The Manager kept it, and told the Division the page was destroyed. He is now the Earth Branch Manager. **[PROPOSAL]** |
| `canon/internal-communications/employee/A-28 — Lior and Chidi The Man Without a Badge.md` | Day 4, 19:12 to 19:40: two Level 3 assets (E-03615, E-03702) talk about the unbadged man in the Level 2 corridor, whose doors open before he reaches them, and Lior decides to ask the floor liaison. **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-27 — Intercept Thread — Lior Asks the Floor Liaison About the Man Without a Badge.md` | Day 5: Lior's polite query to the Floor Liaison, the Liaison's rude reply that PTKW does not know and he should expect updates, and the forward to K-7, who will ask the Manager. **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-28 — K-7 Asks the Earth Branch Manager About EOD and Forwards His Answer to All PTKW.md` | Day 5 to 6: K-7 asks the Manager. The Manager tells all PTKW to tread carefully around his old friend, whose commands apply as if he outranked anyone. He forwards the old manual from C-26 with the page removed, and K-7 sends it to all PTKW against his instruction. **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-29 — Investigation Result ICS-IR3-300Q4-032 - The Source of the Sheet Is Not Found.md` | Day 34: the Investigation Team reports the seven lines of B-26. The page was cut by the Research Division and scanned on a device outside the logged queues; E-03615's document path cannot reach a Board page; nine readers; the Oversight Unit's five-point direction (a recorded exposure is not an incident, repeating is). The source is not found. E-03615 asked one question: "Is it true?" **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-30 — Incident Report ICS-IR3 - PTKW Designation of ICS Written on a Wall.md` | **Newest.** Day 36: the PTKW expansion of ICS ("INFLATABLE CROWD SOLUTIONS") is found in black marker on the Level 3 corridor wall by a night cleaner and removed after 68 minutes; about 450 people may have read it; two sleeping assets' badges pass the doors in the night. Who wrote it, and how they knew, is the investigation; the duty officer notes that Level 5 itself may be where the words left. **[PROPOSAL]** |
| `canon/internal-communications/employee/A-29 — Chidi and Ruth Read It Once REDACTED EVIDENCE.md` | Day 31 chat, redacted by the PTKW investigation team on Day 33 as evidence in ICS-IR3-300Q4-032: two assets say they read the sheet once, do not have it, and discuss what it said. Three redactions and a cover note. **[PROPOSAL]** |
| `canon/internal-communications/employee/A-30 — Femi to Hana New Chapter.md` | Day 9: Femi says goodbye to Hana. **[PROPOSAL]** |
| `canon/internal-communications/employee/A-31 — Sera to Kai A Quick Conversation.md` | Day 24: Sera schedules Kai's Step 1. **[PROPOSAL]** |
| `canon/internal-communications/employee/A-32 — Marcus Draft Fourteen.md` | Day 7: Marcus's fourteenth draft. **[PROPOSAL]** |
| `canon/internal-communications/employee/A-33 — Idris to Kai Thank You for the Tea.md` | Day 19: Idris thanks Kai for the tea. **[PROPOSAL]** |
| `canon/internal-communications/employee/A-34 — Omar Belonging Pulse Drafts.md` | Day 4: Omar drafts his Belonging Pulse answers. **[PROPOSAL]** |
| `canon/internal-communications/employee/A-35 — Tarek Notebook Cakes.md` | Day 41: Tarek's notebook, cakes in the Floor B bins. **[PROPOSAL]** |
| `canon/internal-communications/employee/A-36 — Hana to Sera Which Day.md` | Day 41: Hana asks Sera which day. **[PROPOSAL]** |
| `canon/internal-communications/employee/A-37 — Sera Unsent Hana Desk.md` | Day 58: Sera's unsent note about Hana's desk. **[PROPOSAL]** |
| `canon/internal-communications/employee/A-38 — Noor to the Floor Liaison Three Questions.md` | Day 17: a comfortable asset writes three polite questions to the Floor Liaison. **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-31 — K7 to K12 Floor B and the Ten Per Cent.md` | Day 5: K-7 to K-12 on Floor B and the ten per cent. **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-32 — TOR9 on a Pre-Filled Results Page.md` | Day 41: TOR-9 on a pre-filled Results page. **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-33 — Facilitator to Femi Floor Too Good.md` | Day 6: Facilitator to Femi, Floor B is too good. **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-34 — K12 Belonging Pulse Item 3 and What Comes After.md` | Day 14: K-12 on Belonging Pulse item 3. **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-35 — PTKW Staff Care Outcomes Summary.md` | Day 26: PTKW Q4 Care Outcomes summary. **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-36 — Oversight Perception Alignment Instruction and Withdrawal.md` | Day 41: the Oversight instruction on Perception Alignment and its withdrawal. **[PROPOSAL]** |
| `canon/internal-communications/ptkw/B-37 — Floor Liaison and K12 Comfortable Inquiry Escalation.md` | Day 17: the Floor Liaison and K-12 agree to escalate Noor's questions, and K-12 explains what happens to her. **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-27 — Director to HQ Calibration Round and Tier Velocity.md` | Day 7: Director to HQ on the calibration round and Tier Velocity. **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-28 — HQ to Director Routing E-02210 Voluntary Transition.md` | Day 8: HQ routes E-02210's Voluntary Transition. **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-29 — Director Leadership Reflection Plan.md` | Day 15: the Director's Leadership Reflection Plan. **[PROPOSAL]** |
| `canon/internal-communications/branch-director/C-30 — Earth Branch Manager and Research Team Does EOD Have a Step 5.md` | Day 33: Earth Branch Manager and Research Team, does EOD have a Step 5. **[PROPOSAL]** |
| `canon/internal-communications/design-team/10 — Akar — The Completion Rate.md` | The Completion Rate. **[PROPOSAL]** |
| `canon/internal-communications/design-team/11 — Vance — The Wording on the Growth Plan Form.md` | The wording on the Growth Plan form. **[PROPOSAL]** |
| `canon/internal-communications/design-team/12 — Ohm — The Ten Per Cent and the Resistance Index.md` | The ten per cent and the Resistance Index. **[PROPOSAL]** |
| `canon/internal-communications/design-team/13 — Akar — The Open Door.md` | The open door as a detector: why assets are told to ask a PTKW colleague. **[PROPOSAL]** |

### Human Forces (Earth's strongest formations)

| File | Contents |
|---|---|
| `canon/documents/2.47 — Host Force Assessment The Harrow.md` | **The ground unit.** Global Narcotics Interdiction Command, Special Operations Directorate, known as **the Harrow**. Official and operational names, why it was created, why it is deployed, its weapons, and its **insignia** (black-and-silver spike-harrow patch, six team tabs, motto AGAIN TOMORROW, the Tine badge). Blue Harrow Team is one of its six teams. **[PROPOSAL]** |
| `canon/documents/2.48 — Host Force Assessment Gyrfalcon Wing.md` | **The air unit.** Allied Polar Air Defence Command, 1st Strategic Interception Wing, known as **Gyrfalcon Wing**. Pilots, F-22 aircraft, missiles, standing alert, **insignia** (azure-and-white gyrfalcon patch, bronze/silver/gold wings, three squadron patches, motto SIX MINUTES), the Day 18 incident, and the Day 26 addendum on Day 21. **[PROPOSAL]** |
| `canon/documents/2.49 — The Smile Study.md` | **Sealed.** The Research Team's special study of Captain Eirik Aronsen, opened Day 28, 18:50. Readers: the EOD Research Team, the Earth Branch Manager and EOD only; PTKW are not told it exists and are given a false account of Day 21 in Doc 2.18 Section 2.11. Contains why the file is sealed, the Captain's two transmissions, the debrief of EOD, the five hypotheses on why he was smiling, and the three false statements told to PTKW. Calls the response "the first crack in the entire ICS system". **[PROPOSAL]** |
| `canon/documents/2.50 — ICS Nomenclature Note.md` | **Board access.** The true meaning of the name ICS. Public: Interplanetary Corporate Solutions. PTKW (Doc 2.02): Inflatable Crowd Solutions. Board: the same words read as a procedure, "fill the crowd; dissolve it". Explains "Inflatable" as fill (hire rate to saturation), "Crowd" as the unit, and "Solutions" in the chemical sense (Schedule D, Stage 5), and gives five reasons the third reading is withheld from PTKW. A single sheet stapled behind the PTKW copy of 2.02, with one pencilled word, "Why?". **[PROPOSAL]** |
| `canon/documents/2.51 — Enforcement Asset Executive Handling Protocol.md` | **Branch Director access.** Form GOV-PDR-002-BM: the standardized operational handling directive and briefing template provisioned to Branch Directors / Branch Managers upon active deployment of Enforcement Asset EOD (Executioner of Despair). Contains the eight-part operational handling instructions and the Board-authorized profile excerpt (Section VII). Cited in C-26 and B-28. **[PROPOSAL]** |
| `canon/documents/2.52 — Personal Growth Plan Form ICS-PG1.md` | **Staff access.** The warm form: three goals, a support person, a review date and a signature line. No word "plan" is used outside the title. **[PROPOSAL]** |
| `canon/documents/2.53 — Support Steps Manual.md` | **PTKW access.** Steps 1–5 with scripts, and the rule that the outcome is decided before the process. **[PROPOSAL]** |
| `canon/documents/2.54 — Contribution Distribution Guidance for Managers.md` | **PTKW access.** The ten per cent that must be placed as Support Needed, and how a manager is told to find them. **[PROPOSAL]** |
| `canon/documents/2.55 — Belonging Pulse Survey and Analysis.md` | **Staff and PTKW layers.** The quarterly engagement survey, and what is done with item 3. **[PROPOSAL]** |
| `canon/documents/2.56 — Tier Velocity Standard.md` | **Staff and PTKW layers.** Published review points for tier movement and the hidden Velocity Stall flag. **[PROPOSAL]** |
| `canon/documents/2.57 — Settling-In Period Guidance for Line Managers.md` | **PTKW access.** Probation under another name, and its extension. **[PROPOSAL]** |
| `canon/documents/2.58 — Voluntary Transition Pathway.md` | **Staff and Board layers.** The pathway that is not a resignation. **[PROPOSAL]** |
| `canon/documents/2.59 — Manager Evaluation Rubric.md` | **Branch Director access.** How managers are scored on their placement of Support Needed. **[PROPOSAL]** |
| `canon/documents/2.60 — Perception Alignment Protocol.md` | **Above Branch Director access.** The protocol that adjusts a person's memory of dates and conversations. **[PROPOSAL]** |
| `canon/documents/2.61 — ICS Wellness Assessment Form ICS-WA4.md` | **Staff and PTKW layers.** The assessment form whose Results page is printed before the assessment is held. **[PROPOSAL]** |
| `canon/documents/2.62 — Floor Liaison Guide Receiving Colleague Questions.md` | **Global, PTKW and Board layers.** The leaflet *Ask a Colleague*, the Floor Liaison's ladder and two-officer rule, and why the invitation to ask is a detector for comfortable colleagues. **[PROPOSAL]** |
| `canon/characters/Colonel Leif Aronsen.md` | **The Wing's commander.** History, the night his wife died, the rules he keeps with his son, and Day 21 in the tower cab. Evidence only; the player never meets him. **[PROPOSAL]** |
| `canon/characters/Captain Eirik Aronsen.md` | **The commander's son,** call sign Tern, Gyrfalcon Seven. History, the apron, the kitchen timer, and what the game does and does not know about his last transmissions, including his message to humans. **[PROPOSAL]** |
| `canon/characters/K-7 - PTKW Monitoring and Analysis Team Leader.md` | **The PTKW analyst who notices.** Profile built only from what he does in B-01, B-05, B-10, B-22 and B-28; his workstation is the second-largest mail source in the game. Five open rulings (pronouns, Level 5 or 8, device name, password, rank). **[PROPOSAL]** |


---

## The three-tier access system

Every in-world document has up to three layers. This is non-negotiable across every document:

- **Global Access** — warm, corporate, propaganda. The employees see this.
- **PTKW Access** — operational reality. Mid-level alien management sees this.
- **Board Access** — the deepest truth. The harvest, Schedule D, the Board's nature.

**PTKW** full name: *"Punish who Think, Kill who Wonder"* — coined by a resistor at Labor Source #038, written on a wall. Public cover definition: "Privileged Technology Access, Key Main Workforce."

---

## Key facts — never contradict these

- Earth is **Labor Source #349**, currently **Stage 2 of 5**
- **Stage 5 planets are empty.** 3 confirmed, ~200 billion nodes integrated. Grey dots. No label. No file.
- **Compliance index: 98.3% / Resistance index: 1.7%** — the 1.7% is the point
- **Schedule D** is 94 pages, hidden as Appendix C of Form ICS-T7. The contract does not end at death.
- The **Board** is not a committee. It is an ancient non-physical entity older than ICS itself.
- **AIDEN** full designation: Asset Identification & Data Extraction Node
- **Rania (E-04421)** is from Nairobi. Her daughter is Leila. Her last note points to the Level 0 hatch.
- **Level 0 does not appear on any official map.** Cold air through the Stairwell B gap. The door moves.

---

*The game ends with Phase Six: enough humans choosing purposeful self-destruction over continued compliance that they force ICS to deploy its own automated planetary termination protocol (Category Omega). The humans don't win in a conventional sense. ICS gets the planet. The humans get to choose how it ends. In ICS terms that is the most catastrophic operational failure in portfolio history. In human terms it has a name: freedom.*
