# Arham Snacks — Website

A homemade nasta brand website built with **Streamlit + Python**.

> Fresh • Hygienic • Homemade
> *Crunchy Taste, Pure Trust*

---

## What's inside

A 4-page catalog site with WhatsApp ordering:

- **Home** — hero, brand pillars, featured snacks, free-delivery strip
- **Products** — full menu (7 items) with images, ingredients & "Order on WhatsApp" buttons
- **About** — brand story, FSSAI / Udyam credentials, beliefs
- **Contact / Order** — phone, email, address, hours, QR codes (WhatsApp + Instagram), and a quick-enquiry form that generates a pre-filled WhatsApp message

Every "Order" button opens WhatsApp with a ready-to-send message that includes the product name — so you don't have to type anything.

---

## Quick start

```bash
# 1. (Recommended) create a virtual env
python -m venv .venv
source .venv/bin/activate          # on Windows: .venv\Scripts\activate

# 2. install dependencies
pip install -r requirements.txt

# 3. run the site
streamlit run app.py
```

The site will open in your browser at `http://localhost:8501`.

---

## Project structure

```
arham_website/
├── app.py                      # the entire site (single-file Streamlit app)
├── requirements.txt
├── README.md
└── assets/
    ├── menu.pdf                # original menu PDF
    ├── brand/
    │   ├── logo_circle.jpeg    # round logo (used in sidebar + favicon)
    │   ├── logo_wide.jpeg      # wordmark logo (used on About page)
    │   └── rice_bran_oil_poster.jpeg
    ├── products/
    │   ├── banana_wafers.jpeg
    │   ├── banana_chevdo.jpeg
    │   └── roti_khakhra.jpeg
    ├── qr/
    │   ├── whatsapp_qr.jpeg
    │   └── instagram_qr.jpeg
    └── certificates/
        ├── fssai.jpeg
        └── udyam.pdf
```

---

## How to update content

All editable content lives in **constants at the top of `app.py`** — no need to dig through HTML.

### Add or change a product

Open `app.py` and edit the `PRODUCTS` list:

```python
PRODUCTS = [
    {
        "name": "Banana Wafers",
        "ingredients": "Raw Banana & Spices",
        "blurb": "Thin, golden-fried slices...",
        "image": "products/banana_wafers.jpeg",   # path under assets/, or None
        "tag": "Classic",                          # small label, or None
    },
    # ...
]
```

- To **add a new product**, drop its image into `assets/products/` and append a new dict to the list.
- If a product has no image yet, set `"image": None` — the card will render a clean styled placeholder with the product name (no broken images).

### Update prices

Currently the menu doesn't list prices, so pricing is confirmed on WhatsApp. To show prices on the site, add a `"price"` field to each product dict and edit `render_product_card()` in `app.py` to display it.

### Update contact details

Edit the `CONTACT` dict at the top of `app.py`:

```python
CONTACT = {
    "phone": "+91 8200745911",
    "phone_raw": "918200745911",   # for wa.me links — no + or spaces
    "email": "arhamsnacks@gmail.com",
    ...
}
```

Whenever you change the phone number, **update both `phone` and `phone_raw`** — the second one is what makes WhatsApp links work.

### Replace the logo or QR codes

Just overwrite the file in `assets/brand/` or `assets/qr/` keeping the same filename. No code changes needed.

---

## Deploying

The easiest free option is **Streamlit Community Cloud**:

1. Push this folder to a GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**, point it at your repo, and set the main file path to `app.py`.
4. Deploy. Done.

Other options that also work: Render, Railway, Hugging Face Spaces, or any host that runs Python.

---

## Tech notes

- **Single file, no extra deps.** Everything renders from `app.py` using Streamlit's native components plus injected CSS/HTML. The only dependency is Streamlit itself.
- **Images are inlined as base64.** This keeps the deploy as simple as possible — no static file server config required, and Streamlit Cloud picks it up out of the box.
- **WhatsApp links use `wa.me`** with a URL-encoded message body, which works on both mobile and desktop WhatsApp.
- **Typography**: Fraunces (serif display) + DM Sans (body), loaded from Google Fonts.
- **Colour palette**: cream (`#E8E5DA`) + dark green-black (`#1E2218`) + orange accent (`#D8651D`) — all sampled from the Arham logo.

---

## Credentials displayed on the site

- **FSSAI Registration**: 20726006000231 (valid until 17-02-2027)
- **Udyam Registration**: UDYAM-GJ-05-0087550
- **Address**: 107, Brahma Park, Ring Road, Bharatnagar, Bhavnagar, Gujarat – 364001

---

*|| Shri Mahaviray Namah ||*
