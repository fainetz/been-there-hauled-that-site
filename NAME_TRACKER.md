# Business name tracker

**Current name:** Been There, Hauled That
**Previous names:** Haul for Hope (Nov 17, 2026, never used publicly)

## How to rename

### 1. Website + every blog post (automatic)
1. Edit `site_config.json`: change `name`, `name_part_1` and `name_part_2` (the two halves shown in two colors in the logo).
2. Run `python3 build.py`.
3. Commit and push. Render redeploys in about a minute.

This updates the home page, every blog post, page titles, Google/AI schema data, `llms.txt` and the sitemap.
Never type the name directly into `index.html` or a blog post. Edit `index.template.html` / `build.py` and use the config.

### 2. Places outside the website (manual)

| Where | What to change | How | Status |
|---|---|---|---|
| Facebook page | Page name + bio | Page settings → Name (Facebook reviews name changes; may take a few days and limits how often) | Name: Been There, Hauled That. Bio updated Nov 17, 2026: "Same-day junk removal in Eagan & the South Metro. 10-20% of every job helps a homeless shelter or a dog rescue, and you get a photo & video of who it helped." Location: Eagan. Website link not added yet |
| MN Secretary of State | LLC legal name (now **Breathe & Getaway AI L.L.C.**) | Amendment to Articles of Organization, $55 online | Not renamed yet. Plan: rename when the first customer books |
| Render | Service name / URL `been-there-hauled-that.onrender.com` | The onrender.com address can't be renamed; add a custom domain instead | Using onrender.com |
| GitHub | Repo `fainetz/been-there-hauled-that-site` | Repo Settings → rename (Render follows it) | Optional |
| Profile picture, cover photo, van photos | Text on the van | Regenerate the images with the new name | `~/Desktop/Been There Hauled That pfp/` |
| Google Business Profile | Business name | Profile → Edit | Not created yet |
| Insurance, bank account, payment apps | Business / DBA name | Call or edit in app | Not set up yet |
