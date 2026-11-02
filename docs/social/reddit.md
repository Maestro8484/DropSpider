# Reddit

When: after the video is on YouTube (or the clip is in hand to drag into the post). Reddit shows a video post as a tile that plays in the feed; a text post is a grey card nobody opens. So each of these is a VIDEO post: drag the side-view clip into the post box (under 1 GB, under 15 min; the 10 s clip is fine), put the title in, and paste the text as the first comment. A title can never be edited, so read it twice. No link in the title. One sub per day, not all three at once (Reddit's spam filter).

---

## r/halloween

**Title (under 100 characters):**

Built a porch spider that drops on whoever walks up, then climbs back and waits for the next one

**First comment:**

My son walking up in costume, phone from the side. The second angle is the doorbell camera.

A radar on the device sees someone coming toward the door and how fast, and drops a foam spider out of the dark so it lands about when they get there. Walking away or standing still does nothing. Then a little stepper motor winds it back up until a bead on the line clicks a switch, a finger drops into the spool's teeth, and everything shuts off. It holds up there with no power. Over 500 drops so far over the inside of my front door, and it ran Halloween night.

Everything's run from a web page on your phone: drop it, bring it home, set how far it falls, watch the radar.

It's all free on GitHub if you want one: the 3D printed parts, the wiring, the firmware, a one-page build guide and the parts list with links. About $115 in parts if you have none of it, plus a printer.

https://github.com/Maestro8484/DropSpider

---

## r/3Dprinting

**Title:**

A spider-dropping porch prop: all the mechanism parts are 3D printed, including the one-way clutch spool

**First comment:**

The clip is the thing working. The print side, since that's what this sub cares about:

The whole mechanism rides a 6 mm steel rod: a printed spool with a one-way needle bearing pressed into it, a ratchet with teeth printed right into the spool's face, a servo finger that drops into those teeth, spacers, and a bracket that holds the motor and the far bearing. On the drop the motor spins ahead and the spool follows it down on the clutch, never faster than the motor, so the motor sets the speed and where it stops. All PLA except the finger (PETG). Only the bracket needs supports.

Every part is Python code, not a CAD file. Change a number, run it, and it writes the STLs and checks them (watertight, 2 mm clearance round the spinning spool, the finger actually seats in a tooth gap). The print list says which way each part sits on the bed.

The hard-won bits: printed holes come out 0.2 to 0.3 mm small on my printer, so every fit is drawn oversize; the spool's far wall is a separate flat cap screwed on, because a wall printed as part of the barrel can only be a 45 degree ramp and the line walked up it; and the lock finger needs a 20 degree bevel on its tip or it never seats.

The STLs, the print list and the build guide, all on GitHub: https://github.com/Maestro8484/DropSpider

---

## r/esp32

**Title:**

ESP32 + TMC2209 + mmWave radar: a porch spider that drops on people approaching, with a web page for everything

**First comment:**

An ESP32 DevKit V1, a TMC2209 driving a NEMA 11 through FastAccelStepper, an SG90 for the lock finger, a KW12-3 roller switch as the home sensor, and a DFRobot C4002 24 GHz mmWave radar as the trigger. The radar reports distance, speed and direction over serial; the rule fires on two readings in a row of someone approaching within a set distance, or arriving within a lead time for a fast walker. Its OUT pin is wired as a backup trigger if the serial goes quiet.

The board serves its own page (no app, no cloud): every button sends a console command and the page shows the board's log, so the page and the USB console always agree. Settings live in NVS. OTA updates over WiFi after the first USB flash. Every build is stamped with a version read from git, so the page says exactly what's on the board.

The part I got wrong first: a one-way clutch only free-spins in the direction the motor can drive it. So the drop is motor-led: the motor runs ahead in the unwind direction and the spool lags behind on the clutch. Dropping with the driver off never worked (too much drag on the unpowered motor).

Code, wiring and the build guide: https://github.com/Maestro8484/DropSpider
