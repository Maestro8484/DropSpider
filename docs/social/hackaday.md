# Hackaday.io project page

When: after the YouTube video and once the README shows the photos (Hackaday wants a cover image: use the best porch photo, and the video link in the first log). Project name: DropSpider. Tags: halloween, esp32, stepper, mmwave, 3d printing.

---

**One-liner field (under 140 characters):**

A porch spider that drops on whoever walks up to the door, winds itself back up, and waits for the next one. ESP32, stepper, mmWave radar.

**Description:**

Somebody walks toward my front door. A 24 GHz mmWave radar on the device sees how far away they are and that they're coming closer, and a foam spider drops out of the dark, timed to land about when they get there. Walking away, walking past or standing still does nothing. Then a stepper motor winds it back up until a bead on the line clicks a switch, a servo finger drops into the spool's ratchet teeth, and everything switches off. The finger holds the spider with no power, so armed and waiting it draws almost nothing.

**The mechanism**

A NEMA 11 stepper turns a 6 mm steel rod through a coupler. The spool rides the rod on a one-way needle clutch (an HF0612). On the drop the motor spins fast in the unwind direction and the spool runs down behind it: the clutch lets the spool lag but never overrun the motor, so the motor sets how fast the spider falls and where it stops. On the rewind the clutch locks and the motor winds the spider home. The spool's far wall is a separate flat cap screwed on, because a wall printed as part of the barrel can only be a 45 degree ramp and the line walked up it.

Basically the lesson of the first version: a one-way clutch only free-spins in the direction the motor can drive it, so a free-fall drop can never be wound back by the same motor. The drop has to be motor-led.

**The trigger**

A DFRobot C4002 reports distance, speed and direction over serial ten times a second. The rule fires on two readings in a row of someone approaching within a set distance, or arriving within a lead time for a fast walker, then waits for the doorway to clear before it re-arms. The radar's OUT pin is wired as a backup trigger if the serial link goes quiet.

**The page**

The ESP32 serves its own web page. Every button sends a console command and the page shows the board's log, so the page and the USB console always agree. Drop it, bring it home, set how far it falls, watch the radar live, update the firmware over WiFi. Every build carries a version read from git, so the page says exactly what's on the board.

**Components**

- ESP32 DevKit V1 (30 pin)
- BIGTREETECH TMC2209 on an expansion board
- STEPPERONLINE NEMA 11 stepper, 0.67 A
- SG90 (or MG90) micro servo
- HF0612 one-way needle bearing, 606ZZ ball bearing, 6 mm x 100 mm rod, 5 to 6 mm coupler
- DFRobot C4002 24 GHz mmWave radar (SEN0691)
- KW12-3 roller micro switch
- MP1584EN 5 V buck, 12 V 2 A adapter
- Bonded nylon upholstery thread, size 69 (its stretch is the shock absorber)
- 3D printed bracket, spool, cap, finger, spacers, fairlead block and flap, radar case and mount (PLA; the finger in PETG). Every part is Python code that writes and checks the STLs.

Over 500 drops so far over the inside of my front door, each one winding home and locking. The porch beam install is next.

Everything is on GitHub under MIT (the radar case is CC BY-NC-SA, after a MakerWorld enclosure): https://github.com/Maestro8484/DropSpider. Build guide, parts list with links, firmware, CAD.
