# Todo

*Working list. Items from the author's brainstorm (pasted 2026-11-06) are marked **[brainstorm]**. Anything that adds canon is a [PROPOSAL] until the author rules. Check boxes: `[x]` done, `[ ]` open.*

## A. Already in the repo (from the brainstorm)

- [x] **Incident report: "Subjugator" heard, document found at the asset's position, scan attached.** `canon/internal-communications/ptkw/B-26` (E-03615, Day 32). The pasted text is in it.
- [x] **K-7 character profile** (PTKW team leader). `canon/characters/K-7 - PTKW Monitoring and Analysis Team Leader.md`.
- [x] **Email system named and documented.** Hearth (`design/HEARTH.md`) and ICS-OS (`design/ICS_OS.md`), seven accounts, ICS styling. Prey, Fallout and Shipbreaker are in `meta/HANDOFF_CARTOGRAPHER.md` Section E (unverified).
- [x] **Jobs and career ladder, more than one job.** `design/JOBS_AND_CAREER.md` ([PROPOSAL], parked).
- [x] **The true meaning of "ICS".** Docs 2.02 (PTKW reading) and 2.50 (Board reading).

## B. Writing, done 2026-11-06 **[brainstorm]**

*All eight written as [PROPOSAL]; the author's rulings remain. B1: B-29. B2: B-30 (Level 3 corridor). B3: Docs 2.21, 2.22, 2.23, 2.29. B4: D-01 now names invented companies (Halden Ridge Group, Orrin Systems, Fennick & Dole). B5: `story/trailers/Trailer 6 - The File.md`, **the name field is waiting for the author**. B6: `.ics` scheme, `tools/add_addresses.py`, applied to 92 files. B7 and B8: `design/DEVICES.md`.*

