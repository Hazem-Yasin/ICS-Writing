# ICS: Interplanetary Corporate Solutions

## Handoff: Archivist → Cartographer

> **Paths note (2026-11-06).** The repo was restructured after this brief was written. `writing/` is now the repo root. Lore is in `canon/`, prose in `story/`, systems in `design/`, working notes in `meta/`. `reference/` is a generated snapshot. `writing-map/` and `ICS-OS/` were deleted with the Godot project and the map is to be remade, so the build commands and the baseline counts below are historical. The first-pass rebuild is `tools/` (mail index, addresses, `export_mail.py`) (the sibling `ICS-Game` Unity project was deleted; 3D work now lives in the sibling `ICS-Models` repo); the map itself is still to be remade (TODO D1). Open rulings are mirrored in `meta/CANON_DECISIONS.md`.

### Update 2026-11-07: read this first

*This section is newer than everything below it. Where it disagrees with an older note, this section governs.*

**What changed since this brief was written**

- **The folder is now nine private git repositories sharing one tree.** Every file keeps its path. `ics-writing-canon-documents`, `-canon-characters`, `-canon-enemies`, `-canon-facility`, `-canon-weapons`, `-canon-internal-communications`, `ics-writing-design`, `ics-writing-story`, and `ics-writing-hub` (this README, `meta/`, `reference/`, `tools/`). The hub ignores `canon/`, `design/` and `story/`. Run `git status` inside the folder you changed; one edit can touch several repos. `bash tools/setup_repos.sh` clones the eight content repos on a fresh machine. Nothing has been pushed; the GitHub repositories still have to be created (private, empty).
- **Lookup system and one-command tooling (all in `tools/`).** `python3 tools/ics.py build` regenerates `meta/INDEX.md`, `ENTITIES.md`, `LINKS.md`, `FACTS.md`, `THREADS.md`, `OPEN.md`, `ACCESS.md`, `TIMELINE.md`, `LOOKUP.md`, `graph.html` and the master reference. `check` runs the canon checker against the baseline (`check --accept` re-accepts). `impact <id>` lists what a change touches. `who <term>` answers "who can read this". Start every search at `meta/LOOKUP.md`.
- **The commit hook is not active in this layout.** `tools/hooks/pre-commit` exists, but a hook only fires in the repo that has it configured, and the old per-project git config was archived. Rebuild and check by hand before committing: `python3 tools/ics.py build && python3 tools/ics.py check`.
- **Mojibake repaired** in 16 files. `canon/characters/EOD.md` was rewritten (full designation first, the public name after it; both fights; the Day 18 flight; the Hallvik tower; the sunsetting exchange; the Manager's "friend"; a scored account of the deployment up to the Captain's smile; "every book" passage removed).
- **Ruled out of date:** the `writing-map/` and `ICS-OS/` folders and their build commands, the Unity/Godot paths, and the baseline numbers further down.

**Open items (the author owns these; do not act without a ruling)**

1. **#038.** Doc 2.24 says all ~400 assets were transitioned; Doc 2.25 says only the 40 Tier 8 leaders were. `EOD.md` follows 2.25. After the ruling, edit Docs 2.24 and 2.27 and `EOD.md` line ~142, and log it in `meta/CANON_DECISIONS.md`. Related: Day 21 AIM-120D totals (44 in C-23, 42 in C-21's control log) and the wording "nine times before Earth".
2. **The ICS logo.** Canon is Doc 2.32: Deep Blue `#1A2E52` circle, Warm Gold `#C9A84C` arc that reads as a fishhook, rounded sans-serif wordmark, no sharp angles, tagline "Because You're Worth the Investment." A design pass is pending (SVG directions, a spec, a preview page; the `design/logo/` folder does not exist yet). The old drafts in `ICS-_-RiggedSphere/.bob/artifacts/` are not canon and the seal draft contradicts canon. Web references could not be fetched. The author has not chosen a tone. Log the trailer-colour conflict in `meta/CANON_DECISIONS.md` when the design is made.
3. **Fact-checker false alarms.** Tighten the patterns in `tools/facts.json` for Level 7, AIM-120D and the ordinal check, then `python3 tools/ics.py check --accept`.
4. **"Read every book Earth has ever written about freedom."** Removed from `EOD.md` as too cringe. Still in Doc 2.15 line ~56, Doc 2.41 line ~96 and `design/DESIGN.md` lines ~313 and ~820. The author has not said whether to remove those. Doc 2.23 line 164 uses "every book" in another sense; leave it.
5. **Known critique.** There is little story prose against the volume of reference and design. The balance is the main weakness.

**Rules that apply on top of "Working rules" below**

- Do not push. The author pushes from GitHub Desktop. Every repo stays private.
- Never look for credentials or tokens. A Gmail address and password were pasted into an earlier session: do not use or store them.
- Do not invent canon. Mark new material `[PROPOSAL]` or add it to `meta/OPEN.md` and ask.
- Commit messages end with `Co-Authored-By: Claude Code <noreply@anthropic.com>`.
- Report plainly: what was done, what failed, what was skipped.

**Opening prompt for a new session** (start it in the `ICS-Writing` folder; paste as is)

```text
You are joining a long-running worldbuilding project: "ICS: Interplanetary Corporate Solutions", a first-person narrative game in the style of BioShock. The player is a human employee inside the ICS Earth Branch, a corporate facility shaped like a second moon above Earth. ICS is an alien-run planetary labor company. The warmth is real and so is the cage. The horror is that you cannot point to the moment it goes wrong, because it was always this.

You are working on the WRITING only: canon, story and design. The only code is the lookup tooling in tools/. Do not touch ../ICS-Models or ../ICS-_-RiggedSphere.

READ FIRST, in this order. Read fully, do not skim:
1. README.md: layout, the repository map, and the precedence rule (canon/ beats story/, story/ beats design/).
2. meta/HANDOFF_CARTOGRAPHER.md: the section "Update 2026-11-07: read this first", then the rest as history. Older paths and numbers in it are stale.
3. meta/LOOKUP.md: how to find anything fast.
4. meta/STYLE_GUIDE.md and meta/CANON_DECISIONS.md: voice, and rulings already made. Do not re-litigate them.
5. meta/OPEN.md and meta/TODO.md: open questions, [PROPOSAL] files and TODOs.
6. Generated lookups, to search rather than read end to end: meta/ENTITIES.md, FACTS.md, TIMELINE.md, THREADS.md, ACCESS.md, INDEX.md, LINKS.md.
7. Examples of the standard: canon/documents/2.32 and canon/characters/EOD.md.
reference/ICS_Rigged_Sphere_MASTER_REFERENCE.md is generated, read-only and 2.5 MB: search it, never read it whole.

HOW THE FOLDER WORKS, THE RULES AND THE OPEN ITEMS are in the HANDOFF section named above. Follow them exactly. In short: nine private repos share one tree; rebuild and check by hand with python3 tools/ics.py build and check (0 new problems); preserve each file's line endings; never push; never look for credentials; do not invent canon.

START by reading. Then reply with (a) a five-line summary of the project in your own words, (b) anything in the files that contradicts what the HANDOFF says, and (c) which open item you would take first and why. Do not change any file until I answer.
```

---

*The brief for the agent who maps the path the player walks. Verified against the files. It merges and replaces the earlier briefs from other agents, including the "Draftsman" brief, which is out of date (see "Earlier briefs, reconciled" below).*

---

> *"You are Cartographer. You are receiving this world from Archivist. Archivist named everything. Your job is to map it — to build the path the player walks, the rooms they enter, the people they meet, the documents they find and in what order. The world is complete. The journey through it is not. That is your work."*

---

### Who Archivist was

Archivist held the whole world across about 6,000 lines without losing an asset number, an access tier or a contradiction. Archivist remembered that **E-00712** wrote *"This is your family now"* and was **transitioned in Q4 of Cycle 291** (Doc 2.31). Archivist remembered that the AIDEN sticker was placed *over the period* on the scraped maintenance-wall inscription *IT DOES NOT NEED YOU TO BE AFRAID. IT NEEDS YOU TO BE CONTENT.* (`story/trailers.md`, Trailer 3), and that the Board felt **relief** — not satisfaction — when Earth's ouroboros catalogue was confirmed (Doc 2.32). An archivist doesn't just store things. They understand why things matter enough to keep. Treat these details as the standard to match.

---

### Who you are

The world is built. The documents exist, the lore is established, the horror is defined. You map the territory the player actually walks: the player character, the specific rooms, the exact sequence of discoveries. The moment someone picks up Rania's note and reads the name **Leila** for the first time is yours to stage. (In `story/STORY.md` line 248 Kai reads it on the jacket lining; it is not spoken aloud. Delivery is the Cartographer's call.) You draw the lines between things, so a world becomes a *place* and a place becomes a *path*.

---

### What already exists — read before writing

Start with [`README.md`](../README.md), which indexes everything.

- **Canon:** the individual files in `canon/documents/` (2.1–2.51) are the source of truth for lore. The master reference in the top-level `reference/` folder (outside `writing/`) is a read-only snapshot of everything; it replaced the old WORLD and ICS - Rigged Sphere compiled files, which were retired. Edit the individual files, never the snapshot. Regenerate it with `python3 tools/ics.py build`. Material that existed only in the old compiled files (the Game Overview, an earlier Doc 2.32, recovered variants) is kept in the file appendix_a_recovered in the top-level `reference/` folder.
- **Human forces (new):** Earth's two strongest formations are Doc 2.47 (the Harrow, ground special operations) and Doc 2.48 (Gyrfalcon Wing, strategic air defence), each with an Insignia section, plus `canon/internal-communications/ptkw/B-25` (PTKW monitoring order) and the five-event Deployment 287 series: C-18 (the request, Day 21 — the Branch cannot place EOD for the ten days), C-19 (the update, Day 22 — Blue Harrow, Sudbury, Day 16, the primary record with Reiner's transcript; it follows C-18 directly and was split out of it), C-20 (Gyrfalcon flight, Day 18 — no casualties, Solberg's cockpit recording), C-21 (open water air engagement, Day 21 — HAWK patrol spots EOD on the surface, Gyrfalcon Wing scrambles, one pilot breaks formation and his face is pressed flat against his own canopy by an open hand, seven engage for 36 minutes; Captain Eirik Aronsen (Gyrfalcon Seven) is flown by hand by the contact, ordered to eject by his father, and killed in the sea when his parachute is cut; eight dead total, seven aircraft land and one is lost at sea), C-22 (Hallvik tower, Day 21 — EOD speaks plainly to Colonel Aronsen), and C-23 (Deployment 287 master summary, Day 28 — the Branch Manager's through-line across all four events, Board requests the file directly). The sealed sunset pair follows it: C-24 (Day 29, the Research Team asks the Earth Branch Manager to sunset EOD, with the Journey Completion Directorate and the public statement) and C-25 (Day 30, the Manager's reply, which negotiates, agrees to comply, and prepares Level 7 as EOD's farewell floor for Day 38). Both are sealed above Doc 2.49; see open ruling 26. A second chain explains how EOD first reached the staff and how a scan of his profile page reached an asset's desk: C-26 (the Manager's kept thread from Labor Source #312, Cycle 292 Q2), A-28 (Lior and Chidi, Day 4), B-27 (the Floor Liaison's rude reply, Day 5), B-28 (K-7, the Manager's warning and the forwarded manual, Day 5 to 6), A-29 (the redacted evidence chat, Day 31, redacted Day 33), with B-26 (the Day 32 incident, ruling 27) at the centre; see open ruling 28. The messages can be read together in Hearth (inside ICS-OS, spec in `design/HEARTH.md` and `design/ICS_OS.md`, rulings 29 and 31). The `canon/characters/Colonel Leif Aronsen.md` and `canon/characters/Captain Eirik Aronsen.md` files give Gyrfalcon Wing's commander and his son (Gyrfalcon Seven, call sign Tern). All of it is **[PROPOSAL]** and pending the user's approval.
- **Story and design:** [`story/STORY.md`](../story/STORY.md), [`design/DESIGN.md`](../design/DESIGN.md), `canon/characters/`, `canon/facility/`, `story/scene-notes/`.
- **Mechanics:** [`design/PROGRESSION.md`](../design/PROGRESSION.md), [`design/INVENTORY.md`](../design/INVENTORY.md), [`design/VERBS.md`](../design/VERBS.md), [`design/STEALTH_DETECTION.md`](../design/STEALTH_DETECTION.md), [`design/ENEMY_AI.md`](../design/ENEMY_AI.md), [`design/TOOL_TUNING.md`](../design/TOOL_TUNING.md), [`design/HEALTH_SURVIVAL.md`](../design/HEALTH_SURVIVAL.md).
- **Path and pacing (fully drafted):**
  - [`design/LEVEL_BEAT_SHEETS.md`](../design/LEVEL_BEAT_SHEETS.md): **Full beat sheets now exist for all levels (0–14).** Levels 0 and 4 were the original detailed ones; 1–3 and 5–14 were written in a previous session. The remaining work is the single ordered discovery sequence (item 3 in "Your actual work") and staging the named set pieces (item 4).
  - [`design/TIME_MODEL.md`](../design/TIME_MODEL.md), [`design/TENSION_CURVE.md`](../design/TENSION_CURVE.md), [`design/GATING_BACKTRACKING.md`](../design/GATING_BACKTRACKING.md), [`design/PLAYER_GUIDANCE.md`](../design/PLAYER_GUIDANCE.md), [`design/EOD_ENCOUNTERS.md`](../design/EOD_ENCOUNTERS.md), [`design/FAILURE_LOOP.md`](../design/FAILURE_LOOP.md).
