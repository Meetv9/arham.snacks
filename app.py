"""
Arham Snacks — Homemade Nasta Brand Website
Built with Streamlit + Python
"""

import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st

# ────────────────────────────────────────────────────────────────────────────
# CONFIG
# ────────────────────────────────────────────────────────────────────────────

ASSETS = Path(__file__).parent / "assets"

BRAND = {
    "name": "Arham",
    "full_name": "Arham Snacks",
    "tagline": "Fresh • Hygienic • Homemade",
    "sub_tagline": "Crunchy Taste, Pure Trust",
    "since": "2020",
    "blessing": "|| Shri Mahaviray Namah ||",
}

CONTACT = {
    "phone": "+91 8200745911",
    "phone_raw": "918200745911",  # for wa.me links (no + or spaces)
    "email": "arhamsnacks@gmail.com",
    "instagram": "arham.snacks",
    "instagram_url": "https://instagram.com/arham.snacks",
    "address_lines": [
        "107, Brahma Park, Ring Road,",
        "Bharatnagar, Bhavnagar,",
        "Gujarat – 364001",
    ],
    "hours": "Daily • 10:00 AM – 8:00 PM",
    "delivery_note": "Home delivery in Bhavnagar  •  Free delivery on orders above ₹500",
}

CREDENTIALS = {
    "fssai": "20726006000231",
    "udyam": "UDYAM-GJ-05-0087550",
}

# Products from MENU.pdf — image=None falls back to a styled placeholder card
PRODUCTS = [
    {
        "name": "Banana Wafers",
        "ingredients": "Raw Banana & Spices",
        "blurb": "Thin, golden-fried slices of raw banana with a satisfying snap and a whisper of spice.",
        "image": "products/banana_wafers.jpeg",
        "tag": "Classic",
    },
    {
        "name": "Peri Peri Banana Wafers",
        "ingredients": "Raw Banana & Peri Peri Spices",
        "blurb": "Our classic banana wafers reimagined with a smoky, fiery peri peri rub. For the bold.",
        "image": "products/banana_wafers.jpeg",  # same product family
        "tag": "Spicy",
    },
    {
        "name": "Mix Chevdo",
        "ingredients": "Pauva, Sev, Makhana, Puffed Rice, Makkai Pauva, Peanut & Spices",
        "blurb": "A hand-tossed medley of crisp pauva, sev, makhana and puffed rice. A little of everything you love.",
        "image": None,
        "tag": "Bestseller",
    },
    {
        "name": "Diet Chevdo",
        "ingredients": "Papad, Pauva, Peanut, Raw Coconut, Chana & Spices",
        "blurb": "Lighter on the heart, big on flavour. Roasted, never heavy — for the mindful muncher.",
        "image": None,
        "tag": "Light",
    },
    {
        "name": "Banana Chevdo",
        "ingredients": "Raw Banana, Peanut & Spices",
        "blurb": "Crisp slivers of raw banana tossed with peanuts and a curry-leaf tempered masala.",
        "image": "products/banana_chevdo.jpeg",
        "tag": None,
    },
    {
        "name": "Makkai Chevdo",
        "ingredients": "Makkai Pauva, Peanut & Spices",
        "blurb": "Golden makkai pauva with peanuts — a corn-forward chevdo with gentle warmth.",
        "image": None,
        "tag": None,
    },
    {
        "name": "Roti Khakhra",
        "ingredients": "Wheat Flour, hand-roasted",
        "blurb": "Hand-rolled, hand-roasted whole-wheat khakhras. Honest, simple, endlessly snackable.",
        "image": "products/roti_khakhra.jpeg",
        "tag": "Hand-roasted",
    },
]


# ────────────────────────────────────────────────────────────────────────────
# UTILITIES
# ────────────────────────────────────────────────────────────────────────────

def img_to_b64(rel_path: str) -> str:
    """Encode image file to base64 for embedding in HTML."""
    p = ASSETS / rel_path
    if not p.exists():
        return ""
    return base64.b64encode(p.read_bytes()).decode()


def whatsapp_link(message: str) -> str:
    """Build a wa.me deep-link with a pre-filled message."""
    return f"https://wa.me/{CONTACT['phone_raw']}?text={quote(message)}"


