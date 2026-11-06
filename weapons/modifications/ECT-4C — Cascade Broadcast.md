# ECT-4C — Cascade Broadcast
*Base Tool: EIMU-Jammer (ECT-4 Calibration Tool) | Category: Amplification | Junction: B | Available: Phase 3*

---

## What You Start With

The ECT-4 broadcasts a false EIMU signal — any of 47 emotional state categories at any amplitude — from a single point. The EIMU network reads this signal as a genuine human emotional output. The range of the broadcast is approximately 4 meters from the device, sufficient to register at the nearest EIMU sensor node and be logged as normal.

The ECT-4's transmission architecture uses a single-band antenna — the stub at the top of the device. This was sufficient for the calibration use case: a technician stands near a sensor node, broadcasts a test signal, verifies the node reads correctly, moves to the next node.

The calibration use case required affecting one sensor node at a time.

---

## Components Required

**1. The ECT-4.** Already in the player's inventory.

**2. Antenna array — sourced from:** The Level 6 EIMU infrastructure maintenance cabinet. The EIMU sensor nodes are serviced using spare antenna components stored in this cabinet — small stub antennas, identical in design to the ECT-4's existing antenna, used to replace damaged node antennas. There are eight of them. Three are sufficient for the modification.

**3. Copper wire — sourced from:** Junction B's wire spool. The same 22-gauge copper wire used in the CRD-7R modification.

**4. Solder — sourced from:** Junction D's PTKW maintenance storage. The PTKW maintenance team stocks a basic electronics repair kit including solder wire. Available in Phase 4 after accessing Junction D.

*Note: this modification is listed as Phase 3 available but requires solder from Junction D, accessible Phase 4. The player can partially assemble the ECT-4C in Phase 3 and complete it in Phase 4.*

---

## The Modification Process

**Junction required:** B (soldering heat work using the heat gun as a substitute iron; the vice clamp holds the ECT-4 housing open during soldering).

The ECT-4's single antenna connects to the transmission board through a standard RF connector on the interior housing. The connector accepts a single lead. The modification replaces this connection point with a small distribution hub — made by wrapping the three additional antennas in parallel with the original, using copper wire to create a four-antenna array that is then soldered to the transmission board connector.

The four antennas are mounted in different orientations — one at 0°, one at 90°, one at 180°, one at approximately 45° — using epoxy to hold position after the player establishes the geometry that maximizes coverage through experimental testing (active device, moving antennas until the signal coverage pattern — visible as a feedback reading on the ECT-4's own display — reaches maximum spread).

The modification takes 50 minutes including the testing/calibration phase.

---

## What You End Up With

The ECT-4C looks like the ECT-4 with four antennas instead of one, arranged in different directions, attached with copper wire and epoxy. It looks like an antenna farm. It is slightly unwieldy.

**Performance change:**

**Broadcast radius:** Extended from approximately 4 meters to approximately 18 meters — sufficient to cover an entire standard ICS floor section, or two-thirds of the Level 4 cafeteria.

**Multi-node coverage:** At 18m radius, the ECT-4C simultaneously reaches multiple EIMU sensor nodes. The false signal registers across all of them simultaneously. Instead of one node logging a false reading, the ECT-4C produces a coordinated false reading across a network area — making the false signal more convincing (multiple-node consensus is harder for the monitoring system to flag as anomalous than single-node deviation) and covering a wider area.

**The Phase 5 use:** The player activates the ECT-4C at Junction B, broadcasting "Compliance: High — Sustained" at maximum amplitude for 40 minutes during the Level 5 sweep of the residential floors. Every EIMU node on Levels 3 and 4 reads a sustained compliance spike. K-7's monitoring note: "Compliance index surge, Levels 3–4, 40-minute window. Reviewing for BES optimization trigger — possible environmental effect." It is logged as an environmental success, not an anomaly. The sweep finds nothing unusual because the EIMU system is telling the sweep team that nothing is unusual, and the sweep team trusts the EIMU system.

They built the EIMU system. They should know better than to trust it completely. But they do.

---

## What It Means

The EIMU system was built to read emotions. The ECT-4 was built to calibrate the system that reads emotions. The ECT-4C broadcasts false emotions at scale across an 18-meter radius. The sweep team's own monitoring infrastructure tells them the area is calm.

The player made a calibration tool into a lying machine, using antenna components from the sensor network itself.

The EIMU system is now reading its own maintenance equipment and calling it a human being.

---

*→ See: weapons/compliance/EIMU-Jammer — Emotional Interference Unit — for the base tool.*
*→ See: MODIFICATIONS.md — Junction B specifications.*
*→ See: B-01 — K-7's EIMU anomaly flag. The system the player is now feeding false data to on a 18-meter scale.*
