# ICS: Interplanetary Corporate Solutions
## Environmental Storytelling — Rules and Prop Manifest

*The facility tells its story through objects that were placed by someone for a reason. A cleaned floor, a laminated card, a coffee ring, a bench worn on the right. This sheet sets the rules for placing them and lists, level by level, the props that must exist, with a link to the Blender work that will build them.*

*The design argument: an object in this game is either an instrument of the BES or evidence of a person. If it is neither, it is clutter. The player should be able to read what happened in a room from what is left in it, and should never need to be told.*

---

## How to read this sheet

| Tag | Meaning |
|---|---|
| **Canon** | Already stated in an existing document. The source is named. |
| **[PROPOSAL]** | New. Needs sign-off before it becomes canon. |

The Blender folders `Environments/` and `Props/` are read-only reference for this document. Nothing here edits them. The link is by file name only; the contents of the `.blend` files were not opened to write this sheet.

---

## 1. The rules

| # | Rule |
|---|---|
| 1 | **Every prop is an instrument or evidence.** BES instrument: it makes the player comfortable. Evidence: a person left it. |
| 2 | **The absence is the prop.** A clean floor with no cleaner, a bench worn on one side, an empty coffee queue. |
| 3 | **Same object, different phase.** The AIDEN plush, the laminated card, the poster quote: the object is constant, its meaning shifts. |
| 4 | **Handwriting is human.** Handwritten text belongs to a person (Rania, Tarek, the previous Director). ICS text is typeset. |
| 5 | **Never explain.** No caption, no diary entry that restates what the room shows. |
| 6 | **One discovery per room.** A room can hold many props but only one that rewards a second look. |
| 7 | **Nothing glows.** No highlight on interactables except by accessibility option. (`design/PLAYER_GUIDANCE.md`) |
| 8 | **Evidence is placed where the person would have left it,** not where the player will find it. |

---

## 2. Prop categories

| Category | Examples | Source |
|---|---|---|
| **BES instruments** | Olfactory vents, adjustable-frost glass, acoustic ceiling panels, AIDEN desk cards, posters, coffee machines | **Canon** — `canon/facility/Overview.md`, `canon/facility/Level 3.md` |
| **Evidence of people** | Rania's paper-towel notes, Tarek's notebook, the coffee ring, a Tier 1 badge, tally marks under a bar | **Canon** |
| **Tools and materials** | Maintenance Bar, heat gun, tin snips, pipe coupling joints, HVAC baffles | **Canon** — `canon/weapons/modifications/` |
| **Documents** | Charter, notebook, terminal printouts | **Canon** |
| **Absences** | Clean floor, empty queue, bench worn on the right | **Canon** — scene notes |

---

## 3. Prop manifest by level

Each row: a prop that must exist, who it belongs to, and the Blender file that is expected to hold or build it. "Blender" means the nearest existing file, not a confirmed match.

### Level 0 — Infrastructure Corridor

| Prop | Belongs to | Source | Blender |
|---|---|---|---|
| Raw pipes with Cycle 1 notation | The building | `canon/facility/Level 0.md` | None yet |
| Emergency red lighting fixtures | The building | `canon/facility/Level 0.md` | None yet |
| The device (warm, silent, seamless) in the 15 m recess | The Board | `canon/weapons/found/Level-0-Device.md` | None yet |
| Notebook in the sub-corridor gap | The previous Director | `story/scene-notes/Level 0.md` | None yet |
| Pre-ICS glyph panels (×2) | Unknown | `canon/weapons/improvised/Maintenance-Bar.md` | None yet |
| Rania's hatch kit by the south hatch | Rania | `canon/weapons/found/Rania-Hatch-Kit.md` | None yet |
| The clean floor | Nobody | `canon/facility/Level 0.md` | None yet |

### Level 1

| Prop | Belongs to | Source | Blender |
|---|---|---|---|
| Janitorial station shelf, cart, log | Rania | `canon/facility/Level 1.md` | None yet |
| Stairwell B door, grey, green seal, 2 mm gap | The building | `story/scene-notes/Stairwell B.md` | None yet |
| Maintenance panel in the back wall | The building | `canon/facility/Level 1.md` | None yet |

