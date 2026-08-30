"""Subhendu Mukherjee — personal portfolio, served as a Streamlit app.

The portfolio itself is a plain static page in `site/`. Streamlit is only the
host: it hides its own chrome and renders the page full-bleed, so visitors see
the site and nothing else.

Local run:   streamlit run streamlit_app.py
"""

from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

SITE = Path(__file__).parent / "site"

# Assets are inlined as data URIs because Streamlit renders the page inside a
# srcdoc iframe, where relative asset paths have nothing to resolve against.
ASSETS: dict[str, str] = {
    "portrait.webp": "image/webp",
    "qr.png": "image/png",
}

PAGE_TITLE = "Subhendu Mukherjee — Technical Architect"

# Strip Streamlit's header, footer, menu and default padding, and let the
# component iframe fill the viewport so the portfolio reads as a normal site.
CHROME_CSS = """
<style>
  #MainMenu, footer, header[data-testid="stHeader"],
  [data-testid="stToolbar"], [data-testid="stDecoration"],
  [data-testid="stStatusWidget"], [data-testid="stSidebar"] { display: none !important; }

  .stApp { background: #F3EEE5; }

  .block-container,
  [data-testid="stAppViewContainer"] > .main .block-container,
  [data-testid="stAppViewBlockContainer"] {
    padding: 0 !important; margin: 0 !important; max-width: 100% !important;
  }
  [data-testid="stVerticalBlock"] { gap: 0 !important; }

  /* the portfolio iframe fills the window and scrolls internally */
  [data-testid="stIFrame"], .stApp iframe {
    height: 100vh !important; width: 100% !important;
    border: 0 !important; display: block;
  }
  [data-testid="element-container"]:has(iframe) { height: 100vh !important; }
</style>
"""


@st.cache_data(show_spinner=False)
def build_page() -> str:
    """Read the static site and inline its assets as data URIs."""
    html = (SITE / "index.html").read_text(encoding="utf-8")
    for name, mime in ASSETS.items():
        data = base64.b64encode((SITE / name).read_bytes()).decode("ascii")
        html = html.replace(f'"{name}"', f'"data:{mime};base64,{data}"')
    return html


def main() -> None:
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon="🗂️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.markdown(CHROME_CSS, unsafe_allow_html=True)
    # height is a fallback for browsers where the CSS above cannot reach the
    # iframe; the CSS normally overrides it to the full viewport height.
    components.html(build_page(), height=1200, scrolling=True)


if __name__ == "__main__":
    main()
