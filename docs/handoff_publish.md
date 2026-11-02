# Brief: make DropSpider ready for strangers (README, parts with links, print and build directions, photos and video, social posts)

One task, for a session running Fable 5.1 at effort HIGH with the owner answering one-line questions. The repo is already PUBLIC on GitHub (checked 2026-11-02 with `gh repo view`: visibility PUBLIC, 0 stars, no topics). This is the polish before it is shared anywhere, and the sharing text itself. Everything that can be a script is a script, so the owner's part is dropping files in a folder and double-clicking a .bat.

## Ground truth

This file is a pointer. The repo wins. If a fact here disagrees with a file, this file is stale: say so and go by the file. Staleness check: `git log -1 --oneline` against `git log -1 --oneline -- docs/handoff_publish.md`; the same hash means nothing landed since this was written.

## Before you start (checks to run now, not facts to trust)

- The measure firmware is on the board and the new thread measured: `grep -n "0d" ROADMAP.md` shows row 0d gone or marked done, and `docs/commissioning_log.md` has a 2026-11 row with a `[measure]` line. If not, this brief waits: the README's status section cannot claim a porch-proven device until it is.
- Read `C:\Users\SuperMaster\.claude\skills\joevoice\SKILL.md` in full, then the voice profile it names. Every human-facing word in this task goes through it.
- Read `C:\Users\SuperMaster\.claude\skills\repo-docs\SKILL.md`: the doc roles, and "existing names win".
- The Amazon Associates tag: `maestro8484-20`, recorded in the ChronoBloom project's memory (`C:\Users\SuperMaster\.claude\projects\C--Users-SuperMaster-Documents-PlatformIO-chronobloom-esp32c3\memory\project_state.md`, "recorded but wired nowhere, owner decision"). The owner said yes on 2026-11-02 ("yes to all 3"): the tag goes on every Amazon link, no need to ask again. Amazon's program rules require a plain disclosure near the links ("As an Amazon Associate I earn from qualifying purchases"); the script writes it.
- `scripts\check_repo.bat` option 1 passes before the first edit (passwords out, doc map complete, no dead links, every STL present). It must pass again at the end.

## Read first, in order

