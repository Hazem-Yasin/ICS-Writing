# ICS: Interplanetary Corporate Solutions

## ICS-OS (version 0.1) — the ICS Earth Branch Operating System

*The in-world operating system of the Earth Branch personal device and terminals, and the working page that shows it. ICS-OS boots, signs the player in, and opens a desktop with three apps: Hearth (internal messages), ICS Cloud Drive (a file manager) and Folio (a document viewer). It is built from the files in `canon/internal-communications/` and `canon/documents/` and rebuilt by every map run. **[PROPOSAL]** The names, the look, the clearance rules and the Director's treatment are mine, pending the author's approval. The author's brief is in section 1.*

---

### 1. The brief

The author asked for: an operating system in the lineage of *Her Story*, *Orwell*, *Hypnospace Outlaw* and *Kingsway*; a boot with the ICS logo and a loading screen; a sign-in; a home screen with the ICS logo as the background; Hearth as an app in a window, not a full page; a file explorer connected to an ICS cloud drive with **no option to save a file locally**, so files are always current; an app to open those files, like a word processor; the whole system moved to its own folder, version 0.1; and the Branch Director's access to Staff and PTKW mail made to look wrong.

Everything below that is mine.

### 2. Names **[PROPOSAL]**

| Surface | Name | Why |
|---|---|---|
| The system | **ICS-OS**, version 0.1 | The author's example. Nothing in the canon used it before. |
| The mail app | **Hearth** | Unchanged. See design/HEARTH.md. |
| The file manager | **ICS Cloud Drive** | Plain, as a corporate product would name it. |
| The document viewer | **Folio** | A folio is a sheet and a record. Nothing in the canon used the word as a name. |

Changing them is one block of constants at the top of build_os.py (`OS_NAME`, `CLOUD_NAME`, `DOCS_NAME`) plus this document.

### 3. In the fiction **[PROPOSAL]**

Doc 2.30 (section 1.4) puts every personal-device message through the ICS communications relay, and Doc 2.20 says the device is configured with the employee's access tier. ICS-OS is that configured device: the badge (Doc 2.46) is the access token, the tier decides what the desktop shows, and nothing is stored on the device. Documents live in **ICS Cloud** only. This fits the charter's rule that restricted paper is destroyed within 30 days (Doc 2.21): the device never holds a copy, so there is nothing to destroy, and every reader sees the current version.

For the player, this is the interface of a terminal or a personal device in the game. The look is the ICS look (Doc 2.32: Deep Blue, Warm Gold, round sans-serif, the circle-and-hook mark) in the shape of a 1990s desktop: framed windows with a title bar, a taskbar, a start button, a tray. The warmth is the brand's. The frame is the old machine's. That mismatch is deliberate and is the reference to *Hypnospace Outlaw* and *Kingsway*.

### 4. The sequence

1. **Boot.** The ICS mark on Deep Blue, the words ICS-OS, version 0.1, a loading bar, and a status line that changes through six steps: Starting ICS-OS 0.1, Reading badge, Connecting to ICS Cloud, Starting the CCN relay, Preparing your desktop, Ready. About four seconds. Any key or a click skips it after the first second.
2. **Sign-in.** One card per account (section 5). The mailbox picker narrows Hearth to one person, desk or office.
3. **Desktop.** The ICS mark as wallpaper with the tagline *Because You're Worth the Investment*. Three icons at the left: Hearth, ICS Cloud Drive, Folio. Double-click or Enter opens one.
4. **Taskbar.** The ICS start button (Hearth, ICS Cloud Drive, Folio, About ICS-OS, Sign out), one button per open window (click to raise, again to minimise), and a tray with the cloud status and the account.
5. **Windows.** Drag by the title bar, resize at the corner, minimise, maximise (or double-click the title bar), close. Hearth and ICS Cloud Drive open once; Folio opens one window per document. A narrow window changes layout (Hearth drops to two panes, then one).

The session is remembered for the browser session only. Sign out returns to the sign-in. A reload with a session held goes straight to the desktop.

### 5. Accounts and what they see **[PROPOSAL]**

The same seven accounts as Hearth, now governing mail and documents together. The sign-in is a view, not a lock.

