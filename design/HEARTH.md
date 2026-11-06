# ICS — Rigged Sphere

## Hearth — the ICS Earth Branch Internal Messaging System

*The in-world name, the design and the build notes for the messaging viewer. Hearth is both a piece of the game's fiction (the system the staff and PTKW read their messages on) and a working tool that shows every message in `canon/internal-communications/`. Since ICS-OS version 0.1 it is an app that opens in a window on the ICS-OS desktop, beside the ICS Cloud Drive and Folio; the operating system is specified in design/ICS_OS.md. **[PROPOSAL]** The name, the design and the style are mine, pending the author's approval.*

---

### 1. The name

**Hearth.** **[PROPOSAL]**

The name follows the Doc 2.32 and Doc 2.20 rule that every ICS surface sounds like a place you step toward. A hearth is where people gather and are warm. It also has a second reading, which is the one ICS cares about: it is the place where things are burned. The Board reading of the name is "everything that is said here is kept". Nothing in the canon already uses the word, so it does not collide with canon.

- **Public name (Global Access):** Hearth, "your Branch's home for messages".
- **PTKW name:** Hearth, with the CCN (Care & Connection Network) filter behind it. PTKW read it as the inbox of the intercept (Doc 2.21: CCN filters every message before delivery, and Protocol 7 holds flagged ones indefinitely).
- **Tagline on the welcome screen:** *Because you're worth the investment.* (Doc 2.32's tagline, unchanged.)

Alternatives if you do not like it: **Concord**, **Courier**, **Tether**. Changing it is one constant (SYSTEM_NAME in build_mail.py, in the ICS-OS folder) plus this document.

### 2. What it is, in the fiction **[PROPOSAL]**

Hearth is the Branch's internal messaging system. Every ICS person on the Earth Branch has a Hearth address that is their asset number (E-xxxxx), and the alien staff and PTKW officers use their own codes (K-7, TOR-9, VAH-3). It carries four things that the game files already show:

| In the game | What Hearth does with it |
|---|---|
| Staff messages (series A) | Delivered after the CCN filter. A message can be **held** (Protocol 7) and never arrive. |
| PTKW traffic (series B) | Internal, not visible to standard staff. Includes intercepts forwarded from the CCN. |
| Branch Director and HQ (series C) | Restricted. Some folders are **sealed** to named readers (C-24, C-25). |
| Design Team (series D) | The pre-opening archive, Cycles 287 to 299. |
| Drafts | A message the sender never sent. Hearth keeps the draft. This is why the unsent letters in `employee/` exist at all. |

The floor does not see this view. The viewer in `writing-map/` opens on a sign-in screen (section 7). Signed in as **All emails** it is the **author's master view**: it shows all of it at once, including what no single character could see. The in-game UI would show only the tier the player has reached. That is a later decision (see open rulings).

### 3. The look **[PROPOSAL]**

The style is taken from Doc 2.32 (the Earth Branch brand) and from `story/STORY.md` (the beige paper of the Transit Waiver):

| Element | Value | Source |
|---|---|---|
| Header and selection | ICS Deep Blue `#1A2E52` | Doc 2.32 |
| Accent and links | ICS Warm Gold `#C9A84C` | Doc 2.32 |
| Page | warm beige paper `#F4EEE1` | `story/STORY.md`, the Transit Waiver |
| Mark | the circle and the arc, drawn as the hook | Doc 2.32 |
| Lettering | rounded sans-serif only; no sharp angles | Doc 2.32 typography |
| Tagline | *Because You're Worth the Investment.* | Doc 2.32 |

The Warm Gold arc is drawn as a hook on purpose: the PTKW addendum to Doc 2.32 calls it a fishhook, and the staff are told the resemblance is coincidental.

**Layout.** Three panes: folders and channels on the left, the message list in the middle, the reading pane on the right. It is the plain mail layout that the staff already know, because ICS does not make a new interface when an old one works.