1. `README.md` (the front door as it is: 80 lines, written for the owner's own team, not for a stranger).
2. `docs/build_guide/build_guide.src.html` and `tools/make_build_guide.py` (the one-page build guide and how it is built; this is what a builder follows).
3. `docs/05_assembly.md`, `docs/01_mechanical_design.md` section "Materials and print settings" (the print table), `cad/README.md` (which STLs are current; the owner's own three STLs are never touched).
4. `bom/BOM.csv` (47 rows: 33 have, 1 TO BUY, 3 ONLY IF, 4 ceiling install only, 2 not needed, 1 parked, 1 owner's stock; ASINs are in column `asin_or_part` for the amazon.com rows).
5. `docs/06_installation.md`, `docs/07_commissioning.md` (the new-thread procedure, section A new thread), `docs/04_firmware.md` (the page and commands, for the "what you get" copy).
6. `LICENSE` (MIT, one CC BY-NC-SA exception: the radar case) and `docs/08_open_items.md` (what is not proven; the README must not claim it).
7. The ChronoBloom repo's launch material for the shape that worked before: `C:\Users\SuperMaster\Documents\PlatformIO\chronobloom-esp32c3` (its README, its media locker in `launch.json`, its social text if kept). Borrow the approach, not the words.

## The work, in order

### 1. The name: settled, nothing to ask

The owner said yes on 2026-11-02 ("yes to the removal of inline") and the GitHub repo is now `https://github.com/Maestro8484/DropSpider` (renamed with `gh repo rename`; the old URL redirects). The local folder stays `DropSpider-inline`: Claude's memory for this project keys off the folder path, so do not move it. The git remote, the README link and the build guide link already point at the new name; the GitHub description and topics are set. Mechanism B keeps the name `dropspider-tiltspool` the README reserves. Left for this session: the project page at theschmidtwithin.com, if it links the old URL (the redirect covers it, but fix the text).

### 2. Parts to buy, generated from the BOM, with the owner's Amazon links

Build `tools/make_parts.py`: reads `bom/BOM.csv`, writes `docs/parts.md` (and the same table into the README's parts slot, see step 4) with one row per part a builder needs: item, qty, a link, and the one note that matters. Rules: rows with `source` amazon.com and an ASIN get `https://www.amazon.com/dp/<ASIN>?tag=maestro8484-20` (tag only after the owner's yes; a `--no-tag` switch writes plain links); dfrobot.com rows link to the product page; `any` rows say "any hardware store" or "any" and give the spec. Rows with status `not needed`, `parked`, `ceiling install only`, `owner's stock` and `ONLY IF ...` go to a short second table ("only if...") or are left out; the script decides by status, never by hand. A grouped order: electronics, motion parts, hardware, line and spider. The disclosure line sits above the table. `scripts\check_repo.bat` runs the script and fails if `docs/parts.md` is stale against the CSV (same pattern as the build guide check, read `tools/check_repo.py`). Column `status` keeps its meaning for the owner; a new column is allowed only if the script needs it (for example `group`), and the CSV header line stays the first line.

Prices: the script does not fetch Amazon (their pages block scripts and prices move). The README gives one honest total as a range the owner confirms ("about $X to $Y in parts if you have none of it; the printer, filament and a 12 V adapter you may already own"). The figure comes from `docs/handoff_amazon_prices.md` (roadmap 8d: an Opus session reads his Amazon orders and today's prices into the BOM and writes the total here). If that row is still open when this session runs, the owner said on 2026-11-02 he will give the total "at time of photos": ask in one line when the photos land, and until then the README says "parts total coming"; never invent one.

Parts total (filled by the prices session, 2026-11-02, summed from `bom/BOM.csv` column `price_now_usd`): parts, if you own none of it: about $94 (today's Amazon prices, 9 items; the printer, filament, a 12 V adapter and screws you may already have). Counted: status `have` or `TO BUY` with an Amazon price, spares (notes starting "spare", the LM2596) left out. Not in that figure: the motor (row M1), whose listing is currently unavailable; a replacement listing is owed before the README carries the total, so add it once the BOM has one.

### 3. Photos and video: one folder, one .bat, the README fills itself

The raw originals live outside the repo, as ChronoBloom's do: make `C:\Users\SuperMaster\Documents\_Projects\Projects-Media-Photos-Docs\DropSpider\` (the parent exists; it holds `ChronoBloom\` and `InfinityCube\` and loose July phone files that are not DropSpider's). The owner drops phone photos and clips there, any names, any order. He has not taken photos of the finished device yet (2026-11-02): the README slot under the top picture is marked and empty, roadmap row 8b.

Build `tools/make_media.py` and `scripts\add_photos.bat` (double-click): the script reads that folder, writes web-sized copies into `media/` in the repo (JPEG, 1600 px on the long side, about 300 KB each, Pillow; EXIF orientation applied, GPS and all other EXIF stripped), names them in order `porch_01.jpg` and so on, keeps a `media/captions.txt` the owner can edit (one line per file, `porch_01.jpg: the device on the beam`; the script adds a line for each new file with a placeholder caption and never overwrites a line he changed), and rewrites the README between `<!-- media:start -->` and `<!-- media:end -->` with the pictures and captions. Video: GitHub shows an mp4 inline in a README only when the file was uploaded through the GitHub web editor (drag the clip into the README while editing on github.com; GitHub hosts it and writes the URL); a clip in the repo does not play inline. So the script handles video two ways and the owner picks by what he puts in the folder: an mp4 under 10 MB gets a `media/video.txt` line telling him the one drag-and-drop step on github.com (the script cannot do that step; it is his hand, once), and a `youtube.txt` holding a YouTube or Shorts link gets a clickable thumbnail (the script fetches `https://img.youtube.com/vi/<id>/maxresdefault.jpg` into `media/`) at the top of the README under the title. Both end in the same slot. A clip longer than 20 s or over 10 MB: the script writes a trimmed 10 s copy with ffmpeg if ffmpeg is on the PC (`where ffmpeg`), else says so and leaves it.

The README's top: the video thumbnail (or the drag-and-dropped mp4) first, the best porch photo second, the CAD drawing that is there now third or gone. A stranger decides in three seconds.

### 4. README rewritten for a stranger, in the owner's voice

Shape, top to bottom, the whole thing under about 120 lines: title and one sentence (what it does, said the way the owner says it); the video and photos (step 3); "what it is" in five lines (the drop, the radar trigger, the lock that holds with no power, the phone page, 190 bench drops and the porch); "what it costs and what you need" (the parts total from step 2, a printer, a PC with VS Code once); "build one" as the existing eight steps but each pointing at the build guide section that does it; the parts table (step 2, the short version, full table in `docs/parts.md`); "print these" (step 5); the doc map cut to what a builder opens (build guide, parts, print, assembly doc 05, install doc 06, bench doc 07, firmware doc 04; the handoffs, audits, roadmap, changelog and log get one line between them, "the working files"); the firmware version paragraph cut to two lines; the status section (the README's last heading before License) rewritten from the bench log and roadmap of the day, honest about what is not proven (doc 08); license and the Amazon disclosure. The joevoice skill rules the words: contractions, short sentences, no AI tells, no em dashes, the common part numbers stay (ESP32, TMC2209, SG90, HF0612), process history cut.

The project page `https://theschmidtwithin.com/bench/#dropspider` is linked from the README and the GitHub description: open it in the Browser pane and confirm it exists and says the same thing; if it is thin or missing, write the page text for it in `docs/social/project_page.md` (step 7) for the owner to paste.

### 5. Print directions as one page a builder can follow

Today the print table is in doc 01 under "Materials and print settings" and doc 05 section A says "settings table in 01". A builder wants one list. Write `docs/print.md` (or a "Print" section at the top of doc 05 if that keeps the doc count down; existing names win, so prefer the doc 05 section and have the README and build guide point at it): every STL to print for the inverted install, in print order, with qty, orientation in plain words ("flat side down, the ratchet teeth up"), material (PLA; the finger in PETG if you have it), walls, infill, supports (none, say so per part), and about how long on a Bambu at the owner's stock settings if the `.3mf` beside the STLs carries that number (read it, never slice). The owner's three own STLs (`fairlead_flap_inv.stl`, `c4002_case_base_extended.stl`, `c4002_case_Swivel_mount.stl`) are listed as his, printed as-is. Retired parts (`cad/retired/`, `ld2450_cradle.stl`, `spool_body.stl`, `spool_ratchet.stl`, `spool_shield.stl`, the ceiling-only parts) are listed in one line as "do not print these" with why, or left out, whichever reads cleaner for a builder. The `.3mf` files are mentioned as the owner's own Bambu projects, not as the way to print. Never slice, never suggest print settings beyond what doc 01 already says (owner rule: he controls the slicer).

### 6. The build guide and the assembly doc, read as a stranger

Open `docs/build_guide/build_guide.html` in Chrome (`Start-Process chrome <path>`) and read it start to end as someone who has the parts on the table. Fix in `build_guide.src.html` (then `python tools\make_build_guide.py`): every step says what to do and what you should see; words a non-builder does not know get a gloss the first time (fairlead, stopper, coupler, Vref, buck, OTA, NVS); internal history ("Rev C clutch was backwards") moves out of the guide into the reference doc that holds it; dead ends and "ceiling install" branches are marked so a builder of the inverted install skips them in one glance. Same pass over `docs/05_assembly.md` and `docs/06_installation.md`. Keep the maker's words (firmware, flashed, mmWave, stepper): the owner's voice keeps those.

### 7. Social posts, in the owner's voice, ready to paste

Write `docs/social/` with one file per place, each a paste-ready block plus a one-line note on where it goes and what to attach: `reddit.md` (one post for r/halloween, one shorter for r/3Dprinting, one for r/esp32 or r/arduino; title under 100 characters, the body says what it does, what it cost, the link; no begging, no emojis; Reddit rewards the video first), `youtube.md` (title, description with the parts link and the repo, chapters if the clip is over a minute, tags), `instagram_facebook.md` (a caption, 3 to 5 hashtags, the link in bio line), `x_threads.md` (under 280 characters, one line and the link), `hackaday.md` (a Hackaday.io project description: what, why, the mechanism in three sentences, components list), `makerworld_printables.md` (the listing text for the printed parts, which files, the license line with the CC BY-NC-SA note on the radar case, the link back to the repo for the electronics), `project_page.md` (the theschmidtwithin.com page text if step 4 found it thin). Each file starts with a line saying when to post it (after the video exists, after the parts links are live). The owner's cadence from the voice profile: run-on where he would run on, concrete and tactile, no AI tells, no "excited to share".

### 8. Tie it together and check it

`scripts\publish_prep.bat` (double-click): runs `make_parts.py`, `make_media.py`, `make_build_guide.py`, then `check_repo.py` option 1, and prints what changed. Run the `public-face` skill over README, docs/parts.md, the print page, the build guide and docs/social: attribution drift, stale claims, dead links, placeholders, voice violations. Fix what it finds. Commit by name (`git add "path" "path"`), never a sweep; `cad/stl/DropSpider-inline-v3-invert.3mf` is the owner's and stays unstaged unless he says. Push only when the owner says push.

## Tests (each with its pass mark and where the result goes)

- `scripts\check_repo.bat` option 1: passes, output quoted in the reply.
- `scripts\publish_prep.bat` run twice in a row: the second run changes nothing (idempotent), `git status` shows it.
- Drop two phone photos and one clip into the media folder, run `add_photos.bat`: the README shows both pictures with placeholder captions and the video instruction; change a caption in `captions.txt`, run again: the README has the new caption and the file names did not change.
- Every link in README and docs/parts.md answers 200 (curl from Bash, Amazon links too; an Amazon 503 to curl is their bot wall, open one in the Browser pane instead).
- README read on a phone-width window in Chrome: the video or picture is the first thing on screen under the title.
- Results logged in `CHANGELOG.md` (one line per thing added) and the brief moved to `docs/retired/` when done; roadmap row 8b closes with it.

## Done when

A stranger landing on the GitHub page sees the spider drop in the first screen, knows in five lines what it is and what it costs, can click to every part, can print the list, can follow the guide, and the owner has paste-ready posts for each place, all of it in his voice; and the two .bat files let him add photos and regenerate everything without a session.

## Rules for the session

- The owner is not a developer and reads in a window: never hand him a command; the three things he can be asked are double-click a .bat, change a setting in the app, look at something and answer in one line.
- Joe's voice via the joevoice skill, on every human-facing word; code identifiers and license text untouched.
- No em dashes, en dashes, arrows, emojis or curly quotes anywhere written for him or for the public.
- One change regenerates one thing: never `regen_cad.ps1`, never `--export-all`, never touch an STL; pictures are regenerated only if a doc change needs one.
- Prior art before invention, as a search: a README media-insert script and a BOM-to-links script both exist in the wild (search "markdown readme image gallery generator python", "bom csv to markdown amazon affiliate"); report the table, copy a permissive one if it fits, else build the small form.
- Ask before anything expensive or outward-facing: renaming the repo, pushing, posting. One approval covers that act only.
- The Pi4 at 192.168.1.200 is never touched. `secrets.ini` never leaves the PC.
- Decisions to the owner as one flat numbered list, each with the advice and the question in bold.
