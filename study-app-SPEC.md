# Study Notes App: project spec

A personal notes and spaced-review app that works on phone and PC. It keeps the features of the current Obsidian setup, with one system writing both the notes and the review history.

Give this file to Claude (Sonnet) and ask it to build phase 1 first.

## 1. Goal
- One place for study notes, folders, screenshots and formatting.
- Automatic spaced review: what is due today, and when each topic is next due.
- Progress by topic, folder and group, with a pace and an estimated completion date.
- Works on phone and PC, with the same notes.
- Later: a voice tutor that quizzes the user on their own notes.

## 2. Users and platforms
- Single user. No accounts, no multi-user features.
- Phone and PC. Recommended default: a web app installed as a PWA, so one codebase covers both. A desktop wrapper (Tauri or Electron) can come later.
- Decide with the user before building: how the phone and PC sync (see Open questions).

## 3. Data model (keep plain markdown)
Each topic is one `.md` file with YAML frontmatter. The file is the source of truth, so the notes stay readable outside the app.

Frontmatter fields (same names as the current vault):

| Field | Meaning |
|---|---|
| `rag` | `red`, `amber`, `green`, or empty for not started |
| `confidence` | 0 to 5 |
| `subject` | which subject the topic belongs to |
| `group` | importance group: `main`, `secondary`, `extras`, `personal` |
| `first_studied` | date of the first study (YYYY-MM-DD) |
| `last_review` | date of the last review |
| `next_review` | date the next review is due |
| `review_count` | total reviews so far |
| `green_streak` | Green reviews in a row |
| `amber_streak` | Amber reviews in a row |
| `no_review_needed` | `true` keeps the topic out of the review queue (for example, a reference page) |
| `ignore` | `true` hides the topic from every count and list (it is just a note) |
| `estimated_time` | for example `30–40m`, used for the progress estimate |

Folders are real folders on disk. A folder's progress is the count of its topic files that are studied out of its total.

## 4. Review engine
- Rating a topic (Red, Amber or Green) is one action. It updates the note's frontmatter and appends one line to a review history log. Never write one without the other.
- Next review date = `last_review` + step.
- Green ladder: +7, +21, +45, +90, +180 days, plus `review_count`. The step uses `green_streak - 1` as the index, after the streak is updated.
  - Check against the existing plugin before building. In `.obsidian/plugins/study-review-dashboard/main.js`, read `intervalFor` (around line 298) and `markCurrent` (around line 833).
- Amber ladder: +2, +5, +10, +21 days. Read `intervalFor` for the exact extra term.
- Red: +1 day.
- Acceptance examples (use these as tests):
  - Arrays note: Green, `green_streak` 1, `review_count` 5, reviewed 2026-11-24 gives next review 2026-12-06 (+12).
  - Dictionaries note: Green, `green_streak` 1, `review_count` 7, reviewed 2026-11-26 gives next review 2026-12-10 (+14).

### Pause and rest day (two different things)
- **Rest day:** today's reviews become optional. Nothing else changes, and the day's letter (A, B or C) carries over to the next day.
- **Pause:** a global freeze. No review is due while paused. On resume, every `next_review` moves forward by the length of the pause, so nothing piles up.
- Both are switches the user can turn on and off, with the state shown on the Today screen.

## 5. Screens
1. **Today:** due reviews (with an estimated minutes total), today's assignments, the rest-day and pause switches, and an overload warning when more than 25 reviews are due.
2. **Topic:** the note, with a rating row (Red, Amber, Green), the `no_review_needed` and `ignore` flags, and the dates (started, last, next).
3. **Recent reviews:** the history log, newest first.
4. **Revision timeline:** upcoming reviews by day.
5. **Progress:**
   - Counts for each group: studied and remaining out of total.
   - Folder counts, for example `0/1000` topics studied.
   - Per-topic and per-group pace (topics per week) and an expected completion date.
   - An 8-week chart of weekly progress per group.
6. **Weak spots:** every topic rated Red or Amber, sorted by how overdue it is.

## 6. Notes editor
- Markdown editor with folders, titles, formatting, images and screenshots, and a live preview.
- Use an existing editor component (for example, CodeMirror). Don't build an editor from scratch.
- Images are stored in an `attachments` folder next to the notes.
- Titles can be picked up from the first heading.
- RAG badge from the filename: decide the tag format first (see Open questions).

## 7. Phases
1. **Phase 1:** review engine and dashboards. Reads and writes the existing vault. Test with the acceptance examples above.
2. **Phase 2:** phone access. Read and rate on the phone, with sync.
3. **Phase 3:** notes editor, folders and images.
4. **Phase 4:** voice tutor (see section 8).

Don't start phase 2 until phase 1's tests pass.

## 8. Voice tutor (phase 4, optional)
- Talks to the user about today's plan and quizzes them on their own notes.
- Use the rules in `00 Study/10 - Haiku Tutor Instructions.md` as the system prompt. The rules are: ask two quick questions first, then one closed-book question at a time, mark strictly, and suggest a rating.
- Parts: speech-to-text, an LLM, text-to-speech.
- Privacy: company material may be confidential. Keep the tutor on personal notes, or check the company rules before sending any work material to an outside service.

## 9. Things to add beyond the list
- **Drill runner:** run a drill's tests (for example pytest) from the app and show pass or fail.
- **Backups:** the vault is a folder of files. Use Git, or a sync folder with version history.
- **Export:** a plain-text or PDF export of any folder.
- **Offline use:** the phone app must read and rate without a connection, then sync later.
- **Settings:** the review ladders and the pace target, so they can be changed without editing code.

## 10. Non-goals
- No accounts or sharing.
- No editor built from scratch.
- No AI rating decisions. The user always rates the topic.

## 11. Open questions (answer before phase 2)
1. Sync: is it a sync folder (OneDrive, Dropbox, iCloud), Git, or a hosted database?
2. Platform: PWA only, or a desktop app as well?
3. RAG from filename: what does the tag look like (for example `[G]` or `🟢` in the title)?
4. Pause: is a pause always global, or can a single subject be paused?
5. Should the voice tutor run on the phone, the PC, or both?
