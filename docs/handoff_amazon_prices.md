# Brief: prices into the BOM from the owner's Amazon order history, and today's prices for a builder

One task, for a session on Opus with Claude in Chrome (the owner's own Chrome, signed in to amazon.com). It reads what the owner paid for each part, reads what a new builder pays today, writes both into `bom/BOM.csv`, and leaves a parts total the publish brief (`docs/handoff_publish.md`, step 2 and 4) drops into the README. The owner asked for it 2026-11-02: "generate a handoff to an opus level handoff to access and pull from my amazon order history".

## Ground truth

This file is a pointer. The repo wins; if a fact here disagrees with a file, say so and go by the file. Staleness check: `git log -1 --oneline` against `git log -1 --oneline -- docs/handoff_amazon_prices.md`.

## Before you start (checks to run now)

- Claude in Chrome tools answer: load them with one ToolSearch call (`select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__tabs_create_mcp`) and `tabs_context_mcp` lists his open tabs. If the extension is not connected, say so and stop; the built-in Browser pane has no Amazon sign-in and never gets his password.
- `https://www.amazon.com/your-orders/orders` opens in a new tab already signed in. If it shows a sign-in page, tell the owner in one line ("sign in to Amazon in Chrome, then say go") and wait. Never type a password, never a one-time code, never touch payment or address pages.
- `bom/BOM.csv`: header is line 1, `ref,item,qty,source,asin_or_part,status,notes`; 47 rows; the amazon.com rows carry an ASIN in `asin_or_part`. Count them: `grep -c amazon.com bom/BOM.csv`.

## Read first

1. `bom/BOM.csv`.
2. `docs/handoff_publish.md`, step 2 (what the parts table will do with the numbers) and the Amazon tag line (`maestro8484-20`, owner's yes 2026-11-02).
3. `tools/check_repo.py`, the BOM and doc-map checks, so a new column does not break them.

## The work, in order

1. Add two columns at the end of the header: `paid_usd` (what the owner paid, item price before tax, as the order page shows it) and `price_now_usd` (the product page's price today, the main offer, not a used or third-party box). Leave both blank where unknown; never guess. Add `ordered` (date, YYYY-MM-DD) if the order page gives it with no extra work; it is useful on the README's "where it stands" only as "bought in 2026", so it can be skipped.
2. Order history, one part at a time: on `https://www.amazon.com/your-orders/orders` use the search box with the item's distinctive words (the first three or four words of `item`, or the brand), then open the matching order and read the item price and date. Match by ASIN when the order page shows one (the product link in the order carries `/dp/<ASIN>`); a matching name with a different ASIN is a different listing: record the ASIN he actually bought in `asin_or_part` only if the BOM's ASIN is wrong (say so in the reply), otherwise leave the BOM's ASIN. Rows with `source` other than amazon.com (dfrobot.com, WAWAK, any) get `paid_usd` only if a quick search of the orders finds them (the C4002 may be a DFRobot or Amazon order; the thread may be Amazon); otherwise blank.
3. Today's price, one product page each: `https://www.amazon.com/dp/<ASIN>` in the same Chrome, read the price, record it. A page that says the listing is gone or unavailable: write `gone` in `price_now_usd` and list the row in the reply, because the publish session needs a replacement listing for it (a part the builder cannot buy is a README problem). Do not search for a replacement here unless it is the same part under a new ASIN on the first page of results; otherwise leave it to the owner's one-line answer.
4. The total: a Python one-liner over the CSV (never by hand), summing `price_now_usd` for the rows a new builder must buy: status `have` or `TO BUY`, not `not needed`, `parked`, `ceiling install only`, `owner's stock`, nor the `ONLY IF` rows; multiply by `qty` where qty is a count (the thread's `2.2 m` is one spool). Report it as "parts, if you own none of it: about $X (today's Amazon prices, N items; the printer, filament, a 12 V adapter and screws you may already have)" and write that line into the top of `docs/handoff_publish.md` step 2 as the figure, so the publish session does not ask the owner for it. A second figure, the owner's own spend (`paid_usd` summed the same way), goes in the reply only, not in a public file, unless he says to publish it.
5. `scripts\check_repo.bat` option 1 passes with the new columns. Commit `bom/BOM.csv` and `docs/handoff_publish.md` by name.

## Privacy rules for this session

- Read only the rows the BOM needs. Other orders on the page are not read into the reply, the repo, or memory.
- No screenshots saved anywhere; `get_page_text` and `read_page` over the order page are enough. No order numbers, no addresses, no card digits, no account email in any file.
- Nothing is bought, returned, carted, reviewed or clicked beyond opening an order and a product page. The "Buy again" and "Buy now" buttons are never pressed.
- The owner's own spend stays out of public files.

## Tests

- `python -c` over the CSV prints the total and the item count, quoted in the reply.
- `scripts\check_repo.bat` option 1: ALL PASS, quoted.
- Three rows picked at random by the owner, read back to him with the price so he can say "right" in one line.

## Done when

Every amazon.com row has `price_now_usd` (or `gone`), the rows he bought have `paid_usd`, the builder's total is written into `docs/handoff_publish.md` step 2, the check passes, and it is committed.

## Rules for the session

- The owner is not a developer; never hand him a command. He can sign in to Amazon in his own Chrome and answer one-line questions.
- Claude in Chrome is the tool, in his Chrome; the built-in Browser pane and curl are not signed in and get no credentials.
- No em dashes, arrows, emojis or curly quotes in anything written.
- Commit by name. The Pi4 at 192.168.1.200 is never touched.