def order_link(product_name: str | None = None) -> str:
    if product_name:
        msg = (
            f"Hi Arham Snacks 👋\n\n"
            f"I'd like to order: *{product_name}*.\n"
            f"Could you please share availability, pricing and delivery details?\n\nThank you!"
        )
    else:
        msg = (
            "Hi Arham Snacks 👋\n\n"
            "I'd like to place an order. Could you please share your current menu, prices and delivery details?\n\nThank you!"
        )
    return whatsapp_link(msg)


# ────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title=f"{BRAND['full_name']} — {BRAND['tagline']}",
    page_icon=str(ASSETS / "brand" / "logo_circle.jpeg"),
    layout="wide",
    initial_sidebar_state="expanded",
)


# ────────────────────────────────────────────────────────────────────────────
# CSS — refined, editorial, minimalist (matched to the logo)
# ────────────────────────────────────────────────────────────────────────────

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Sans:wght@300;400;500;600;700&display=swap');

:root {
    --bg:        #E8E5DA;   /* logo background cream-sage */
    --bg-soft:   #F1EFE6;
    --surface:   #FBF9F2;
    --ink:       #1E2218;   /* logo dark, almost-black with green hint */
    --ink-soft:  #4A4E42;
    --muted:     #8B8B7E;
    --accent:    #D8651D;   /* the orange dot from the logo */
    --accent-hi: #B8530E;
    --line:      #C7C2B3;
    --whatsapp:  #25D366;
    --whatsapp-hi: #1FB855;
}

/* ── Global reset / Streamlit overrides ───────────────────────────────── */
html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--ink);
    font-family: 'DM Sans', system-ui, sans-serif;
}
[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }
.block-container { padding-top: 2rem !important; padding-bottom: 4rem !important; max-width: 1200px; }

h1, h2, h3, h4 { font-family: 'Fraunces', serif; color: var(--ink); letter-spacing: -0.01em; }
p, li, span, div { color: var(--ink-soft); }

/* ── Sidebar styling ──────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: var(--bg-soft) !important;
    border-right: 1px solid var(--line);
}
[data-testid="stSidebar"] > div:first-child { padding-top: 1.5rem; }

.sidebar-logo {
    display: flex; flex-direction: column; align-items: center;
    padding: 0.5rem 0 1.5rem 0;
    border-bottom: 1px solid var(--line);
    margin-bottom: 1.25rem;
}
.sidebar-logo img {
    width: 110px; height: 110px; border-radius: 50%; object-fit: cover;
    box-shadow: 0 6px 24px rgba(30, 34, 24, 0.08);
}
.sidebar-logo .since {
    font-family: 'Fraunces', serif; font-size: 0.72rem;
    letter-spacing: 0.25em; color: var(--muted);
    margin-top: 0.85rem; text-transform: uppercase;
}

.sidebar-foot {
    margin-top: 2rem; padding-top: 1.25rem; border-top: 1px solid var(--line);
    font-size: 0.78rem; color: var(--muted); line-height: 1.7;
}
.sidebar-foot a { color: var(--ink-soft); text-decoration: none; }
.sidebar-foot a:hover { color: var(--accent); }

/* Sidebar radio – nav-style */
[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 0.25rem;
}
[data-testid="stSidebar"] [role="radiogroup"] label {
    width: 100%;
    padding: 0.55rem 0.85rem !important;
    border-radius: 6px;
    font-family: 'Fraunces', serif !important;
    font-size: 1.02rem !important;
    color: var(--ink) !important;
    cursor: pointer;
    transition: background 0.18s ease, color 0.18s ease;
}
[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: rgba(216, 101, 29, 0.08);
}
[data-testid="stSidebar"] [role="radiogroup"] label > div:first-child {
    display: none !important;
}
[data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"],
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
    background: var(--ink);
    color: var(--bg-soft) !important;
}
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {
    color: var(--bg-soft) !important;
}