| Account | Mail | Documents | Theme |
|---|---|---|---|
| Standard employee | 16 of 93 | 19 of 50 | Deep Blue and Warm Gold on beige |
| PTKW employee | 61 | 36 | Cool slate |
| Branch Director | 83 | 38 | Formal navy and ivory |
| EOD Research Team | 21 | 37 | Laboratory green |
| Design Team | 25 | 19 | Plum and copper |
| All access | 93 | 48 | Dark midnight |
| All files | 93 | 50 | Graphite. The author's view: Writer's notes, file paths, proposal chips, copying allowed. |

### 6. ICS Cloud Drive **[PROPOSAL]**

A file manager over the documents the signed-in account may open. A folder tree at the left, a sortable list (name, clearance, last synced, size), a path bar, search and a status bar that reads *Stored in ICS Cloud only*.

**The folders** are groupings I made so the drive is browsable. No document is moved; the numbering is unchanged.

| Folder | Documents |
|---|---|
| Recruitment and Public | 2.04, 2.05, 2.19, 2.24, 2.26 |
| Handbook and Forms | 2.03, 2.06, 2.07, 2.10, 2.20, 2.29, 2.30, 2.33 |
| Operations and Commerce | 2.01, 2.02, 2.08, 2.09, 2.11, 2.13, 2.28, 2.36, 2.40, 2.43, 2.45, 2.46 |
| Governance and Policy | 2.12, 2.14, 2.21, 2.22, 2.23, 2.38, 2.44, 2.50, 2.51 |
| Research and Assessment | 2.15, 2.16, 2.17, 2.18, 2.25, 2.27, 2.41, 2.47, 2.48, 2.49 |
| Brand and Communications | 2.31, 2.32, 2.34, 2.37 |
| Outside the ICS System | 2.35, 2.39, 2.42 |

A new document needs one line in the `DOCS` table in build_os.py (its tier and its folder). Until it has one it is left out of the drive; the build now prints a warning naming it. Documents 2.52 to 2.62 mark their sheets with `*[Access: X]*` lines instead of the older marker patterns, so they use a `LAYERS` entry of `{"access": True, "default": …}`. Their closing `*[PROPOSAL]*` note is not shown in the document; the All files view shows it as "Writer's notes". **[PROPOSAL]**

**No local save.** The drive has no Save, Save as, Download, Copy to this device, Print or Upload. Where a right-click menu would offer them, they are shown greyed out with the tip *Disabled by ICS Cloud policy*. Ctrl+S and Ctrl+P open a notice: *Files in ICS Cloud are kept in ICS Cloud only… so that every employee reads the current version.* Text in a document cannot be selected or copied, and the browser's print command prints a single line saying the file cannot be printed. (The All files view is exempt from the copy block, because it is the author's.) The *Last synced* time on every file is the file's modified time at the last build, so a document the author edits shows its new time on the next map run.

### 7. Folio **[PROPOSAL]**

A document viewer in a page-on-canvas layout: a toolbar (the sync status, disabled Save and Print, find in file with next and previous, Open), an outline of the headings at the left, and a white page at the centre with chips for the document number, its clearance, its drive folder and *Read only · ICS Cloud*. Cross-references to other documents ("Document 2.29") are links that open that document in Folio, subject to the same clearance. Message codes in Hearth open that message.

**Clearance, whole file.** Each document has a tier, read from its own classification line.

| Tier | Documents |
|---|---|
| All staff | 2.04, 2.05, 2.06, 2.07, 2.10, 2.19, 2.20, 2.24, 2.26, 2.29, 2.30, 2.31, 2.32, 2.33, 2.34, 2.36, 2.37, 2.40, 2.45 |
| PTKW | 2.01, 2.02, 2.03, 2.08, 2.09, 2.11, 2.12, 2.13, 2.18, 2.21, 2.25, 2.27, 2.28, 2.43, 2.46, 2.47, 2.48 |
| Branch Director | 2.22 (its own line: "PTKW access — Branch Director and above"), 2.51 |
| Board | 2.14, 2.15, 2.16, 2.17, 2.23, 2.38, 2.41, 2.44, 2.50 |
| Outside the tiers | 2.35 (not an ICS document), 2.39 (found by you), 2.42 (not from ICS), 2.49 (sealed) |

A tier reads itself and everything below it. The Branch Director never reads a Board-tier document; that is the whole point of the Board.

