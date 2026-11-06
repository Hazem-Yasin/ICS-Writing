## Devices and addresses: where the mail lives, and how it is reached

*Companion to `design/HEARTH.md` (the mail app) and `design/ICS_OS.md` (the operating system). Everything here is **[PROPOSAL]** except what the author's brainstorm of 2026-11-06 fixed: department mailboxes in the style of `icsresearch@ics.org`; mail and files scattered over the game, with only a few devices (the PTKW team leader K-7 and the Earth Branch Manager) holding many; a first test with a Branch Manager's office, a chair that can be sat in, and a device whose password, "smiling-man", is written on a note.*

---

### 1. The rule

A message is not "in the game". It is on a **device**, and a device is in a **place**. A player who wants the Manager's thread of the first arrival must reach the Manager's terminal. Hearth and ICS-OS are the software; this page is the map of where the software runs.

The mail files in the repo are the full set (95 messages, series A to D). Each device holds a **slice** of them, chosen by whose mailbox it is, and the in-game screen shows only that slice.

### 2. The address scheme **[PROPOSAL]**

The brainstorm gave `icsresearch@ics.org` as a model. `ics.org` is a real-world domain family and is not used. ICS addresses end in an invented top-level name, `.ics`, with the Labor Source or HQ as the domain:

| Part | Meaning |
|---|---|
| `@e349.ics` | Earth, Labor Source #349 |
| `@e312.ics` | Labor Source #312 (the Manager's previous Branch, C-26 only) |
| `@hq.ics` | Interplanetary HQ and the Research Division |

Why not `ics.org`: a real address would point outside the fiction. Why a Labor Source in the domain: it matches the portfolio numbering (Doc 2.22) and lets later planets reuse the scheme.

**Mailboxes.** Individuals use a code or asset number. Offices use a role. PTKW codes keep the form the files already use.

| Kind | Address | Used for |
|---|---|---|
| Staff | `e-03615@e349.ics` | Every asset number, lower case (29 appear in the files) |
| PTKW officers | `k-7@`, `k-12@`, `tor-9@`, `vah-3@e349.ics` | Series B |
| PTKW offices | `ptkw-duty@`, `ptkw-investigation@`, `ptkw-liaison@`, `ptkw-all@e349.ics`; `ptkw-oversight@hq.ics` | Duty Officer, Investigation Team, Floor Liaison, the all-PTKW list, Oversight Unit |
| Branch Director | `director@e349.ics` | Series C (20 messages) |
| Earth Branch Manager | `manager@e349.ics` (and `manager@e312.ics` in C-26) | Series C and B-28 |
| Regional Sector Lead | `sector-lead@hq.ics` | Brant, and the HQ line in C-26 |
| EOD Research Team | `eod-research@hq.ics` | The sealed Research Team files |
| Interplanetary HQ | `hq@hq.ics` | HQ, the Board channel |
| Design Team | `design@e349.ics`; `bes@e349.ics` (the working group) | Series D |
| Facilities | `facilities@e349.ics` | M. Castile |
| Lists | `all-staff@e349.ics`, `people@e349.ics` | Broadcasts, People & Culture |

`eod-research@hq.ics` is the brainstorm's `icsresearch@` renamed. Say if the exact form `icsresearch@` is wanted.

**The pass.** `tools/add_addresses.py` appends `<address>` to the From, To and Cc lines of series A to D. It is idempotent, it keeps each file's line endings, and a dry run is the default. Last run: 197 lines in 92 files. Parts that match no mailbox are left alone (drafts to nobody, notes to a wall, "Dad", the Vantage consortium channel). `tools/mail_index.py` counts messages per mailbox from the same headers.

### 3. Device map **[PROPOSAL]**

Counts are messages whose From, To or Cc names the mailbox; they overlap, since one thread has several addresses. "Unlock" is how the in-game screen lets the player in. Account names are those in `design/ICS_OS.md` section 5.