/* ── HERO (Home) ──────────────────────────────────────────────────────── */
.hero {
    position: relative;
    margin: 1rem 0 3rem 0;
    padding: 4rem 3rem 4.5rem 3rem;
    background: linear-gradient(180deg, var(--bg-soft) 0%, var(--bg) 100%);
    border: 1px solid var(--line);
    border-radius: 4px;
    overflow: hidden;
}
.hero::before {
    content: ""; position: absolute; top: 1.5rem; left: 1.5rem; right: 1.5rem; bottom: 1.5rem;
    border: 1px solid var(--line); pointer-events: none;
}
.hero .blessing {
    font-family: 'Fraunces', serif; font-style: italic;
    text-align: center; color: var(--muted);
    letter-spacing: 0.18em; font-size: 0.78rem;
    text-transform: uppercase; margin-bottom: 2rem;
}
.hero .display {
    font-family: 'Fraunces', serif; font-weight: 400;
    font-size: clamp(3.2rem, 8vw, 6.5rem); line-height: 0.95;
    text-align: center; color: var(--ink); margin: 0;
}
.hero .display .dot {
    display: inline-block; width: 0.18em; height: 0.18em; border-radius: 50%;
    background: var(--accent); transform: translateY(-0.15em);
    margin: 0 0.05em;
}
.hero .since-row {
    display: flex; align-items: center; justify-content: center; gap: 0.85rem;
    margin: 1rem 0 1.5rem 0;
    font-family: 'Fraunces', serif; letter-spacing: 0.3em;
    color: var(--muted); font-size: 0.78rem; text-transform: uppercase;
}
.hero .since-row::before, .hero .since-row::after {
    content: ""; height: 1px; width: 60px; background: var(--line);
}
.hero .tagline {
    text-align: center; font-family: 'Fraunces', serif;
    font-style: italic; font-size: 1.35rem; color: var(--ink-soft);
    margin: 0 auto 2.5rem auto; max-width: 540px;
}
.hero .cta-row { display: flex; justify-content: center; gap: 0.85rem; flex-wrap: wrap; }

/* ── CTA buttons ──────────────────────────────────────────────────────── */
.btn {
    display: inline-flex; align-items: center; gap: 0.55rem;
    padding: 0.85rem 1.6rem;
    font-family: 'DM Sans', sans-serif; font-weight: 500; font-size: 0.92rem;
    letter-spacing: 0.04em; text-decoration: none;
    border-radius: 2px; cursor: pointer; border: 1px solid transparent;
    transition: all 0.2s ease;
}
.btn-primary { background: var(--whatsapp); color: white; }
.btn-primary:hover { background: var(--whatsapp-hi); transform: translateY(-1px); }
.btn-secondary { background: transparent; color: var(--ink); border-color: var(--ink); }
.btn-secondary:hover { background: var(--ink); color: var(--bg); }
.btn-accent { background: var(--accent); color: white; }
.btn-accent:hover { background: var(--accent-hi); }

/* ── Section headers ──────────────────────────────────────────────────── */
.section-eyebrow {
    display: flex; align-items: center; gap: 0.85rem;
    font-family: 'Fraunces', serif; font-style: italic;
    color: var(--accent); font-size: 0.85rem;
    letter-spacing: 0.3em; text-transform: uppercase;
    margin: 3.5rem 0 0.75rem 0;
}
.section-eyebrow::before {
    content: ""; display: inline-block; width: 8px; height: 8px;
    border-radius: 50%; background: var(--accent);
}
.section-title {
    font-family: 'Fraunces', serif; font-weight: 400;
    font-size: clamp(2rem, 4vw, 3rem); line-height: 1.05;
    color: var(--ink); margin: 0 0 2rem 0; max-width: 720px;
}

/* ── Pillars (Home) ───────────────────────────────────────────────────── */
.pillars { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0; margin: 1rem 0 2rem 0; }
.pillar {
    padding: 2rem 1.75rem;
    border: 1px solid var(--line);
    background: var(--surface);
}
.pillar + .pillar { border-left: none; }
.pillar .num {
    font-family: 'Fraunces', serif; font-style: italic; color: var(--accent);
    font-size: 0.85rem; letter-spacing: 0.25em; margin-bottom: 1rem;
}
.pillar h3 { font-size: 1.4rem; margin: 0 0 0.6rem 0; font-weight: 500; }
.pillar p { font-size: 0.92rem; line-height: 1.65; color: var(--ink-soft); margin: 0; }
@media (max-width: 800px) {
    .pillars { grid-template-columns: 1fr; }
    .pillar + .pillar { border-left: 1px solid var(--line); border-top: none; }
}

