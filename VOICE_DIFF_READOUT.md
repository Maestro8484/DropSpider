# Voice readout, 2026-11-02: the public text before and after

What this is: the joevoice skill's PRE/POST readout for the pass that made the README, the build guide and doc 05 read for a stranger. Excerpts only, paired, from the git diff of the commit this file lands in. Scan it before any push; delete the file once read, or keep it as the record.

## README.md

PRE: `**A Halloween prop that drops a foam spider on people walking up to the door, winds it back up and waits for the next one.** This is Mechanism A, the in-line single-axle clutch spool, Rev C.1. A stepper motor, a one-way bearing, a servo-driven ratchet finger and a 24 GHz mmWave radar, all on an ESP32, in a 3D printed bracket that sits upside down on two steel corner braces on the porch beam. Drops 0.5 to 1.2 m. Draws almost nothing while it waits.`

POST: `**A Halloween prop that drops a foam spider on whoever walks up to the door, winds it back up, and waits for the next one.**` then the video and photo slots, then "What it is" in five bullets (the drop, the motor-led spool, the finger that holds with no power, the phone page, the Python parts).

PRE: `## What's in here` with a 30-row table of every file, every handoff and audit on its own row, `A **handoff** is work still to do, written so someone can pick it up cold.`

POST: `## The files`: 12 rows, builder first (build guide, parts, print list, assembly, install, bench, firmware), the four design docs on one row, the working files on one row.

PRE: `2. Buy what's on the TO BUY lines in `bom/BOM.csv`.`

POST: `2. Buy what's in the parts table below (guide, section 01).` and a generated table with a link and a price per part, the Amazon disclosure above it, the total line: `Parts, if you own none of it: about $94 (today's Amazon prices, 9 items; ...). Plus the STEPPERONLINE NEMA 11 bipolar 0.67A 6Ncm: the listing I bought from is gone (it was $21), so its link is a search for the same part.`

PRE: `## Where it stands` ... `about 190 drops so far, radar-fired` ... `What's left is on the roadmap: the last radar walk tests, hanging it on the porch, and a few page refinements waiting for their flash.`

POST: `Built and running. It has hung over the inside of my front door since October 2026, fired by the radar, more than 500 drops counted on the board, each one winding home to the switch and locking. Halloween night it ran there. What's next is on the roadmap: the new firmware that measures the thread itself, then the braces on the porch beam.`

Cut: the Mechanism B paragraph from the top (one line near the end now), the drawing's caption about the fork and the Fusion file, the firmware version paragraph (two lines now), the "Firmware version" heading.

## docs/build_guide/build_guide.src.html

PRE: `Where the board stands: it runs flash 10 (the firmware reports its version on the page's Status card from flash 11 on). About 190 drops on the bench so far ... What's still owed is on the roadmap: the last radar walk tests, flash 11, and the porch.`

POST: `Where it stands: built and running over the inside of my front door since October 2026, more than 500 drops counted on the board, fired by the radar, each one winding home to the switch and locking. Next: the firmware that measures the thread itself, then the braces on the porch beam.`

PRE: `<h3>Electrical parts (all already owned)</h3>`

POST: `<h3>Electrical parts (links and prices in the parts list, docs/parts.md)</h3>` plus a new panel, "Words used on this page": fairlead, stopper, coupler, buck, driver and its pot, dupont, flash, the page.

PRE: `The seat is drawn 17.0 mm from 2026-09-27 (it was 16.8, which would not take the bearing even heated); the print comes out 0.1 to 0.2 small, which is the press. On a bracket printed before then, sand the seat ...`

POST: `The seat is drawn 17.0 mm; the print comes out 0.1 to 0.2 small, which is the press. If it won't go, sand the seat with rolled sandpaper until the bearing presses in.`

PRE: `<b>My build, Rev C.4, against the earlier C.3 one-piece stack:</b> motor side unchanged; on the 606ZZ side take <b>one shim_2mm out</b> (spacer B and its shims now fill 51.25 mm, was 53.0), which leaves 0.25 mm of play ...`

POST: `Spacer B passes through the cap's 11 mm centre hole and bears on the one-way bearing's end, not on the cap: look at that end first, the steel rim should be the highest thing there. Stack spacer B and add shims until the end play is under 0.5 mm, snug but not tight.` (This also fixes a disagreement with doc 05 step 9, which says no shim comes out.)

PRE: `<h3>Measure the line</h3><p>Unwind fully. Barrel knot to stopper, line straight but not pulled: that number is <b>Line length</b> on the web page.</p>`

POST: `<h3>Leave the thread long</h3><p>Don't measure it. Once the board is wired and on its page, <b>Measure the thread</b> (section 09) lets the whole thread out, winds it back counting, and saves the length itself. Tie about 7 ft and move on.</p>`

PRE: `<h3>Line length <b class="chip ready">WORKS</b></h3><p>Enter the measured number (assembly step 13) in <b>Line length</b>, <b>Save settings</b>.`

POST: `<h3>Measure the thread <b class="chip plan">NOT YET FLASHED</b></h3>` with the procedure from doc 07 and the old measure-and-type kept as the fallback until the flash.

PRE: every `FLASH 11` chip (Last cycles card, the hands-on page features, the 5-press sleep).

POST: `WORKS` where the bench log shows the thing used; `NOT TRIED` on the 5-press sleep, which nobody has pressed since it went on the board.

## docs/05_assembly.md

PRE: `## A. Print` ... `All PLA except the finger (PETG if you have it). Settings table in 01_mechanical_design.md. Minimum set: 1 of each part.`

POST: one table, print order, 13 rows: file, qty, how it sits on the bed, infill, supports; my own three files named as mine; one paragraph of what not to print and why.

PRE (step 5): `Wind on about 1.5 m of spare first (two drops' worth): about 10 turns, under one layer on the 3.5 mm barrel, so the drop length changes by about 1 percent. If the line breaks, unwind the spare and retie. Set line to the working length only ...`

POST: `About 7 ft of thread; the board measures it later (step 18). No elastic, no braid.`

PRE (step 9): `**My build, Rev C.4, as a change from the C.3 one-piece stack:** ... If the 2026-10-04 stopgap is fitted (the old spool_shield disc on the far side plus a 2 mm shift shim), take both out. On another frame, stack snug but not tight the same way.`

POST: `Spacer B passes through the cap's 11 mm centre hole and bears on the one-way bearing's far end, not the cap. Look at the bearing's far end first ... Stack snug but not tight, shims to make up the gap, end play under 0.5 mm (mine is 0.36).`

PRE (step 18): `Unwind fully and measure from the barrel knot to the stopper, line straight but not pulled. That is the line value for the firmware.`

POST: `Leave the thread long. Once the board is wired and on its page, Measure the thread (07_commissioning.md, A new thread) lets it all out, winds it back counting, and saves line itself. Until that firmware is on your board: unwind fully, measure ... and enter that as line.`

## docs/06_installation.md

POST, new second paragraph: `Two installs are in this doc. The first half is the ceiling install, drawn first and never built. **The one I'm building is the inverted install**, further down ... If that's yours, skip to it; the build guide covers only that one.`

## Checked after the rewrite

No em dash, en dash, curly quote, ellipsis character or arrow in README.md, docs/parts.md, docs/05_assembly.md, docs/06_installation.md, docs/social/ or the build guide source (grep, 2026-11-02). No "repo", "commit", "ship", "deploy" or the rest of the banned developer words in the README or the posts (grep). Numbers, part names and direction rules unchanged.
