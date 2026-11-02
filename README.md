# DropSpider

**A Halloween prop that drops a foam spider on whoever walks up to the door, winds it back up, and waits for the next one.**

<!-- video:start -->
<!-- video:end -->

<!-- media:start -->
<!-- media:end -->

![The device turned over on two corner braces on the porch beam, line out through the base](docs/img/inverted_install.png)

*The drawing. Photos and a clip of the real thing dropping go above it as soon as I've shot them.*

## What it is

- Somebody walks toward the door and a 24 GHz mmWave radar on the device sees how far away they are and that they're coming closer. The spider drops out of the dark, 0.5 to 1.2 m, timed to land about when they get there. Walking away, walking past, or standing still does nothing.
- A small stepper motor spins the spool out under power, so the motor sets how fast it falls and where it stops. Then it winds the spider back up until a stopper on the line clicks a switch: home.
- A servo swings a finger into the spool's ratchet teeth and everything switches off. The finger holds the spider with no power. Armed and waiting, it draws almost nothing.
- Everything is run from the board's own web page on your phone: drop it, bring it home, set how far it drops, watch the radar, update the firmware over WiFi.
- All of it on an ESP32, in a 3D printed bracket that sits upside down on two steel corner braces on the porch beam. The printed parts are Python code, so every dimension is a number you can change.

## What it costs, and what you need

- The parts below, about a hundred dollars from Amazon if you own none of it (the exact total is in the table). The ESP32, driver and bearings come in multi-packs, so you'll have spares.
- A 3D printer and about 5 hours of PLA. Nothing needs supports except the bracket.
- A PC with VS Code and the PlatformIO extension, once, to load the firmware over USB. After that, updates go over WiFi.
- A phone on the same WiFi. No app, no account, no cloud.

## Build one

Everything below is in the build guide, `docs/build_guide/build_guide.html`: one page with pictures, wiring to arming. On GitHub it shows as code, so click it, press the download button, and open the file in your browser. A web address for it is coming.

1. Print the parts: the print list in [05_assembly.md](docs/05_assembly.md), section A.
2. Buy what's in the parts table below (guide, section 01).
3. Wire it (guide, sections 02 to 05). Meter the 5 V buck before anything is connected and set the driver to 0.85 V before the motor goes on.
4. Load the firmware: VS Code, PlatformIO, your WiFi name in `secrets.ini`, plug in by USB, double-click `scripts\update_firmware.bat` (guide, section 05c). The board's page then shows the version it runs.
5. Assemble it (guide, section 06; the long form is [05_assembly.md](docs/05_assembly.md)).
6. Power up one layer at a time (guide, section 07), then set it up from the web page at `http://dropspider.local` (guide, sections 08 and 09).
7. Hang it on the beam, walk toward it, arm it (guide, sections 11 and 12; the porch numbers are in [06_installation.md](docs/06_installation.md)).

## Parts

The full list with the "only if" rows is [docs/parts.md](docs/parts.md). Both come from `bom/BOM.csv`.

<!-- parts:start -->
As an Amazon Associate I earn from qualifying purchases. The Amazon links below carry my tag; the price is the same for you.

