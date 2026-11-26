# Copy Audit: daily-reach (Neon)

## Issues Found and Changes Made

### Metadata and Manifest (`index.html`, `site.webmanifest`)
- Page `<title>`: expanded from bare `Reach` to `Reach: Movement for the time you have` so tabs and bookmarks identify the site clearly.
- Meta, OG, Twitter, and manifest descriptions: replaced vague `Focused` and jargon `time-first` with plain `Guided mobility and strength routines` matching the app's timer and library.
- OG/Twitter titles, `og:image:alt`, and manifest `name`: removed em dashes, used colons, and described the card contents in `og:image:alt`.

### Interface Copy (`index.html`)
- Home resume card: changed eyebrow `Continue` to `Continue session` to match `Start session` and `Discard saved session`.
- Library count and loading state: removed the em dash and figurative `read them like a book` / `Loading the shelf…`; replaced with plain `Read through or filter by type and tag.` and `Loading moves…`.
- Library tag filter chips: changed `Every tag` to `All tags` for consistency with `All`, and applied sentence case (`Toe-touch`, `Pull-up`, `Mobility`, `Strength`, `Recovery`) to match `Yoga` and `Calisthenics`.
- Move illustrations (`moveCard`, `paintIllus`): normalized fallback text from `illustration · ...` to `Illustration: <Name>` and improved image `alt` text to `<Name> illustration` instead of repeating the heading verbatim.
- Routines intro: replaced figurative `Curated playlists of library moves` with plain `Guided sequences built from the move library. Start a timer or read through the steps.`
- Routine detail buttons: clarified `Resume at N` to `Resume at step N` and explicit destructive label `Delete` to `Delete routine`.
- Routine builder: clarified `Name it` to `Routine name`, `Pick moves below to start.` to `Select moves below to add them to your routine.`, and default saved note `Your routine.` to `Custom routine.`
- Player cues and next preview: replaced em dashes in the `A thought to sit with`, `Then`, and `Next` prefixes with colons, and changed vague `Last one.` to `Last move.`

### Exercise and Routine Copy (`reach-data.js`)
- Punctuation: replaced all 18 em dashes and 2 en dashes in user-facing cues, move text, routine names/notes, rep ranges (`8 to 12 reps`), and check-in replies with periods, colons, parentheses, or `to` (also improves spoken audio cues).
- Routine naming consistency: changed the Home and Traveling pull-up routine titles from lowercase `Pull-up` with em dashes to `Pull-Up Work: Home` and `Pull-Up Work: Traveling` to match `Pull-Up` capitalization across the move library.
- Directional clarity in `thread_needle`: made instructions side-neutral (`slide one arm under the other`) because the routine plays it separately for Right side and Left side.
- Wording fixes: removed repetition in `plank_hold` (`Brace as if bracing` -> `Brace your core as if expecting`) and aligned `cobra` (`Lying on the front` -> `Face down`) with `superman` and `ytw`.

## Left Alone on Purpose
- Home tagline (`Everything out of reach is just training away.`) and `og-card.svg` / `og-card.png`: personal tagline authored by Stephanie and baked into the social card image.
- `THOUGHTS` array in `reach-data.js`: personal reflections authored by Stephanie; kept verbatim.
- `credit: 'Sequence by Emma'` and personal yoga cues (such as Warrior 2 and Standing Split): preserved exact phrasing aside from replacing em dashes with periods.
- British spellings (`centre`, `mobilisation`) and existing routine note voice: kept author's spelling conventions and tone.
- `towel_row` safety setup wording (`securely latched door handle (hinge side, door open)`): left untouched to avoid altering physical safety instructions without verification.
- Move data `mins`, step durations, tags, and IDs: left unchanged per scope rules.

## Not Done (Next Pass)
- Empty states for zero-match filter combinations in Library (for example, Calisthenics + Toe-touch) and missing routine IDs in `renderRoutine` need markup/logic changes.
- Singular/plural grammar (`1 moves`) in the routine builder summary needs a small logic update.
- Missing `aria-label` attributes on builder duration inputs and remove (`×`) buttons need DOM attribute additions.
- Static `og-card.png` and `og-card.svg` were not rebuilt (no build/asset pipeline run).
