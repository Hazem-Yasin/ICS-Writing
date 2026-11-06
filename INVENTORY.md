# ICS — Rigged Sphere
## Inventory System Design

*The player's inventory is not a bag. It is a collection of things they have decided to carry through a facility that was not designed for them to be carrying anything. The design principle: every item the player holds is a choice that costs something — space, weight, the risk of carrying contraband, the risk of leaving something behind.*

*The inventory is deliberately small. Not because the player can't handle complexity — because every item must feel consequential. A game where the player can carry forty items trains them that items are cheap. This game has ten slots.*

---

## Physical Constraints

The player has **10 inventory slots**. This is not explained to them as a mechanic. It resolves naturally from the interface: the badge itself has a small secondary display that the player can open by pressing the badge face, which shows the player's current load as a visual grid of ten squares. Full squares are items. Empty squares are space. The player understands the limit by looking at the grid; no tutorial explains it.

**The badge acts as the inventory interface.** This is intentional — the badge is the compliance architecture's tracking device. The inventory list is visible to the player but is also, canonically, a data manifest readable by authorized CCN personnel. An inventory full of improvised tools and contraband documents is itself an EIMU anomaly flag if a PTKW officer runs a badge manifest check. This mechanic exists but is only activated once — during the Phase 4 advance team sweep, where one of the two non-standard officers performs a badge manifest check on any non-PTKW staff they encounter. This is the one moment in the game where carrying the wrong items in the wrong slots triggers an immediate State 2 alert without any prior visual detection.

**Item size:** Most items take one slot. Two items take two slots:
- The Board Governance Charter (physical copy from Level 0) — two slots because it is thick
- The Omega-1 countermeasure device found in the Rania cache kit — two slots; the player must decide if carrying it is worth the sacrifice

---

## Item Categories

### Documents (non-consumable, can be stored)

Documents take one slot and can be stored at the player's quarters safe (accessible in Phase 0, Phase 1 confined, and Phase 5+ when quarters restriction lifts). The safe is not on the CCN manifest. It is a physical safe, not an electronic locker — Rania's note, found early, told the player about the safe because it belonged to a previous occupant of those quarters.

**Why carry documents instead of storing them:** Several documents need to be physically shown to NPCs to trigger conversation options (Tarek/Khalid registry, Sera/Yusra flag, Marcus/Board Charter section). These moments are time-sensitive — the NPC must be found when they are accessible, and the player cannot guarantee they will be able to return to quarters to retrieve the document in time. Deciding which documents to carry versus store is a constant low-level tension.

**The document weight problem (Phase 4):** The advance team manifest check means carrying the Board Governance Charter in Phase 4 is a direct risk. The player may have just retrieved it from Level 0. They are now moving through a Phase 4 facility. Storing it requires going back to quarters — possible, but time-costly. The charter is two slots. The player has to decide.

### Tools (consumable or limited-use)

| Item | Slots | Uses | Source |
|---|---|---|---|
| CRD-7 Compliance Tool | 1 | 8 charges | Found in Level 5 security storage locker, Phase 2 |
| ACS-9 Presence Projector | 1 | 4 uses | PTKW floor storage, requires Tier 3 access |
| AMB-3 Atmospheric Modifier | 1 | 3 deployments (once deployed, not recoverable) | Medical station, Phase 2+ |
| EIMU-Jammer | 1 | Continuous while active; battery drains over 8 minutes | Found in Yusra's cache |
| CCN-Spoofer | 1 | 3 spoof sessions before ID burn | Level 8 network closet, Phase 4 |
| Maintenance Bar | 1 | Unlimited (it is a bar) | Maintenance closets throughout |
| Olfactory Canister | 1 | 2 deployments | Cafeteria storage, Phase 3+ |
| AIDEN Unit (improvised) | 1 | 1 use; throws EIMU detection focus | Found on work floor, post-Phase 2 |
| Pressurized Pipe Tool | 1 | 5 uses | Level 0 maintenance room |
| EIMU Diagnostic Accessory | 1 | Passive; always active when carried | Level 3 medical station |

### Recovery items (consumable, one slot each)

The player's health tracks recover slowly passively from facility health nodes (food dispensers, water points, the warm panel in the maintenance passage). Active recovery items are scarce and do not respawn:

| Item | Effect | Source |
|---|---|---|
| Cafeteria ration pack | Physical Integrity +2 | Cafeteria (accessible through Phase 2; lockdown in Phase 4) |
| Level 3 medical kit | Thermal Regulation +3, Physical +1 | Medical station (once per phase, limited stock) |
| Tarek's supply cache kit | Full thermal reset + Physical +2 | Level 3 mop closet (Phase 5, once) |
| Comfort beverage (cafeteria machine) | Neurological Status +1, EIMU Coherence +2 | Cafeteria machines (Phase 0–4 only; shut down Phase 5) |
| Water (maintenance access point) | Physical +1, Thermal +1 | Maintenance network (unlimited, slow) |

