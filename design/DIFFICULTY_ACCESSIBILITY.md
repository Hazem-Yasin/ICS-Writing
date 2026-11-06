# ICS: Interplanetary Corporate Solutions
## Difficulty & Accessibility

*This game has no difficulty setting that makes EOD weaker. It has no setting that adds enemies, adds damage, or removes the ending. Difficulty here is a question of how much the game tells the player, not how hard it hits them. Accessibility is the same question asked more carefully: for whom is the information missing, and how do we put it back without breaking the fiction?*

*The design argument: the facility never lies about what it knows. It only declines to say. Every option below hands the player information the facility already holds — it never changes what the world does.*

---

## How to read this sheet

| Tag | Meaning |
|---|---|
| **Canon** | Already stated in an existing design document. The source is named. |
| **[PROPOSAL]** | New. Needs sign-off before it becomes canon. |

Almost everything in this document is a proposal, because almost nothing about difficulty, accessibility or controls is written down. The one canon hook is a single sentence in `design/STEALTH_DETECTION.md`: *"Players who need the explicit meter can enable it in accessibility options — it is not the default."* This document is the "accessibility options" that sentence promises.

---

## Part 1 — Difficulty

### The principle

**The game is not made easier by weakening the world. It is made easier by telling the player more.**

- Combat is a failure mode, not a skill check (`canon/weapons/OVERVIEW.md`).
- EOD cannot be beaten at any setting. That is a lore decision, not a balance decision.
- Omega-1 is avoidance only at any setting.
- Death states are narrative (reclassification, Schedule D completion). They are not tuned.
- No setting changes dialogue, the irreversible-events list, the four ending states, or the 22-hour clock's length.

### What cannot change at any difficulty

| Fixed | Why | Source |
|---|---|---|
| EOD unbeatable | Lore: nine deployments, perfect record | `canon/weapons/OVERVIEW.md` |
| Capture is "processed," not death | Tone | `design/HEALTH_SURVIVAL.md` |
| Detection build time 1.5–3s | The player learns the feel | `design/STEALTH_DETECTION.md` |
| Sound radii | Learned by ear | `design/STEALTH_DETECTION.md` |
| Ten inventory slots | The badge is the interface | `design/INVENTORY.md` |
| One manual save, quarters only | Saves are rest points, not undo | `design/SAVE_SYSTEM.md` |
| Irreversible events | "The people in them are real" | `design/SAVE_SYSTEM.md` |
| Four endings; no branching on difficulty | The ending is chosen, not won | `design/ENDINGS.md` |

### Three presets — "How much does the facility tell you?"

**[PROPOSAL]** Presets are named after how the facility treats the player, not after enemy strength. Each is a bundle of the individual options in Part 2.

| Preset | Name | Intent | What it changes |
|---|---|---|---|
| 1 | **Employee** | The default. Intended experience. | Nothing. Amber pulse only. No meter. No hints. |
| 2 | **Analyst** | The player is good at noticing; they want a little more. | Explicit detection meter available; Diagnostic Accessory readout found earlier (Phase 1 instead of Phase 2–3); patrol routes appear on the floor plan when read. |
| 3 | **Clearance** | The player wants the story and the choices, with less friction. | Everything in Analyst, plus: CCN Anomaly Score visible on the Diagnostic readout; longer Curious period before State 2 (+4s); autosave also fires before each tool use; optional in-world notebook for documents and names. |

**Never changed by a preset:** enemy count, damage numbers, EOD behavior, Omega-1 behavior, ending logic.

### Why not "Easy / Normal / Hard"?

Because "Hard" would mean more PTKW officers, and more PTKW officers means more of the thing the game is not about. The player at the hardest setting should still be asking *"what is the building doing?"*, not *"how many are left?"*

**[PROPOSAL] Optional "No Assist" mode.** Hides the amber pulse and the vitals display, leaving only the world. The player judges detection by the officers' behavior alone. Intended for second playthroughs. It removes information; it does not add a threat.

---

## Part 2 — Individual options

### 2.1 Information options