### Level 2

| Prop | Belongs to | Source | Blender |
|---|---|---|---|
| Mezzanine rail | The building | `canon/facility/Level 2.md` | `Environments/OfficeOne/OfficeOne.blend` (office space; **[PROPOSAL]** reuse for manager corridor) |
| Branch Director's desk and AIDEN plush (left of desk) | The Director | `canon/facility/Level 2.md` | `Environments/OfficeTwo/OfficeTwo.blend` (**[PROPOSAL]** nearest match) |
| Lost property: Rania's jacket | Rania | `canon/facility/Level 2.md` | None yet |
| PWRP terminals (leftmost is Sera's) | Sera | `canon/facility/Level 2.md` | None yet |

### Level 3

| Prop | Belongs to | Source | Blender |
|---|---|---|---|
| Work desk, 140 × 80 cm, with EIMU panel | The player | `canon/facility/Level 3.md` | `Environments/OfficeOne/OfficeOne.blend` (**[PROPOSAL]**) |
| Drawer: coffee ring, scrap of numbers, face-down AIDEN card | The player | `canon/facility/Level 3.md` | None yet |
| Collaboration pod, round table | The building | `canon/facility/Level 3.md` | `Environments/OfficeOne/OfficeOne.blend` |
| Medical Centre waiting room (3,000K) | The building | `canon/facility/Level 3.md` | None yet |
| Pool, 25 × 8 m, 28°C | The building | `canon/facility/Level 3.md` | None yet |
| Lamp (desk or floor) | The building | Not in canon | `Props/Lamp/Lamp_Prop.blend` |

### Level 4

| Prop | Belongs to | Source | Blender |
|---|---|---|---|
| Round tables, eight seats | The building | `canon/facility/Level 4.md` | `Environments/Env1_BreakArea/ProjectFile_/BreakArea.blend` (break area; **[PROPOSAL]** also cafeteria) |
| Break room sofas, bookshelf, game tables, Earth screen | The building | `canon/facility/Level 4.md` | `Environments/Env1_BreakArea/ProjectFile_/BreakArea.blend` |
| AIDEN plush, 30 cm, east wall | The Director's brand | `canon/facility/Level 4.md` | `Environments/PureRef_Reference/BreakArea_Reference.pur` (reference only) |
| Four coffee machines | The building | `canon/facility/Level 4.md` | `Environments/Env1_BreakArea/ProjectFile_/BreakArea.blend` |
| Earth View panel, 3 × 2.5 m, and bench worn on the right | The building | `story/scene-notes/Earth View Window.md` | None yet |
| Quiet room, eight seats | The building | `canon/facility/Level 4.md` | None yet |
| Third stall; paper-towel notes | Rania | `canon/facility/Level 4.md` | None yet |

### Levels 5–10

| Prop | Belongs to | Source | Blender |
|---|---|---|---|
| EIMU racks, review terminal | PTKW | `canon/facility/Level 5.md` | None yet |
| Black card reader | The building | `canon/facility/Level 5.md` | None yet |
| Library alcoves, bar tally marks | Staff | `canon/facility/Level 6.md` | None yet |
| Departure form ICS-T8, stall door with "94" | Staff | `canon/facility/Level 7.md` | None yet |
| 22 EIMU workstations | PTKW | `canon/facility/Levels 8-10.md` | `Environments/OfficeOne/OfficeOne.blend` (**[PROPOSAL]** repeating desk unit) |
| Category Omega release mechanism, 40 × 40 × 60 cm | The Board | `canon/facility/Levels 8-10.md` | None yet |

### Levels 11–14

| Prop | Belongs to | Source | Blender |
|---|---|---|---|
| Board elevator | The Board | `canon/facility/Levels 11-14.md` | None yet |
| EOD quarters on Level 13 | EOD | `canon/characters/EOD.md` | None yet |

### The building as a whole

| Prop | Source | Blender |
|---|---|---|
| Exterior of the facility | `canon/facility/Overview.md` | `Props/building/building.blend` (**[PROPOSAL]** nearest match) |
| "Distorted Land" and hallway exports | Unknown | `Environments/OfficeOne/Exports/Distored Land.fbx`, `Hallway and One Room.glb`, `Ome Hallway.fbx` |

---

## 4. Tools in the Blender folder

`Props/Shotgun/` holds several versions of a rusty-metal shotgun (`Shotgun Beta One.blend`, `Shotgun uv and shading test.blend`, PBR textures). **There is no firearm in the design.** (`canon/weapons/OVERVIEW.md`: combat is a failure mode; every tool is a compliance tool.)

**Options for the prop [PROPOSAL]:**
1. Repurpose it as the **BAR-FL Fragment Launcher** (`canon/weapons/modifications/BAR-FL — Fragment Launcher.md`): a rebar and pipe-coupling launcher. The rusty-metal PBR textures fit the improvised look.
2. Use it as a **non-functional prop** in the PTKW storage on Level 5.
3. Remove it from the game scope.

Option 1 requires redesigning the model to match the 12 mm rebar and 22 cm pipe-coupling description. A shotgun silhouette would contradict the design's tone.

---

## 5. Evidence trails

Chains of props that tell a story across levels.

| Trail | Props, in order | Where |
|---|---|---|
| **Rania** | Paper-towel notes → third stall (Level 4) → lost property jacket (Level 2) → janitorial shelf (Level 1) → Stairwell B (Level 0) → hatch kit (Level 0) | Levels 4 → 0 |
| **The previous Director** | Notebook entry → inside cover → terminal message | Level 0 |
| **Tarek** | Notebook → maintenance route schedule → standing in the cafeteria | Levels 1–4 |
| **The 94** | Stall door scratch on Level 7 → Schedule D (94 pages) in the transit waiver ICS-T7 → the departure form ICS-T8 | Level 7 |
| **The 847** | Operational transfers → adjacent corridor → undeactivated badges | Levels 7, 9 |
| **Sera** | Report terminal → framed commendation in quarters | Levels 2, 3 |

---

## 6. Phase changes in the same room

| Room | Phase 0 | Phase 2+ |
|---|---|---|
| Cafeteria | Full, loud, hot food | Empty, cold, the same tables |
| Break room | AIDEN card current | Card the same; a different quote on the poster |
| Earth View Window | Music, warmth | Silence; coffee ring on the left of the bench |
| Work floor | People, light conversation | Lights on, desks empty, drawers closed |
| Janitorial station | Night shift, active | Dust; the log's last entry is Rania's |

---

## 7. What to avoid

- No blood stains, no scratched walls, no "diary pages" explaining the plot.
- No audio logs in places where no one would leave one.
- No message written in the facility's own text that admits its function.
- No props that exist only as player rewards. Every item has an owner.
- No weapon silhouettes.

---

## Open questions

1. **Which Blender files correspond to which levels?** The `.blend` files were not inspected. The mapping above is a guess from folder names.
2. **Break room vs cafeteria.** `BreakArea.blend` is the only break-room asset; the cafeteria (5,000 m²) is much larger.
3. **The Lamp.** `Props/Lamp/Lamp_Prop.blend` has no canon description.
4. **The shotgun.** See Part 4.
5. **Distorted Land.** The exported file name suggests an effect environment but no canon scene matches.

---

*→ See: canon/facility/Overview.md — the BES and the building.*
*→ See: design/LEVEL_BEAT_SHEETS.md — per-level beats these props serve.*
*→ See: design/ART_DIRECTION.md — light, colour and material.*
*→ See: canon/weapons/OVERVIEW.md — combat as failure.*
*→ See: canon/weapons/found/Rania-Hatch-Kit.md — Rania's kit.*
*→ See: story/scene-notes/Earth View Window.md — the window and bench.*
*→ See: design/PLAYER_GUIDANCE.md — no highlights.*