**Outside the tiers.** Doc 2.35 is the Director's own paper journal and appears only to All files. Doc 2.39 "does not exist in the ICS system" and likewise appears only to All files. Doc 2.42 says the three-tier system does not apply, so it appears to All access and All files. Doc 2.49 is sealed to the EOD Research Team, the Earth Branch Manager and EOD, so it appears to the Research Team, the Branch Director (standing in for the Manager) and the two archive views. PTKW are "not to be told that this file exists" and do not see it in the drive.

**Clearance, inside a file.** Thirteen documents are layered. Folio reads the marker lines already in the files and sorts each section into a tier. A reader below the tier sees a **redaction block** in place of the section: *Access restricted · PTKW clearance required · section withheld*, with black bars sized to the length of what is hidden. A reader at the tier sees the section with a gold bar and a *PTKW layer* or *Board layer* label. (The page file still holds the hidden text; see section 10.)

| Document | How the layers are read |
|---|---|
| 2.24 | Each PTKW ANNOTATION block |
| 2.25, 2.33, 2.34, 2.37 | The PTKW annotation or note block |
| 2.29 | Under each TERM: GLOBAL, PTKW, BOARD |
| 2.31 | Each Access marker (Global, PTKW, BOARD; one marker is PTKW, Branch Directors and above) |
| 2.32 | The PTKW ACCESS and BOARD ACCESS blocks |
| 2.40 | The PTKW Access Layer |
| 2.43 | GLOBAL ACCESS, PTKW ACCESS and BOARD ACCESS |
| 2.45 | The PTKW and BOARD markers |
| 2.47, 2.48 | The BOARD ADDENDUM sheet (to the next rule) |

Layers are read by pattern. If a document changes the wording of its marker lines, the layer will not be found and the section will show to everyone at the file's tier. A new layered document needs a pattern in `LAYERS` in build_os.py.

### 8. The Branch Director and the retained copies **[PROPOSAL]**

The Director has "full operational visibility" (Doc 2.21, section 3), and PTKW "report directly to the Branch Director on PTKW matters". The Director can therefore read PTKW mail without anyone being wrong. What the Director cannot be told is that the **staff** mail is read as well, and that the **PTKW** mail they were never sent is copied to them. The author asked that this look weird. It should be the kind of weird that a competent system produces without meaning to.

In Hearth, signed in as the Branch Director:

- **Folder.** *Retained copies* (56), listed in the folder pane. Each such message carries a dashed grey margin and a chip, *Retained copy*, whose icon is the mark mirrored.
- **Banner on the message.** A hatched box with a mirrored stamp, COPY, and the text: *Retained copy. You were not an addressee. The sender and the recipients were not told that this copy exists. It reached the Office of the Branch Director by CCN relay and was not requested.*
- **Two extra header rows.** *Route:* Sender → CCN relay → addressees. Copy → Office of the Branch Director. *This copy:* Opened N times before today. Opened by: no record. (N is 1 to 6, fixed per message so a rebuild does not change it.)
- **A line that appears late.** Three and a half seconds after a message opens, *Your open was recorded.* fades in.
- **The status bar.** *56 retained copies · Requested: 0 · Acknowledged: 0.*
- **The taskbar.** *CCN copy: on.* Clicking it says the copy to the Office of the Branch Director is on, set by *no record*, and not managed from this account.

Nothing is announced and nothing is hostile. Every line is a field a log would have. The reader supplies the horror: someone opened the Director's copies before the Director did, and no one asked for them. This matches the house tone, horror through precision.

It also leaves the author's question open: does the Director know. See open ruling 3.

Other accounts see none of this. Staff and PTKW do not know the copies exist.

### 9. How it is built

**Where it lives (2026-11-08 [PROPOSAL]).** ICS-OS is its own repository, `Hazem-Yasin/ICS-OS`, a sibling folder of this repo and not a folder inside it. It is linked to Vercel (project "ics.os"). It no longer needs the writing map or any database.

```
canon/documents/2.*.md                  (documents: the only source)
canon/internal-communications/**/*.md   (messages: the only source)
        │
        ▼
python build_os.py                        (run in the ICS-OS repo; reads this repo
        │                                  directly, ../ICS-Writing or $ICS_WRITING)
        ▼
ics-os.html                               (one offline page; open it in a browser)
```

