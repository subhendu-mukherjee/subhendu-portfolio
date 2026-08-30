# Subhendu Mukherjee — Portfolio

A one-page personal portfolio (Technical Architect · Cloud, AI/ML & Distributed
Systems), served as a Streamlit app.

The portfolio itself is a plain static page — `site/index.html` — with no build
step, no framework and no JavaScript. Streamlit is only the host: it hides its
own chrome and renders the page full-bleed.

```
streamlit_app.py        Streamlit host (hides chrome, inlines assets, renders the page)
requirements.txt        streamlit
.streamlit/config.toml  theme + server defaults
site/index.html         the portfolio (responsive: desktop / tablet / phone)
site/portrait.webp      headshot, transparent background
site/qr.png             QR code to linkedin.com/in/mukherjee-subhendu
```

## Run it locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Opens on http://localhost:8501.

To preview just the site without Streamlit:

```bash
python3 -m http.server 8000 --directory site
# then open http://localhost:8000
```

## Deploy to Streamlit Community Cloud

1. Create a **public** repo on GitHub (e.g. `subhendu-portfolio`).
2. Push this folder (it is already a git repo with an initial commit on
   `main`, so you only need the remote):

   ```bash
   git remote add origin https://github.com/<your-username>/subhendu-portfolio.git
   git push -u origin main
   ```

3. Go to <https://share.streamlit.io>, sign in with GitHub and authorise it.
4. **Create app → Deploy a public app from GitHub** and fill in:
   - Repository: `<your-username>/subhendu-portfolio`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
5. Deploy. You get a URL like
   `https://<your-username>-subhendu-portfolio.streamlit.app` — editable under
   the app's **Settings → General → App URL**.

Every push to `main` redeploys automatically.

> Community Cloud sleeps free apps after a period of inactivity; the first
> visit after that takes a few seconds to wake. If you want a link that is
> always instant for recruiters, the same `site/` folder also works as-is on
> GitHub Pages or Netlify with no Python at all.

## Editing

Content and styling live entirely in `site/index.html` — copy is plain HTML and
the design tokens (colours, fonts, spacing) are CSS custom properties at the top
of its `<style>` block:

```css
--paper: #F3EEE5;   /* background   */
--ink:   #17150F;   /* text         */
--accent:#C05B3B;   /* terracotta   */
```

Breakpoints: 1080px, 900px (side rails hide, hero stacks), 560px.

`streamlit_app.py` only needs touching if you add a new image to `site/` — add
its filename to the `ASSETS` map so it gets inlined.