| Option | Default | Effect | Source / status |
|---|---|---|---|
| **Detection meter** | Off | Adds an explicit visual bar for detection build, replacing the amber pulse. | Canon (`design/STEALTH_DETECTION.md` line 24); design details **[PROPOSAL]** |
| **Detection audio cue** | Off | A soft tone rises as detection builds, falls if broken. | **[PROPOSAL]** |
| **Diagnostic Accessory readout available from start** | Off | The four-ring readout (signal strength, nearest node, stress status, K-7 pulse) available from Phase 1. | **[PROPOSAL]**; the Accessory is canon (Level 3 medical station) |
| **CCN Anomaly Score display** | Off | Shows the hidden score as a number and band on the Diagnostic readout. | **[PROPOSAL]** |
| **Patrol route overlay** | Off | Draws known patrol routes on floor plans the player has read. | **[PROPOSAL]**; routes are in Document 2.36 |
| **Interaction highlights** | Off | Outlines the things the player can pick up or use. | **[PROPOSAL]** |
| **Objective reminder** | Off | A single line in the badge menu: the last thing the player was doing. | **[PROPOSAL]**. Not available in Phase 6, where the canon is "no objective marker, no task log." |
| **In-world notebook** | Off | A personal notebook (Tarek's, as a model) that records document titles, names, times and where things were found. | **[PROPOSAL]** |

### 2.2 Time options

| Option | Default | Effect | Status |
|---|---|---|---|
| **Pause on open (inventory)** | Off | The world pauses while the badge inventory is open. | **[PROPOSAL]** |
| **Pause on open (documents)** | On in Phases 0–5 | The clock and patrols pause while a document is open. | **[PROPOSAL]** (matches `design/VERBS.md`) |
| **Extended Curious window** | Off | Adds +4s to State 1 before escalating to State 2. | **[PROPOSAL]**; canon already uses +4s in Emergency lighting |
| **22-hour clock speed** | Standard | Phase 6 runs at 100%, 75% or 50% speed. The in-fiction deadline does not change. | **[PROPOSAL]** |
| **Phase 6 clock display** | Badge clock only | Optional on-screen remaining time. | **[PROPOSAL]**. Canon: the game does not tell the player their remaining time (`design/SAVE_SYSTEM.md`). |
| **Quick-hold timing** | Off | Extends the window on any hold-to-act input (e.g. modifying, prying a panel). | **[PROPOSAL]** |

*The 22-hour clock is the one place where "slower" means "less tense." The slow settings give the player longer to act in-fiction without changing what the clock represents.*

### 2.3 Combat and risk options

| Option | Default | Effect | Status |
|---|---|---|---|
| **Autosave before tool use** | Off | An extra silent autosave before any tool discharge. | **[PROPOSAL]** |
| **Reduced neurological impairment** | Off | CRD-7 / ACS-9 effects on fine motor control last half as long. | **[PROPOSAL]**; canon effect: impairs tool use and modification |
| **Reduced UI degradation** | Off | Hypothermia no longer removes UI choice options; ACS-9 flicker disabled (see Part 3). | **[PROPOSAL]**; canon effect: UI shows fewer choices at critical Thermal |
| **Capture screen length** | 8 seconds | Reclassification screen can be shortened or skipped. | Canon default (`design/SAVE_SYSTEM.md`); option **[PROPOSAL]** |

---

## Part 3 — Accessibility

### 3.1 Vision

**Colour.** The health display is four LED strips: green → amber → red → dark. Detection feedback is an amber pulse. The Diagnostic Accessory uses Green / Amber / Red. The Level 0 red emergency light is a narrative signature. All of these lean on red/green/amber.

| Option | Effect | Status |
|---|---|---|
| **Colour-blind modes** | Deuteranopia, protanopia, tritanopia presets for the badge LEDs, the amber pulse and the Diagnostic readout | **[PROPOSAL]** |
| **Shape and pattern redundancy** | Each LED strip also changes pattern: solid → striped → blinking → dark. The amber pulse changes rhythm, not just hue. | **[PROPOSAL]** |
| **High-contrast badge** | Thicker strips, larger ring readout | **[PROPOSAL]** |
| **UI scale** | 75%–150% | **[PROPOSAL]** |
| **Subtitle and text size** | Separate scale | **[PROPOSAL]** |
| **Reduce red-wash** | Level 0 and Emergency lighting reduced in saturation; detection and navigation unaffected | **[PROPOSAL]**. The Level 0 look is canon; this is an *option*. |

**The red in Level 0 is design intent** (`canon/facility/Level 0.md`: "Just red. Steady, low, even."). The option softens saturation and leaves hue, brightness and mood intact.

### 3.2 Hearing

The game's most important information is often heard. Where canon makes something audible-only, a visual alternative is required.

| Audible-only information | Where | Visual alternative **[PROPOSAL]** |
|---|---|---|
| Footstep radius awareness | Move | Optional ring on the ground; or subtitle-style "sound radius" pulse on the badge edge |
| Enemy proximity by sound | State 0 patrol talk, K-7 hum | Directional indicator at the screen edge when Diagnostic Accessory is on; closed-caption tags |
| Badge reader tones (accepted/denied) | Badge | Green/red light on the reader (already physical) plus a badge flash |
| Ambient Update broadcast | Earth View Window | Captioned |
| Ventilation, pipe ticking, Level 0 hum | Atmosphere | Optional caption "[low hum]" tags; the hum is not information, so captions are optional |
| ACS-9 | **Not heard.** It is felt as anxiety (18 Hz). | Diagnostic Accessory shows a pulse; accessibility option may add a screen-edge vignette so players with no audio or limited feeling-through-sound can still read it |
| Eleven voices | Audio logs | Full subtitles. Canon: Rania (Swahili), Tarek (Arabic) and EOD (non-human) are already subtitled. |
| Audio log playback while walking away | `design/AUDIO_VOICE.md` | A transcript is added to the in-world notebook only if the notebook is on |

**Rania's recording is single-use** (`design/AUDIO_VOICE.md`). A hearing-impaired player must be able to read it as it plays. It is not a "replayable" log, so the *subtitles are the only chance*. They must be complete, timed and not skippable by mistake.

**Subtitle design:** speaker name; language tag for non-English (e.g. "Swahili — subtitled"); sound tags for non-speech; background boxes optional; no colour-only speaker coding.

### 3.3 Motor

| Option | Effect | Status |
|---|---|---|
| **Full remapping** | Every input, keyboard, mouse, controller | **[PROPOSAL]** |
| **Hold / toggle** | Crouch, run, aim, sit (Witness) | **[PROPOSAL]** |
| **Press / hold equivalence** | Any "hold to act" (modify, pry, search) has a tap-to-start, tap-to-cancel alternative | **[PROPOSAL]** |
| **One-handed layouts** | Presets for left and right hand | **[PROPOSAL]** |
| **Reduced precision input** | Larger interaction radius; aim assist for the CRD-7 directed field (≤3m) | **[PROPOSAL]** |
| **Auto-move** | Auto-walk toggle | **[PROPOSAL]** |
| **Rumble and haptics** | Off, reduced, full | **[PROPOSAL]** |
| **Inventory navigation** | Directional (grid) or cursor | **[PROPOSAL]** |
| **No timed inputs** | Canon: no QTEs. Keep it. | Design rule |

The neurological impairment from CRD-7 and ACS-9 canonically **degrades fine motor control** (tool use and modification). A player with a motor disability should not experience *additional* in-game impairment as a penalty on top. See "Reduced neurological impairment" above.

### 3.4 Cognitive and reading

| Option | Effect | Status |
|---|---|---|
| **Document summary** | A one-line summary at the top of each document, in the notebook voice | **[PROPOSAL]** |
| **Reading mode** | Dyslexia-friendly font, line spacing, no justified text | **[PROPOSAL]** |
| **Pacing control** | Documents can be opened and closed without penalty; the clock pauses (Phases 0–5) | **[PROPOSAL]** |
| **Reminder of last action** | Part of "Objective reminder" above | **[PROPOSAL]** |
| **Save reminder** | Badge prompt in quarters | **[PROPOSAL]** |
| **Content notes** | See Part 4 | **[PROPOSAL]** |

### 3.5 Photosensitivity and motion

Canon effects that touch the screen:

- ACS-9 extended exposure: *"subtle UI flicker at mild levels, partial UI blackout at severe"* (`design/HEALTH_SURVIVAL.md`)
- ACS-9 7–8 Hz "peripheral motion artifacts, transient edge distortion"
- Hypothermia: tunnel vision, slowed movement, fewer UI choices
- Neurological: fine motor impairment
- Amber pulse at the badge edge

A visual flicker at 7–8 Hz is in the range that can affect people with photosensitive epilepsy (commonly cited concern band is roughly 3–30 Hz). **This is the highest-priority accessibility item in this document.**

| Option | Effect | Status |
|---|---|---|
| **Photosensitivity safe mode** | All flicker and strobing replaced by a steady edge tint or slow pulse (< 3 Hz). ACS-9 disturbance becomes an edge vignette with a symbol on the badge. | **[PROPOSAL]**, **required** |
| **Reduce motion** | Camera sway, head bob, tunnel vision strength, edge distortion | **[PROPOSAL]** |
| **Reduce screen effects** | Blur, chromatic offsets, vignettes | **[PROPOSAL]** |
| **Field of view** | Adjustable | **[PROPOSAL]**. No FOV is currently defined. |
| **Camera shake** | Off / low / full | **[PROPOSAL]** |
| **First-launch warning** | Photosensitivity notice, with a link to the setting | **[PROPOSAL]** |

*The ACS-9's diagnostic design — "anxiety with no identifiable cause" — is meant to be felt. In safe mode the same feeling can be conveyed by audio (very low sub-bass, not 18 Hz sine), the badge ring, and the NPC reactions. The mechanic survives; the strobe does not.*

---

## Part 4 — Content warnings (not accessibility, but adjacent)

The game contains: institutional coercion; planetary-scale death (Schedule D; Category Omega); the transition of a mother separated from her daughter (Rania, Leila); disappearance and presumed death of a Branch Director (the notebook); psychological manipulation; and, in Doc 2.38 and Phase 6, discussion of self-sacrifice and "purposeful self-destruction" as historical and in-world ideas. **[PROPOSAL]** The self-sacrifice material is argued from the system's point of view and must never be framed as an instruction or a solution; a note is warranted wherever it is read in full. A first-launch content note, and an in-menu summary, without spoilers.

---

## Part 5 — What accessibility must not do

**[PROPOSAL]** — Principles.

1. **No accessibility option changes the story.** No ending, dialogue branch or irreversible event is gated by a setting.
2. **No option reveals canon the player has not discovered.** The CCN Anomaly Score display shows a *number*, not why. The Diagnostic readout shows *signal*, not names.
3. **No option removes EOD.**
4. **No option makes the facility warmer.** The facility's warmth is a feature of its horror.
5. **Options are shown in-world where possible.** The detection meter is a badge setting. The Diagnostic readout is on the badge. The notebook is Tarek's kind of notebook.
6. **Nothing is penalized for turning options on.** No achievements, no flagged saves, no label.

---

## Part 6 — Input and controls

`README.md` records that movement-related verbs are undefined. `design/VERBS.md` defines the eight verbs. This section lists the inputs they imply.

| Verb | Primary | Notes |
|---|---|---|
| Move | Analog / WASD | Walk default; crouch hold/toggle; run hold/toggle |
| Read | Interact | Opens a document; closes with the same input |
| Badge | Badge button | Taps readers; long-press opens the grid |
| Use | Tool button (hold to aim, release to act) | One input for all tools |
| Modify | Interact at a junction | Sequence of 3–5 steps |
| Speak | Interact; option select | No wheel; text lines |
| Slip | Interact at a panel | Camera lowers by type |
| Witness | Sit (hold) | Hold to stay |

**[PROPOSAL]** All verbs have a single-button alternative where hold or two-input is the default.

---

## Open questions

1. **Omega-1 capture and reload.** `design/HEALTH_SURVIVAL.md` says Omega-1 exposure is **"game over, no reload"** and is the only non-recoverable death. `design/SAVE_SYSTEM.md` says Omega-1 capture **"returns to last autosave."** These conflict. They matter here because any "extra life" or "skip" accessibility option interacts with it. **Needs a ruling.** This sheet assumes `design/SAVE_SYSTEM.md` (reload), since the "Last Entry" save exists for Phase 6 replay.
2. **Does the amber pulse count as "always on"?** Canon says it is the only feedback. "No Assist" mode would turn it off. Confirm this is wanted.
3. **Is a notebook an in-world object or a menu?** Tarek's notebook is a strong model. If it is an object, it must be shown being used.
4. **Subtitle languages.** Rania's recording is Swahili, Tarek's is Arabic. Are subtitles localized per player language?
5. **FOV and camera.** None defined. A default of 90° with a 70–110° range is a placeholder.
6. **Does Phase 6 allow the notebook?** The canon intent is "no task log." A notebook that logs *names* is arguably thematic (Tarek's names), but a notebook that logs *tasks* breaks the rule.
7. **22-hour clock speed.** Is "slower" a difficulty option or an accessibility option? This sheet calls it both.

---

*→ See: design/STEALTH_DETECTION.md — the optional meter, the amber pulse, the Diagnostic Accessory.*
*→ See: design/HEALTH_SURVIVAL.md — the four tracks, the UI degradation, the death states.*
*→ See: design/SAVE_SYSTEM.md — autosave rules and the conflicting Omega-1 line.*
*→ See: design/AUDIO_VOICE.md — the eleven voices and subtitled recordings.*
*→ See: design/INVENTORY.md — the badge grid.*
*→ See: design/VERBS.md — the eight verbs and their input needs.*
*→ See: design/TENSION_CURVE.md — the pacing these options must not flatten.*
*→ See: canon/weapons/OVERVIEW.md — combat as a failure mode.*