- [x] **B1. Investigation result for B-26.** The form promises file `ICS-IR3-300Q4-032 "to follow"`. Write the follow-up (the seven-part scope: the object, the scan queues, the hands, the asset's access path, other copies, the Protocol 7 list, PTKW exposure). Needs an author ruling on where the page came from: the handoff has a proposed answer in ruling 27; confirm or replace.
- [x] **B2. Graffiti incident report.** Not written anywhere. A second ICS-IR3 (or sibling form) for graffiti on the Earth Branch reading **Inflatable Crowd Solutions**, with an investigation into who wrote it and how they knew. Notes before drafting:
  - It must differ from B-26: B-26 is one asset and one desk, so this one is a *public wall that many people saw*. Decide the location (candidates: Stairwell B or C, a Level 4 corridor, a maintenance door) and who first reports it (a cleaner is the natural witness).
  - It must not repeat what B-26 already shows (the "how did he get a classified page" question). The new question is *how many people read it before it was removed*.
  - Canon check: the PTKW reading is in Doc 2.02, the Board reading in Doc 2.50. Ordinary staff should not know the words. Doc 2.50 says the Board's own designation has no written form.
  - The Level 2 restroom pencil line (`canon/facility/Level 2.md`) is deliberately *not* graffiti. Keep them separate.
  - Keep the [PROPOSAL] tag and cite sources in the header.
- [x] **B3. Mention the real name "Inflatable Crowd Solutions" in other classified files.** Today only 2.02, 2.50, README and the handoff use it. The brainstorm asks for more references in files whose classification already allows it. Plan: list every document and message with a PTKW or Board access line (Docs 2.14, 2.15, 2.16, 2.21, 2.22, 2.23, 2.29 and the C and B series are candidates), add one short in-voice mention per file where it fits, and log each in `meta/CANON_DECISIONS.md`. Respect the access rule: a mention appears only where the *reader* is cleared for it. Needs author approval before editing canon files.
- [x] **B4. Remove the real companies from Design Team D-01** (`canon/internal-communications/design-team/01 — Akar — Design Philosophy.md`). The brainstorm asked for this at "d01". It still names Apple (and Norman Foster), Google and Zappos, and quotes Tony Hsieh. Replace with invented or generic companies. This also clears the Handoff Rule C problem of attributing a quotation to a real person. Check the other design-team files and `reference/` snapshot for the same names, and check what the other documents cite D-01.
- [x] **B5. EOD trailer ending.** The brainstorm wants a trailer that plays as a normal trailer, and at the very end a **sound of a computer file opening**, then the EOD file shown, giving his real name. Trailer 5 (`story/trailers/Trailer 5 - The Envoy.md`) already has the three-tier reveal, but it ends on a redacted name field and the line "The Board does not have complete records of what EOD was before he was this." Rulings needed:
  - Is this a new trailer or a new final beat for Trailer 5?
  - "His real name" = the full designation *Executioner of Despair* (already revealed mid-trailer), or a human name (which contradicts the redaction and the "no complete records" line)?
  - Does the file-opening sound belong to Hearth/ICS-OS (a Folio-style viewer) so the trailer teaches the player the interface?
- [x] **B6. Email address scheme** (e.g. a department mailbox like the brainstorm's `icsresearch@ics.org`). No file uses `@` addresses; Hearth addresses are asset numbers (E-xxxxx, K-7). Decide: department mailboxes (research, HR, PTKW, Director, Broadcast, Facilities), in-world domain, and who may write to whom. **Do not use a real domain** such as ics.org; pick an invented one (for example `ics.branch` or `ics.349`) and ask the author. Then add the addresses to From/To lines across series A–D in one scripted pass.
- [x] **B7. Record the Branch Manager terminal password, "smiling-man"** [PROPOSAL]. It fits the thread (the Manager's old friend smiles, K-7 "would rather he had smiled"). K-7's workstation password is still open (K-7 file, open ruling 4). Add both to the relevant character files and decide where the note with the password is found.
- [x] **B8. Which computers hold which messages.** The brainstorm wants emails scattered across the game, with only a few devices (PTKW team leader K-7, the Earth Branch Manager) holding many. `design/ICS_OS.md` gives seven *accounts*, not a *device map*. Write a table: device, location (level and room), account, number and series of messages, how it is unlocked (password note, badge tier). Start with the four test devices: Manager, K-7, a Level 3 work-floor desk, the Director.

## C. Game build **[brainstorm]**

*Unity test build made and verified in batchmode on 2026-11-06, then **deleted** at the author's request to focus on writing and modelling. Mail export still works: `tools/export_mail.py <output path>`.*

The Godot project was deleted and this repo holds writing only. The brainstorm names **both Godot and Unity** for the same test: a playable 3D character, an office for the Branch Manager (desk, chair you can sit on, a device with a screen, password on a note: "smiling-man"), and a test room with several computers at different access levels.

- [x] **C1. Choose the engine** (Godot or Unity) and where the game repo lives (separate from this one).
- [x] **C2. Branch Manager office vertical slice:** walk, sit, use the terminal, enter "smiling-man", read mail. Tests the Hearth/ICS-OS design against a real screen.
- [x] **C3. Multi-computer test room** using the device map from B8.
- [x] **C4. Rebuild the mail viewer** from the canon files. The builder now lives in the separate `ICS-OS` repo (2026-11-08). See D1.

## D. Carried over (earlier lists)

- [x] **D1. Remake the writing map.** Recovered into the `ICS-OS` repo as `writing-map/` and ported to this layout (2026-11-08). It is manual (no hook here), so the writing repo stays writing only.
- [ ] **D2. Repo description and licence** (deferred).
- [ ] **D3. Stale paths in `meta/HANDOFF_CARTOGRAPHER.md`** body (`writing/`, old baseline counts; the `writing-map/` and `ICS-OS/` folders now live in the ICS-OS repo).
- [ ] **D4. Rulings 1–11 in `meta/CANON_DECISIONS.md`**, plus Omar's tenure (3 vs 5 years), the Wellness Hub level, and whether Kai's quarters terminal can send anything.
- [ ] **D5. Verify real-world claims** (Doc 2.18 Milgram, Doc 2.38 Perimeter, Barrett 2000, handoff Section E) once web tools work (`/login`).
- [ ] **D6. Push approval** for the local commits (`ce482f3`, `6ddee4c`) and later work. Not given.
- [ ] **D7. Voice check** on scenes 1.1–1.13: tell me the first line that sounds wrong.