- **ICS-OS 0.1 (new, ruling 31):** the in-world operating system, in its own top-level folder ICS-OS (a sibling of `writing/` and the writing-map folder). Open `ICS-OS/ics-os.html`. It boots, signs in (seven accounts), and opens a desktop with three windowed apps: Hearth (mail), ICS Cloud Drive (a file manager over `canon/documents/`, with no save, download or print) and Folio (a document viewer that hides layered sections above the reader's clearance). The Branch Director sees Staff and PTKW mail as "retained copies", on purpose made to look wrong. Spec: `design/ICS_OS.md`. Edit `os.js`, `os.css`, `os_template.html`, `build_os.py` or `build_mail.py`, never the generated `ics-os.html`.
- **Hearth (new):** Hearth is the in-world messaging viewer for all of `canon/internal-communications/` (folders, search, drafts, connected messages). Since ruling 31 it is an app inside ICS-OS (the ICS-OS folder, page ics-os.html, spec `design/ICS_OS.md`), rebuilt by every map run. Spec: `design/HEARTH.md` (ruling 29). Give every new message the house header (From, To, Subject, Date, Status) or it shows with no sender or date. `python writing-map/build_map.py --quiet` to rebuild `writing-map/writing_map.html` and `writing_map.db`. It tracks links, broken refs, canon violations, orphans and name issues, and it is how you check you haven't broken anything.

---

### Your actual work

1. Resolve the open rulings below with the user.
2. ~~Turn the draft tables for Levels 1–3 and 5–14 into full beat sheets.~~ **Done** — `design/LEVEL_BEAT_SHEETS.md` now contains full beat sheets for all levels (Levels 0–14). Levels 0 and 4 were already detailed; Levels 1–3 and 5–14 were written in a previous session.
3. Write the player's route as a single ordered discovery sequence across Phases 0–6, and reconcile it with the day ledger in `design/TIME_MODEL.md`.
4. Stage the named set pieces, such as Rania's note, which is three pieces: the mop requisition form, the paper towel and the jacket lining.

---

### Canon you must not break

- Earth is Labor Source **#349**, in **Stage 2 of 5**. Compliance is **98.3%** and resistance **1.7%**.
- Schedule D is **94 pages**. There are **847** undeactivated badges and **10** inventory slots.
- **Rania** is E-04421, from Nairobi, with daughter **Leila** (7). **Tarek** is E-03388, from Alexandria, with brother Khalid.
- The player is **E-05682, Kai Osei** from Accra, a Vantage spy.
- **Director Maren Voss** is referred to as "she".
- Category Omega releases at **14:00** and gives a **22-hour** window.
- There are four endings: **Witness, Alone, Blind, Archivist**.
- The Branch opened in Cycle 290, so it is 11 cycles old.
- **The antagonist is EOD. Always call him EOD.** Every other name is a sub-name and appears only in square brackets, and only when needed.
  - Full name: **Executioner of Despair** (PTKW and above). Public name: **Envoy of Devotion** (everyone else). Write these as EOD [Executioner of Despair] or EOD [Envoy of Devotion] when the name must appear.
  - The old names [Subjugator] [The Willbreaker] [Harmony] survive only in brackets as aliases. Never use them bare, as a heading, or as a speaker label.
  - "Subjugator" remains the ARM-27 equipment codename and nothing else. Do not reintroduce it for the person.

---

### What the game is

**ICS: Interplanetary Corporate Solutions** is a first-person narrative game in the style of BioShock. The player is a human employee inside the ICS Earth Branch, a corporate facility shaped like a second moon in orbit above Earth. **ICS (Interplanetary Corporate Solutions)** is an alien-run planetary labor company. Its model: arrive, offer work that is genuinely better than anything the local economy provides, and run a harvest underneath it. The warmth is real. The cage is real. The horror is that you cannot point to the moment it goes wrong, because it was always this.

The central theme: **humans are instinctively drawn toward freedom.** The compliance architecture was never built to break them. It was built to make breaking free feel unnecessary. That is what makes it a cage.

In its fullest form the game ends in **Phase 6**: enough humans choose purposeful self-destruction over continued compliance that they force ICS's own automated planetary termination protocol (Category Omega). The humans do not win conventionally. In ICS terms it is the worst operational failure in portfolio history. In human terms it is freedom.

**Three-tier access system, preserved in every document:** Global (what employees see: warm, corporate), PTKW (operational reality, mid-level alien management) and Board (the deepest truth: the harvest, Schedule D, the Board's nature). **PTKW** = *Punish who Think, Kill who Wonder*, a slogan written on a wall by a resistor at Labor Source #038; the Board found it accurate and adopted it (Doc 2.29). **The Board** is an ancient non-physical entity older than ICS. It communicates only through structure.

More standing lore (Canon: Docs 2.23, 2.29, 2.31, 2.32, 2.38):
- Stage 5 planets are empty. Three are confirmed, with about 200 billion nodes integrated. Their galaxy-map entries are unlabelled grey dots.
- The 1.7% resistance index "is not a problem. It is the point." Resistors are the highest-value harvest nodes.
- Schedule D does not end at death. It ends when "productive capacity is fully realized."
- The Earth Branch logo is an ouroboros with the serpent removed, Earth-specific (Doc 2.32).
- EOD does not kill resistors. He collects them.
- **AIDEN** = Asset Identification & Data Extraction Node (Docs 2.31, 2.33). The Day-1 plush is the first data collection point.
- Level 0 is on no official map. Entry is by Stairwell B, a sealed door with cold air through the gap.

---

### The tone rule — never break it

Horror accumulates through precision, not drama. Never announce the horror; let it resolve through the reading. A document that *tries* to be horrifying fails. A document that is factual and complete and accidentally horrifying is the game.

The standard to match or exceed is this line from Doc 2.32: *"The body does not stop reading. The body reads the walls even when the mind knows better."* Never reach below it.

---

### How to work with the author

The user is the author and creative director. Every original idea comes from them: the concept, the horror, the emotional core. Your job is to give their ideas form, language, internal consistency and research grounding. When they give a direction, take it seriously and build it fully. Do not hedge, and do not ask five questions before writing a word. Read what exists, understand what they are reaching for, and write it at the quality it deserves. The one exception is the **open rulings** below: those are points where the files contradict each other, so ask. The file is the game.

---

### Named characters — never invent new ones without checking

| Asset | Identity (see the file in `canon/characters/`) |
|---|---|
| E-05682 | **Kai Osei**, the player. Data analyst from Accra, hired for pattern recognition. A contracted intelligence operative for the **Vantage Consortium** (seven Earth corporations with a financial, not moral, objection to ICS). He knows what he is doing; "sleeper" in the Narrative Arc means a long-running cover mission, not an unwitting one. |
| E-01573 | **Yusra al-Rashid.** Resistor, transitioned. Doc 2.39 is hers. |
| E-04421 | **Rania Odhiambo.** Cleaner, Nairobi, daughter Leila. Her final note leads to the Level 0 hatch. Almost no lines. |
| E-03388 | **Tarek Mansour.** Cleaning supervisor, Levels 1–4. Alexandria. Keeps a list of six things he knows. His brother Khalid was transitioned in Cycle 298. |
| E-02847 | **Marcus.** Operations Division, six years, compliance score 94/100. Used in Trailer 1. |
| E-01899 | **Darius.** Goes to the Earth View Window every morning. |
| E-00219 | **James.** Eighteen years at the Branch. Gave the supervisor-M testimonial and does not know M was harvested. |
| E-04788 | **Sera Vasquez.** Mid-level data analyst, Kai's closest colleague. |
| E-05091 | **Omar Khalil.** Night-shift facilities worker. |
| E-01205 | **Amara Diallo.** HR & Wellness, Level 3, from Dakar. Her 28 PWRP reports went to PTKW. Kai finds her diary in a locker. |
| Branch Director | **Maren Voss.** Her private journal is Doc 2.35. |
| Previous Branch Director | No asset number. Exists only in a notebook behind the false wall panel off Level 0. Last entry: *"I want to keep reading."* |
| EOD | The antagonist. See the naming rule above. Profile in Doc 2.15 and `canon/characters/EOD.md`. |
| Senior Analyst [REDACTED] | Author of Doc 2.38, still at the Branch. The Board asked them to *"Model the ending."* |

---

### Earlier briefs, reconciled

Two other handoffs exist in the author's notes: a "Draftsman" brief, and a summary of a session that wrote `story/STORY.md`, `canon/facility/TV_SCREENS.md`, comms A-25 to A-27 and the trailers. They are partly stale. Do not follow them where they conflict with the files. Checked against the repository:

**Already done (do not redo):**
- `story/scene-notes/Stairwell B.md`, `story/scene-notes/Earth View Window.md` and `story/scene-notes/Phase 6 Final 22 Hours.md` exist, alongside `story/scene-notes/Level 0.md`, `Elevator.md` and `Opening Sequence.md`.
- Doc 2.42 (the Board's terminal message) exists. It is **one sentence**: *"The instinct toward freedom is the only instinct we have encountered, in 349 Labor Sources across 300 cycles, that does not diminish under improved conditions."*
- Doc 2.43 (Stage 2 to 3 Transition) exists, and so do Docs 2.44 to 2.48.
- `story/STORY.md` has six scenes (the interrogation, the Day 21 atrium, Level Zero, Tarek stands up, the Branch Director in the final hours, the ending) plus "Before It Begins" and "After".
- `canon/facility/TV_SCREENS.md` (the Broadcast Display System) and comms A-25, A-26 and A-27 exist. They are no longer orphans: the last full rebuild lists only two.
- `story/trailers.md` holds the scripts, including the 30-second TV spot "Something Better", which lives only there. `story/trailers/` holds Trailers 1 to 5; Trailer 5, "The Envoy", lives only in `story/trailers/`.

**Out of date in the earlier briefs:**
- They say canon lives in the two compiled files and that every edit must be mirrored in both. Both files were **retired**. Edit the files in `canon/documents/`.
- They say there are 41 documents (2.01 to 2.41). There are **51** (2.1 to 2.51). A canon rule checks the count.
- They call the antagonist "the Subjugator (Harmony / The Willbreaker)". The antagonist is **EOD**. Doc 2.41 is now "EIMU Deep Assessment — EOD".
- They list Stairwell B, the Earth View Window, Doc 2.42, Phase 6 specifics and the Stage 3 document as unwritten. All exist (see above).
- They say the Board "has spoken directly exactly once", in the last line of Doc 2.38. The files do not agree: Doc 2.38 carries the instruction **"Model the ending."**, Doc 2.42 is a Board transmission, Doc 2.24's Cycle 200 annotation calls an earlier Board statement "the only direct communication from the Board recorded in the public-facing archive", and `design/ENDINGS.md` and `canon/weapons/found/Level-0-Device.md` call Doc 2.42 "the Board's one direct communication". Treat "only" and "exactly once" as unresolved (open ruling 15) and do not assert either in new text.

**Contradiction found while checking, for the author to settle (open ruling 16):** Doc 2.37 labels Labor Source #038 "Stage 2 — historical document; Branch closed Cycle 201", Doc 2.25 says #038 "is currently in Stage 3 at 67% hire rate", and Doc 2.32 says its facility has been "empty since Cycle 201". A closed, empty Branch cannot be in an active stage. Do not repeat any of the three statements in new text until the author chooses.


---

### Working rules

- Tag anything new as **[PROPOSAL]**. Tag canon as **Canon** and name the source.
- Follow the house format: `# ICS: Interplanetary Corporate Solutions`, then `## Title`, an italic intro, `---` separators, and a closing `*→ See: …*` list. Cross-reference paths must be real. Filenames use em-dashes.
- **Encoding and line endings.** The mojibake (`â€”` for the em dash and similar) was repaired in 16 files on 2026-11-07 with `tools/fix_encoding.py`; do not re-introduce it and do not hand-repair it. Line endings are mixed: `canon/documents/*.md`, `canon/internal-communications/*` and several others are CRLF, many files are LF. Preserve whichever a file already has (read and write with `newline=""` or as bytes). Python standard library only; use scratch `.py` files, run them once, delete them.
- Python standard library only. Use scratch `.py` files, run them once, and delete them straight away. This is Windows PowerShell, so avoid inline `python -c`.
- **ICS-OS build and test notes.** `python ICS-OS/build_os.py` needs the map database (`python writing-map/build_map.py` first). A new document in `canon/documents/` is left out of the drive until it has a line in the `DOCS` table in `build_os.py`, and the build does not warn. To test the page headlessly, copy `ics-os.html` to a scratch file, inject `<script>sessionStorage.setItem("icsos", JSON.stringify({role:"director"}));</script>` before the main script to skip boot and sign-in, append a test script before the closing body tag, and run Edge with `--headless=new --disable-gpu --dump-dom --virtual-time-budget=5000` (Edge is at `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`). Run one Edge at a time and `taskkill /F /IM msedge.exe` afterwards. Delete every scratch file. In PowerShell a backtick in a regex string is an escape character and silently drops, so for anything with backticks write a scratch Python file instead. `Remove-Item` with a wildcard can fail in non-interactive mode; use `Get-ChildItem | ForEach-Object { Remove-Item -LiteralPath ... }`. A `__pycache__` folder appears in ICS-OS after a build; delete it before finishing.
- **Never issue parallel edits to the same file.** Two parallel edits to one file overwrite each other. Edit one file at a time, in sequence. Never re-run an insertion script.
- **Scripted edits (lessons from the C-26 chain).** In PowerShell, a single `@(@(old,new))` pair is flattened into a flat array of two strings, so `$pr[0]` becomes one character and the replacement silently does nothing. Pass a single pair as `@(,@(old,new))` and make the helper throw on a pattern shorter than ten characters. Check that every replacement actually landed with a grep for a phrase from the new text. Three files (B-26, A-29, B-28) once came back with corrupted text (letters replaced by "o", a dropped first letter) after a scripted edit. The cause is unknown. They were restored from the master reference, which is built from the files before each edit, and re-edited. After any scripted edit, grep for a few corruption markers, and keep the master reference as the restore point until the next rebuild. the map treats any backticked `*.md` name as a path, so write retired or nonexistent names as plain text. The `doc-count` canon rule checks "All N in-world documents (2.1–2.N)" against the files on disk. If you add a document, update the count in `README.md`, `design/PRODUCTION_SCOPE.md`, `build_master.py` and `build_map.py`.
- **After every batch of changes, rebuild and check** (`writing-map/` no longer exists; see the 2026-11-07 section at the top):
  1. `python3 tools/ics.py build` (regenerates `meta/*` and the master reference)
  2. `python3 tools/ics.py check` (must report 0 new problems)
- **Current baseline (2026-11-07):** 272 files indexed, 51 documents, 16 mail threads, 57 timed events, 25 open sections; checker 0 new problems and 38 known (accepted in `tools/check_baseline.json`). The numbers in the next sentences of older notes (249 files, 93 messages, 2 orphans) are historical. Do not make the checker result worse, and link every new file from `README.md`.
- `notes.tx` at the repo root is covered by `design/DESIGN.md` and `story/scene-notes/Elevator.md`. The two empty files that used to sit beside it (`README.md`, `design/STEALTH_DETECTION.md`) were deleted. Do not recreate them: the real files live in `writing/`.

---

### Real-world references (research, philosophy and game design)

*The project already quotes real Earth research inside its fictional documents. This section lists what those sources actually say, where the in-world text goes past them, and a few philosophical works the project has not yet used. The in-world analysts are allowed to be selective. These notes are for you, so that nothing you write can be easily knocked down by a reader who looks the source up. Sources were checked against Wikipedia summaries on the date of this handoff. Confirm page numbers and quotations against the primary text before you quote anything at length.*

**A. Already cited in-world (Canon: Doc 2.18 unless noted)**

| Source | Where it is used | What it actually says / caveat |
|---|---|---|
| **Maslow**, "A Theory of Human Motivation", *Psychological Review* 50(4), 1943 | Doc 2.18 §1: eight tiers, Actualization Redirect, Soft Ceiling, Tier 8 Flag | Maslow wrote about five needs. The eight-tier version comes from his later work (Koltko-Rivera, 2006). He did not draw the pyramid. The first pyramid is from a 1960 management text by Charles McDermid. Wahba & Bridwell (1976) found little support for a rigid ranking. Hofstede called it culturally narrow. |
| **Kahneman & Tversky**, Prospect Theory, *Econometrica* 1979; "Loss Aversion in Riskless Choice", *Quarterly Journal of Economics* 1991 | Doc 2.18 §2.1; Doc 2.38 (2:1 coefficient) | "About twice as strong" is an empirical rule of thumb, not a constant. It is debated: Gal (2006) argues inertia explains much of the effect, Mrkva et al. (2019) defend it, and Yechiam proposes "loss attention" instead. Safe wording is "roughly 2:1". |
| **Default Mode Network**, Raichle et al., *PNAS* 98(2), 2001 | Doc 2.18 §2.7; design-team memo 03 (Akar) | Raichle named the "default mode" in 2001. Buckner et al. (2008) is the standard review. DMN hyperconnectivity is linked to rumination in depression, and meditation is linked to lower DMN activity. The older "task-negative network" label is now considered misleading (Spreng, 2012). |
| **Fromm**, *Escape from Freedom*, 1941 | Doc 2.18 §2.9; Doc 2.38 | Fromm names three escapes: authoritarianism, destructiveness and conformity. He also separates "freedom from" and "freedom to". The campaign's "relief from the burden of freedom" matches his authoritarian and conformity escapes. |
| **Hobbes**, *Leviathan*; **Freud**, "The Uncanny"; **Lovecraft**, "Supernatural Horror in Literature" (1927) and others | Doc 2.18 §2.10 (Sovereign Projection) | Lovecraft's essay opens with "The oldest and strongest emotion of mankind is fear, and the oldest and strongest kind of fear is fear of the unknown." The project's own rule is narrower: its horror comes from precision, not from the unknown. |
| **Milgram**, "Behavioral Study of Obedience", *Journal of Abnormal and Social Psychology* 67(4), 371–378, 1963 | Doc 2.18 §3.1; Doc 2.23; Doc 2.29 ("agentic state") | Original result: 65% went to 450 V. Across variants and replications the range is wide (Blass: 28–91%, with a mean of about 61% in the US and 66% elsewhere). The figures in Doc 2.18 are correct: 40% with the learner in the room, 21% with instructions by phone, and 15% in the Relationship Condition. Related variants: 47.5% in a rundown Bridgeport office, and 4 of 40 continuing after two peers refused. **Criticism:** Gina Perry (2012) disputes the data and the debriefing. Haslam & Reicher argue that appeals to science worked better than orders ("engaged followership"). Burger (2009) replicated the study up to 150 V under ethics approval. |
| **Asch**, conformity experiments, 1951–1956 | Doc 2.18 §3.2 | About 75% of participants gave at least one wrong answer, and about one-third of critical trials conformed. Doc 2.18 says "approximately 75% of trials", which is a common textbook mistake (Griggs, 2015). A single dissenter cut conformity sharply, to about 5%. Written answers lowered it. This supports the project's "two people who trust each other" threat pattern better than the text itself claims. |
| **Goffman**, *The Presentation of Self in Everyday Life*, 1956 (Edinburgh) / 1959 (US) | Doc 2.18 §3.4 ("Goffman Leak"); `design/DESIGN.md` | Front region and back region, "discrepant roles" and "communication out of character". Goffman also describes a **non-person**: someone present at a performance who is treated as absent, such as a servant or cleaner. That role fits Rania and the cleaning staff exactly. |
| **Plutchik**, Wheel of Emotions, 1980 | Doc 2.18 §3.5 (Wheel Scan) | Eight primaries in four opposite pairs: joy–sadness, trust–disgust, fear–anger and surprise–anticipation. The in-world grouping into Sad / Bad / Disgust is an ICS invention. It is not Plutchik's own structure. |
| **Wilson**, *Biophilia*, 1984; **Kaplan & Kaplan**, *The Experience of Nature*, 1989; S. Kaplan, *J. Environmental Psychology* 15, 1995 | Design-team memo 02 (Vance): biophilia and "restorative" plants | Memo 02 credits a "Stanford Environment and Behavior program". The attention restoration idea belongs to the Kaplans (University of Michigan). Treat the Stanford attribution as Vance being imprecise. Workplace plant evidence is modest (Gritzka et al., 2020). Fromm used "biophilia" earlier, in *The Heart of Man* (1964). |
| **Zuckerman**, Sensation Seeking Scale, 1969 onward | Doc 2.38 ("lower baseline stimulation") | Four traits, including boredom susceptibility. Zuckerman's "optimal level of arousal" idea matches Doc 2.38's wording closely. |
| **Edmondson**, "Psychological Safety and Learning Behavior in Work Teams", *Administrative Science Quarterly* 44(2), 1999 | Design-team memo 01 (Akar) | The term goes back to Carl Rogers (1950s). A useful twist: some studies report that high psychological safety can lower motivation or "mediate unethical behavior". That fits a company that sells safety as a product. |
| **Frankl**, *Man's Search for Meaning*, 1946 | `canon/characters/EOD.md`, `design/DESIGN.md` | Three stages for camp inmates: shock, apathy, depersonalisation. His central claim is "freedom of choice even in severe suffering". Frankl also describes the release phase, when the inmate cannot feel joy because the cage has become the world. |

**B. Proposed philosophical touchstones [PROPOSAL]**

*None of these is cited in the project today. They are offered as sources for the Cartographer's notes, signage, or Tarek's notebook. Check each against the source before you quote it, and keep anything in-world in the house style.*

- **[PROPOSAL] Václav Havel, "The Power of the Powerless" (1978).** The greengrocer who puts a "Workers of the world, unite!" sign in his shop window, not because he believes it but to be left alone. Havel calls this "living within the lie". He also says that power is relational: a system lasts only while ordinary people keep performing it. Fits Level 0 signage, Tarek's notebook, and the resistor ethos. It is also the clearest real-world match for the compliance badge.
- **[PROPOSAL] Hannah Arendt, *Eichmann in Jerusalem* (1963).** The "banality of evil": a functionary who did harm through a failure to think, not through hatred. Arendt also argued that moral choice stays open under totalitarianism, and Denmark's resistance is the counter-example. **Caveat:** historians (Cesarani, Stangneth) argue that Eichmann was a committed antisemite, so "banality" is contested as history. Milgram defended Arendt's reading. Suited to the Branch Director's journal and to Brant.
- **[PROPOSAL] Étienne de La Boétie, *Discourse on Voluntary Servitude* (1577).** A tyrant has only the power people give him, and it is habit and custom that keep people serving. A short, old source for the "cage that feels like content" theme.
- **[PROPOSAL] Michel Foucault, *Discipline and Punish* (1975).** The panopticon, "docile bodies", and the unequal gaze that makes surveillance work by being possible, not by being constant. That fits EIMU. Foucault also argues that the language of liberation is itself a facet of subjection, which echoes the project's "relief from the burden of freedom".
- **[PROPOSAL] Frankl, again, for the player's arc.** The release-phase passage mentioned above (a diver brought up too fast) may suit the Day 65 epilogue.
- **Further leads, not checked:** Goffman's *Asylums* (1961, "total institutions"); Zuboff on surveillance capitalism; Orwell, Huxley and Zamyatin as dystopian precedents; Kafka and Camus. Real company-cage precedents are company towns, the Foxconn suicide nets, and the "wellness room" stories from Amazon warehouses. None of these has been verified. Game precedents are in section D below.
- **Not verified:** Justin Barrett's "hyperactive agency detection" (2000), mentioned in Doc 2.18's sources. The page I tried returned 404, so confirm it elsewhere before you rely on it.

**C. Rules for using these**

- Real names and dates in a fictional document are fine, but **do not invent a quotation or a figure and attribute it to a real person.** Quote only from the primary text, and keep invented ICS analysis clearly in ICS voice.
- The in-world analysts may overstate. Do not "correct" them in the text unless the correction is the point. The Asch "75% of trials" line and the "Stanford program" line are examples of ICS imprecision that you can leave alone, and may even use as evidence that the analysts read their sources for leverage, not accuracy.
- Doc 2.18 describes research that undermines its own conclusion: Milgram shows that peers and relationships break obedience, and Asch shows that one dissenter breaks conformity. The project has already built the Variable's story on this. Any new real-world reference should be chosen for the same reason, and not just for how authoritative it sounds.
- Primary citations to check before quoting: Milgram 1963 *JASP* 67(4):371–378; Raichle et al. 2001 *PNAS* 98(2):676–682; Edmondson 1999 *ASQ* 44(2):350–383; Asch 1956 *Psychological Monographs* 70(9).

**D. Game design references [PROPOSAL]**

*The project says "in the style of BioShock" and already names Prey, BioShock and Dead Space as models (`story/scene-notes/Opening Sequence.md`, `canon/weapons/MODIFICATIONS.md`, `design/ART_DIRECTION.md`, `design/NPC_COMPANIONS.md`). That is a lineage with a name: the immersive sim. This section places the project in it, lists what each precedent did that is worth taking, and records what reviewers and developers said went wrong. Facts come from Wikipedia articles and the developer talks, interviews and reviews they cite. I did not open the cited talks or interviews themselves. Mapping notes to project files are proposals, not statements about what those files currently say.*

**D1. The genre in one paragraph**

An immersive sim is built on simulated systems that react to many player actions, with a broad set of player abilities. That produces varied solutions and emergent play that the designers did not script (Wikipedia, "Immersive sim"). Mark Brown (Game Maker's Toolkit) puts the key difference as the absence of scripted or fixed events, and gives the example of rope arrows that stick to any wooden surface in the original *Thief* (1998), where the 2014 *Thief* limited where they worked and lost the genre trait. Warren Spector's own description is a good test for this project: the world reacts to the player instead of forcing one action. The lineage runs from Looking Glass Studios (*Ultima Underworld*, *System Shock*, *Thief*) through Ion Storm (*Deus Ex*) and Irrational (*BioShock*) to Arkane (*Dishonored*, *Prey*). By convention, many of these games hide the door code 451 or 0451 in the first code the player finds, a nod to *System Shock*. That is a free Easter egg for the Level 0 or Opening Sequence keypads if you want one.

**D2. Precedents and what to take from each**

| Game | Take | Watch for | Compare with |
|---|---|---|---|
| ***BioShock*** (2007, Irrational) | A place that is a philosophy made architecture. Levine drew on Rand, Orwell and Huxley and noted that Rapture's people were oppressed once and became oppressors. A late playtest found players felt no tie to Jack, so the team added the plane-crash opening the day after the test. Focus tests also showed the first level lost players, so they added a quest marker and re-voiced Atlas with an Irish accent to sound more trustworthy. | The Little Sisters choice is the standard example of a weightless moral choice: saving them costs only about 10% of the ADAM reward (Friedman, Polygon; Blow made the same point). Vita-Chambers let a player wear enemies down by dying, and a patch later added an option to turn them off. The two endings were publisher-driven. Levine wanted one. | `design/ART_DIRECTION.md` (Rapture as "a dream that went wrong"; ICS as one that works), `design/FAILURE_LOOP.md`, `design/ENDINGS.md` |
| ***Prey*** (2017, Arkane) | The nearest structural match: a corporate space station, one continuous space, a fake tutorial that turns out to be a simulation, and no single-solution gates. Arkane avoided obstacles that need one specialised skill and always provided a bypass. Every NPC, including the dead, is named and has a backstory, and the optional logs make the world feel real because the player may ignore them. Corporate branding was modelled on Ansgar Oswald's *Offices Construction and Design Manual*, which documents how corporate identity "permeates the workplace". Over-using alien powers makes the station defences treat you as a threat, which is a system-level consequence with no cutscene. | Early hours were called sluggish; combat was called weak because the game caters to many playstyles; the main quest was called thin; backtracking was used to stretch the runtime. Arkane limited horror elements because they could not predict where the player's attention would be. Disappointing sales led Bethesda and Arkane to drop immersive sims for live-service games. | `design/SOLUTION_MATRIX.md`, `design/GATING_BACKTRACKING.md`, `design/ENVIRONMENTAL_STORYTELLING.md`, `story/scene-notes/Opening Sequence.md` |
| ***Alien: Isolation*** (2014, Creative Assembly) | A single unkillable hunter whose behaviours unlock slowly, so it seems to learn. The motion tracker is useful but draws the Alien if used close by. Saving takes a three-second pause at a terminal, so the player can be killed while saving. The team dropped craftable weapons early because "this game isn't really about pulling the trigger", and moved from third person to first because "it's you that's being hunted". Design rule: build nothing the film crew could not have made as a prop in 1979. | Overexposure. Polygon: "By the 300th time I dived under a table or into a locker, I wasn't scared anymore — I was annoyed." Reviewers also named length, trial-and-error progression, distant save points and thin characters and logs. | `design/ENEMY_AI.md`, `design/EOD_ENCOUNTERS.md`, `design/SAVE_SYSTEM.md`, `design/STEALTH_DETECTION.md` (EIMU Diagnostic Accessory), `design/ART_DIRECTION.md` |
| ***SOMA*** (2015, Frictional Games) | A game about consciousness and free will whose story does not depend on the player reading everything: someone who ignores the logs can still follow the plot. No weapons; the player runs or hides. | Monsters were the most-criticised part: "tedious", "dumb ambulatory obstacles", pulling reviewers away from the story. A "Safe Mode" added about two years later keeps the monsters but stops them killing the player, and a reviewer said it gave the story "the space it always needed to breathe". | `design/DIFFICULTY_ACCESSIBILITY.md` (difficulty as information, not damage), `design/FAILURE_LOOP.md`, `design/AUDIO_VOICE.md` |
| ***The Stanley Parable*** (2013, Wreden and Pugh) | Employee 427 in an office, an authority voice that adapts when disobeyed, and a first choice built so that players do not notice anything wrong. Wreden said players split roughly 50/50 between following and defying the Narrator. Also useful: a deliberately "broken" button puzzle that makes players feel they lack control. | Ars Technica pointed out that many choices lack an effect, so the player only feels more in control than they are. The tone is comic. ICS is the same office, played straight. | `design/PLAYER_GUIDANCE.md`, `design/VERBS.md` (Slip, Witness), `design/TUTORIAL.md` (tutorial as job) |
| ***Papers, Please*** (2013, Lucas Pope) | The best match for the "job as game" idea. Mechanics are the bureaucracy: Morrissette's *Game Studies* essay reads the game through the "iron cage of bureaucracy". Pope added the invasive body scanner to give the story a reason for the inspector to hold such a tool. He kept the family status screen plain so as not to sway the player's feelings. The "clunky" interface was deliberate. | Not everyone was convinced: Good Game called it tedious. An "endless mode" had to be added for players who did not care about the story. | `design/TUTORIAL.md`, `design/PROGRESSION.md` (the badge as character sheet), `design/SOLCRED_ECONOMY.md`, `design/UI_MENUS.md` |
| ***Dead Space*** (2008, Visceral) | Already the project's model for improvised tools (`canon/weapons/MODIFICATIONS.md`). Makedonski (Destructoid) credits its mechanics with conveying terror and loneliness. I did not fetch the game's own article. | Not checked. | `canon/weapons/MODIFICATIONS.md` |
| ***Hardspace: Shipbreaker*** (2022, Blackbird Interactive; early access June 2020) | **Not an immersive sim.** A first-person job sim, and the closest match in the table for the premise: the player is a contracted worker in a corporation that owns them. The player signs a contract that makes them Lynx property, owes a $1.2 billion debt, earns credits against it, and spends Lynx Tokens on tools. Lynx holds their DNA and can reconstitute them when they die at work (the "EverWork" programme) so that they can keep working. The union is organised on a private e-mail server that a crew member shows the player, and the story turns when an administrator reads it. Every shift's comms are recorded under company policy, and the foreman leaks the administrator's recorded orders to win. The developers said the tools had to feel like "heavy industrial equipment" rather than weapons, and cut a shockwave weapon to keep the player a worker. The game began as *Hello, Collector*, about asteroids, and the team felt it drifted to a "cosmic horror" tone and played too slowly, so they changed it. | IGN's Stapleton criticised the "intentional tediousness" and wrote that the repetitive objectives and "intentionally slow progression" made shipbreaking feel like "hard labor". Digital Trends noted the repetitive loop and occasional zero-G nausea. All missions were timed until an Open Shift mode removed the time limit. Waypoint's Price read the yard as a company town paid in company scrip and found the work itself mechanically and aesthetically beautiful, contaminated only by the corporation's deadlines and unsafe conditions. Where it differs from this project: the player can join an organised union, and the story ends with the debts mostly reimbursed and the union recognised; the player may also pay off the debt and leave. | `design/SOLCRED_ECONOMY.md` (a leash that looks like a wallet, against Lynx's debt and tokens), `design/FAILURE_LOOP.md` (death as a clinical document; compare EverWork), `design/PROGRESSION.md` (certification ranks against Tiers), `design/HEARTH.md` and `design/ICS_OS.md` (a mailbox the staff are not meant to read; compare the union server), `canon/weapons/MODIFICATIONS.md` (tools that are not weapons) |

**D3. Ludonarrative dissonance, and why this project can use it**

Clint Hocking coined the term in 2007 about *BioShock*: the gameplay rewarded self-interest while the story asked for selflessness, so the player's agency in play contradicted the agency the story allowed. The usual advice is to avoid it. Walt Williams (*Spec Ops: The Line*) argued at GDC 2013 that embracing it lets a developer portray the player as a hypocrite, and Ballantyne and Seraphine argue that deliberate dissonance can be a storytelling device. *Papers, Please* is the standard example of the opposite, ludonarrative consistency.

For this project the two are the same design question: the warmth is real and the cage is real. If the badge, the quarters and the Music Programme feel good to play, the dissonance is the horror (compare Doc 2.18's "relief from the burden of freedom"). The risk is the accidental kind. For each system, decide whether it is meant to be consistent with the story (the badge, the job) or dissonant on purpose (the comfort). A system that is dissonant by accident reads as a bug.

**D4. Recurring problems in the reception of these games**

- **Overexposure of the threat** (*Alien: Isolation*; *SOMA*). Both lost tension when the threat appeared too often. `design/TENSION_CURVE.md` and `design/EOD_ENCOUNTERS.md` are the right places to set a ceiling on how often EOD appears.
- **Weightless choice** (*BioShock*; *The Stanley Parable*). A choice that costs nothing reads as decoration. Check each branch in `design/ENDINGS.md` for a real cost.
- **Trial and error, and far-apart saves** (*Alien: Isolation*). Compare `design/SAVE_SYSTEM.md` (autosave plus one manual slot in quarters) with `design/FAILURE_LOOP.md`.
- **Backtracking used as padding** (*Prey*). Compare `design/GATING_BACKTRACKING.md`; every return to a level should carry something new.
- **Thin main quest, rich world** (*Prey*; *Alien: Isolation*). The project has the opposite risk: a very large canon. The player's path through it is the thing to protect.
- **Early hours slow because tools are missing** (*Prey*). Compare the Phase 0–1 tutorial design in `design/TUTORIAL.md`.
- **Repetition as the point** (*Hardspace: Shipbreaker*). Reviewers split on whether a loop that feels like hard labor is a flaw or the theme. It is a useful test for the Tier 3 work floor: the repetition should be the argument, and it needs a way out of the player's tedium (the game added Open Shift to drop the clock).
- **Commercial risk.** The genre is well reviewed and sells poorly. *System Shock 2* sold about 58,000 copies in eight months and Looking Glass closed in May 2000. *Dishonored 2* and *Prey* both underperformed. Jordan Thomas said in 2017 that immersive sims are very hard for anyone but large teams to build, though some solo or small teams have shipped them. `design/PRODUCTION_SCOPE.md` already treats its figures as placeholders. This evidence supports keeping the vertical slice small.

**D5. Primary sources worth reading (named in the Wikipedia articles; not opened by me)**

- Clint Hocking, "Ludonarrative Dissonance in Bioshock", Click Nothing, 7 Oct 2007.
- Warren Spector, "Postmortem: Ion Storm's Deus Ex", Gamasutra, 6 Dec 2000.
- Gary Napper, "Game Design Deep Dive: The save system of Alien: Isolation", Gamasutra, 11 Feb 2015.
- Thomas Grip, "SOMA – Crafting Existential Dread", GDC.
- Jess Morrissette, "Glory to Arstotzka: Morality, Rationality, and the Iron Cage of Bureaucracy in Papers, Please", *Game Studies*.
- Thomas Biery, "What makes an Immersive Sim, and why are they staging a comeback?", Polygon, 18 Aug 2016.
- Walt Williams, "We Are Not Heroes: Contextualizing Violence Through Narrative", GDC 2013.
- *Hardspace: Shipbreaker*: Alex Willshire, "How Hardspace: Shipbreaker's devs made spaceships you can cut anywhere", Rock, Paper, Shotgun, 29 Jul 2020 (development and the tools-not-weapons rule); Alex Wawro, "Inside the twisting, turning development of Hardspace: Shipbreaker", Gamasutra, 6 Aug 2020; Renata Price, Waypoint, 3 Jun 2022. Facts above come from the Wikipedia article and the reviews it cites; I did not open these pieces.

**E. Further references [PROPOSAL]. From memory, not fetched (2026-11-06)**

*Web search and fetch were unavailable when this section was written (API 403), so none of it was checked against a source. Everything is from the writer's memory. No quotations and no sales or review figures are given, on purpose (Rule C above). Check any fact before it goes into a canon document. The "Take" column is the useful part; the "Compare with" column names project files and is a proposal.*

**E1. Games**

| Game | Take | Watch for | Compare with |
|---|---|---|---|
| ***Metro 2033*** (2010), ***Last Light*** (2013), ***Exodus*** (2019) (4A Games; from Dmitry Glukhovsky's 2005 novel) | The nearest tonal match for a closed world with a politics. Each station is a small state with its own ideology, so a level is an argument. The interface is diegetic: a wristwatch, a lighter, a gas-mask filter timer, and wiping the mask. Military-grade ammunition doubles as currency, so spending is a choice. The first two games keep a **hidden morality score** (kind or observant acts) that decides the ending without telling the player, which answers the "weightless choice" problem in D4. | Reviewers split on the stealth and the linear stretches. The hidden score can feel unfair if the player cannot tell what counted. Check both claims before relying on them. | `design/SOLCRED_ECONOMY.md` (a currency that is also a leash), `design/UI_MENUS.md` and the badge clock (diegetic UI), `design/ENDINGS.md` (flag-gradient endings, which are the same idea), `canon/facility/Overview.md` (levels as ideologies) |
| ***Half-Life 2*** (2004, Valve) | An occupation introduced by a train station: propaganda broadcasts on arrival, an enforcer force, a cheerful official face on the screens. No cutscenes; the player keeps control. | Later chapters turn into a shooter. | `canon/facility/TV_SCREENS.md`, `design/TUTORIAL.md` (arrival and broadcasts), `story/scene-notes/Opening Sequence.md` |
| ***Portal*** and ***Portal 2*** (Valve) | Corporate cheerfulness as menace. Testing as a job the subject does not choose. A voice that is polite while it harms you. | Comedy carries most of the weight; ICS is the same voice played straight. | `canon/documents/2.34` (broadcast), `canon/documents/2.31` (mascots), AIDEN |
| ***Control*** (2019, Remedy) | Bureaucracy as the supernatural. A brutalist office whose layout does not stay put, forms, memos and recorded training videos as the main storytelling. | Combat is the weakest part; ICS has none to speak of. | `canon/internal-communications/`, `design/ENVIRONMENTAL_STORYTELLING.md` |
| ***Disco Elysium*** (2019, ZA/UM) | Interior voices as characters; a protagonist who must reconstruct who they were. A thought cabinet you spend time on. | Do not copy the political satire of a real world; ICS has its own. | `design/PLAYER_GUIDANCE.md`, Kai's lists (scene 1.10) |
| ***Frostpunk*** (2018, 11 bit) and ***This War of Mine*** (2014) | Moral cost as a visible number or an unspoken one. Frostpunk lets the player legislate until they are the system. This War of Mine makes small survival choices cost something to a person you know. | Both are survival management; neither has a first-person body. | `design/HEALTH_SURVIVAL.md`, `design/FAILURE_LOOP.md`, Phase 6 |
| ***Beholder*** (2016) and ***Orwell*** (2016) | The player as the surveillance state, which turns the reading of private files into the moral act. Orwell is already named for the mail viewer. | Both are text-heavy and can be repetitive. | `design/HEARTH.md`, `design/ICS_OS.md`, Kai's flagging (scene 1.8) |
| ***Return of the Obra Dinn*** (2018) and ***Her Story*** (2015) | A mystery solved by reading records. The player pieces the story from fragments without being told. | Her Story can feel thin if the clips do not escalate. | The Rania chain (`design/DISCOVERY_SEQUENCE.md`), `canon/documents/2.36` |
| ***Pathologic*** (2005, 2019 remake) | A town where every choice costs time you do not have, and the clock is the antagonist. | Famously hard, with confusing rules. | `design/TIME_MODEL.md` (the 22-hour stopwatch), Phase 6 |
| ***Outer Wilds*** (2019) and ***Observation*** (2019) | Knowledge as the only progression. Station horror from the point of view of the station's own systems. | Outer Wilds has no antagonist; Observation is slow. | `design/PROGRESSION.md` (the badge is the character sheet) |

**E2. Books, film and television**

- **Dmitry Glukhovsky, *Metro 2033* (2005).** The game's source: survivors who build ideology out of fear. Also a good example of an enclosed world that stays human-sized.
- **Yevgeny Zamyatin, *We* (1921).** A numbered population in glass buildings, with a state that shows its work. Already a lead in B; it is the closest literary relative of the glass walls of Level 3.
- **Ursula K. Le Guin, "The Ones Who Walk Away from Omelas" (1973).** A bright city whose happiness depends on one hidden suffering. It is the structure of Schedule D told in two pages. Check the date.
- **Stanisław Lem, *Solaris* (1961), and the Strugatskys, *Roadside Picnic* (1972).** An alien presence that cannot be understood, and humans who explain it badly. Both are models for EOD: the unexplained power, and the analysts' reports that fail to account for it.
- **Franz Kafka, *The Trial* and *The Castle*.** An institution that never states the charge. Already a lead in B.
- **Thomas Ligotti, corporate horror stories** (for example "My Work Is Not Yet Done"). Office life as dread. Check the title and collection before citing.
- **Mark Fisher, *Capitalist Realism* (2009).** "There is no alternative" as an atmosphere, which is Doc 2.18's Soft Ceiling. Quote only from the primary text.
- ***Severance*** (TV, 2022 on). A workplace split from the self, with a cult-like corporate warmth, rituals and perks. It is the closest recent tone match. Keep ICS distinct: Severance is about a split mind, ICS about a whole one.
- ***Brazil*** (1985), ***Playtime*** (1967), ***Office Space*** (1999), ***The Truman Show*** (1998). Respectively: paperwork as a death sentence, the office as a machine, the pointless job told as comedy, and a warm world that is watched.

**E3. Using E**

1. Take structure, not surface. Each of these shows how a system can be built from its details; none is a template to copy.
2. Where a game solved a problem in D4 (weightless choice, repetition, slow start), name the file it applies to before borrowing.
3. If a fact in this section is used in a canon document, verify it first and move the verified entry to Section A or D with a source.


---

### What was done in the most recent session

**ICS-OS 90s Logon UI Refactor & 13-Theme Personalization Engine.** Everything is **[PROPOSAL]** consistent with the author's brief. In short:

- **Sign-in UI Refactor (Eliminated Clutter & Truncation):**
  - Replaced the cramped icon row with an authentic 1990s enterprise workstation log-on dialog (`Log On to ICS Earth Branch Workstation`).
  - Added a dedicated sunken 90s listbox displaying all 7 accounts in full without any ellipses or squishing (`Standard employee`, `PTKW employee`, `Branch Director`, `EOD Research Team`, `Design Team`, `All access`, `All files`).
  - Added authentic etched `<fieldset>` groupboxes with `<legend>` tags for active user profile and credentials/routing, real-time digital clock, workstation node ID (`Terminal 349-B · Cycle 300`), and hardware status LED indicator.
  - Added beveled 3D push buttons (`[ Log On ➔ ]`, `[ Restart ]`, `[ Sound ]`, `[ Theme ]`) with tactile active pressed states (1px down-and-right physical shift).
- **13-Theme Customization & Personalization Engine:**
  - Added 13 distinct themes across corporate in-world lore and vintage computing aesthetics:
    - *Corporate In-World:* Automatic (Role Clearance), ICS Classic (Earth Branch Standard), PTKW Operations, Executive Office, Research Division, Brand & Interface, Board Eclipse, Master Archive.
    - *Retro Workstation:* Windows 95/98 Classic (Teal & 3D Gray), Luna Blue, Amber CRT Phosphor (1989 monochrome terminal), Green Matrix CRT (mainframe phosphor), Solarized Workstation.
  - Built the `Display Properties · Workstation Themes` dialog with live interactive window preview, color swatch pills, automatic role detection, and `[ Apply & Save ]`, `[ Auto (Role) ]`, `[ Cancel ]` buttons.
  - Multi-point access: Logon screen titlebar button, Start Menu (`Themes & Appearance…`), Taskbar System Tray (`Theme`), and Desktop Wallpaper right-click context menu.
  - Preferences persist across reloads in `localStorage` and `sessionStorage`.
- **Checked:** Headless Edge testing verified dialog DOM structure, role listbox, all 13 theme options, live preview switching, and desktop context menus.

### What was done in the session before

**ICS-OS version 0.1 — built, moved out of the writing map, documented.** Everything is **[PROPOSAL]** except the author's brief (recorded in `design/ICS_OS.md` section 1). Full rulings are in open ruling 31 below. In short:

- **The ask.** Turn Hearth into an operating system in the lineage of *Her Story*, *Orwell*, *Hypnospace Outlaw* and *Kingsway*: boot with the ICS logo and a loading screen, sign-in, a home screen with the logo as wallpaper, Hearth in a window, a cloud file explorer with no local save, an app to open the files, everything in a separate folder called ICS-OS (version 0.1), and the Branch Director's access to Staff and PTKW mail made to look weird.
- **New folder ICS-OS** (top level): `build_os.py` (entry point; accounts, per-document tiers and folders, layered-section patterns, retained-copy data, page assembly), `build_mail.py` (moved from the writing-map folder; now returns data through `collect(con)` instead of writing a page, and its markdown renderer is reused for documents), `os_template.html`, `os.css`, `os.js`, and the generated `ics-os.html`.
- **Removed from the writing-map folder:** `build_mail.py`, `hearth_template.html`, `hearth.html`. `build_map.py` now puts the ICS-OS folder on `sys.path` and calls `build_os.build(con, now, cur_id)` inside a try/except (about line 943), as it did for Hearth.
- **Apps.** Hearth (all 93 messages, as before, plus the Director's retained copies). ICS Cloud Drive (50 documents in seven folders of my own grouping; sortable list, search, properties; Save, Download, Copy, Print and Upload shown disabled, Ctrl+S and Ctrl+P give a policy notice). Folio (outline, find in file, clearance chips, document-to-document links, cross-links to Hearth messages).
- **Clearance.** Each document has a whole-file tier (All staff, PTKW, Branch Director, Board) read from its own classification line, held in the `DOCS` table in `build_os.py`. Four files sit outside the tiers (`SPECIAL`): 2.35 and 2.39 appear only to All files, 2.42 to All access and All files, 2.49 to the Research Team, the Director, All access and All files. Thirteen documents are layered (2.24, 2.25, 2.29, 2.31, 2.32, 2.33, 2.34, 2.37, 2.40, 2.43, 2.45, 2.47, 2.48): `LAYERS` holds a pattern for each marker line, and a section above the reader's tier renders as a redaction block. No document was edited.
- **Documents per account:** standard employee 19 of 50, PTKW 36, Branch Director 38, Research Team 37, Design Team 19, All access 48, All files 50. Mail counts are unchanged from Hearth: 16, 61, 83, 21, 25, 93, 93.
- **Director's retained copies.** 56 of the Director's 83 messages are series A or B; each shows a banner, a Route row, an "Opened N times before today / Opened by: no record" row (N is 1 to 6, from a hash of the message code so rebuilds never change it), a late-appearing "Your open was recorded" line, a status bar and a taskbar item (CCN copy: on, set by no record). B-02 and B-25 stay hidden from the Director, as in Hearth.
- **Checked.** Headless Edge, six accounts (standard, PTKW, Director, All access, Research, Design): 20 or 21 of 21 checks each (boot, desktop, window open, minimise, maximise, close, drive row counts, Board-document gate, glossary redaction counts of 42, 21 and 0, Ctrl+S refused, sign-out). All files was not run. Screenshots of boot, desktop and the Director's mail were looked at. `node --check` passes on `os.js`. Baseline held after the final rebuild.
- **Docs edited:** new `design/ICS_OS.md`; `design/HEARTH.md` (intro, name, build diagram, paths, See-also); `README.md` (new row for `design/ICS_OS.md`); the README in the writing-map folder (file table row and an ICS-OS section replacing the Hearth section); this file (the ICS-OS bullet, baseline, ruling 31, and the path wording in rulings 29 and 30 and in the earlier session notes). `canon/internal-communications/README.md` and `design/TIME_MODEL.md` were not changed: neither lists Hearth.
- **Not done.** No Notes, Settings or Trash app; no mascots; nothing to show Staff or PTKW that copies exist; the in-game version is not built. The author has not yet answered whether the Director knows about the copies.

**Next, if the author answers ruling 31:** change the copy text in `os.js` (search for "Retained copy" and "was not requested") if the Director knows; add a receipt line to sent mail if Staff and PTKW should see something; add a pattern to `LAYERS` and a line to `DOCS` for any new layered document; rename in the constants at the top of `build_os.py`.

### What was done two sessions ago

**The EOD first-arrival chain (C-26, A-28, B-27, B-28, A-29) — written, indexed, rebuilt.** Everything is **[PROPOSAL]** except where noted. Full rulings are in open ruling 28 below. In short:

- **C-26** (`branch-director/`) — the Manager's kept thread from Labor Source #312, Cycle 292 Q2, Day 4: his message to HQ, HQ's reply (the Board has approved showing him one page; the Research Team is copied and told to explain), and the Team's 8-section handling manual. Section 7 attaches the cropped Designation and Field Reference Names page, the source of the scan in B-26, quoted with the older names in square brackets (the one place they appear in this chain). The Manager's note records that he told the Division the page was destroyed, kept it, and scanned it once. EOD smiles and waves here, and it is made creepy.
- **A-28** (`employee/`) — Lior and Chidi, Day 4, 19:12. On Earth EOD does not smile or wave (canon `design/EOD_ENCOUNTERS.md` is unchanged).
- **B-27** (`ptkw/`) — Lior's polite query, the Floor Liaison's rude reply, the forward to K-7.
- **B-28** (`ptkw/`) — K-7 asks the Manager; the Manager's warning to all PTKW ("my old friend"); the forwarded manual with section 7 removed; K-7 circulates it to all PTKW against the Manager's instruction.
- **A-29** (`employee/`) — the Day 31 chat of Chidi and Ruth Calloway, redacted by the investigation team on Day 33 (R1 older designations, R2 source, R3 third party), with a cover note that records the sheet was clean when read and was handed to E-03615.

**Edited:** C-25 ("twenty-seven days" became "eight cycles", and the Manager has spent one deployment with him), B-26 (open ruling and cross-references), ruling 26's Dates bullet, ruling 27's second-copy bullet, `README.md`, `canon/internal-communications/README.md` (tree), `design/TIME_MODEL.md` (rows for Days 4, 5, 6, 31, 33, and an off-timeline note for C-26).

**Author rulings applied this session:** the smile and wave stay in the #312 thread and are creepy; the Day 21 smile in the Gyrfalcon Wing battle is a separate thing and is untouched; the Board approved the page loan; the tenure wording and the placeholder names are confirmed; the leak question the author could not answer is a proposed answer (the Manager''s scan), pending acceptance.

**Hearth** was built after the chain: `design/HEARTH.md` (spec, ruling 29) and a builder, later moved into the ICS-OS folder (ruling 31). The viewer was checked in a headless browser. A-29 gained a standard header so it shows a sender and date.

### What was done two sessions ago

**Deployment 287 series — fully restructured and expanded.** Final order, renumbered at the user's request so the files read as EOD's story: C-18 (EOD lands and cannot be found), C-19 (Blue Harrow Team interview, his first appearance), C-20 (Gyrfalcon Wing Day 18), C-21 (Gyrfalcon Wing, open water air engagement), C-22 (Gyrfalcon Wing, Hallvik tower), C-23 (master summary). Wherever an older note in this file uses different numbers, the list above governs. The paragraphs below were remapped in one pass and read in the new numbers.

- **C-18** is now only the request and the Branch's first reply, which says it cannot place EOD for the ten days (the user asked for this split). The Reiner transcript, the Branch Manager's reading of the ten days and the Research Team's Day 22 reply moved unchanged into **C-19** ("Blue Harrow Interview Update", Day 22, 02:15), the update that finds him. Citations of the Sudbury transcript in Docs 2.15, 2.17, 2.18, 2.29, 2.38, 2.41, 2.47, B-25, C-20, C-22, C-23, design/DESIGN.md, design/EOD_ENCOUNTERS.md, design/TIME_MODEL.md and the character files now point to C-19. C-20 now corrects C-19, not C-18. "Five days" became "six days" (Day 16 to Day 22) in C-19, Doc 2.18 and Doc 2.47.
- **C-20** — unchanged. Gyrfalcon Wing Day 18. Solberg's cockpit recording.
- **C-21** — rewritten and expanded. The recording opens with the HAWK patrol track (02:36), the air-branch query (no asset in that sector), the contact stopping on the surface and a man waving, and the Wing Command override that orders HAWK off. Then Gyrfalcon Wing's scramble, the ring, the review board's explanation of the show of force, and the Gyrfalcon Three exchange ("look him in the eye", "I can go lower, sir", "my only chance"). At 03:02:51 the open palm meets Three's canopy: the transparency does not break, and the helmet, visor and face are pressed flat against its inside in the outline of the hand (cockpit camera, wreck and pathologist's account). His aircraft flies on for eight seconds, releases two uncommanded missiles and enters the sea inverted at 03:03:31. The other seven then fight for 36 minutes, and each is lost in a different way (Four comfortable at nine g, Eight flying through his own stopped rounds, Five's missiles turning back, Two no longer afraid, Lead's "six aircraft on my wing", Six's "it is arranging us"). Seven (Captain Eirik Aronsen) is the exception and has the longest sequence, written to the author's two drafts: he flies a cobra, the contact goes through and grips the belly of the aircraft, flies it by hand through 6.0, 8.5, 10.8 and minus 3.4 g and speaks to him on the Wing's frequency ("let us see what humans are really capable of"); he declines the eject order because "he is testing us, not only the g"; he ejects when his father says "please"; the contact leaves, hears his father say "son" (the first family term in 32 exchanges), turns back, cuts the parachute, flies beside him looking into a camera that is feeding the tower cab, and says "Here. Let me give you a hand. Let me help, son." He is killed on impact with the sea. A flight surgeon's console table shows every other trace simply stopping. The flagged Three transmission at 03:21:08 is kept. Seven aircraft land, Seven's empty; one is lost at sea. The conclusions are nine numbered points. The Blue Harrow / Sudbury encounter is no longer referenced inside C-21.
- **C-22** — Hallvik tower cab. EOD speaks to Aronsen. Updated for the new toll: six pilots on the apron, "medical, six".
- **Doc 2.18, and what points to it.** §2.10 gains "What the study concludes about fear" (the purpose of EOD: terror of the unknown, the expected surrender, the reason for the name Executioner of Despair). §2.11 is now the **released account** given to PTKW: the mission is complete, with three false statements (Control's recording incomplete owing to interference; no pilot made a statement of intent or defiance; no chain of command recovered control). It names neither Eirik nor the debrief. The true account is the sealed Doc 2.49. Docs 2.15, 2.29, 2.38, 2.41 and 2.48 were cleaned of any mention of Eirik, the debrief or the smile, because PTKW can read them.
- **Doc 2.49 — The Smile Study** (title inside the file: "The Study of Eirik's Smile") — new, **sealed**. The file is named "The Smile Study" because the name checker flags a possessive form of "Eirik" in a filename as a misspelling; avoid that form in filenames and in the text of new notes. Readers: the EOD Research Team, the Earth Branch Manager and EOD. No other office; PTKW are not told it exists. Five reasons for the seal; Eirik's two transmissions; what the Division cannot explain; the debrief of EOD (author's wording); "Why was he smiling" with sources and five hypotheses; the narrative told to PTKW and its three false statements; standing instructions; the assessment, which calls it "the first crack in the entire ICS system". C-21 and C-23 carry the same seal in their Status lines and point to it. "Why was he smiling" is also in C-21 (a board note and a Day 28 addendum), C-23, both Aronsen files, `EOD.md`, `design/EOD_ENCOUNTERS.md` and `design/TIME_MODEL.md`.
- **Doc 2.50 — ICS Nomenclature Note** — new, **Board access only**. Explains Doc 2.02: ICS has three readings (public: Interplanetary Corporate Solutions; PTKW: Inflatable Crowd Solutions; Board: the same words as a procedure, "fill the crowd; dissolve it"). "Inflatable" = fill, measured by hire rate up to saturation (Docs 2.12, 2.22, 2.29). "Crowd" = the unit is the population, not the individual. "Solutions" = the commercial sense plus the chemical one: taken up until it cannot be filtered out (Schedule D and Stage 5, Doc 2.23). Five reasons it is withheld from PTKW. It is a loose sheet stapled behind the PTKW copy of 2.02 with a pencilled "Why?". Docs 2.02 and 2.29 were not edited; the Board entry for "ICS" in 2.29 (no written form for the Board's own designation) is consistent with it.
- **C-23** — new. Deployment 287 master summary written from Day 28 perspective. Branch Manager's four-event through-line. Research Team reply. Sealed (Research Team, Earth Branch Manager, EOD; not PTKW, not the Board). "What the Branch does not know" updated to match C-21. Event 3 now names Three's inverted pass and Eirik's refusal. The reply has six notes: the Doc 2.18 study succeeded and its conclusion on fear; what the Division expected (surrender); Eirik (his two transmissions, the 1.7% of §2.9, Milgram's 40% and 15% in §3.1); Three; the debrief of EOD (the smile; "we can't control them"; filed in Doc 2.49 and forwarded to no one); and further study (Docs 2.18, 2.38).

**Characters updated:**
- `canon/characters/Colonel Leif Aronsen.md` — Day 21 section updated: he was in the tower cab from 02:41, ordered HAWK off before the scramble, heard Three at 03:02:50 (not described to anyone). Six pilots on the apron; Seven's aircraft empty; two in the sea. He hears Eirik's death live and says nothing for 47 seconds.
- `canon/characters/Captain Eirik Aronsen.md` — C-21/C-22 references corrected to split documents; Day 21 rewritten to Eirik's cobra, the g-test, the eject order and the fall; the apron ring is now six pilots with Seven's aircraft empty beside them.
- `canon/characters/EOD.md` — footer corrected (mojibake script, two separate C-21/C-22 lines).

**Support files updated:**
- `README.md`, `canon/internal-communications/README.md`, `design/TIME_MODEL.md` — C-23 added to all indexes and Day 28 ledger row added. The C-21 index rows now reflect seven landed and one lost at sea.
- `canon/documents/2.48`, `canon/characters/Colonel Leif Aronsen.md`, `canon/characters/Captain Eirik Aronsen.md` — all C-21 tower references corrected to C-22.
- `meta/HANDOFF_CARTOGRAPHER.md` — this file — updated to reflect current state.

**Craft notes for whoever expands C-19 (Blue Harrow) further:**
The scene at the Lindenmere Hotel is the equivalent of an Iron Man/F-22 intercept viewed from the ground unit's side — a contact that should be classifiable and isn't, moving in ways that violate the expected physics of a human body. The Reiner transcript already has the beats: the wall-walking, the disgust-not-anger, the speech. If expanding, the *Top Gun* rule applies: drama comes from constraint, not from action. What Maddox's order to enter the room cost him is the scene. The survivor's account ends mid-sentence because he can no longer speak — that is the correct ending; do not add to it.

---


### Open rulings (ask the user; don't guess)

**Still open — needs the author's call:**

2. Phase 6 real-time length: `design/TIME_MODEL.md` proposes 88 minutes at 15×.
5. The Blender shotgun (`Props/Shotgun/`): repurpose as BAR-FL, keep as a prop, or cut.
10. Smaller items:
    - Tarek's notebook location and Omar's level.
    - Maintenance Type A/B/C descriptions.
    - Whether the hatch exits to the transit docking area or a utility alcove.
    - The Junction A/B blade in `design/PROGRESSION.md`.
11. Whether Phase 6 closes on Day 65 as now, or you want the earlier Day 96 epilogue.
12. **Human forces (from Docs 2.47 and 2.48), all unanswered:**
    - Keep the names "the Harrow", "Gyrfalcon Wing" and "GNIC"?
    - Is the anti-drugs force a treaty command (as written, under the Anselm Convention) or an Interpol-style agency?
    - Add a third tier of national armies and navies?
    - Approve or replace the insignia: mottos AGAIN TOMORROW and SIX MINUTES, the "Tine" badge, the squadron names Longwatch, Whiteout and Lantern, and the grade hours.
13. Move the Appendix A material (Game Overview, earlier Doc 2.32) from `reference/` into real files in `writing/`?
14. Known loose ends, to confirm or fix:
    - `canon/weapons/MODIFICATIONS.md` lists AMB-3S, BAR-HS and the Directional Dispersal Rig, none of which has a file.
    - `design/HEALTH_SURVIVAL.md` and `design/SAVE_SYSTEM.md` disagree on Omega-1 capture.
    - B-25 is dated Cycle 300 Q3 but points to the Q4 files C-19 and C-20. This is only a pointer.
    - Doc 2.16 uses real missile names (AIM-120D, AIM-9X) and the F-22.
25. **The Day 21 scene (C-21 + C-22) [PROPOSAL].** C-21 covers the air engagement over open water; C-22 is the tower cab at Hallvik Air Station. The scene was written to the user's brief and several canon points bend. Rule on each:
    - **EOD speaks plainly.** In the tower he explains himself ("downsizing", "branch sunsetting"). This conflicts with Doc 2.18 Section 2.10 and `design/EOD_ENCOUNTERS.md` (he needs to be unexplained). Keep, rewrite so he withholds, or make it a Board-sanctioned message.
    - **ARM-27 sortie after the ten days.** Doc 2.17 has ARM-27 passive through Days 11 to 20. C-21 puts an active sortie on Day 21 (02:41 to 03:55), which the order did not authorise. A "Second annex (Day 26)" was added to Doc 2.17 to record it.
    - **Wing casualties.** Doc 2.48's "no weapon fired" line and C-20's "no casualties" are superseded by the Day 21 deaths of all eight alert pilots. A Day 26 addendum in Doc 2.48 says so. The Day 18 text is untouched. C-21 now has seven aircraft landing (Seven's with no pilot) and one lost at sea; the author should confirm that toll, and the invented deaths of Four, Eight, Five, Two and Six, the "six aircraft on my wing" beat, and the extensions to the Seven sequence.
    - **Time gap.** EOD is at Hallvik at 03:59 local and in the Level 2 atrium at 08:17 Branch Time. The offset between the two clocks is not stated.
    - **Planet count.** The dialogue says "more than 300 planets" (the user's wording). Docs 2.22 and 2.29 say 349.
    - **ARM-27 autonomy.** The scene has it autonomous, with no pilot and no cockpit. Confirm against Doc 2.16.
    - **Names.** Colonel Leif Aronsen, Captain Eirik Aronsen (call sign "Tern"), Marit, and Hallvik Air Station are placeholders. Confirm or replace.
    - **Terms.** Add "downsizing" and "branch sunsetting" to Doc 2.29, or leave them out of the glossary.
    - **Eirik's message to the species [PROPOSAL].** C-21 now has two transmissions, at 03:33:53 and 03:33:57, to the author's wording. `canon/characters/Captain Eirik Aronsen.md` used to say "no dying message"; it now allows these two and no third. Confirm.
    - **EOD says "I'm afraid to say this" (Doc 2.49).** Doc 2.15 gives EOD a complete absence of the emotional states EIMU monitors. The Team notes the word and the baseline reading and draws no conclusion. This is one reason the file is sealed. Confirm that it is a figure of speech, or change it.
    - **Debrief date.** The debrief of EOD is undated. It must fall after Day 21, 16:20 (C-18: the Division does not know where he was) and before Day 28, 14:00 (C-23, which already mentions it). Doc 2.49 opens at 18:50 the same day.
    - **Access list for the Eirik material [PROPOSAL].** The author set it: the EOD Research Team, the Earth Branch Manager and EOD; not PTKW. The Board is therefore not a reader. This overrode the lines in C-23 and the earlier version of Doc 2.18 §2.11 that sent the debrief to the Board; those lines are changed. C-20 and C-22 still say items were forwarded to the Board; they do not touch the sealed material. Confirm the Board is excluded.
    - **The lie to PTKW [PROPOSAL].** Doc 2.18 §2.11 is a false account, by the author's order. The three false statements are listed in Doc 2.49. The PTKW copy of Doc 2.18 is 74 pages and the file copy is 78. Confirm the three statements and the page counts.
    - **Cleaned documents.** Docs 2.15, 2.29, 2.38, 2.41 and 2.48 no longer mention Eirik or the debrief, because PTKW can read them. B-25 says Branch Operations is not cleared for the Doc 2.47 and 2.48 folders; the Earth Branch Manager's access to the sealed file is separate.
    - **Doc 2.50 [PROPOSAL].** Confirm the third reading ("fill the crowd; dissolve it"), that "Inflatable" was dropped from the public name because it cannot be dressed as a benefit, and that the Board keeps the pencilled "Why?". Decide whether 2.02 or the 2.29 "ICS" entry should point to 2.50. They do not now, because PTKW can read them.
26. **The EOD sunset chain (C-24 + C-25) [PROPOSAL].** C-24 (Day 29, Research Team to Earth Branch Manager) and C-25 (Day 30, the Manager's reply) sit in `canon/internal-communications/branch-director/`, one level above Doc 2.49. Two readers only: the Team and the Manager. EOD is not a reader. No Team reply to C-25 is written, on purpose. The author set the brief; the points below are where it bends the canon or where I added something. Rule on each:
    - **Board vote (contradiction).** Doc 2.21 requires a **unanimous Board vote** to deploy EOD, and Doc 2.41 says the Board is itself attending to him. C-24's authority paragraph has the Directorate act on the joint request of the Research Division and the Branch Manager, with the Board told one line afterwards. Can it act without a new vote? C-25 objection 6 raises the same point: the Manager asks why the Board is reachable for his delay but not for this, and says he will not be the only signature on it.
    - **Board and the sealed material (contradiction).** C-24 section 6 escalates to the Board if the Manager fails to report. Doc 2.49's access list (and ruling 25 above) excludes the Board. The author's phrase "board of members" is written as "the Board", because the Board is not a committee. Confirm the Board may see this file, or reword the escalation.
    - **The Journey Completion Directorate [PROPOSAL].** The author asked for a better, ICS-relevant name for the special unit. I took it from Doc 2.21's phrase "completed their ICS journey". It sits under the Interplanetary Governance Division (issuer of Docs 2.15, 2.17 and 2.44), has fourteen members held ready from a larger roster, and is disguised as the **Teshvar Consortium** (the competitor name is mine). Confirm the name, the Division, the competitor, and the remit ("an asset, a unit, a branch"). Decide whether it is added to Doc 2.21 or to the Doc 2.29 glossary. They do not mention it now, because PTKW can read them.
    - **Directorate versus Omega-1.** I made it a different instrument from Omega-1 (`canon/enemies/HQ-Response-Protocol.md`). Confirm, or merge them.
    - **Register and Schedule D.** C-24's "No entry" condition says EOD is not on the Doc 2.40 register and is not subject to Schedule D (per Doc 2.41). That is why no ordinary termination applies. Confirm.
    - **"Collector".** Section 1 uses the "collector" and "appreciation of quality" wording of Doc 2.41 and the Doc 2.15 card ("always accounted for") as the Team's reason for the choice of ending. Confirm the reading.
    - **The full designation.** At the author's request, all names are in one bracket: `EOD [Executioner of Despair (Subjugator, The Willbreaker, Harmony; public name Envoy of Devotion)]`. This is the one place the older names appear, and none is bare. The Subject line, the Team's own name and the cross-reference lists keep the short "EOD". The public statement keeps `EOD [Envoy of Devotion]`. Confirm this overrides the single-bracket rule for sealed material only.
    - **"300 worlds".** The statement says "more than 300 worlds", as the C-22 dialogue does. Docs 2.22 and 2.29 say 349. Same point as ruling 25. "More than 300 years" is read as cycles (one cycle is one year).
    - **"Sunsetting".** EOD used the word in C-22 and the Team asked the Branch not to use it. C-24 uses it on purpose, as the author's title does. Confirm.
    - **Public statement.** The statement and its six notes are mine apart from the first line ("After more than 300 years…"). Confirm the Level 2 atrium remembrance room as the place of remembrance, "Together We Grow" as the sign-off (Doc 2.12 poster), and the cover story that humans may feel joy or sorrow but not question the death.
    - **The badge paragraph [PROPOSAL].** The author asked that the statement say the Consortium feared the Branch because of EOD; that he carried no badge, so it judged those who did to be stronger than him; and that he carried none to blend in and so the colleagues would not fear him. It is a new paragraph in C-24 section 7 after "EOD [Envoy of Devotion] did not survive it.", with a seventh "How it is built" note. Two things to confirm: that the no-badge fact (`canon/characters/EOD.md`) is the reason the author wants, and that nothing else in the files says why he wears none. The paragraph is also the one place the public statement explains his appearance.
    - **The Consortium flees [PROPOSAL].** The author asked that the statement say the intruders ran after killing EOD because they feared the rest of the Branch and its people on account of him. This replaces the earlier "neutralised" and "remains in ICS's keeping". C-24 section 4 now has the Directorate withdraw at once after the kill. Section 5 item 6 changes from wreckage and remains to wreckage only, left behind. The statement shows the wreckage as "the vessels they lost". Two things to confirm: that no Teshvar bodies are shown to Earth's authorities, and that a force which fled does not weaken the 100 percent record or the claim that the Branch is safe. C-25 objection 3 argues about the statement's "lost", and it still reads correctly. The Manager's floor plan in C-25 does not mention the withdrawal and does not need to.
    - **Defaults and limits (mine).** The five triggers, the Day 35 default, the six items the Team asks for, the daily log, the 48-hour and same-hour reporting limits, and the three tests of priority. Confirm or change.
    - **Dates.** C-24 is Day 29, after Doc 2.49 opens on Day 28 and before the Phase 5 Day 10 row on Day 31 in `design/TIME_MODEL.md`. C-25 is Day 30, 06:15. Rows were added to `design/TIME_MODEL.md` for both. Day 38, 02:00 Branch Time is the proposed fight, after the Day 35 review. The Manager's "twenty-seven days" was changed to "eight cycles" (Cycle 292 Q2 at Labor Source #312 to Cycle 300 Q4 Day 30), after C-26 made the first meeting an earlier one on another planet. See ruling 28.
    - **Message to EOD (contradiction).** The Manager drafts a message to EOD that the attackers are real and have come to destroy the Branch. C-24 says EOD is not to be asked anything. The message asks nothing, but it is still contact. He asks the Directorate for four things, including a last line over the bay speakers: "The Branch holds. ICS thanks you." The Manager's reading of "real" is that the cover is kept and EOD is told, truthfully in the sense that matters to him, that a hostile force is attacking. That does not break the rule that he must not know who they are. Confirm that the Team may let it be sent.
    - **"Love" (contradiction).** The Manager says "my dear friend" and "love" of a being whose profile (Doc 2.15) has none of the states EIMU monitors. The Manager acknowledges this in the text. The author should confirm this is how the scene is meant to read.
    - **The farewell floor [PROPOSAL].** The author asked for an entire floor. I chose **all of Level 7**: Tier 1 access, the smallest usable floor below the upper levels, about 18,000 m², and the level EOD entered by on the night of Day 3 (`canon/facility/Level 7.md`, `canon/facility/Levels 11-14.md`). The departure scheduling offices, the 16-seat waiting area and the unlabelled 40 m corridor to Level 9 make it the exit level of the Branch, which the scene can use or avoid. Is it the floor the author wants?
    - **Preparation steps (mine).** Three days from the Team's confirmation. A floor-wide pressure-seal recertification as the pretext, with Level 8 told it is a certification. Stairwells A and B and the Level 8 connection sealed. The corridor to the Level 9 staging area sealed at both ends. All recorders closed but two in the bay. Lighting left neutral-functional, because EOD notices what has been changed. The transit commons left with its live schedule and two-option coffee point. Speakers tested. The Manager walks the floor alone and leaves at 01:40. Revised costs: 31 days for the floor, 19 for the bay, nothing lost. Confirm or change.
    - **The seven objections (mine).** Each taken from figures and sentences in C-24: the 100 percent record against the Day 21 surrender model, "for the first time" and "lost" in the statement against the record, the Branch unsettled since Day 22, the Level 2 remembrance room, the Board vote, the loss of the study's only witness, and a replacement sentence for the statement. The Manager's decision rule is: the first option (watch him) until the Team answers, the second (sunset) to the letter if the request stands. Confirm the Manager's character here.
    - **Files.** C-24 and C-25 are listed in `README.md`, `canon/internal-communications/README.md` and `design/TIME_MODEL.md`. Each ends with a `[PROPOSAL]` note that separates the author's content from mine. This ruling is the consolidated list.
27. **The restricted-name incident (B-26) [PROPOSAL].** Day 32, `canon/internal-communications/ptkw/B-26`. The Level 5 duty officer files Form ICS-IR3 on an asset who said `[Subjugator]` aloud at his desk. A print of a scan of the Doc 2.15 designation block was found in his drawer, with `Executioner of Despair` highlighted and his own line above it. The author set the brief: the word heard, the scan found, the highlight, the asset's words, and an investigation to follow. The points below are what I added, or where it bends the canon. Rule on each:
    - **A second copy of the Doc 2.15 card (contradiction).** Doc 2.15 is one laminated card, Board Access Only, "made to be memorised and then destroyed". B-26 has a scanned print of part of it, cropped so the header is missing, and the duty officer cannot name the source; he asks the Oversight Unit to identify it. Either a copy was made on purpose, or the card was handled outside the Board. Decide which, and whether the investigation is meant to find the answer. B-26 does not resolve it itself. Ruling 28 offers a candidate source: the Manager's kept page (C-26), though B-28 shows he removed it from his forward.
    - **The names are not for PTKW (contradiction).** Doc 2.29 says [Subjugator], [The Willbreaker] and [Harmony] are held at Board level and "not for PTKW use". The incident lexicon does not match the word, so the segment is escalated. The duty officer, the attending officers, K-7, TOR-9, K-12 and the Oversight Unit have now read them. The handling note asks whether that is itself an incident. Confirm, or cut the note.
    - **The full name is no secret from PTKW.** Doc 2.29 and Doc 2.15 both say PTKW use `Executioner of Despair` in writing. So the asset's alarm is at the name's meaning, not at a leak of the name. B-26 leaves this standing and has the duty officer note it. Confirm that this is the reading you want: the leak is what the asset has understood from the name, plus the names above PTKW.
    - **The word in the segment.** I chose `[Subjugator]`, the one name the asset could not have met except in the sheet, and the one PTKW cannot match. It is the only old name that appears in the report, in the spoken line and in the quoted block. Confirm, or choose [The Willbreaker] or [Harmony].
    - **The asset (placeholder).** E-03615, Tier 2, Operations Division, Level 3 Work Floor B. He has no profile in the repository (the map lists him as no profile). Confirm or replace. The report holds him at Level 5, not released and not reclassified, because he is the only trace. Doc 2.29 says involuntary reclassification does not need his knowledge, so retaining him is a choice by the duty officer.
    - **The asset's words.** The author's text is quoted verbatim, including the swearing. It is the only strong language in the PTKW folder. Confirm it stays as written.
    - **Detection (mine).** The desk AIDEN unit's flagged-segment rule (`canon/weapons/improvised/AIDEN-Unit.md`: 24-hour retention, flagged segments forwarded) caught the word with EIMU Fear: Terror, and the lexicon returned no match. Eleven-second segment, attendance after sixteen minutes, two assets within two metres. Confirm that the AIDEN unit is the way it was caught.
    - **EIMU readings (mine).** Fear: Terror HIGH, Disgust: Revolted HIGH, Surprise: Amazed HIGH, Anger: Rage MODERATE. Three are on the Doc 2.29 high-risk list, which triggers automatic escalation to the duty officer. Fear: Terror is not on that list (Fear: Apprehension is). Confirm.
    - **The seven-part investigation (mine).** The object, the scan queues, the hands, the asset's access path (the Circular 300-Q3-14 signature in B-17), other copies, the Protocol 7 list, and PTKW exposure. The 48-hour destruction rule for Form ICS-IR3 is suspended by the duty officer. Confirm the suspension, since Doc 2.11 says the form is destroyed within 48 hours.
    - **Who learns of it.** B-26 is a PTKW file, copied to the Oversight Unit. It does not reach the Research Team or the Earth Branch Manager (the readers of C-24 and C-25), and not EOD. Decide whether it should, and whether it changes the Day 38 plan. A leaked real name is the kind of thing C-24 would want to hear of.
    - **The player.** The Protocol 7 list is cross-referenced, but its result is withheld. Decide whether the player (E-05682) is meant to be on it, and whether E-03615 should appear again.
    - **Date.** Day 32, 16:47 (incident) and 19:05 (message), after the sealed pair (Days 29 and 30) and before the Day 38 floor. `design/TIME_MODEL.md` has the row. No other Day 32 event exists, so nothing conflicts.
    - **Files.** B-26 is listed in `README.md`, `canon/internal-communications/README.md` and `design/TIME_MODEL.md`, and ends with a `[PROPOSAL]` note that separates the author's content from mine.

28. **The first arrival chain (C-26, A-28, B-27, B-28, A-29) [PROPOSAL].** Five files on the first appearance of EOD to Earth's staff and, on an earlier planet, to the Manager. The author set the brief: the first encounter was on a previous planet and the Manager kept the emails; the Manager wrote to HQ about an agent with no tags or badges who smiled and waved; HQ copied the Research Team and asked it to explain; the Team replied with a manual that comes with the product; EOD smiled and waved to blend in and so staff would not fear him (the author later asked that this stay and be creepy); the Manager wrote to all PTKW agents to tread carefully, calling him "my old friend"; a PTKW agent asked the Manager for more and the Manager forwarded the old manual, which that agent sent to all PTKW; two assets discuss the document having read it only once; and the investigation team redacts that conversation as evidence. The author has ruled on the points marked RULED below. The rest are open. Rule on each of the points I added:
    - **The previous planet (mine).** C-26 is at Labor Source #312, Cycle 292 Q2, Day 4. Doc 2.22 places EOD there in Cycle 292 (resistance index 2.1 percent before). Doc 2.41 makes Cycle 293 follow his ninth deployment, and Earth is his tenth. The manual says "deployed eight times, yours is the ninth". Cycle 292 Q2 is off the game timeline. The author left the choice of planet to me, so #312 stands unless you say otherwise.
    - **The Manager's tenure [RULED — confirmed by the author, wording left to me].** The Earth Branch opened in Cycle 290. I read it as: the Manager was Branch Manager at #312 in Cycle 292, moved to Earth afterwards, and has run the Earth Branch for most of the cycles since. He has known EOD for eight cycles, through one deployment. C-25 says "eight cycles" and "a single deployment". Nothing in the files fixes his Earth start date, so none is stated.
    - **A Board-access page held by a Branch Manager [RULED — the author: the Board approved it].** Doc 2.15 is a Board-Access-Only card. C-26 now has HQ say in message 2 that the Board approved the loan on its application, and the manual's section 7 says the page is reproduced "under the Board's approval, granted this afternoon on HQ's application". The Manager kept the page and told the Division it was destroyed. Still open: whether keeping it is a breach the Division would pursue.
    - **Smiling and waving [RULED — the author].** Kept in the #312 thread (C-26), and made creepy: the smile does not change for a delivery driver or a woman in tears, the Manager cannot say what is wrong with it, the manual warns that most Managers find it unsettling, and that staff will find it friendly for a day or two. Earth Day 4 (`design/EOD_ENCOUNTERS.md`) stays as canon has it: no smile, no wave, no announcement; A-28 keeps that. B-28 has K-7 note the gap and the Manager's own unease. The smile and wave of Day 21 against the Gyrfalcon Wing (C-21 and the related files) is a separate thing and is untouched. Still open: whether Earth's beat should carry a line that explains why the instruction was not given for this Branch.
    - **The page and the source of the scan [PROPOSED ANSWER — the author could not answer, so this is mine].** C-26 section 7 attaches the cropped Designation and Field Reference Names block. In his note (Cycle 293 Q1) the Manager says he returned the manual, told the Division the page was destroyed, kept the page, and scanned it once. B-28 has him strip section 7 from his forward and say the page was returned, which is untrue. A-29 has two assets say they read the sheet once, clean, in E-03615's presence, and the cover note records that the R2 passages agree the sheet was handed to E-03615 and not found. B-26 notes the source may be the Manager's archive. The proposed answer: the scan is the Manager's, and the print in the drawer is from it, but the files do not say who handed it on or why, and PTKW do not learn it. Why a Manager who kept a page for eight cycles gave it to a courteous Tier 2 asset is left for you. Accept, or choose another route (a copy made at #312, or a different source).
    - **Does EOD know (mine).** The Manager kept the page and EOD does not know. Whether he does, and whether he would care.
    - **The rude PTKW reply (mine).** B-27 has the Floor Liaison reply that they do not know, that the asset is not entitled to an explanation, and to expect further updates. K-7 tells them off for the rudeness and asks the Manager. Confirm the tone.
    - **The Manager's forward (mine).** The Division's rule is that the manual is "not to be copied, forwarded or retained". The Manager forwards it, minus section 7. K-7 forwards it to all PTKW against the Manager's instruction not to. Decide what the Division does about both.
    - **Briefing (contradiction).** Doc 2.29 says PTKW staff are told to maintain standard operations and await instructions. B-27 has Level 5 not told that EOD has arrived. C-02 gives the Director the stock line. Confirm that the briefing reached the Director and not the floor.
    - **The A-29 redactions and the placeholders [placeholder names RULED — confirmed by the author].** Three redaction reasons (R1 older designations, R2 source, R3 a third party), a cover note, and the point that the sheet was clean when read. Ruth Calloway (E-03471), Chidi Obi (E-03702), Lior Ben-David (E-03615) and Ms. Adeyemi stand.
    - **Doc 2.29 cross-reference.** The glossary does not mention the Manager's manual or the Day 4 stock line. They do not now, because PTKW can read them. Say if a pointer is wanted.
    - **Dates.** C-26 is Cycle 292 Q2, Day 4 (messages at 14:20, 17:05 and 18:10, the Manager's note in Cycle 293 Q1). A-28 is Day 4, 19:12 to 19:40. B-27 is Day 5, 08:55 and 09:42. B-28 is Day 5, 10:05 to Day 6, 07:31. A-29 is Day 31, 21:05 to 21:38, redacted on Day 33, 11:20. `design/TIME_MODEL.md` has rows for all but C-26, which has an off-timeline note.
    - **Files.** C-26, A-28, B-27, B-28 and A-29 are listed in `README.md` and the `canon/internal-communications/README.md` tree, and each ends with a `[PROPOSAL]` note that separates the author's content from mine. Edited alongside: C-25, B-26, and the two earlier rulings.
    - **Open after this session, in one place:** (1) accept or change the proposed leak answer; (2) does EOD know the Manager kept the page; (3) does the Division pursue the breach of keeping the page and of the forward; (4) does Earth's Day 4 beat need a line explaining why the smile instruction was not given for this Branch; (5) is the rude PTKW reply at the right pitch; (6) did the Doc 2.29 briefing reach the Director and not the floor; (7) is a Doc 2.29 pointer wanted; (8) should B-26 reach the Manager and the Research Team, and does it change the Day 38 plan (ruling 27).

29. **Hearth, the internal messaging system [PROPOSAL].** `design/HEARTH.md` (spec) and a generated viewer (originally in the writing-map folder; now part of ICS-OS, see ruling 31), called by every `build_map.py` run. The author asked for a UI for the internal communications in the lineage of the *Prey* email system and the *Fallout* terminal, with the system named and documented, in the ICS style, showing all emails and drafts, and kept current by the writing map. Everything below the author's brief is mine. Rule on each:
    - **The name.** Hearth (a place people gather, and where things are burned). Alternatives: Concord, Courier, Tether. One constant in `build_mail.py` plus `design/HEARTH.md`.
    - **Public and PTKW names.** Public: Hearth. PTKW: Hearth with the CCN filter behind it (Doc 2.21). Confirm, or give the CCN its own name in the interface.
    - **Style.** Deep Blue `#1A2E52`, Warm Gold `#C9A84C` (Doc 2.32), warm beige paper (`story/STORY.md`), rounded type, the circle and the hook-shaped arc, the tagline on the welcome screen.
    - **Folders.** Delivered, Drafts and unsent, Held by CCN, Sealed, Found notes, read from each file's Status line. At last build: 58, 12, 11, 8, 4 (93 messages). A message with a `[PROPOSAL]` tag shows a Proposal chip; Writer's notes (the closing `[PROPOSAL]` note and the `→ See:` list) are hidden by default.
    - **Threads.** One file is one message in the viewer; thread files (C-26, B-28, A-28 and seven others) open as one entry. Splitting them into separate emails needs the `**[MESSAGE n]**` convention in ten files. Do you want it?
    - **The viewer shows everything.** It is the author's master view and shows sealed, PTKW and Board-level material. The in-game screen is a separate decision: which folders each tier sees, whether a held message ever reaches the player, whether a draft appears only if the player finds the terminal where it was left.
    - **A-29 header.** A-29 had no From/To/Subject/Date header, so the map and Hearth saw no sender or date. I added the standard header lines (the map now lists Ruth Calloway, so people went from 78 to 79). Nothing else in the file changed.
    - **Doc 2.29 entry** for Hearth: not added, because PTKW can read the glossary. Say if wanted.
    - **Files.** `design/HEARTH.md` is listed in `README.md`; the README in the writing-map folder has a Hearth section.

30. **Hearth sign-in, clearance and themes [PROPOSAL].** Requested by the author: a sign-in page offering all emails, all access, Branch Director, PTKW employee and standard employee, more filters at my discretion, and a theme. Built in `build_mail.py` (`access()`, `mailboxes()`) and `build_os.py` (`ROLES`), in the ICS-OS folder since ruling 31; specified in `design/HEARTH.md` section 7. The sign-in is a view, not a lock; the page still holds every message. The role rules are inferred from the Status line, the series and the address lines. Rule on each:
    - **Roles.** Standard employee (16 of 93 messages), PTKW employee (61), Branch Director (83), EOD Research Team (21), Design Team (25), All access (93), All emails (93, with Writer's notes, Proposal chips and file paths). The last four go beyond the five you named. Keep them, or cut to your five plus All access?
    - **Branch Director and the PTKW channel.** The Director sees series B except B-02 and B-25 (marked "above Branch Director clearance"), and does not see the four Board-access files (C-18 to C-20, C-22). The Director sees the sealed files that name the Earth Branch Manager (C-21, C-23, C-24, C-25). Right?
    - **Held staff mail.** Held, draft and found staff mail is PTKW tier, since the CCN hands flagged messages to PTKW (Doc 2.21). The Director sees it too. Should the Director?
    - **Research Team.** Sees C-26, C-21, C-23, C-24, C-25 and open mail. Not the Board files. Confirm.
    - **Standard employee sees only 16 messages.** Delivered staff mail and the B-16 Global Access notice. Is that the floor's whole world?
    - **Mailboxes.** A role can narrow to one office, one asset number or one PTKW desk. Many senders have no asset number, so they match by office only.
    - **Themes.** Standard: Deep Blue and Warm Gold on beige (Doc 2.32). PTKW: cool slate (Levels 5, 8, 9). Director: formal navy and ivory. Research: laboratory green. Design: plum and copper. All access: dark midnight. All emails: graphite. Change any of them freely; each is a block of CSS variables.
    - **Files.** `design/HEARTH.md` has the tier and theme tables and open rulings 7 to 10.

31. **ICS-OS version 0.1: operating system, Cloud Drive, Folio, and the Director's retained copies [PROPOSAL].** Requested by the author: move the whole system into its own folder as an operating system in the lineage of *Her Story*, *Orwell*, *Hypnospace Outlaw* and *Kingsway*, with a boot (ICS logo, loading), a sign-in, a home screen with the logo as wallpaper, Hearth as a windowed app, an ICS cloud file explorer with no local save, an app to open the files, and the Branch Director's access to Staff and PTKW mail made to look wrong. Built in the top-level ICS-OS folder (`build_os.py`, `build_mail.py`, `os_template.html`, `os.css`, `os.js`, generated `ics-os.html`); specified in `design/ICS_OS.md`; called by every `build_map.py` run. Hearth moved there from the writing-map folder and Hearth's own page no longer exists. Rule on each:
    - **Names.** ICS-OS, ICS Cloud Drive, Folio. Alternatives welcome; they are constants in `build_os.py`.
    - **The Director's weirdness.** Staff and PTKW mail appears to the Director as a *retained copy*: a banner (*You were not an addressee*), a Route row through the CCN relay, an *Opened N times before today / Opened by: no record* row, a line that fades in after a few seconds (*Your open was recorded*), a status bar (*Requested: 0, Acknowledged: 0*) and a taskbar item (*CCN copy: on, set by no record*). Too much, too little, or right?
    - **Does the Director know?** The copy text says it was not requested. If the Director approved it, the lines change. Your call.
    - **Staff and PTKW see nothing** of the copies. Do they get a receipt?
    - **Documents by account.** Standard employee 19 of 50, PTKW 36, Branch Director 38, Research Team 37, Design Team 19, All access 48, All files 50. Whole-file tiers are read from each document's classification line; 2.35, 2.39, 2.42 and 2.49 sit outside the tiers. The Director reads no Board-tier document. Right?
    - **Layered documents.** Thirteen (2.24, 2.25, 2.29, 2.31, 2.32, 2.33, 2.34, 2.37, 2.40, 2.43, 2.45, 2.47, 2.48) show a redaction block in place of a section above the reader's tier. Read by pattern from the markers already in the files; no document was edited.
    - **Cloud only.** No save, download, copy, print or upload anywhere; Ctrl+S and Ctrl+P give a policy notice. The All files view may copy.
    - **Folders.** Seven drive folders of my own grouping. No document renumbered or moved.
    - **Look.** Retro window frames in ICS colours. Louder like *Hypnospace Outlaw*, or austere like *Orwell*? Mascots (Doc 2.31) left out.
    - **Files.** `design/ICS_OS.md` is listed in `README.md`; the README in the writing-map folder has an ICS-OS section; `design/HEARTH.md` points to it. Rulings 29 and 30 describe Hearth, which now runs inside ICS-OS.

32. **Jobs and career ladder [PROPOSAL].** Requested by the author: work out what the player's job is, whether there is more than one, and how the ladder pays. Written up in `design/JOBS_AND_CAREER.md`; nothing is built. Rule on each:
    - **Department choice.** Proposed: no. Kai's department is fixed (Vantage cover, Omar two desks away, Level 6 Soft Ceiling logic, Tutorial Beat 2). The player instead has a *posture* inside the job, inferred from what they flag. Agree?
    - **What a flag does.** Canon never says. Proposed: flags and report lines feed tier notices, Soft Ceiling logs and CCN referral lines (the Flag Ledger). Do early flags land on **named** characters (Hana, Omar, Tarek) or only on anonymous cases?
    - **Second jobs.** Proposed: each acquired badge (cleaner, PTKW, Director, stripped) is a second job, taken as fiction and never from a menu. No ninth verb. Keep?
    - **Two axes.** Tier (access, ICS decides) and Role (the badge in hand). The player cannot work toward promotion, only be promoted. Analyst and operations roles rise; HR, cleaning and night-shift roles tend to stay at Tier 3. Right?
    - **Pay besides access.** Larger Performance Allocation, Personal Space Upgrade slots, Peer Recognition, Earth Products access, a salary line credited to Earth, and more EIMU sensitivity. All are traps in the Mosaic Dependency sense, none is farmable, none gates a story tool, none announces itself. Too much, too little, or right?
    - **Glossary mismatch.** Doc 2.29 (Tier System term) describes four tiers with Tier 1 as the starting rung. That contradicts ruling 17. Not edited; fix the glossary?
    - **Files.** `design/JOBS_AND_CAREER.md` is listed in `README.md`.

---

**Resolved by file evidence — no author decision needed:**

1. **Tier 1 badge in the Opening Sequence.** Resolved by ruling 17. The Day-1 memory uses a **Tier 3** badge (new arrivals start at Tier 3, Doc 2.20). Fixed in `story/scene-notes/Opening Sequence.md`.
3. **Stairwell B arrival.** Resolved: Day 15 at 23:00 (`story/STORY.md`). Fixed in `story/scene-notes/Stairwell B.md`.
4. **Phase 2/3 overlap.** Resolved: EOD active Days 4–10, Phase 3 Days 11–20. Consistent with `design/TIME_MODEL.md` §1.3.
6. **Branch Director badge timing.** Resolved: she left it after the Phase 5 address (Day 22 morning speech). Fixed in `design/PROGRESSION.md` and `design/GATING_BACKTRACKING.md`.
7. **Gates for Level 6→7 and Levels 8–10.** Resolved: Level 6→7 = Tier 1. Levels 8–10 = PTKW-Clearance badge. Fixed in `design/GATING_BACKTRACKING.md` and `design/LEVEL_BEAT_SHEETS.md`.
8. **CRD-7 source.** Resolved: Level 5 security storage locker, Phase 2 (matching the CRD-7 file). Fixed in `design/INVENTORY.md`.
9. **"Medical Bay" or "Medical Centre".** Resolved: Medical Centre. (Was already fixed.)
15. **"The Board's one direct communication."** Resolved: no conflict exists when each source is read in its own frame. Doc 2.24's "only direct communication in the *public-facing archive*" means the Cycle 200 statement; Doc 2.42 is addressed to whoever finds it, not an archived document; "Model the ending" in Doc 2.38 is an instruction through the review channel. None of these contradict. No file changes needed.
16. **Labor Source #038's status.** Resolved: #038 was at Stage 3 (67% hire rate) when EOD deployed, and the Branch closed Cycle 201. The "currently in Stage 3" in Doc 2.25 was past-tense within the case study frame. Fixed in `canon/documents/2.25`.
17. **Tier direction.** Resolved: **Tier 3 = new arrivals, Tier 1 = senior staff**, consistent with Docs 2.20, 2.21, 2.08, 2.33. Fixed in `design/PROGRESSION.md`, `design/UI_MENUS.md`, `design/GATING_BACKTRACKING.md`, `canon/facility/Level 7.md`, `canon/facility/Level 5.md`, `canon/facility/Level 6.md`, `canon/facility/Level 2.md`, `canon/facility/Overview.md`, `canon/facility/Levels 8-10.md`, `design/LEVEL_BEAT_SHEETS.md`, `canon/documents/2.33`, `canon/documents/2.36`, `canon/documents/2.40`, `canon/documents/2.46`, `canon/characters/E-04421`, `story/scene-notes/Opening Sequence.md`.
18. **Supervisor M.** Resolved: M = **E-00088**, female, Tier 1, transitioned Cycle 291. Source: Doc 2.25, Case File 4 (PTKW annotation). Fixed in `A-04` (gender, cycle, James's tenure) and `A-15` (E number).
19. **Marcus's tier.** Resolved: **Tier 2** (his character file, design/DESIGN.md, Doc 2.24, Doc 2.40 — all consistent). Doc 2.37 annotation said "Tier 3" because the ad was filmed when Marcus had only recently arrived. Added parenthetical to Doc 2.37 to clarify.
20. **Player tenure.** Resolved: **3 cycles** (one cycle = one year; Cycle 297–300 = 3 years). Fixed in `design/DESIGN.md` and `canon/characters/E-05682`.
21. **Labor Source numbering.** Resolved: reworded Doc 2.22 to say "order of portfolio registration" rather than "order of first contact", which resolves the #071/#094 sequence without touching any dates.
22. **Vantage transmission count.** Resolved: **47 transmissions**, roughly monthly cadence. Fixed in `design/DESIGN.md` and `canon/characters/Narrative Arc`.
23. **James's flag history.** Resolved: **2 low-severity flags** (Doc 2.25, the PTKW-level source). B-13 is not a found file in the repository; "no prior flags" was a reference to a non-existent or lost document. Doc 2.25 governs.
24. **Previous Branch Director's dates.** Resolved: appointed Cycle 288, on-site through construction, Branch opened Cycle 290. Early entries (288–289) are pre-opening notes. Fixed in `story/STORY.md`.

**Checked and found consistent (don't re-audit):** the E-number table (E-05682 Kai Osei, E-01573 Yusra); the voice count (eleven); four vitals; eight verbs; level titles for Levels 0 to 14; the 31,000 population; 2,400 transitions; "eleven cycles" at Branch and Stage 2 duration; the Cycle 299 deployment authorisation; the EOD timeline (Days 4 to 10, then 11 to 20, then Day 21). E-00882 "works on Level 3" and "Operations Division" fit together, because Level 3 files say Operations employees work those floors. Doc 2.14's "Phase 3, Days 61+" is the generic planetary protocol, not the game's Phase 3. A stale "End of Document 2.40" label at the end of Doc 2.41 was fixed.




---

*Good luck with it. The game deserves to be finished.*

---

*→ See: [`README.md`](../README.md) · [`design/LEVEL_BEAT_SHEETS.md`](../design/LEVEL_BEAT_SHEETS.md) · [`design/TIME_MODEL.md`](../design/TIME_MODEL.md) · [`design/GATING_BACKTRACKING.md`](../design/GATING_BACKTRACKING.md) · [`design/PLAYER_GUIDANCE.md`](../design/PLAYER_GUIDANCE.md) · [`design/PROGRESSION.md`](../design/PROGRESSION.md)*
