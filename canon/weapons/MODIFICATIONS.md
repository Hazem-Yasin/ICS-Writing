# Weapon Modifications — System Design

*This document covers how the player physically modifies tools and weapons in ICS: Interplanetary Corporate Solutions. The modification system is modeled on the principle that every tool in this facility has a second life waiting inside it — if the person holding it understands what it is well enough to take it apart and put it back together as something different.*

*The reference model is Dead Space: the player is not a soldier finding military weapons. They are a person with pattern recognition and problem-solving ability, surrounded by industrial equipment that was designed for specific non-combat purposes, using that equipment against the architecture that built it.*

---

## The Core Principle

ICS built every tool in this facility for compliance. The compliance tools subdue, contain, and regulate. The maintenance equipment moves heat, pressure, power, and compounds through the facility's body. None of it was designed to be lethal.

But everything here was designed with care — by engineers who understood physics, chemistry, materials, and human biology at a precise level. That care went into making things that work extremely well for their intended purpose. The same precision that makes the CRD-7 an effective neural interrupt makes it, with modification, something more. The same pressure lines that carry steam for the facility's climate systems can, redirected and focused, do things the climate engineering team never modeled.

The player does not find weapons. The player *makes* them — out of things that were made for something else.

---

## How Modifications Work

### The workbench

There is no single workbench. The player modifies tools at **junction points** — specific locations in the maintenance network where multiple system types are present simultaneously: power conduits, pressurized lines, raw materials, and a space wide enough to work in.

There are four primary junction points in the maintenance network:

**Junction A — Level 3, main service corridor junction.** The junction where the Level 6-to-Level 3 route meets the Level 3 janitorial station route. Power conduits, water and steam lines, and — critically — a hydraulic work cart that a maintenance team left in Cycle 299 and never retrieved. The cart has a basic tool set: cutter, heat gun, wrenches. This is the first junction the player can use. Available from Phase 2.

**Junction B — Level 1, sub-Level infrastructure room.** A larger space, roughly 4 meters × 5 meters, where the water main junction and the primary power distribution grid for Levels 1–4 share a service room. Has a workbench — an actual workbench, with a vice clamp and mounted tool rack — because this junction requires regular maintenance and the infrastructure team requested it in Cycle 292. The tool rack is mostly empty (equipment has been removed over years) but the bench and the clamp remain. The best modification space in the facility. Available from Phase 3.

**Junction C — Level 0 maintenance sub-corridor.** The narrower branch corridor off Level 0, near the power conduit junctions. Cold, cramped, lit only by emergency red. What it has that nothing else does: direct access to the pre-ICS structural elements and the unlabeled conduit systems. Certain modifications require materials only found here. Available from Phase 3; first required in Phase 4.

**Junction D — Level 5 east perimeter, PTKW-clearance zone.** The player cannot access this legitimately. They reach it through the maintenance network in Phase 4 after acquiring the Level 7 access code from Yusra's cache. This junction has the most complete tool set in the facility — it was the PTKW engineering team's primary maintenance point. Has a full tool set, spare parts for most ICS security equipment, and materials not available elsewhere. Available from Phase 4.

---

### The modification process

Every modification has:

1. **A base tool** — the item being modified.
2. **Components** — physical materials sourced from specific locations in the facility. Each component has an in-world origin: a specific pipe, a specific storage locker, a specific piece of equipment. The player does not find "crafting materials." They find things with names and purposes, and they take them apart.
3. **A junction requirement** — which junction is required for the modification. Some need the vice at Junction B. Some need the heat gun at Junction A. Some need the pre-ICS conduit access at Junction C.
4. **A cost** — not resources. Time and noise. Every modification takes time. The facility is not a safe space. Working at a junction for 20 minutes is 20 minutes in a location without EIMU coverage, but also 20 minutes of noise that may reach sensors in adjacent habitable areas.
5. **A result** — what the tool becomes. Always physically described: what it looks like after, what changed, what the modification did to the object. Not stats. Specific physical consequences.

---

### Modification categories

**Amplification** — taking a tool's existing function and extending its range, power, or duration beyond the intended spec. The CRD-7 neural interrupt at contact range becomes a ranged burst. The ACS-9's infrasound at ambient dispersal becomes a focused directional beam. These modifications do not change what the tool does — they change how far or how hard it does it.

**Conversion** — changing what a tool does. The CRD-7's neural interrupt, inverted, becomes a pain-delivery system rather than a movement-interruption system. The maintenance bar, fitted with a fragment launcher mechanism from a pressurized line joint, becomes something that fires shrapnel. These modifications require components that fight against the tool's original purpose — the tool resists, in a sense, and the modification shows it.

**Lethalization** — the most significant category. ICS designed every tool to be non-lethal. Lethal modifications require overriding specific safety mechanisms built into the tool's design — not bypassing them, because that would be obvious, but understanding them well enough to invert them. A safety mechanism that prevents the CRD-7 from exceeding 40 volts can be removed. But removing it requires understanding why it was put there — what damage 40+ volts does to the nervous system, what the engineers were protecting against — and that understanding is in the PTKW technical documentation. You have to read the safety spec to know how to defeat it.

---

### The modification leaves a mark

Every modification is visible. The player's tools do not look like retail products after modification. They look like what they are: things that have been taken apart and reassembled for a different purpose. Exposed wiring wrapped with insulation tape from the tool cart. Housings cracked open and wedged with a pipe bracket. Conduit fittings repurposed as barrels. The tools look improvised because they are.

This matters in-world: a player carrying modified tools cannot pass a standard security inspection. Modified tools flag on the Level 5 scanner because their electromagnetic profile no longer matches their registered ICS spec. The player has to choose when to carry modifications and when to carry clean versions.

It also matters narratively: the tools the player makes are ugly. They are the opposite of the facility's design aesthetic — the warmth, the soft edges, the "Asset Welfare Series" branding. The modification process is the player building something the facility did not sanction out of the facility's own materials. It looks exactly like that.

---

## Modification Index

| Base Tool | Modification Name | Category | Junction | Available |
|---|---|---|---|---|
| CRD-7 | Compliance Reversal (CRD-7R) | Lethalization | B | Phase 3 |
| CRD-7 | Extended Burst (CRD-7X) | Amplification | A | Phase 2 |
| ACS-9 | Directed Beam (ACS-9D) | Amplification | A | Phase 2 |
| ACS-9 | Resonance Shell (ACS-9RS) | Conversion | C | Phase 4 |
| AMB-3 | Fracture Baton (AMB-3F) | Lethalization | B | Phase 3 |
| AMB-3 | Signal Sever (AMB-3S) | Conversion | D | Phase 4 |
| Maintenance Bar | Fragment Launcher (BAR-FL) | Conversion | B | Phase 3 |
| Maintenance Bar | Hull Spike (BAR-HS) | Amplification | A | Phase 2 |
| Olfactory Canister | Directional Dispersal Rig | Amplification | A | Phase 2 |
| Olfactory Canister | Ignition Canister | Lethalization | C | Phase 4 |
| EIMU-Jammer | Cascade Broadcast (ECT-4C) | Amplification | B | Phase 3 |

---

*→ See: individual modification files in `canon/weapons/modifications/` for full component lists, junction requirements, and physical descriptions.*
*→ See: OVERVIEW.md — the three-tier knowledge system. Modifications generally require Tier 2 or Tier 3 knowledge of the base tool.*
