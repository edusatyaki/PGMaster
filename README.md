# PG Master

**Every PostgreSQL function. Exact syntax. Real, executed output.**

A single-page, zero-dependency reference covering **459 PostgreSQL functions, operators and
constructs** across 21 categories. Each entry ships with a runnable example and the *actual*
result — every query in this site was executed against **PostgreSQL 16.14** at build time and its
output captured verbatim. Nothing is hand-written or guessed.

This is the PostgreSQL companion to [SQL-Master](https://github.com/edusatyaki/SQL-Master).

## What's inside

| # | Category | Count |
|---|----------|-------|
| 1 | Math & Numeric | 51 |
| 2 | String & Text | 55 |
| 3 | Binary, Bit & Encoding | 22 |
| 4 | Data Type Formatting | 7 |
| 5 | Date / Time | 30 |
| 6 | Conditional | 8 |
| 7 | Array | 22 |
| 8 | Range & Multirange | 13 |
| 9 | JSON & JSONB | 31 |
| 10 | XML | 15 |
| 11 | Full Text Search | 22 |
| 12 | Aggregate | 40 |
| 13 | Window | 14 |
| 14 | Set Returning | 7 |
| 15 | Sequence | 6 |
| 16 | Network Address | 14 |
| 17 | Geometric | 16 |
| 18 | Enum, UUID & Type Info | 10 |
| 19 | System Information | 32 |
| 20 | System Administration | 29 |
| 21 | Trigger & Event | 15 |
| | **Total** | **459** |

## Design

Styled as the VS Code editor itself, in **Dark+** and **Light+**: activity bar, Explorer
sidebar, editor tab and breadcrumbs, a line-number gutter down the entry list, and the blue
status bar. Function names, signatures and results are set in JetBrains Mono and coloured with
VS Code's own SQL token palette — keywords blue, control flow purple, types teal, function
names yellow, strings rust, numerals green.

## Features

- **Explorer sidebar** listing all 21 sections with entry counts, tracking your position as you
  scroll and updating the breadcrumb and status bar with it.
- **Instant search** across name, signature and description. Sections and contents entries fold
  away as you type.
- **Peek pane** — click any entry for a split editor with the section locator, signature,
  description, the sample data the query runs against, the setup SQL where one is needed, the
  query (syntax-highlighted, with a copy button), and the real result with a row count.
- **Browse without closing** — arrow keys or the pane's prev/next buttons step through the
  current filter, so you can read a whole section in one pass.
- **Keyboard driven** — `/` or `Cmd/Ctrl+K` to search, `↑` `↓` to move through results, `Enter`
  to open, `←` `→` to browse, `F` for fullscreen, `Esc` to close.
- **Fullscreen** from the top bar or the `F` key, for presenting or distraction-free reading.
- **Light and dark**, following your OS by default and remembered per browser.
- **Progress tracking** — mark entries as read from the list or the pane. Stored in
  `localStorage` and survives reloads.
- Fully responsive, no build step to view, and no runtime dependencies. It is one HTML file.

## How the output is verified

`index.html` is generated, not written by hand. The build pipeline is in `build/`:

| File | Role |
|------|------|
| `build/catalog.py` | The catalog: category, function name, signature, description, example SQL and optional setup SQL for all 459 entries. |
| `build/seed.sql` | The demo schema (`employees`, `departments`, an enum, a sequence, a view, an index) that the examples query. |
| `build/run.py` | Runs one example through `psql` inside a transaction that is rolled back, and parses the result into headers and rows. |
| `build/verify.py` | Runs every example and reports any that fail. Used while editing the catalog. |
| `build/build.py` | Runs every example, captures the real output, and renders `build/template.html` into `index.html`. |
| `build/template.html` | The page shell: styles, markup and the client-side JavaScript. |

Nine administrative entries — `pg_terminate_backend`, `pg_switch_wal`, `pg_read_file` and the
like — are **not** executed, because they would disrupt the server or leak local filesystem
paths. Those are clearly labelled "Reference output" in the UI and carry a documented example
result instead.

### Regenerating

```bash
createuser -s pgmaster
createdb -O pgmaster pgmaster_demo
psql -U pgmaster -d pgmaster_demo -f build/seed.sql
python3 build/build.py
```

`build/run.py` points at the Homebrew `psql` binary and the `pgmaster_demo` database; adjust
`PSQL` and `DB` at the top of that file if your setup differs.

## Deployment

Pushing to `main` publishes the site to GitHub Pages via
`.github/workflows/static.yml`.

---

Ideation & development [Satyaki Das](https://github.com/edusatyaki) | PG Master v2
