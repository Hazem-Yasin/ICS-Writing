# ICS — Rigged Sphere

**A first-person narrative game in the style of BioShock.** The player is a human employee inside the ICS Earth Branch — a corporate facility shaped like a second moon in orbit above Earth. ICS is an alien-run planetary labor company. The warmth is real. The cage is real. The horror is that you cannot point to the moment it goes wrong, because it was always this.

---

## Files

### Canon & Narrative

| File | Contents |
|---|---|
| `documents/` | **The canon.** All 51 in-world documents (2.1–2.51), one file each, including the Glossary (2.29). The source of truth for lore, access tiers, and cross-references. The two old compiled files (WORLD and ICS - Rigged Sphere) were retired; their unique text lives in the master reference below. |
| `reference/` folder, file ICS_Rigged_Sphere_MASTER_REFERENCE (one level above `writing/`) | **Master reference (snapshot).** One large read-only file with every file in `writing/` verbatim, plus Appendix A (Game Overview, the earlier Doc 2.32 version, recovered variants). Sits outside `writing/`; regenerate it, don't edit it. |
| [`DESIGN.md`](DESIGN.md) | **The blueprint.** Characters, narrative arc (Phases 0–6), scene notes, and Document 2.41 (EOD's perspective). This is where the game lives. |
| [`STORY.md`](STORY.md) | **The story itself.** Six scenes written as experienced narrative: the interrogation, what happened in the atrium on Day 21, the Level 0 descent and Section 7, Tarek standing up, Maren Voss in the final hours, and the ending. |
| [`EXTENDED.md`](EXTENDED.md) | **The long reads.** Schedule D pages 1–6, Yusra's full resistance document, and the Branch Director's address — the three documents the player finds and must read completely. |
| [`trailers.md`](trailers.md) | **Six trailer/ad scripts.** "The Crack," "The Offer" (revised), "The Contract," "The Archive" (post-release, Board POV), the 30-second in-world TV spot "Something Better," and "The Envoy" (EOD, told across Global, PTKW and Board access). Four are also split into `trailers/`; the TV spot lives only in `trailers.md`; "The Envoy" lives only in `trailers/Trailer 5 - The Envoy.md`. |

### Game Design Systems

| File | Contents |
|---|---|
| [`PROGRESSION.md`](PROGRESSION.md) | **Badge tier system.** The badge IS the character sheet. Tier 1–5 unlock mechanics, 847 undeactivated badges in the system, the badge as the game's primary progression mechanic. |
| [`HEALTH_SURVIVAL.md`](HEALTH_SURVIVAL.md) | **Four-track vitals system.** Physical Integrity, Neurological Status, Thermal Regulation, EIMU Coherence — each track, its sources of damage and recovery, and what flat-lining each one looks like. |
| [`ENEMY_AI.md`](ENEMY_AI.md) | **Behavioral states for all 5 enemy categories.** PTKW Security, True Believers (Marcus/Lani/Cho), Arrangement Class (Dayo/Priti), Omega-1, and EOD advance team. Four-state alert ladder. |
| [`STEALTH_DETECTION.md`](STEALTH_DETECTION.md) | **Full detection architecture.** Visual, EIMU, and acoustic detection inputs. Zone coverage map. CCN Anomaly Score. Maintenance passage rules. EIMU Diagnostic Accessory. Phase-by-phase detection summary. |
| [`NPC_COMPANIONS.md`](NPC_COMPANIONS.md) | **Tarek, Omar, Sera — dynamic interaction.** Phase-by-phase behavior for each NPC. Specific conversation options, flags, and Phase 6 outcomes. The unannounced relationship design principle. |
| [`INVENTORY.md`](INVENTORY.md) | **10-slot inventory system.** Badge-as-interface design. Item categories (documents, tools, recovery, key items). Inventory pressure in Phase 5. The Phase 4 manifest check. |
| [`AUDIO_VOICE.md`](AUDIO_VOICE.md) | **11 voices, full audio log design.** Who speaks, what they say, why audio vs. text, performance notes. Includes Rania's single recording and the Senior Analyst's 11-second log. Ambient audio by phase. |
| [`SAVE_SYSTEM.md`](SAVE_SYSTEM.md) | **Save architecture.** Continuous autosave, one manual save slot (quarters only), irreversible events list, death save behavior, and the "Last Entry" Phase 6 permanent save. |
| [`TUTORIAL.md`](TUTORIAL.md) | **Tutorial-as-job design.** 10 mechanic introduction beats across Phase 0–1. Discovery tutorial schedule for Phases 2+. What is never explicitly taught and why. |
| [`ENDINGS.md`](ENDINGS.md) | **Endings branching chart.** Full flag reference (Phases 0–5). Four ending states: The Witness, The Alone, The Blind, The Archivist. Gradient states. What does not branch. New Game+ implications. |
| [`VERBS.md`](VERBS.md) | **The verb sheet.** The eight things the player can do (Move, Read, Badge, Use, Modify, Speak, Slip, Witness), how each feels, and what each costs. Canon and proposals tagged separately. |
| [`SOLUTION_MATRIX.md`](SOLUTION_MATRIX.md) | **Obstacles × answers.** Every obstacle in the facility with the non-lethal answers the existing tools and verbs give, and what each answer costs. |
| [`TENSION_CURVE.md`](TENSION_CURVE.md) | **Pacing across Phases 0–6.** Intensity targets, peaks, valleys, safe-space ledger, pacing rules, playtime split. |
| [`LEVEL_BEAT_SHEETS.md`](LEVEL_BEAT_SHEETS.md) | **Level beat-sheet template**, filled in for Levels 0–14 (Levels 0 and 4 in detail; the rest are draft tables). Includes inconsistencies found between level files. |
| [`DISCOVERY_SEQUENCE.md`](DISCOVERY_SEQUENCE.md) | **Discovery sequence & narrative spine.** Single ordered path across Phases 0–6, room-by-room trajectory, key document pickups, and full staging of named set pieces (Rania's 3-part note, Level 0 Charter retrieval, Atrium confrontation, Cafeteria stand, PTKW backlog). |
| [`TIME_MODEL.md`](TIME_MODEL.md) | **Time model.** Weekday anchor, phase boundaries, day-by-day ledger, Phase 6 arithmetic, NPC schedules, real-time rates, action time costs. |
| [`EOD_ENCOUNTERS.md`](EOD_ENCOUNTERS.md) | **EOD, encounter by encounter.** Modes A/B/C, Phase 2 beats, Day 21 atrium, capture flow, tools versus him. |
| [`PLAYER_GUIDANCE.md`](PLAYER_GUIDANCE.md) | **How the game says "go there."** Five channels, guidance by phase, what never appears, Phase 6 as unguided. |
| [`GATING_BACKTRACKING.md`](GATING_BACKTRACKING.md) | **Gates and backtracking.** Credential ladder, level graph, what closes, what never closes, sequence breaks. |
| [`FAILURE_LOOP.md`](FAILURE_LOOP.md) | **Death, capture and retry.** The failure states, the retry flow, target fail rates, when the player is stuck. |
| [`UI_MENUS.md`](UI_MENUS.md) | **HUD, badge, menus.** What is on screen, the badge tabs, boot, pause, save/load, settings, credits. |
| [`SOLCRED_ECONOMY.md`](SOLCRED_ECONOMY.md) | **SOLCRED as a mechanic.** Canon prices, where it appears, what it is for, detection flags. |
| [`TOOL_TUNING.md`](TOOL_TUNING.md) | **Tool numbers in one place.** Charges, durations, ranges, build times, enemy parameters, playtest targets. |
| [`ART_DIRECTION.md`](ART_DIRECTION.md) | **Visual direction.** Brand colours, light by place and phase, materials, mascots, camera. |
| [`BADGES_AND_UNIFORMS.md`](BADGES_AND_UNIFORMS.md) | **Badges and attire.** Tier cards, department glyphs, per-character badge sheet, PTKW/Director/stripped badges, uniforms for every group. Canon vs [PROPOSAL] marked. |
| [`ENVIRONMENTAL_STORYTELLING.md`](ENVIRONMENTAL_STORYTELLING.md) | **Placement rules and prop manifest per level,** linked to the Blender files in `Environments/` and `Props/`. |
| [`PRODUCTION_SCOPE.md`](PRODUCTION_SCOPE.md) | **Production questions.** What the design fixes, scope drivers, vertical slice, engine, localization, QA. All figures are placeholders. |
| [`JOBS_AND_CAREER.md`](JOBS_AND_CAREER.md) | **Jobs and the career ladder.** What the player's job produces, why the department is fixed, second jobs through acquired badges, tier versus role, and what a rung pays besides access. All [PROPOSAL]. |

| [`DIFFICULTY_ACCESSIBILITY.md`](DIFFICULTY_ACCESSIBILITY.md) | **Difficulty as information, not damage.** Presets, individual options, vision/hearing/motor/cognitive/photosensitivity accessibility, controls. |
| [`HANDOFF_CARTOGRAPHER.md`](HANDOFF_CARTOGRAPHER.md) | **Handoff brief: Archivist → Cartographer.** What exists, what is missing, canon not to break, working rules, and the open rulings to resolve with the user. |



### Facility

| File | Contents |
|---|---|
| [`facility/Overview.md`](facility/Overview.md) | The full facility — orbital position, BES design philosophy, level structure, what it smells like. |
| [`facility/TV_SCREENS.md`](facility/TV_SCREENS.md) | **The Broadcast Display System.** 200+ screens, the advertising characters (SONA, BRIK, the Wellness Pair), all products, SOLCRED pricing, and what the BDS looks like when the warmth is gone. |
| `facility/Level 0.md` through `facility/Levels 11-14.md` | Individual level files. |
| `facility/Maintenance Network.md` | The parallel map — Type A, B, C passages. |

### Internal Communications

| File | Contents |
|---|---|
| `internal-communications/README.md` | Index of all recovered correspondence: A (employees), B (PTKW), C (Branch Director / HQ), D (design team). |
| [`HEARTH.md`](HEARTH.md) | **Hearth, the ICS Earth Branch internal messaging system.** The in-world name, the design (Deep Blue and Warm Gold, three panes), the folders (delivered, drafts, held by CCN, sealed, found notes), and how the viewer is built from the messages and kept current by the writing map. **[PROPOSAL]** |
| [`ICS_OS.md`](ICS_OS.md) | **ICS-OS (version 0.1), the ICS Earth Branch operating system.** Boot, sign-in and desktop; three windowed apps (Hearth mail, ICS Cloud Drive, Folio document viewer); cloud-only files with no local save; clearance by whole file and by layered section; and the Branch Director's retained copies of Staff and PTKW mail. Lives in its own folder, ICS-OS, beside the writing map. **[PROPOSAL]** |
| `internal-communications/branch-director/C-18 — EOD Research Team - Deployment 287 Field Report Update Request.md` | The EOD Research Team asks the Earth Branch Manager for findings on Deployment Order 287; the Branch replies that it cannot place EOD at any point in the ten days. **[PROPOSAL]** |
| `internal-communications/branch-director/C-19 — EOD Research Team - Deployment 287 Field Report Update - Team Blue Harrow - Last Survivor Interview.md` | **Newest.** Day 22: the Branch Manager's update to C-18. It places EOD at Sudbury on Day 16, explains the ten days and reproduces the Blue Harrow survivor's transcript; the Research Team replies. Split out of C-18. **[PROPOSAL]** |
| `internal-communications/branch-director/C-20 — EOD Research Team - Deployment 287 Field Report Update - Team Gyrfalcon Wing - Incident Report.md` | The Branch Manager corrects C-19: the second demonstration (Gyrfalcon Wing, Day 18) was not ARM-27's. A cockpit and radio transcript, no casualties; the Research Team replies. **[PROPOSAL]** |
| `internal-communications/branch-director/C-21 — EOD Research Team - Deployment 287 Field Report Update - Team Gyrfalcon Wing - Open Water Combat Report.md` | Day 21: the air engagement — HAWK patrol spots EOD on the surface, Gyrfalcon Wing scrambles, one pilot breaks formation and his face is pressed flat against his own canopy by an open hand before weapons release; the other seven engage for 36 minutes with no hits. One of them, Captain Eirik Aronsen (Gyrfalcon Seven), is flown by hand by the contact, ordered to eject by his father, and killed in the sea after his father says "son", the contact turns back and the parachute is cut. On the way he tells his father he is dead and knows it, and tells humans to be afraid and to proceed despite being afraid. Eight pilots dead total; seven aircraft land, one empty. ARM-27's first active sortie since the Show of Force. Sealed with C-23 and Doc 2.49; the question of why the Captain was smiling is first raised in a board note. **[PROPOSAL]** |
| `internal-communications/branch-director/C-22 — EOD Research Team - Deployment 287 Field Report Update - Team Gyrfalcon Senior Officer - Hallvik Tower Conversation Report.md` | Day 21 (continues C-21): EOD and ARM-27 stand at the Hallvik tower; the Wing's commander shoots at him through bullet-proof glass and EOD speaks plainly ("downsizing", "branch sunsetting"). The tower cab recording, the Branch Manager's conclusions and the Research Team's reply. **[PROPOSAL]** |
| `internal-communications/branch-director/C-23 — EOD Research Team - Deployment 287 Field Report Update - Master Summary.md` | **Newest.** Day 28: the Branch Manager's master summary of all four Deployment 287 events (C-19 through C-22), drawing the through-line — four demonstrations, four audiences, one argument. The Research Team replies at length: its human-psychology study (Doc 2.18) succeeded and fear is a useful instrument; what it expected of humans facing EOD; Eirik's refusal and his message to the species, and Gyrfalcon Three's inverted pass, which it did not expect and will study further; and EOD's own debrief statement, that humans who smile at certain death cannot be controlled. Sealed: readers are the Research Team, the Earth Branch Manager and EOD, not PTKW. **[PROPOSAL]** |
| `internal-communications/branch-director/C-24 — EOD Research Team - The Discussion of EOD Sunsetting.md` | **Newest.** Day 29: the Research Team to the Earth Branch Manager, two readers only (one level above Doc 2.49; EOD is excluded). The words EOD said about Eirik must never be said or heard in any branch or asset planet, given ICS's record of never failing. The Team asks the Manager to watch EOD closely, or to sunset him: the Journey Completion Directorate (fourteen of its members held ready, from a larger roster) will arrive disguised as a rival company's force, he will fight it, and the analysis says 100 percent. Failure to report puts the whole Branch before the Board and the Directorate. He will be announced as a hero who died defending ICS, and the humans must never question it. The Team asks the Branch for the location, the damage costs and the repair time, and supplies the public statement ("After more than 300 years…"). **[PROPOSAL]** |
| `internal-communications/branch-director/C-25 — Earth Branch Manager - Reply to The Discussion of EOD Sunsetting.md` | **Newest.** Day 30: the Earth Branch Manager's reply to C-24, two readers only. It opens to EOD by his full name and "my dear friend" (a line he will never read), then argues seven reasons to hold the sunset order, proposes the first option under his own hand, and prepares the entire Level 7 floor for EOD's farewell and the fight, "the least he can do for an old friend" (Day 38, 02:00 Branch Time). He says he will comply if the Team insists, and asks that EOD be told the attackers are real and have come to destroy the Branch, so that he dies believing he protected the ICS he served. **[PROPOSAL]** |
| `internal-communications/ptkw/B-25 — HQ Host Force Monitoring Instruction.md` | **Newest.** PTKW Oversight tells Level 5 to monitor the Harrow and Gyrfalcon Wing by open sources only, and not to tell Branch Operations. **[PROPOSAL]** |
| `internal-communications/ptkw/B-26 — Incident Report ICS-IR3 - Restricted Designation Heard and Document Recovered.md` | **Newest.** Day 32: PTKW Level 5 duty officer to K-7 and TOR-9. A human asset (E-03615, Operations Division, Work Floor B) is heard saying "[Subjugator]" at his desk, and a print of a scan of the Doc 2.15 designation block is found in his drawer, with "Executioner of Despair" highlighted and, above it, his own written reaction. Form ICS-IR3 and the seven-part source investigation; the asset is retained, not released and not reclassified, because he is the only trace. The handling note records that PTKW officers have now read names that are not for PTKW use. **[PROPOSAL]** |
| `internal-communications/branch-director/C-26 — Earth Branch Manager - EOD First Arrival at Labor Source 312 - Cycle 292 Thread.md` | **Newest.** Cycle 292 Q2 (an earlier planet, off the game timeline): the Manager of Labor Source #312 writes to HQ about a man with no badge who smiles and waves at everyone, and whom he finds hard to look at; HQ copies the EOD Research Team and tells it to explain; the Team sends the eight-section handling manual that comes with EOD, with a cropped one-page scan of his profile as section 7. The Manager kept it, and told the Division the page was destroyed. He is now the Earth Branch Manager. **[PROPOSAL]** |
| `internal-communications/employee/A-28 — Lior and Chidi The Man Without a Badge.md` | Day 4, 19:12 to 19:40: two Level 3 assets (E-03615, E-03702) talk about the unbadged man in the Level 2 corridor, whose doors open before he reaches them, and Lior decides to ask the floor liaison. **[PROPOSAL]** |
| `internal-communications/ptkw/B-27 — Intercept Thread — Lior Asks the Floor Liaison About the Man Without a Badge.md` | Day 5: Lior's polite query to the Floor Liaison, the Liaison's rude reply that PTKW does not know and he should expect updates, and the forward to K-7, who will ask the Manager. **[PROPOSAL]** |
| `internal-communications/ptkw/B-28 — K-7 Asks the Earth Branch Manager About EOD and Forwards His Answer to All PTKW.md` | Day 5 to 6: K-7 asks the Manager. The Manager tells all PTKW to tread carefully around his old friend, whose commands apply as if he outranked anyone. He forwards the old manual from C-26 with the page removed, and K-7 sends it to all PTKW against his instruction. **[PROPOSAL]** |
| `internal-communications/employee/A-29 — Chidi and Ruth Read It Once REDACTED EVIDENCE.md` | Day 31 chat, redacted by the PTKW investigation team on Day 33 as evidence in ICS-IR3-300Q4-032: two assets say they read the sheet once, do not have it, and discuss what it said. Three redactions and a cover note. **[PROPOSAL]** |

### Human Forces (Earth's strongest formations)

| File | Contents |
|---|---|
| `documents/2.47 — Host Force Assessment The Harrow.md` | **The ground unit.** Global Narcotics Interdiction Command, Special Operations Directorate, known as **the Harrow**. Official and operational names, why it was created, why it is deployed, its weapons, and its **insignia** (black-and-silver spike-harrow patch, six team tabs, motto AGAIN TOMORROW, the Tine badge). Blue Harrow Team is one of its six teams. **[PROPOSAL]** |
| `documents/2.48 — Host Force Assessment Gyrfalcon Wing.md` | **The air unit.** Allied Polar Air Defence Command, 1st Strategic Interception Wing, known as **Gyrfalcon Wing**. Pilots, F-22 aircraft, missiles, standing alert, **insignia** (azure-and-white gyrfalcon patch, bronze/silver/gold wings, three squadron patches, motto SIX MINUTES), the Day 18 incident, and the Day 26 addendum on Day 21. **[PROPOSAL]** |
| `documents/2.49 — The Smile Study.md` | **Sealed.** The Research Team's special study of Captain Eirik Aronsen, opened Day 28, 18:50. Readers: the EOD Research Team, the Earth Branch Manager and EOD only; PTKW are not told it exists and are given a false account of Day 21 in Doc 2.18 Section 2.11. Contains why the file is sealed, the Captain's two transmissions, the debrief of EOD, the five hypotheses on why he was smiling, and the three false statements told to PTKW. Calls the response "the first crack in the entire ICS system". **[PROPOSAL]** |
| `documents/2.50 — ICS Nomenclature Note.md` | **Board access.** The true meaning of the name ICS. Public: Interplanetary Corporate Solutions. PTKW (Doc 2.02): Inflatable Crowd Solutions. Board: the same words read as a procedure, "fill the crowd; dissolve it". Explains "Inflatable" as fill (hire rate to saturation), "Crowd" as the unit, and "Solutions" in the chemical sense (Schedule D, Stage 5), and gives five reasons the third reading is withheld from PTKW. A single sheet stapled behind the PTKW copy of 2.02, with one pencilled word, "Why?". **[PROPOSAL]** |
| `documents/2.51 — Enforcement Asset Executive Handling Protocol.md` | **Branch Director access.** Form GOV-PDR-002-BM: the standardized operational handling directive and briefing template provisioned to Branch Directors / Branch Managers upon active deployment of Enforcement Asset EOD (Executioner of Despair). Contains the eight-part operational handling instructions and the Board-authorized profile excerpt (Section VII). Cited in C-26 and B-28. **[PROPOSAL]** |
| `characters/Colonel Leif Aronsen.md` | **The Wing's commander.** History, the night his wife died, the rules he keeps with his son, and Day 21 in the tower cab. Evidence only; the player never meets him. **[PROPOSAL]** |
| `characters/Captain Eirik Aronsen.md` | **The commander's son,** call sign Tern, Gyrfalcon Seven. History, the apron, the kitchen timer, and what the game does and does not know about his last transmissions, including his message to humans. **[PROPOSAL]** |
| `characters/K-7 - PTKW Monitoring and Analysis Team Leader.md` | **The PTKW analyst who notices.** Profile built only from what he does in B-01, B-05, B-10, B-22 and B-28; his workstation is the second-largest mail source in the game. Five open rulings (pronouns, Level 5 or 8, device name, password, rank). **[PROPOSAL]** |


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
