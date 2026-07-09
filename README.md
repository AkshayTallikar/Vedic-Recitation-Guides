# Vedic Recitation Guides

This workspace has two independent guides, joined by a landing page at [`index.html`](index.html):

- **[`sadachara-website/`](sadachara-website/)** — a searchable, categorized reference collection of
  127 individual shlokas (Devanagari, IAST, meaning, ritual action, audio) extracted from the
  *Sadāchāra Saṅgrahaḥ* manual. See [`sadachara-website/README.md`](sadachara-website/README.md).
- **[`site/`](site/)** — the Deva Pūjā Paddhati step-by-step walkthrough described below.

Each site links back to the landing page via a small "← All guides" pill in its header.

---

# Deva Pūjā Paddhati — Recitation Guide

An interactive, single-page guide to the **Deva Pūjā Paddhati** (ದೇವಪೂಜಾ ವಿಧಾನ) of the
Mādhva (Dvaita) tradition. The page has **three tabs**, each built from a different instructional video:

1. **Detailed · 56 min** — [*Deva Pooja Paddhati*](https://www.youtube.com/watch?v=hTSDBlRFJkQ),
   Vid. Sriramavittala Achar (JnanaGamya Prasarana) — **47 steps**.
2. **Concise · 35 min** — [*Deva Pooja Paddathi*](https://www.youtube.com/watch?v=dNfaFhNGfaY),
   SCT — a shorter, musically-chanted version — **29 steps**.
3. **Sung · 67 min** — [*Madhwa Sampradaya Devara Pooje*](https://www.youtube.com/watch?v=sxnnYn9Iu94),
   Nithya Devatharchane — a fully-sung rendition with bhajans and a closing discourse — **38 steps**.

For each step you get:

- 🔊 an **audio clip** cut from the original recitation (with a sticky player + slow-down speeds for practice),
- 📜 the mantra in **romanised IAST** (readable Sanskrit),
- 🌷 a plain-English **meaning** of what the step accomplishes,
- ▶ a link to **watch that exact step on YouTube**.

> **Please note:** the IAST and translations follow the standard Mādhva paddhati recited in the
> video. Steps marked **`verify`** were reconstructed from the audio. This is a *practice and memory
> aid* — confirm exact wording with an authoritative text or your ācārya before ritual use.

## View it

`site/index.html` is **self-contained** — just **double-click it** (or drag it into a browser) and
it works, no server needed. The only external thing it reads is the `audio/` folder next to it, so
keep `index.html` and `audio/` together.

If your browser blocks local audio playback on `file://` (rare — mainly older Safari), serve it instead:

```bash
cd site
python3 -m http.server 8000
# open http://localhost:8000
```

## Publish on GitHub Pages

1. Create a new repository on GitHub and push this project to it:
   ```bash
   git init
   git add .
   git commit -m "Deva Pūjā Paddhati recitation guide"
   git branch -M main
   git remote add origin https://github.com/<you>/<repo>.git
   git push -u origin main
   ```
2. On GitHub: **Settings → Pages**.
3. Under *Build and deployment*, set **Source = Deploy from a branch**, **Branch = `main`**,
   **Folder = `/site`**, then **Save**.
4. After a minute your guide is live at `https://<you>.github.io/<repo>/`.

   > Note: `/site` only publishes this guide. To publish the combined landing page too (linking to
   > both this guide and `sadachara-website/`), set **Folder = `/ (root)`** instead — both sub-sites'
   > relative links (`../index.html`, `sadachara-website/index.html`, `site/index.html`) work either way.

## Save as PDF

Open the page in a browser and **Print** (Ctrl/Cmd-P) → *Save as PDF*. A print stylesheet hides the
player and controls and lays out the mantras and meanings cleanly.

## Project layout

```
index.html            ← landing page linking to sadachara-website/ and site/
sadachara-website/    ← the other guide (127-shloka reference collection); see its own README
site/                 ← everything GitHub Pages serves
  index.html          ← the whole app, self-contained (layout + both guides + player)
  data.js             ← guide 1 content: 47 steps (IAST + meanings) ← edit here
  data2.js            ← guide 2 content: 29 steps                    ← edit here
  data3.js            ← guide 3 content: 38 steps                    ← edit here
  app.js              ← script source (tabs, player, search, navigation)
  audio/              ← guide 1: 47 mp3 clips
  audio2/             ← guide 2: 29 mp3 clips
  audio3/             ← guide 3: 38 mp3 clips
  .nojekyll
build/                ← kept locally, not published
  sections.json       ← guide 1 step boundaries (timestamps)
  sections2.json      ← guide 2 step boundaries
  sections3.json      ← guide 3 step boundaries
  cut_audio.py        ← re-cuts the mp3 clips from source audio (all guides)
  inline.py           ← rebuilds the self-contained index.html
  index.template.html ← template used by inline.py
README.md
.gitignore            ← excludes source*/ and build/
```

### Editing the content

Each guide's Sanskrit and translations live in [`site/data.js`](site/data.js) (guide 1) and
[`site/data2.js`](site/data2.js) (guide 2) as simple lists. Because `index.html` is self-contained,
after editing a `data*.js` (or `app.js`) **rebuild** the page:

```bash
python3 build/inline.py     # regenerates the self-contained site/index.html
```

Step boundaries are in `build/sections.json` / `build/sections2.json`; re-cut clips only if you change
those:

```bash
python3 build/cut_audio.py           # both guides
python3 build/cut_audio.py sct       # just guide 2  (needs source2/full_audio.mp3)
```

### Adding another video as a new tab

1. Download its audio to `sourceN/full_audio.mp3`.
2. Add a `build/sectionsN.json` with the step boundaries and register it in `build/cut_audio.py`.
3. Create `site/dataN.js` (copy the shape of `data2.js`, with a unique `key` and `audioDir`).
4. Add `dataN.js` to the `SCRIPTS` list in `build/inline.py` and the `<script>` tags in
   `build/index.template.html`, then run `python3 build/inline.py`.

## Credits

Recitation and original video © **JnanaGamya Prasarana / Vid. Sriramavittala Achar**. The audio clips
are excerpts from that video, included here for personal study and practice. Please support the
original creators and refer to the [source video](https://www.youtube.com/watch?v=hTSDBlRFJkQ).
