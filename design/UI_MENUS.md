# ICS: Interplanetary Corporate Solutions
## UI, HUD and Menus

*The interface is the badge. There is no separate game menu pretending to be outside the fiction: the inventory grid, the clock, the health strips, the documents and the settings all live on the device the facility issued to the player. The one place the game steps outside the building is the boot screen, and even that is an ICS document.*

*The design argument: if the badge is the compliance architecture's tracking device, then every screen the player opens is a screen the facility can also read. The interface should feel like a tool the player trusts and be written so that, later, they do not.*

---

## How to read this sheet

| Tag | Meaning |
|---|---|
| **Canon** | Already stated in an existing document. The source is named. |
| **[PROPOSAL]** | New. Needs sign-off before it becomes canon. |

---

## 1. Principles

| Principle | Source |
|---|---|
| The badge is the inventory interface. | **Canon** — `design/INVENTORY.md` |
| Inventory is a grid of ten squares. The limit is understood by looking. | **Canon** — `design/INVENTORY.md` |
| Health is four LED strips: green → amber → red → dark. | **Canon** — `design/HEALTH_SURVIVAL.md`, `design/DIFFICULTY_ACCESSIBILITY.md` |
| Detection feedback is an amber pulse at the badge edge. No meter by default. | **Canon** — `design/STEALTH_DETECTION.md` |
| Autosave is invisible. No spinner, no icon. | **Canon** — `design/SAVE_SYSTEM.md` |
| No objective marker and no task log in Phase 6. | **Canon** — `story/scene-notes/Phase 6 Final 22 Hours.md` |
| No QTEs. | **Canon** — `design/DIFFICULTY_ACCESSIBILITY.md` |
| The facility never explains itself. | Design rule |

---

## 2. In-world HUD

**[PROPOSAL]** Default state: *nothing on screen* except what the world shows.

| Element | Where | Shown when | Notes |
|---|---|---|---|
| **Crosshair / interaction cue** | Centre, small | Only when an interactable is in range | A single dot becomes a ring. Off in Phase 6 cutscenes. |
| **Amber pulse** | Screen edge | Detection is building | **Canon**. Rhythm changes with detection stage (see `design/DIFFICULTY_ACCESSIBILITY.md`, shape/pattern redundancy). |
| **Health strips** | Badge, bottom left of the viewmodel | When badge raised, or when any track is amber or below | Four strips: Physical Integrity, EIMU Coherence, Neurological Status, Thermal Regulation. |
| **Clock** | Badge face | When badge raised | Branch Time. |
| **Subtitle line** | Lower third | When a voice plays | Speaker name, language tag. |
| **Context line** | Lower third, small | One line for what the player just did (document picked up, tool charged) | Replaces pickup toasts. |

**Never on screen:** a minimap, a compass, health numbers, ammo counters, quest text, damage numbers.

---

## 3. The badge

Raising the badge is a verb ("Badge", `design/VERBS.md`). It is the one in-fiction menu.

| Tab | Contents | Source |
|---|---|---|
| **Grid** | The ten-square inventory | **Canon** — `design/INVENTORY.md` |
| **Documents** | Documents the player has read, by title | **[PROPOSAL]**. The game does not offer a log library for *audio*. Documents are kept. |
| **Tools** | Charges, state, last modification | **[PROPOSAL]** |
| **Clock** | Branch Time and day | **Canon** for Branch Time |
| **Diagnostic** | The four-ring readout (signal strength, nearest node, stress, K-7 pulse) | **Canon** once the Diagnostic Accessory is found |
| **Settings** | Accessibility, controls, audio | **[PROPOSAL]** |

**Open question:** whether the pause (see Part 5) opens the badge or a separate screen.

### Badge display by tier

The badge colour, text and sensor behaviour follow `design/PROGRESSION.md`:

| Badge | Colour | Notes |
|---|---|---|
| Tier 3 | Deep blue / gold | Retroactive (Day 1 memory) |
| Tier 2 | Deep blue / silver | Game start |
| Tier 1 | Midnight blue / platinum | Phase 2 |
| PTKW-Clearance | Grey / white lettering, no ICS logo | Phase 4 |
| Branch Director | Standard with a thin gold stripe | Phase 5 |