/* ── Product card ─────────────────────────────────────────────────────── */
.product-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.75rem; margin-top: 1rem;
}
.product-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 2px;
    overflow: hidden;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    display: flex; flex-direction: column;
}
.product-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 36px rgba(30, 34, 24, 0.10);
}
.product-image {
    width: 100%; aspect-ratio: 4 / 5; object-fit: cover;
    display: block;
}
.product-image-placeholder {
    width: 100%; aspect-ratio: 4 / 5;
    background: linear-gradient(135deg, #DED9C8 0%, #C9C3B0 100%);
    display: flex; align-items: center; justify-content: center;
    position: relative; overflow: hidden;
}
.product-image-placeholder::before {
    content: ""; position: absolute; inset: 1.25rem;
    border: 1px solid rgba(30, 34, 24, 0.18);
}
.product-image-placeholder span {
    font-family: 'Fraunces', serif; font-style: italic;
    color: var(--ink); font-size: 1.5rem; text-align: center;
    padding: 0 1.5rem; line-height: 1.2;
    position: relative; z-index: 1;
}
.product-image-placeholder::after {
    content: ""; position: absolute; bottom: 1.85rem; left: 50%;
    transform: translateX(-50%);
    width: 8px; height: 8px; border-radius: 50%; background: var(--accent);
}
.product-body { padding: 1.5rem 1.5rem 1.75rem 1.5rem; flex: 1; display: flex; flex-direction: column; }
.product-tag {
    display: inline-block; align-self: flex-start;
    font-family: 'Fraunces', serif; font-style: italic;
    font-size: 0.72rem; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--accent); margin-bottom: 0.5rem;
}
.product-name {
    font-family: 'Fraunces', serif; font-weight: 500;
    font-size: 1.45rem; color: var(--ink); margin: 0 0 0.5rem 0;
}
.product-ingredients {
    font-size: 0.78rem; color: var(--muted);
    letter-spacing: 0.04em; margin-bottom: 0.75rem;
    font-style: italic;
}
.product-blurb {
    font-size: 0.93rem; line-height: 1.6; color: var(--ink-soft);
    margin: 0 0 1.25rem 0; flex: 1;
}
.product-card .btn {
    align-self: flex-start; padding: 0.65rem 1.1rem; font-size: 0.85rem;
}

/* ── About page bits ──────────────────────────────────────────────────── */
.about-grid {
    display: grid; grid-template-columns: 1.1fr 1fr; gap: 3rem;
    align-items: start; margin-top: 1rem;
}
@media (max-width: 800px) {
    .about-grid { grid-template-columns: 1fr; gap: 2rem; }
}
.about-prose p {
    font-size: 1.02rem; line-height: 1.8; color: var(--ink-soft);
    margin-bottom: 1.1rem;
}
.about-prose .lede {
    font-family: 'Fraunces', serif; font-size: 1.35rem;
    font-style: italic; color: var(--ink); line-height: 1.5;
    margin-bottom: 1.5rem;
}
.about-image {
    width: 100%; border: 1px solid var(--line); border-radius: 2px;
    box-shadow: 0 18px 40px rgba(30, 34, 24, 0.10);
}
.about-image-frame { padding: 0.75rem; background: var(--surface); border: 1px solid var(--line); }
.about-image-frame img { display: block; width: 100%; }

.credentials {
    display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;
    margin-top: 1.5rem;
}
.credential {
    padding: 1.1rem 1.25rem; background: var(--surface);
    border: 1px solid var(--line);
}
.credential .label {
    font-family: 'Fraunces', serif; font-style: italic;
    font-size: 0.78rem; letter-spacing: 0.18em;
    color: var(--accent); text-transform: uppercase; margin-bottom: 0.35rem;
}
.credential .value {
    font-family: 'DM Sans', monospace; font-weight: 500;
    color: var(--ink); font-size: 0.95rem; letter-spacing: 0.04em;
}

/* ── Contact page ─────────────────────────────────────────────────────── */
.contact-grid {
    display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem;
    margin-top: 1rem;
}
@media (max-width: 800px) {
    .contact-grid { grid-template-columns: 1fr; }
}
.contact-card {
    padding: 2rem; background: var(--surface);
    border: 1px solid var(--line);
}
.contact-row {
    display: flex; align-items: flex-start; gap: 1rem;
    padding: 1rem 0; border-bottom: 1px solid var(--line);
}
.contact-row:last-child { border-bottom: none; }
.contact-row .ico {
    font-size: 1.1rem; min-width: 1.4rem; text-align: center;
    color: var(--accent); margin-top: 0.1rem;
}
.contact-row .label {
    font-family: 'Fraunces', serif; font-style: italic;
    font-size: 0.75rem; letter-spacing: 0.2em; text-transform: uppercase;
    color: var(--muted); margin-bottom: 0.2rem;
}
.contact-row .value { color: var(--ink); font-size: 0.98rem; line-height: 1.55; }
.contact-row a { color: var(--ink); text-decoration: none; border-bottom: 1px solid var(--line); }
.contact-row a:hover { color: var(--accent); border-bottom-color: var(--accent); }