| # | Device | Place | Account | Mail on it | Unlock |
|---|---|---|---|---|---|
| 1 | **Earth Branch Manager's terminal** | Level 2, east quadrant, the Manager's office (`canon/facility/Level 2.md`) | Branch Director tier, Manager's view | About 10 (C-18 to C-26, B-28); the sealed Research Team pair is here. The largest source. | Password `smiling-man`, on a note (section 4) |
| 2 | **K-7's workstation** | Level 5, Monitoring & Analysis room | PTKW employee | About 20 (series B in full) | Password in K-7's own words, still open (section 4) |
| 3 | **Branch Director's desk machine** | Level 2, west quadrant, the Director's suite | Branch Director | About 20 (series C), plus retained copies of staff and PTKW mail per `ICS_OS.md` section 8 | Badge, no password. The machine is already signed in. |
| 4 | **A Work Floor B desk** | Level 3, Work Floor B | Standard employee | Up to 16 (series A only) | Badge. Any staff badge. |
| 5 | **Level 3 locker device and notes** | Level 3 lockers | None (personal device) | Found notes: A-04, A-10, A-14, A-16, B-13 | Locker code; the item is read in place |
| 6 | **Design Team workstation** | Design office (the Design Team has its own rooms) | Design Team | 6 to 25 (series D) | Badge with Design clearance |
| 7 | **HQ and Research relay** | Not on Earth | EOD Research Team | The sealed Research Team files | Not reachable in play |

Rules:

- **Only devices 1 and 2 hold many.** The brainstorm asks for exactly this, so the player finds a small thing on most desks and a great deal in two places.
- **The same message can be on more than one device.** A thread is on both ends. B-28 is on the Manager's terminal and on K-7's workstation. This is how the player learns the two men were writing to each other.
- **The Director's machine is wrong in a particular way.** It holds mail the Director never received (retained copies). It opens without a password because nobody has ever needed to stop it.

### 4. Passwords and notes **[PROPOSAL]**

**The Manager: `smiling-man`.** The author's. It fits the thread: the Manager's first message (C-26) says that he is the only person on the concourse who did not wave back to a man who smiled without changing; K-7 later "would rather he had smiled" (K-7 file). The password is the Manager's private name for EOD, which he does not say aloud. Written on a note stuck to the underside of the desk lamp's base, in the Manager's hand, the way a man writes a thing he is ashamed to have to remember. The note reads only the password. A second, older note in the drawer says *do not wave*.

**K-7: open.** K-7's file (ruling 4) offers a phrase from B-05, such as the 156 weeks of Monday data (`156-mondays`). It is not written on a note. A player gets it from K-7's own drafts and from his habit of writing the weekday at the top of a message. The author decides.

**The Director: none.** The machine is signed in, and the Director's real secret is in the paper journal under the false bottom of the drawer (Doc 2.35).

**Why a note for one and not the other.** The Manager writes down what he wants to forget. K-7 remembers what he wants to keep.

### 5. Build checklist (for the game repo)

1. One scene: the Manager's office. Desk, chair, lamp, terminal. The player can sit; sitting puts the camera at the screen.
2. A terminal screen that boots into ICS-OS (`design/ICS_OS.md` section 4), asks for a password, and opens Hearth on the Manager's slice.
3. `tools/mail_index.json` is the data: mailbox to message codes. The game reads the message files from the repo's `canon/internal-communications/`.
4. A second room with devices 2, 3 and 4 and their different accounts. The accounts are already defined; only the unlock and the slice differ.
5. A `Key: password` table per device, so a test can start at any desk.

### 6. Open rulings **[PROPOSAL]**

1. **The domain.** `.ics` with `e349`, `e312` and `hq` parts, or another invented form. Not `ics.org`.
2. **The Research address.** `eod-research@hq.ics` or the exact `icsresearch@` from the brainstorm.
3. **Staff addresses.** Asset numbers, as above, or names (`lior.ben-david@e349.ics`). Asset numbers match Hearth and the files; names read better on screen.
4. **K-7's password.** `156-mondays` or another.
5. **Where the Manager's note is.** Under the lamp, as written, or on the screen bezel.
6. **The Director's unlocked machine.** Intentional, as written, or does the Director know?
7. **Is the Manager's slice the whole thread of C-26?** Or does the player find the original on paper, since he "kept" it? C-26's header says it is held in his personal archive, which fits a drawer, not the network.

---

*→ See: `design/HEARTH.md` — the mail app. `design/ICS_OS.md` — the operating system and accounts.*
*→ See: `canon/characters/K-7 - PTKW Monitoring and Analysis Team Leader.md` — his workstation, ruling 4.*
*→ See: `tools/mail_index.py`, `tools/add_addresses.py`, `tools/mail_index.json`.*
*→ See: `meta/TODO.md` — items B6, B7, B8, C1 to C4.*
