# MakerWorld and Printables listing

When: after the README shows the photos (the listing wants real photos of printed parts and the device, plus the video link). Upload the STLs from the print list in docs/05_assembly.md, section A, and nothing from cad/retired. Same text both sites. License on the listing: MIT for all files except the three radar case files, which are CC BY-NC-SA 4.0 (the site makes you pick one license per listing, so pick CC BY-NC-SA for the listing and say in the text that everything but the case is MIT on GitHub).

---

**Model name:**

DropSpider: a porch spider that drops on whoever walks up (ESP32, stepper, mmWave radar)

**Summary:**

The printed parts of a Halloween prop that drops a foam spider on people walking up to the door, winds it back up and waits for the next one. A radar sees them coming, a stepper motor drops the spider under power so it lands where it should, and a servo finger locks the spool with no power. Electronics, wiring, firmware and the one-page build guide are on GitHub.

**Description:**

These are the printed parts. The electronics (an ESP32, a TMC2209 driver, a NEMA 11 stepper, an SG90 servo, a DFRobot C4002 mmWave radar, a roller switch), the wiring, the firmware and the build guide are on GitHub: https://github.com/Maestro8484/DropSpider. The parts list there has links for everything.

What's here, in print order, all PLA at 0.2 mm, 4 walls, 5 top and bottom layers. Every file is already oriented: load it and print it as it lands.

- bracket (1): base down, gyroid 40%, tree supports everywhere. The only part that needs supports.
- spool_onepiece (1): the ratchet teeth, separator and barrel in one piece. Teeth down, 15% infill (it's nearly all walls), no supports. An HF0612 one-way bearing presses into it.
- spool_cap (1): the spool's flat far wall, screwed on with 3 M3x8. Outer face down, lugs up, 15%.
- spacer_A_nose_7_5mm (1) and spacer_B_50mm (1): on end, 100%, 5 mm brim.
- shim_1mm and shim_2mm (2 each): take up end play on the rod. 100%.
- finger (1, print a spare): the lock. Flat top face down, hub up, 100%, 5 mm brim. PETG if you have it.
- fairlead_base (1): the block under the base the line runs through, carrying the flap and the switch. Gyroid 40%, 5 mm brim.
- fairlead_flap_inv (1, print a spare): the hinged flap a bead on the line lifts when the spider is home. Flat side down, 100%.
- c4002_case_base_extended, c4002_case_lid, c4002_case_Swivel_mount (1 each): the radar's snap-lid case and a mount that tilts and swivels. Gyroid 40%, no supports.
- bearing_retainer: only if the 606ZZ sits loose in its seat.

Every part except the three radar case files and the flap is Python code (cad/generate.py and friends, on GitHub): change a number, run it, and it writes the STLs and checks them (watertight, 2 mm clearance round the spinning spool, the finger seats in a tooth gap).

Printed holes come out 0.2 to 0.3 mm small on my printer, so every fit is drawn oversize; your first print may still want a turn of a drill by hand in a hole or two. The build guide says where.

**License:**

MIT for everything except the radar case. The case (c4002_case_base_extended, c4002_case_lid, and c4002_case_base, also on GitHub) is drawn after "DFRobot C4002 mmWave enclosure" by user_643277529 on MakerWorld (https://makerworld.com/en/models/2826754), CC BY-NC-SA 4.0, and carries that license: credit the original, no commercial use, share changes the same way.

**Tags:**

halloween, spider, prop, esp32, stepper, ratchet, clutch, mmwave, porch