.qr-card {
    padding: 1.75rem; background: var(--surface);
    border: 1px solid var(--line); text-align: center;
}
.qr-card img {
    width: 160px; height: 160px; object-fit: contain;
    background: white; padding: 8px; border: 1px solid var(--line);
}
.qr-card .qr-label {
    font-family: 'Fraunces', serif; font-style: italic;
    margin-top: 0.85rem; color: var(--ink-soft); font-size: 0.95rem;
}
.qr-row { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }

/* ── Footer ───────────────────────────────────────────────────────────── */
.footer {
    margin-top: 5rem; padding-top: 2rem;
    border-top: 1px solid var(--line);
    text-align: center; color: var(--muted); font-size: 0.82rem;
    font-family: 'DM Sans', sans-serif;
}
.footer .bless {
    font-family: 'Fraunces', serif; font-style: italic;
    color: var(--ink-soft); margin-bottom: 0.5rem;
    letter-spacing: 0.15em; font-size: 0.8rem;
}

/* ── Misc helpers ─────────────────────────────────────────────────────── */
.divider-dot { display: flex; align-items: center; justify-content: center;
    margin: 3rem 0; gap: 0.7rem; }
.divider-dot::before, .divider-dot::after {
    content: ""; flex: 0 0 60px; height: 1px; background: var(--line);
}
.divider-dot .d {
    width: 6px; height: 6px; border-radius: 50%; background: var(--accent);
}

.note-strip {
    background: var(--ink); color: var(--bg-soft);
    padding: 1.5rem 2rem; margin: 2.5rem 0;
    display: flex; justify-content: space-between; align-items: center;
    flex-wrap: wrap; gap: 1rem;
}
.note-strip .note-text {
    font-family: 'Fraunces', serif; font-style: italic;
    font-size: 1.1rem; color: var(--bg-soft);
}