**The EIMU Coherence track specifically:** This track only recovers through two routes — the Comfort beverage (small, from the compliance architecture's wellness system) and extended time in compliance-normal behavioral states. There is no active item that restores EIMU Coherence quickly. This is by design. The player who has spent Phase 3 in Level 0 crawlways will arrive in Phase 4 with degraded EIMU Coherence and no fast recovery. The game does not tell them this was coming. They feel the gap.

### Key items (non-consumable, permanent, can be stored but rarely should be)

Some items are key items — they exist for a specific purpose and once that purpose is resolved, they can be stored. But the player does not know when a key item's purpose is resolved. Storing a key item too early is the game's version of permanent missable content.

| Item | Purpose | Can be stored safely after... |
|---|---|---|
| Rania's note (full set) | Triggers Tarek conversation; readable to James | After Phase 5 cafeteria scene (Tarek reads it aloud) |
| Board Governance Charter | Showable to Marcus; Section 7 is the revelation | After Phase 6 begins |
| Level 0 device | Sends the message (Phase 5 action); provides Phase 6 Omega-1 gap | After the message is sent |
| Khalid transition record | Showable to Tarek; triggers Tarek arc | After Tarek receives it |
| Yusra escalation flag | Showable to Sera; triggers Sera arc | After Sera receives it |
| Omar's personal analysis | No NPC use; player reading only | Immediately |
| Sera's note to Yusra | Deliverable to Level 0 | After delivered (Phase 6) |

---

## Inventory Pressure — The Design Intent

Ten slots is enough for two tools, two documents, two recovery items, and one key item, with three slots of margin. The player will almost never be at full slots — until Phase 5, when everything is happening simultaneously.

**Phase 5 inventory pressure:** The player will have: Rania's note (if not yet shared), the Board Charter (if retrieved from Level 0), the EIMU-Jammer (if in use), the Maintenance Bar (always useful), at minimum two recovery items (critical in Phase 5), and the CCN-Spoofer or EIMU Diagnostic Accessory depending on route. That is 7–8 slots. The player still has 2–3 slots, but they will feel the pressure of what to prioritize.

**The one decision the inventory forces deliberately:** In Phase 6, the player receives Sera's note to Yusra (2 slot item: the note plus the sealed envelope). If they are carrying the Board Governance Charter (2 slots), they must make a choice. The game does not flag this as a choice. The player looks at their grid, counts the squares, and decides. They can leave one behind. They cannot carry both to Level 0. One goes into the quarters safe. Which one they choose is a statement about what they think matters most in the last 22 hours.

---

## Inventory UI — The Anti-Tutorial

The inventory interface (badge secondary display) shows items as uniform squares with a small icon. No labels — the player recognizes items by their icon after the first time they pick them up. The icon for Rania's note is a folded piece of paper. The icon for the Board Governance Charter is a document with a corner-fold. They look similar at a glance. This is not a bug.

The interface does not show item descriptions while in the field. Item descriptions are available only in the quarters safe interface, while browsing stored items. In the field, the player must remember what they're carrying.

**The badge manifest check (Phase 4 advance team mechanic):** When the advance team officer runs a manifest check, the badge display activates in their hands — the player watches their inventory be read. The officer doesn't take items. They log them. If any flagged items are present (improvised tools, PTKW-access documents the player's tier shouldn't have, the Level 0 device), the flag is immediate. The player knows because the officer's behavior changes: the pleasant professional manner disappears and the State 2 escalation begins. Smooth and sudden, with no warning sound effect. Just a change in posture.

---

## What the Player Cannot Carry

The game does not have weapons in the traditional sense — compliance tools are not weapons even when the player uses them offensively, and the improvised tools are industrial equipment, not arms. The one item category the player truly cannot carry is: other people's badges.

The compliance architecture requires every badge to be physically attached to its registered asset. A badge separated from its wearer generates an immediate CCN alert (the EIMU Coherence track on a detached badge flat-lines, which the system reads as a medical emergency or a transition event). The player cannot steal a badge, cannot use a stolen badge, cannot substitute a badge. This is a deliberate constraint that the game's worldbuilding mandates — and it is the reason the CCN-Spoofer is valuable. You cannot be someone else. You can only confuse the system about who you are.

---

*→ See: weapons/ — full item specifications for all tools.*
*→ See: HEALTH_SURVIVAL.md — the badge health tracks that recovery items affect.*
*→ See: ENEMY_AI.md — the Phase 4 advance team manifest check mechanic.*