---

## 4. Boot and title

**[PROPOSAL]**

| Screen | Content |
|---|---|
| **Boot** | An ICS logo, then a single employee onboarding line from Document 2.33. No publisher splash after the first. |
| **Content note** | A short first-launch notice (see `design/DIFFICULTY_ACCESSIBILITY.md`, Part 4). |
| **Photosensitivity notice** | On first launch, with a link to the safe mode setting. **Required.** |
| **Title** | The Earth View, 06:00 terminator line. A single line of text. No music. |
| **Menu items** | *Continue* · *Load* · *Settings* · *Credits* · *Quit* |

The title screen is the Earth View Window. It is the same image the player will stand in front of in Phases 4–6.

---

## 5. Pause

**[PROPOSAL]**

| Rule | Detail |
|---|---|
| **Pause key** | Opens a pause screen that stops the world. |
| **Contents** | *Resume* · *Settings* · *Quit to Title*. |
| **No save here** | Saving is a quarters-safe action. **Canon**: one manual slot, quarters only (`design/SAVE_SYSTEM.md`). |
| **Pause vs the badge** | The badge never pauses the world in Phases 0–5 unless "Pause on open" is set. The pause key always does. |
| **Phase 6** | The pause screen still works. The 22-hour clock does not advance while paused. |

---

## 6. Save and load

| Screen | Content | Source |
|---|---|---|
| **Quarters safe** | One manual save slot. Writes over the previous one. | **Canon** — `design/SAVE_SYSTEM.md` |
| **Load** | The last autosave (timestamped), the manual save, and *"Day [X] — Last Entry"* once Phase 6 has begun. | **Canon** for Last Entry |
| **Display** | Branch Time, Day, Level, Phase. No screenshots. **[PROPOSAL]** | — |
| **Delete** | Not offered for Last Entry. | **Canon** |

There is no chapter select. (`design/SAVE_SYSTEM.md`)

---

## 7. Settings

All options in `design/DIFFICULTY_ACCESSIBILITY.md` appear in four tabs. **[PROPOSAL]**

| Tab | Contents |
|---|---|
| **Preset** | Employee · Analyst · Clearance · No Assist |
| **Accessibility** | Vision · Hearing · Motor · Cognitive · Photosensitivity |
| **Controls** | Remapping, hold/toggle, one-handed |
| **Audio / Video** | Volume sliders, subtitles, FOV, motion, red-wash |

Every setting that changes the world's information, not its behaviour, is labelled as such.

---

## 8. Documents on screen

Documents are read in a full-screen reader.

| Property | Detail |
|---|---|
| **Layout** | The document as it exists in the ICS system: header, ID, date. |
| **Controls** | Scroll; close with the same input that opened it. |
| **Clock** | Pauses in Phases 0–5. **[PROPOSAL]** |
| **Cross-references** | A *See* line at the end. It does not link. The player has to find the place. **[PROPOSAL]** |
| **Summary** | Optional one-line header in the notebook voice. |

---

## 9. Credits

**[PROPOSAL]** Run in the style of an ICS Asset Register: names, asset numbers, a single line each. Final card: *"Productive capacity fully realized."* is not used here; the credits do not repeat the system's language. They end on the Earth View.

---

## Open questions

1. **Does the pause open the badge or a separate screen?** The principle says the badge is the interface; the pause is the exception.
2. **Controller layout.** None defined.
3. **Credits tone.** The Asset Register style is a proposal.
4. **Photosensitivity notice wording.** Must be written with a safety review.

---

*→ See: design/INVENTORY.md — the badge grid.*
*→ See: design/PROGRESSION.md — the badge colours and tiers.*
*→ See: design/HEALTH_SURVIVAL.md — the four strips.*
*→ See: design/STEALTH_DETECTION.md — the amber pulse.*
*→ See: design/SAVE_SYSTEM.md — saves and Last Entry.*
*→ See: design/DIFFICULTY_ACCESSIBILITY.md — the options that populate the settings.*
*→ See: design/FAILURE_LOOP.md — what happens when the player fails.*
*→ See: design/VERBS.md — the Badge verb.*