**Models, and what was taken from each.** The references below come from the handoff's lineage (*Prey*, the immersive-sim section) and from the terminal tradition of *Fallout*. I did not open any of the games' files; the notes are about the pattern, not copied from any design.

| Reference | What the pattern gives | What Hearth does with it |
|---|---|---|
| *Prey* (Arkane) | Company email and logs as the main way the world is told; corporate branding that "permeates the workplace" (the handoff cites the *Offices Construction and Design Manual*) | Branded header on every screen; the messages are the story |
| *Fallout* terminals | Messages with a header block, then plain text; reading in order | From / To / Date header block, body in plain paragraphs |
| *System Shock* and *BioShock* audio logs | A voice that is not the player's | Each series keeps its own voice (staff, PTKW, Director, Design) |

### 4. Folders and states **[PROPOSAL]**

The viewer sorts each message into one folder by reading its **Status** line.

| Folder | Rule (from the file's Status or name) | Count at last build |
|---|---|---|
| Delivered | `SENT`, `CCN SENT`, `PTKW INTERNAL`, `BRANCH DIRECTOR`, `RECEIVED` and the rest | 58 |
| Drafts and unsent | `DRAFT`, `UNSENT`, `NOT SENT`, `NEVER SENT`, or "(unsent)" in the file name | 12 |
| Held by CCN | `INTERCEPTED`, an "Intercept Thread" file, or a "Redacted by" header | 11 |
| Sealed | `SEALED` or `BOARD ACCESS` | 8 |
| Found notes | `NOT A MESSAGE` | 4 |

Each message also carries a **Proposal** chip when its file carries a `[PROPOSAL]` tag, so the author can see at a glance which messages are mine and which are not.

**Writer's notes** (a switch in the top bar) shows the closing `[PROPOSAL]` note and the `→ See:` list at the foot of the message. They are hidden by default so the message reads as the character would have read it.

### 5. What it reads, and how it stays current

Hearth is a generated file. It is never edited by hand.

```
canon/internal-communications/**/*.md   (the messages: the only source)
        │
        ▼
python writing-map/build_map.py          (rebuilds writing_map.db, then calls ↓)
        │
        ▼
ICS-OS/build_os.py  →  build_mail.py     (reads messages and msg_dates from the DB,
        │                                 re-reads each file for headers and body)
        ▼
ICS-OS/ics-os.html                       (one offline page; open it in a browser)
```

- **Automatic.** `build_map.py` calls build_os.py at the end of every run, so the git hook (`install_hook.py`), the watcher (`watch.py`) and the VS Code tasks described in the writing-map folder's README keep Hearth current. Tick **Auto-reload** in the Hearth window to follow the watcher (All files view only).
- **Manual.** `python ICS-OS/build_os.py` rebuilds ICS-OS, Hearth included.
- **A new message appears by itself** when its file is in `canon/internal-communications/` and has the house header (From, To, Subject, Date, Status). A new series letter needs one line in build_mail.py (SERIES).
- **If the build fails,** the map still builds, and `build_map.py` prints a warning.

**What the file header drives:**

| Hearth shows | From |
|---|---|
| Sender, recipient, subject | `From`, `To`, `Subject` lines, as parsed by the map |
| Date and story-time sort | `Date` or `Timestamp`, as parsed by the map (Cycle, Quarter, Day, clock). Messages with no date go to the end under "Undated". |
| The coloured strip above the body | `Status` line |
| Connected messages | every other message code (`A-24`, `C-26`) that the file cites, and every file that cites it |
| Writer's notes | everything after the last `---`: the `[PROPOSAL]` note and the `→ See:` lines |

### 6. How to use it

| Key or control | Does |
|---|---|
| Folders, Channels | Filter by state, and by series (Staff, PTKW, Branch Director and HQ, Design Team) |
| Search box (or `/`) | Searches subject, sender, recipient and the whole body of every message |
| `j` and `k` | Next and previous message in the current list |
| Sort | **Story time** (Cycle, Quarter, Day, clock) or **Message code** |
| Blue links in a message | Open the message they name (`B-28` and so on) |
| Connected messages | The other messages that cite this one, and the ones it cites |
| Writer's notes | Show or hide the `[PROPOSAL]` note and the cross-references |
| Print | Prints the open message on its own |

### 7. Sign-in, clearance and themes **[PROPOSAL]**

Hearth opens on a sign-in screen. The author asked for all emails, all access, Branch Director, PTKW employee and standard employee, with more filters at my discretion and a theme. Everything below is mine. The choice is held for the browser session only; **Switch role** in the top bar returns to the sign-in screen.

**Clearance tiers.** The builder (`access()` in build_mail.py) gives each message one tier, read from the Status line, the series and the From, To and Cc lines of every message block in the file.

| Tier | Rule |
|---|---|
| Open | Series A mail that was delivered, and the B-16 Global Access notice |
| Design Team | Series D working files not marked PTKW |
| PTKW | Series B except the above-Director files; series A mail that is held, a draft or a found note; series D files marked PTKW or Board Communication (D-07) |
| Branch Director | Series C, delivered |
| Above Branch Director | Status says "ABOVE BRANCH DIRECTOR CLEARANCE" (B-02, B-25) |
| Sealed | Status says SEALED; the readers are taken from the Status line (C-21, C-23, C-24, C-25) |
| Board | Status says BOARD ACCESS (C-18, C-19, C-20, C-22) |

**Who signs in as what.**

| Role | Sees | Count |
|---|---|---|
| Standard employee | Open | 16 |
| PTKW employee | Open and PTKW, including the Design Team files marked PTKW | 61 |
| Branch Director | Everything PTKW sees, series C, and the sealed files whose readers include the Earth Branch Manager. **Not** the above-Director files and **not** the Board files. | 83 |
| EOD Research Team | Open, the series C files that name the Research Team (C-26), and the sealed files that list it as a reader | 21 |
| Design Team | Open and the Design Team files | 25 |
| All access | Every message, the Board and above-Director files included. No author tools. | 93 |
| All emails | Every message, with the author's tools: Writer's notes, the Proposal chips and the file path | 93 |

**Mailbox.** Under each role you can narrow the view to one mailbox: an office (Branch Director, Earth Branch Manager, EOD Research Team, Interplanetary HQ), a staff member by asset number (the name shows when the file gives one), or a PTKW desk (K-7, K-12, VAH-3, TOR-9). A mailbox matches any message the person or office appears in, as sender, recipient or Cc, including inside thread blocks.

**Filters.** Mailbox, folder, channel, clearance tier, cycle, sort and search. The counts in the folder list follow the role and the mailbox.

**Refusals.** A link to a message above your tier opens a short "Outside your clearance" screen. The message text is in the page file, so this is a story device, not security: a reader who opens the page source can read it.

**Themes.** Each role has its own palette, set by CSS variables on a `data-role` attribute. The sign-in screen previews each theme on its card and takes the chosen role's theme as soon as you click it.

| Role | Palette | Reason in canon |
|---|---|---|
| Standard employee | Deep Blue `#1A2E52`, Warm Gold `#C9A84C`, beige paper `#F4EEE1` | Doc 2.32 brand; BES warmth on employee levels (Doc 2.40) |
| PTKW employee | Slate `#183247`, steel `#6FA3B5`, cool grey paper | Cool functional lighting on Levels 5, 8 and 9 |
| Branch Director | Navy `#10203f`, dull gold `#B8923A`, ivory | Level 2 warmth, more formal |
| EOD Research Team | Deep green `#1d3a36`, sage, grey-green paper | Laboratory register of the Interplanetary Research Division |
| Design Team | Plum `#3a2f5c`, copper `#E39B6B`, warm paper | The design studio, a bright working room |
| All access | Midnight `#0b1022` with gold, dark pages | Board clearance, apart from every floor |
| All emails | Graphite `#23262e`, gold, neutral paper | The author's tool; belongs to no level |

EOD Research Team, Design Team, All access and All emails go beyond the five roles the author named.


### 8. Limits **[PROPOSAL]**

- **One file is one message.** A thread file (for example C-26, B-28 or A-28) opens as a single entry, with its messages in order. Hearth does not yet split a thread into separate emails with their own From, To and time. Ten files have several message blocks; splitting them would need a convention in the files (`**[MESSAGE n]**` blocks are already used, and are the natural split point).
- **Dates are the map's.** The 28 undated messages stay at the end of Story time until their files carry a date line.
- **Sign-in is a view, not a lock.** There is no password. Any visitor may pick any role, and the page holds every message. It is not a build of the in-game interface.
- **Roles are inferred.** Access is read from the Status line, the series and the address lines. Twelve files have no Status line (A-25 to A-27, A-29, B-11 to B-14, B-18, B-19, B-21, B-27); they take the rule for their series and folder.
- **Mailboxes are thin.** Many senders carry no asset number ("Branch Director", "Earth Branch Operations"). They match by office name only, and a few names are lost to the parser.
- **Not checked by the canon rules.** Hearth reads files; it does not add rules.

### 9. Open rulings **[PROPOSAL]**

1. **Name.** Hearth, or another (Concord, Courier, Tether)?
2. **Public and PTKW names.** Is the PTKW reading ("the CCN filter behind it") right, or should the CCN have its own name in the interface?
3. **Thread splitting.** Do you want threads split into separate emails (the next step), at the cost of a header convention in ten files?
4. **The in-game version.** Should the game show a Hearth screen to the player at a terminal? If so, which folders does a Tier 3 asset see, and does a held message ever reach the player?
5. **Draft behaviour.** Drafts are kept as written. Should the game show an unsent draft only if the player finds the terminal where it was left?
6. **A Doc 2.29 entry** for Hearth in the glossary, or leave it out because PTKW can read the glossary.
7. **The role rules.** Should the Branch Director see PTKW traffic at all? I gave the Director the PTKW channel but not the two above-Director files (B-02, B-25) and not the Board files (C-18 to C-20, C-22). Is that right?
8. **Held mail.** I put held (Protocol 7) staff mail in the PTKW tier, since the CCN hands flagged messages to PTKW. The Branch Director sees it too. Should the Director?
9. **The Research Team's reach.** It sees the series C files that name it (C-26) and the sealed files that list it (C-21, C-23, C-24, C-25). It does not see the Board files. Confirm.
10. **The extra roles.** Keep EOD Research Team and Design Team as sign-ins, or reduce the screen to the five you named plus All access?

---

*→ See: design/ICS_OS.md — the operating system Hearth now runs in, the Director's retained copies, the Cloud Drive and Folio.*
*→ See: the ICS-OS folder — build_mail.py (the message builder), os.js and os.css (the page).*
*→ See: the README in the writing-map folder — the map, the watcher and the git hook that keep it current.*
*→ See: `canon/internal-communications/README.md` — the message index Hearth reads.*
*→ See: Document 2.32 (Brand Identity — The Logo) — the colours, the mark and the tagline.*
*→ See: Document 2.21 (Organizational Charter) — the Care & Connection Network and Protocol 7.*
*→ See: Document 2.20 (Employee Handbook) — "Communications manages all internal messaging".*

*[PROPOSAL] New material, written to the author's brief. The author's: that there should be a UI for what has been written; that it should be an email system for the internal communications, in the lineage of the *Prey* email system and the *Fallout* terminal; that the system itself should be named and documented; that it should carry the ICS style; that it should show all the emails and drafts; and that the `writing-map` folder should be what keeps it updated. Proposed: everything else, including the name Hearth and its second reading, the public and PTKW names, the colours and layout, the folder rules, the Proposal chip and Writer's notes switch, the keys, the build flow, and the limits.*