Parts, if you own none of it: about $94 (today's Amazon prices, 9 items; the printer, filament, a 12 V adapter and screws you may already have). Plus the STEPPERONLINE NEMA 11 bipolar 0.67A 6Ncm: the listing I bought from is gone (it was $21), so its link is a search for the same part.

| Part | Qty | Where | Note | Price |
|---|---|---|---|---|
| **Brain and power** | | | | |
| ESP32 DevKit V1 30-pin CP2102 USB-C (3 pk) | 1 | [Amazon](https://www.amazon.com/dp/B0CR5Y2JVD?tag=maestro8484-20) | a 3 pack; the 38-pin NodeMCU-32S works too, same pin numbers | $16.99 |
| 12 V 2 A adapter with screw-terminal jack | 1 | [Amazon](https://www.amazon.com/dp/B01AZLA9XQ?tag=maestro8484-20) | 12 V for the motor; the buck makes 5 V from it for everything else | $8.99 |
| MP1584EN mini buck module fixed 5 V out 5 to 30 V in | 1 | any | fixed 5 V out; meter it before anything is connected | |
| snappable protoboard (one quarter used: 17 x 19 holes) | 1 | any | the ESP32 sits on one quarter of it in sockets (build guide, section 05b) | |
| 15-pin female socket strip | 2 | any | the ESP32's sockets | |
| male header pins | about 20 | any | signal and power pins on the protoboard | |
| dupont jumpers female-female and 22 AWG wire + heat shrink | 1 set | any | signals by jumper; the 12 V run in 22 AWG | |
| 4-conductor cable 1 m or dupont extensions | 1 | any | radar and switch leads round the end of the base to the board | |
| 5.5 x 2.1 mm DC extension cable 3 to 5 m | 1 | any | 12 V from the outlet up to the beam | |
| **Motor, drive and lock** | | | | |
| STEPPERONLINE NEMA 11 bipolar 0.67A 6Ncm (round shaft) | 1 | [Amazon search](https://www.amazon.com/s?k=STEPPERONLINE+NEMA+11+bipolar+0.67A+6Ncm&tag=maestro8484-20) (my listing is gone) | set the driver to 0.85 V before it moves (build guide, section 07) | |
| BIGTREETECH TMC2209 V1.3 stepstick | 1 | [Amazon](https://www.amazon.com/dp/B07ZPV4HFP?tag=maestro8484-20) | the stepper driver | $9.99 |
| A4988/DRV8825 stepper driver expansion board (2 pk) | 1 | [Amazon](https://www.amazon.com/dp/B0FQC39GJ2?tag=maestro8484-20) | the driver plugs into this; it has the screw terminal for 12 V | $7.99 |
| SG90 micro servo | 1 | [Amazon](https://www.amazon.com/dp/B072V529YD?tag=maestro8484-20) | swings the finger that locks the spool; an MG90 works too | $19.99 |
| uxcell 5 to 6 mm rigid coupler L20 D12 | 1 | [Amazon](https://www.amazon.com/dp/B07P5Z25H8?tag=maestro8484-20) | joins the motor shaft to the rod; blue threadlocker on the set screws | $7.79 |
| 6 mm x 100 mm hardened chrome rod | 1 | [Amazon](https://www.amazon.com/dp/B0D2BK3X8P?tag=maestro8484-20) | the axle everything rides on | $7.09 |
| HF0612 one-way needle bearing | 1 | [Amazon](https://www.amazon.com/dp/B0BKY2ZSTR?tag=maestro8484-20) | the one-way clutch inside the spool; comes as a 5 pack; which way round it goes in matters (doc 05, step 1) | $6.79 |
| 606ZZ bearing 6x17x6 | 1 | [Amazon](https://www.amazon.com/dp/B0FQ4WJ8FQ?tag=maestro8484-20) | carries the far end of the rod; comes as a 10 pack | $8.26 |
| **Radar and home switch** | | | | |
| DFRobot Fermion C4002 24 GHz mmWave radar (SEN0691) | 1 | [DFRobot](https://www.dfrobot.com/product-3081.html) | the trigger: a 24 GHz mmWave radar that reports how far away someone is and which way they're walking | |
| KW12-3 micro switch with roller lever (SPDT) | 1 | any | the home switch, under the base in the fairlead block | |
| **Screws and small hardware** | | | | |
| M2 x 12 screws | 2 | any hardware store | limit switch to the fairlead block | |
| M2 bolt 16 to 20 mm | 1 | any hardware store | the flap's hinge pin | |
| 1.75 mm filament (10 mm piece) | 1 | any hardware store | a 10 mm scrap of printer filament the line is tied round inside the spool | |
| M3 bolt 25 to 30 mm + M3 nut | 1 | any hardware store | the radar case's pivot bolt | |
| M3 x 12 screw | 2 | any hardware store | fairlead block to the base | |
| M3 x 10 bolt + M3 nut | 2 | any hardware store | radar mount to the base | |
| steel corner brace 6 in + screws for the beam and bolts for the base | 2 | any hardware store | two 6 inch steel corner braces hold the device on the beam; the bolts through the base are yours to place (doc 06) | |
| M3x8 self-tapping or machine screws | 3 | any hardware store | spool cap to spool body | |
| M2.5x6 screws | 4 | any hardware store | motor to the motor plate | |
| **Line and spider** | | | | |
| bonded nylon upholstery thread size 69 (Tex 70) black (0.29 mm; 11 lb; about 22 percent stretch) | 2.2 m | [WAWAK](https://www.wawak.com/) or any sewing supply | limp thread that lies flat on the spool and stretches, which is the shock absorber; 7 ft is plenty | |
| 8 mm hard plastic bead (the stopper on the line) | 1 | any | the stopper: slides on the line and lifts the flap when the spider is home | |
| small fishing barrel swivel (size 10 to 14) | 1 | any | between the stopper and the spider | |
| soft foam spider about 13 g brought to about 30 g with added weight | 1 | any | a soft foam spider only, weighted to about 30 g; keep it under 60 g | |
<!-- parts:end -->

## The files

| Open this | For |
|---|---|
| `docs/build_guide/build_guide.html` | **start here to build one.** One page, wiring to arming, with pictures |
| `docs/parts.md` | every part with a link, and what it's for |
| `docs/05_assembly.md` | the print list (section A), then assembly step by step with pictures |
| `docs/06_installation.md` | the porch: heights, the braces, the line length, safety |
| `docs/07_commissioning.md` | the bench checklist, each step with its pass mark, and what to do when something fails |
| `docs/04_firmware.md` | what the firmware does, how to load it, every command, the web page |
| `docs/01_mechanical_design.md`, `docs/02_electrical.md`, `docs/03_sensor.md`, `docs/09_fairlead_switch.md` | the design in depth: the parts on the rod and the lock, the wiring and power, the radar and its trigger rule, the flap and switch under the base. `docs/wiring_guide.html` is the wiring as one printable page |
| `docs/08_open_items.md` | what's proven, what isn't, what could stop your build |
| `cad/` | every printed part as Python (`cad/generate.py` and friends; `cad/README.md` says how), the STLs in `cad/stl/`. Old parts in `cad/retired/`: don't print those |
| `platformio.ini`, `src/`, `include/` | the firmware, standard PlatformIO layout, for a 30-pin ESP32 DevKit V1 |
| `secrets.ini.example` | copy to `secrets.ini`, fill in your WiFi and an update password. `secrets.ini` never goes to GitHub |
| `scripts\` | double-click tools: `update_firmware.bat` (load the firmware by WiFi or USB), `check_repo.bat` (check the files), `add_photos.bat` and `publish_prep.bat` (mine: photos into this page, regenerate everything) |
| the working files | `ROADMAP.md` (what's still to do), `CHANGELOG.md` (what got done, newest first), `docs/commissioning_log.md` (every bench result, failures included), the briefs `docs/handoff_task1_firmware.md`, `docs/handoff_sensor_bearings.md`, `docs/handoff_flash11_page_sleep_led.md`, `docs/handoff_amazon_prices.md`, and the reference notes `docs/M1_fix_handoff.md`, `docs/audit_spider_runaway.md`, `docs/audit_webui_horizon.md`, `docs/PUBLIC_FACE_REVIEW_2026-11-02.md` |

Every firmware the PC builds carries a version read from git, shown on the page's Status card: `fw-16` is the sixteenth firmware that went onto my board, `fw-16+3.91261ef` is three changes past it. Details in `docs/04_firmware.md`.

## Where it stands

Built and running. It has hung over the inside of my front door since October 2026, fired by the radar, more than 500 drops counted on the board, each one winding home to the switch and locking. Halloween night it ran there. What's next is on the roadmap: the new firmware that measures the thread itself, then the braces on the porch beam. What isn't proven yet is in `docs/08_open_items.md`, and the bench log has every result, failures included.

The name `dropspider-tiltspool` is kept for Mechanism B (a servo tilts the spool and the spider free-falls). Not started.

Project page: https://theschmidtwithin.com/bench/#dropspider

## License

MIT for all of it, firmware, tools, CAD, printed parts and docs, by Joe Schmidt. The one exception is the C4002 radar case, drawn after a MakerWorld enclosure and carrying its CC BY-NC-SA terms. All of it in `LICENSE`.

As an Amazon Associate I earn from qualifying purchases.
