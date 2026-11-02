# Parts

Every part a builder needs for the inverted install (the device turned over on two steel corner braces on the porch beam), generated from `bom/BOM.csv` by `tools/make_parts.py`. Edit the CSV, not this file. The printed parts are in the print list in `05_assembly.md`, section A.

As an Amazon Associate I earn from qualifying purchases. The Amazon links below carry my tag; the price is the same for you.

Parts, if you own none of it: about $94 (today's Amazon prices, 9 items; the printer, filament, a 12 V adapter and screws you may already have). Plus the STEPPERONLINE NEMA 11 bipolar 0.67A 6Ncm: the listing I bought from is gone (it was $21), so its link is a search for the same part.

## Buy these

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

## Only if

Skip these to start. Each one has a test that says whether you need it.

| Part | Qty | Where | When |
|---|---|---|---|
| 4 mm OD PTFE tube (3D printer kind; 2 mm bore) | 41 mm | any | a guide tube for the line through the base; try it without first |
| 2 mm round elastic cord | 150 mm | any | only if you use braid or fishing line instead of the nylon thread |
| 470 uF 16 V electrolytic capacitor | 1 | any | only if the board restarts when the finger moves |

## Not on this list

- The ceiling install's own screws and anchors (BOM rows N7, H9, H10) are in `bom/BOM.csv`; this list is the inverted install.
- Spares I had on the bench and don't use: ESP32-S NodeMCU 38-pin (ESP-WROOM-32 CP2102); LM2596 buck converter (5 pk).