</style>
"""

st.markdown(CSS, unsafe_allow_html=True)


# ────────────────────────────────────────────────────────────────────────────
# COMPONENTS
# ────────────────────────────────────────────────────────────────────────────

def sidebar_nav() -> str:
    """Render the sidebar (logo + nav + contact) and return the active page."""
    logo_b64 = img_to_b64("brand/logo_circle.jpeg")
    st.sidebar.markdown(
        f"""
        <div class="sidebar-logo">
            <img src="data:image/jpeg;base64,{logo_b64}" alt="Arham" />
            <div class="since">Since {BRAND['since']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    page = st.sidebar.radio(
        "Navigate",
        ["Home", "Products", "About", "Contact / Order"],
        label_visibility="collapsed",
    )

    wa = order_link()
    st.sidebar.markdown(
        f"""
        <div class="sidebar-foot">
            <p style="margin:0 0 0.5rem 0; color: var(--ink-soft); font-family: 'Fraunces', serif; font-style: italic;">
                Order on WhatsApp
            </p>
            <p style="margin:0 0 0.85rem 0;">
                <a href="{wa}" target="_blank">{CONTACT['phone']}</a>
            </p>
            <p style="margin:0 0 0.4rem 0;">
                <a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a>
            </p>
            <p style="margin:0;">
                <a href="{CONTACT['instagram_url']}" target="_blank">@{CONTACT['instagram']}</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    return page


def render_product_card(p: dict) -> str:
    """Return HTML for a single product card."""
    if p["image"]:
        b64 = img_to_b64(p["image"])
        media = f'<img class="product-image" src="data:image/jpeg;base64,{b64}" alt="{p["name"]}" />'
    else:
        media = (
            f'<div class="product-image-placeholder">'
            f'<span>{p["name"]}</span>'
            f'</div>'
        )

    tag_html = f'<span class="product-tag">{p["tag"]}</span>' if p["tag"] else ""
    return f"""
    <div class="product-card">
        {media}
        <div class="product-body">
            {tag_html}
            <h3 class="product-name">{p['name']}</h3>
            <div class="product-ingredients">{p['ingredients']}</div>
            <p class="product-blurb">{p['blurb']}</p>
            <a class="btn btn-primary" href="{order_link(p['name'])}" target="_blank">
                Order on WhatsApp
            </a>
        </div>
    </div>
    """


def footer():
    st.markdown(
        f"""
        <div class="footer">
            <div class="bless">{BRAND['blessing']}</div>
            <div>© {BRAND['since']}–present  •  {BRAND['full_name']}, Bhavnagar, Gujarat  •  FSSAI {CREDENTIALS['fssai']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ────────────────────────────────────────────────────────────────────────────
# PAGES
# ────────────────────────────────────────────────────────────────────────────

def page_home():
    # Hero
    st.markdown(
        f"""
        <div class="hero">
            <div class="blessing">{BRAND['blessing']}</div>
            <h1 class="display">A<span class="dot"></span>rham</h1>
            <div class="since-row">Snacks • Since {BRAND['since']}</div>
            <p class="tagline">{BRAND['tagline']}<br/>{BRAND['sub_tagline']}</p>
            <div class="cta-row">
                <a class="btn btn-primary" href="{order_link()}" target="_blank">📱 Order Now on WhatsApp</a>
                <a class="btn btn-secondary" href="?page=products">View Products</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Pillars
    st.markdown('<div class="section-eyebrow">Why Arham</div>', unsafe_allow_html=True)
    st.markdown(
        '<h2 class="section-title">Snacks made the way they were always meant to be — by hand, with care.</h2>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="pillars">
            <div class="pillar">
                <div class="num">01 — Fresh</div>
                <h3>Made in small batches</h3>
                <p>We cook in small batches so every packet reaches you with the snap, scent and crunch of freshly-fried snacks.</p>
            </div>
            <div class="pillar">
                <div class="num">02 — Hygienic</div>
                <h3>Clean kitchen, every step</h3>
                <p>Prepared in a hygienic environment with hand-picked ingredients and oils chosen for healthier frying.</p>
            </div>
            <div class="pillar">
                <div class="num">03 — Homemade</div>
                <h3>The taste of home</h3>
                <p>Family recipes, traditional spice blends and zero shortcuts. Snacks that taste like someone made them for you.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Featured products (first 3 with images)
    st.markdown('<div class="section-eyebrow">From the kitchen</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">A few favourites</h2>', unsafe_allow_html=True)

    featured = [p for p in PRODUCTS if p["image"]][:3]
    cards = "".join(render_product_card(p) for p in featured)
    st.html(f'<div class="product-grid">{cards}</div>')

    # Note strip
    st.markdown(
        f"""
        <div class="note-strip">
            <div class="note-text">Free home delivery on orders above ₹500 in Bhavnagar.</div>
            <a class="btn btn-accent" href="{order_link()}" target="_blank">Order Now →</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_products():
    st.markdown('<div class="section-eyebrow">The Snacks Menu</div>', unsafe_allow_html=True)
    st.markdown(
        '<h2 class="section-title">Seven things we make really, really well.</h2>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <p style="max-width: 640px; font-size: 1rem; line-height: 1.7; margin: -1rem 0 2rem 0;">
            Every Arham snack is hand-tossed in our Bhavnagar kitchen using fresh ingredients
            and time-tested family recipes. Tap any item below to order on WhatsApp — we'll
            confirm pricing, pack size and delivery details right there.
        </p>
        """,
        unsafe_allow_html=True,
    )

    cards = "".join(render_product_card(p) for p in PRODUCTS)
    st.html(f'<div class="product-grid">{cards}</div>')

    st.markdown(
        f"""
        <div class="note-strip">
            <div class="note-text">Bulk orders, gift hampers, festival packs — we do it all.</div>
            <a class="btn btn-accent" href="{order_link()}" target="_blank">Talk to us on WhatsApp →</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_about():
    st.markdown('<div class="section-eyebrow">Our story</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">A small kitchen with a big idea.</h2>', unsafe_allow_html=True)

    logo_wide = img_to_b64("brand/logo_wide.jpeg")
    st.markdown(
        f"""
        <div class="about-grid">
            <div class="about-prose">
                <p class="lede">
                    Arham Snacks began in 2020 as a homemade nasta brand built on one simple
                    promise — fresh, hygienic, honest snacks that taste like they came from
                    a loved one's kitchen.
                </p>
                <p>
                    We blend the traditional and the modern: family recipes for chevdo, banana
                    wafers and khakhra, made with carefully chosen ingredients, hygienic methods
                    and small-batch attention to every packet.
                </p>
                <p>
                    Quality isn't an afterthought for us — it's the entire point. From the
                    raw banana we slice each morning to the spices we hand-blend, every step
                    is watched over so that the snack reaching you tastes the way it should.
                </p>
                <p>
                    Today Arham Snacks delivers fresh nasta across Bhavnagar — and we're proud
                    to be FSSAI registered and Udyam (MSME) certified.
                </p>
            </div>
            <div>
                <div class="about-image-frame">
                    <img src="data:image/jpeg;base64,{logo_wide}" alt="Arham logo" />
                </div>
                <div class="credentials">
                    <div class="credential">
                        <div class="label">FSSAI No.</div>
                        <div class="value">{CREDENTIALS['fssai']}</div>
                    </div>
                    <div class="credential">
                        <div class="label">Udyam No.</div>
                        <div class="value">{CREDENTIALS['udyam']}</div>
                    </div>
                    <div class="credential">
                        <div class="label">Based in</div>
                        <div class="value">Bhavnagar, Gujarat</div>
                    </div>
                    <div class="credential">
                        <div class="label">Since</div>
                        <div class="value">{BRAND['since']}</div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # What we believe
    st.markdown('<div class="divider-dot"><div class="d"></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-eyebrow">What we believe</div>', unsafe_allow_html=True)
    st.markdown(
        '<h2 class="section-title">Three things we will never compromise on.</h2>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="pillars">
            <div class="pillar">
                <div class="num">— On freshness</div>
                <h3>Cooked the day it leaves us</h3>
                <p>No long shelf-life shortcuts. We make in small batches and dispatch fresh.</p>
            </div>
            <div class="pillar">
                <div class="num">— On ingredients</div>
                <h3>The good stuff, every time</h3>
                <p>Quality raw banana, real peanuts, hand-blended spices and rice bran oil for healthier frying.</p>
            </div>
            <div class="pillar">
                <div class="num">— On trust</div>
                <h3>Transparent and traceable</h3>
                <p>FSSAI registered, Udyam certified — and a WhatsApp message away if you ever have a question.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_contact():
    st.markdown('<div class="section-eyebrow">Get in touch</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Let\'s pack you a fresh batch.</h2>', unsafe_allow_html=True)
    st.markdown(
        """
        <p style="max-width: 640px; font-size: 1rem; line-height: 1.7; margin: -1rem 0 2rem 0;">
            The fastest way to order is WhatsApp — we usually reply within minutes. You can
            also email us, drop by, or scan the QR codes below to message and follow.
        </p>
        """,
        unsafe_allow_html=True,
    )

    address_html = "<br/>".join(CONTACT["address_lines"])
    wa_link = order_link()
    wa_qr = img_to_b64("qr/whatsapp_qr.jpeg")
    insta_qr = img_to_b64("qr/instagram_qr.jpeg")

    st.html(
        f"""
        <div class="contact-grid">
            <div class="contact-card">
                <div class="contact-row">
                    <div class="ico">●</div>
                    <div>
                        <div class="label">WhatsApp / Phone</div>
                        <div class="value"><a href="{wa_link}" target="_blank">{CONTACT['phone']}</a></div>
                    </div>
                </div>
                <div class="contact-row">
                    <div class="ico">●</div>
                    <div>
                        <div class="label">Email</div>
                        <div class="value"><a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></div>
                    </div>
                </div>
                <div class="contact-row">
                    <div class="ico">●</div>
                    <div>
                        <div class="label">Instagram</div>
                        <div class="value"><a href="{CONTACT['instagram_url']}" target="_blank">@{CONTACT['instagram']}</a></div>
                    </div>
                </div>
                <div class="contact-row">
                    <div class="ico">●</div>
                    <div>
                        <div class="label">Address</div>
                        <div class="value">{address_html}</div>
                    </div>
                </div>
                <div class="contact-row">
                    <div class="ico">●</div>
                    <div>
                        <div class="label">Hours</div>
                        <div class="value">{CONTACT['hours']}</div>
                    </div>
                </div>
                <div class="contact-row">
                    <div class="ico">●</div>
                    <div>
                        <div class="label">Delivery</div>
                        <div class="value">{CONTACT['delivery_note']}</div>
                    </div>
                </div>
                <div style="margin-top: 1.5rem;">
                    <a class="btn btn-primary" href="{wa_link}" target="_blank">📱 Open WhatsApp Chat</a>
                </div>
            </div>

            <div>
                <div class="qr-row">
                    <div class="qr-card">
                        <img src="data:image/jpeg;base64,{wa_qr}" alt="WhatsApp QR" />
                        <div class="qr-label">Scan to chat<br/>on WhatsApp</div>
                    </div>
                    <div class="qr-card">
                        <img src="data:image/jpeg;base64,{insta_qr}" alt="Instagram QR" />
                        <div class="qr-label">Scan to follow<br/>on Instagram</div>
                    </div>
                </div>
                <div class="contact-card" style="margin-top: 1.5rem;">
                    <div class="label" style="font-family: 'Fraunces', serif; font-style: italic;
                         font-size: 0.78rem; letter-spacing: 0.2em; text-transform: uppercase;
                         color: var(--accent); margin-bottom: 0.85rem;">A note on delivery</div>
                    <p style="margin: 0; font-size: 0.95rem; line-height: 1.7;">
                        We deliver across Bhavnagar daily. Delivery charges depend on your
                        location and are confirmed on WhatsApp before dispatch. Orders above
                        <strong>₹500</strong> ship free.
                    </p>
                </div>
            </div>
        </div>
        """,
        )

    # Quick order form
    st.markdown('<div class="divider-dot"><div class="d"></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-eyebrow">Quick enquiry</div>', unsafe_allow_html=True)
    st.markdown(
        '<h2 class="section-title">Prefer to send us the details first?</h2>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <p style="max-width: 640px; font-size: 0.98rem; line-height: 1.7; margin: -1rem 0 1.5rem 0;">
            Fill in the boxes below — we'll generate a ready-to-send WhatsApp message with
            your details. One tap and it lands in our inbox.
        </p>
        """,
        unsafe_allow_html=True,
    )

    with st.form("enquiry_form", clear_on_submit=False):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Your name *", placeholder="e.g. Riya Shah")
            area = st.text_input("Your area in Bhavnagar *", placeholder="e.g. Kalanala")
        with c2:
            picks = st.multiselect(
                "Which snacks would you like? *",
                [p["name"] for p in PRODUCTS],
                placeholder="Choose one or more",
            )
            occasion = st.selectbox(
                "Occasion (optional)",
                ["—", "Daily snacking", "Festival pack", "Gift hamper", "Bulk / event order"],
            )
        notes = st.text_area("Anything else? (quantity, spice level, deadline)", height=90)
        submitted = st.form_submit_button("Generate WhatsApp message →")

    if submitted:
        if not name or not area or not picks:
            st.warning("Please fill in your name, area, and at least one snack.")
        else:
            picks_text = ", ".join(picks)
            extras = []
            if occasion and occasion != "—":
                extras.append(f"Occasion: {occasion}")
            if notes.strip():
                extras.append(f"Notes: {notes.strip()}")
            extras_text = ("\n" + "\n".join(extras)) if extras else ""

            msg = (
                f"Hi Arham Snacks 👋\n\n"
                f"I'd like to place an order.\n\n"
                f"Name: {name}\n"
                f"Area: {area}, Bhavnagar\n"
                f"Items: {picks_text}{extras_text}\n\n"
                f"Could you please confirm pricing and delivery? Thank you!"
            )
            link = whatsapp_link(msg)
            st.success("Your message is ready — tap below to open WhatsApp.")
            st.markdown(
                f'<a class="btn btn-primary" href="{link}" target="_blank">📱 Send on WhatsApp</a>',
                unsafe_allow_html=True,
            )
            with st.expander("Preview the message"):
                st.code(msg, language=None)


# ────────────────────────────────────────────────────────────────────────────
# MAIN
# ────────────────────────────────────────────────────────────────────────────

def main():
    page = sidebar_nav()

    if page == "Home":
        page_home()
    elif page == "Products":
        page_products()
    elif page == "About":
        page_about()
    elif page == "Contact / Order":
        page_contact()

    footer()


if __name__ == "__main__":
    main()