The page is assembled from os_template.html, os.css and os.js, which build_os.py inlines. Edit those, never the generated page.

- **Manual only.** Rebuild with `python build_os.py` in the ICS-OS repo after the writing changes, then commit and push there. `tools/ics.py build` in this repo does not rebuild it. The old writing map (graph, timeline, canon rules, history) was recovered into the same repo as `writing-map/`; `python writing-map/build_map.py` rebuilds it and the OS together.
- **Python standard library only.** No database. Build 2026-11-08: 119 messages, 62 documents.
- **Checked.** The page was run in a headless browser for six accounts: boot, sign-in, desktop, opening each app, window minimise, maximise and close, the drive listing the right number of documents per account, the clearance gate on a Board document, the redaction blocks in the glossary (42 for a standard employee, 21 for PTKW, none for All access), Ctrl+S refused, and sign-out.

### 10. Limits **[PROPOSAL]**

- **It is a viewer, not a game build.** The in-game version is the game's to make. This is the reference for how it looks and what it shows.
- **Sign-in is a view, not a lock.** The page holds every message and every document, including the sections a reader sees as a redaction block. Anyone can open the page source.
- **No write path.** No app creates, edits or deletes a file. There is no Notes app, no Settings, no Trash. The brief asked for three apps.
- **Folder groupings are mine.** The author's documents are numbered, not filed.
- **The layered documents are read by pattern** (section 7). The thirteen are listed; a fourteenth is not found by itself.
- **Documents are shown as the map renders them.** Tables, quotes and lists render; images do not exist in the source.
- **One person, one machine.** No other users, no live Cloud, no real "last opened by".

### 11. Open rulings **[PROPOSAL]**

1. **Names.** ICS-OS, ICS Cloud Drive and Folio, or others?
2. **Staff and PTKW mail on the Director's machine.** I kept the Director able to read all Staff and PTKW mail except B-02 and B-25, as Hearth already did, and made it strange. Is that the right amount of strange?
3. **Does the Director know?** The retained-copy treatment says the copies were "not requested" and "set by no record". If the Director knows and approved it, the lines should say so. If the Director does not know, the player is the first to notice. Which?
4. **Do Staff and PTKW see anything?** At present nothing. Option: a faint "CCN: delivered" footer on sent mail that the player can read as the copy receipt.
5. **Which documents does a Director read?** I let the Director read every document marked PTKW or Branch Director, and none marked Board, plus the sealed file 2.49 (standing in for the Manager). Right?
6. **Does a staff account see a Cloud Drive at all?** I gave it 19 documents. Another option is a drive with only handbook items, or none.
7. **Doc 2.35 and Doc 2.39** (the Director's journal and Yusra's document) appear only to All files, because they are not ICS documents. Should the Director's own journal appear on the Director's drive?
8. **Hearth's open rulings** (the name, PTKW naming, thread splitting, the in-game version) are unchanged. See design/HEARTH.md.
9. **The look.** Retro window frames in ICS colours. Closer to the tone of *Hypnospace Outlaw* (louder, more themes, a mascot), or more austere, like *Orwell* or *Her Story*?
10. **Mascots.** AIDEN, SOL, CLEO and VELO (Doc 2.31) could appear as a boot greeter or a help window. I left them out.

---

*Everything above that is not in the brief in section 1 is a proposal. The author's content is the brief, the canon documents and the messages; the operating system around them is mine.*

*→ See: design/HEARTH.md — Hearth, now the mail app inside ICS-OS.*
*→ See: the ICS-OS repo - build_os.py, build_mail.py, os_template.html, os.css and os.js.*
*→ See: the README in the ICS-OS repo's writing-map folder - the map and the watcher.*
*→ See: Document 2.32 (Brand Identity — The Logo) — the colours, the mark and the tagline.*
*→ See: Document 2.21 (Organizational Charter) — the Director's visibility, the CCN and the 30-day rule.*
*→ See: Document 2.30 (Workplace Conduct and Facility Use Policy) — all personal-device communications pass through the relay.*
*→ See: Document 2.46 (Employee Badge Technical Specification) — the badge as access token.*
*→ See: Document 2.29 (Acronym and Terminology Glossary) — the three versions of one document.*
