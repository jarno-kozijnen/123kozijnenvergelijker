"""
123KozijnenVergelijker.nl — Blog generator
==========================================
Genereert SEO-blogposts via Claude API en slaat ze op als standalone HTML-bestanden.
Werkt samen met onderwerpen.json (topics) en blogs_index.json (gepubliceerde blogs).

Gebruik:
  python blog_genereren.py              # genereer 10 nieuwe blogs
  python blog_genereren.py --aantal 5   # genereer N blogs
"""

import sys
import os
import json
import logging
import re
import time
import unicodedata
import xml.etree.ElementTree as ET
import argparse
import random
from pathlib import Path
from datetime import datetime, timedelta

import anthropic
from dotenv import load_dotenv

# --- Setup ---
BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env", override=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    handlers=[
        logging.FileHandler(BASE_DIR / "blog_genereren.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)

# --- Config ---
ANTHROPIC_KEY    = os.getenv("ANTHROPIC_API_KEY")
BLOGS_PER_RUN    = 10
SITEMAP_FILE     = BASE_DIR / "sitemap.xml"
ONDERWERPEN_FILE = BASE_DIR / "onderwerpen.json"
INDEX_FILE       = BASE_DIR / "blogs_index.json"
OUTPUT_DIR       = BASE_DIR
CTA_URL          = "https://123kozijnenvergelijker.nl/offerte-vergelijken#offerte-aanvragen"

# Categorie-toewijzing op basis van titelwoorden
CAT_MAP = {
    "deur": "Deuren",
    "voordeur": "Deuren",
    "achterdeur": "Deuren",
    "garagedeur": "Deuren",
    "schuifpui": "Schuifpuien",
    "tuindeur": "Schuifpuien",
    "openslaande": "Schuifpuien",
    "subsidie": "Subsidie",
    "isde": "Subsidie",
    "energiebespar": "Verduurzamen",
    "verduurzam": "Verduurzamen",
    "isolat": "Verduurzamen",
    "warmtepomp": "Verduurzamen",
    "rc-waarde": "Verduurzamen",
    "u-waarde": "Verduurzamen",
    "hr++": "Verduurzamen",
    "hr+++": "Verduurzamen",
    "glas": "Verduurzamen",
    "tips": "Tips",
    "kleur": "Tips",
    "onderhoud": "Tips",
    "reiniging": "Tips",
    "schoonmaken": "Tips",
    "maat": "Tips",
    "offerte": "Tips",
}

STEDEN_SAMPLE = [
    "Almelo", "Hengelo", "Enschede", "Deventer", "Zwolle", "Apeldoorn",
    "Borne", "Wierden", "Rijssen", "Oldenzaal", "Vriezenveen", "Losser",
    "Hardenberg", "Ommen", "Holten", "Goor", "Diepenheim", "Delden",
    "Gronau", "Haaksbergen",
]


# --- Hulpfuncties ---
def laad_json(pad: Path) -> list:
    with open(pad, encoding="utf-8") as f:
        return json.load(f)

def sla_json_op(pad: Path, data) -> None:
    with open(pad, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def slugify(tekst: str) -> str:
    tekst = unicodedata.normalize("NFD", tekst)
    tekst = "".join(c for c in tekst if unicodedata.category(c) != "Mn")
    tekst = tekst.lower()
    tekst = re.sub(r"[^a-z0-9\s-]", "", tekst)
    tekst = re.sub(r"\s+", "-", tekst.strip())
    tekst = re.sub(r"-+", "-", tekst)
    return tekst[:70]


def bepaal_categorie(titel: str) -> str:
    titel_lower = titel.lower()
    for sleutel, cat in CAT_MAP.items():
        if sleutel in titel_lower:
            return cat
    return "Kozijnen"


def schat_leestijd(html_content: str) -> int:
    tekst = re.sub(r"<[^>]+>", " ", html_content)
    woorden = len(tekst.split())
    minuten = max(3, round(woorden / 250))
    return minuten


def format_datum(dt: datetime) -> str:
    maanden = ["januari", "februari", "maart", "april", "mei", "juni",
               "juli", "augustus", "september", "oktober", "november", "december"]
    return f"{dt.day} {maanden[dt.month - 1]} {dt.year}"


# --- Sitemap lezen voor interne links ---
def haal_interne_links() -> list:
    links = []
    if not SITEMAP_FILE.exists():
        log.warning("sitemap.xml niet gevonden")
        return links
    NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    try:
        root = ET.parse(SITEMAP_FILE).getroot()
        for url_el in root.findall(".//sm:url", NS):
            loc = url_el.find("sm:loc", NS)
            if loc is None:
                continue
            url = (loc.text or "").strip()
            if not url:
                continue
            # Maak relatief pad
            pad = url.replace("https://123kozijnenvergelijker.nl/", "")
            if pad.endswith("/"):
                pad = pad.rstrip("/") + ".html"
            # Leesbare titel
            naam = pad.replace(".html", "").replace("-", " ").replace("/", " ").title()
            links.append({"url": pad, "naam": naam})
    except Exception as e:
        log.warning(f"Sitemap lezen mislukt: {e}")
    return links


# --- Kies onderwerpen ---
def kies_onderwerpen(onderwerpen: list, aantal: int) -> list:
    beschikbaar = [o for o in onderwerpen if not o.get("gebruikt")]
    if len(beschikbaar) < aantal:
        log.warning(f"Nog maar {len(beschikbaar)} onderwerpen beschikbaar!")
    return beschikbaar[:aantal]


# --- Blog genereren via Claude ---
SYSTEM_PROMPT = """Je schrijft SEO-blogposts voor 123KozijnenVergelijker.nl.

=== OVER HET PLATFORM ===
- 123KozijnenVergelijker.nl is een vergelijkingsplatform voor kunststof kozijnen, deuren en schuifpuien
- Bezoekers vergelijken offertes van meerdere installateurs en vinden zo de beste prijs
- Werkgebied: heel Nederland, met focus op Overijssel, Gelderland, Drenthe en Groningen
- USPs: gratis offertes vergelijken, geen aanbetaling bij installateurs, onafhankelijk advies, 20 jaar garantie standaard, HR++ glas inbegrepen
- Tone of voice: betrouwbaar, praktisch, drempelverlagend — ALTIJD je/jij, nooit u/uw

=== MENSELIJKE SCHRIJFSTIJL (KRITISCH) ===
De tekst mag NIET herkend worden als AI-gegenereerd. Schrijf zoals een ervaren vakman:
- Gebruik GEEN emdashes of gedachtestreepjes (---, --) in de lopende tekst
- Gebruik GEEN AI-woorden: cruciaal, esthetisch, naadloos, robuust, innovatief, transformeren, optimaliseren, revolutionair, veelzijdig, uitgebreid, uitdagend, uniek, perfect, geweldig, ideaal, essentieel, onmisbaar, optimaal
- Gebruik GEEN AI-constructies: "zowel ... als ...", "enerzijds ... anderzijds", "bovendien", "tevens", "derhalve", "dientengevolge", "hetgeen", "waarbij"
- Zorg voor echte ongelijkmatigheid in zinlengte: soms een korte knaller van 5 woorden, dan een langere uitleg
- Maak alineas ongelijk lang
- Gebruik soms omgangstaal: "dat merk je meteen", "dat scheelt je echt een hoop gedoe"
- Gebruik retorische vragen: "Maar wat kost dat dan? Tja, dat hangt ervan af."
- Begin sommige zinnen met "En" of "Maar"
- Spreek de lezer ALTIJD aan met je/jij/jouw
- Schrijf in de actieve vorm
- Herhaal NIET dezelfde woorden binnen een alinea

=== SEO-REGELS ===
- Verwerk het hoofdzoekwoord in de eerste 100 woorden
- Gebruik het hoofdzoekwoord 3-5x verspreid (niet spammen)
- Verwerk semantisch gerelateerde termen (LSI): bij kozijnen ook PVC ramen, isolatieglas, energiebesparing, HR++ glas, U-waarde, kozijnvervanging
- Totaal minimaal 1800 woorden, maximaal 2500 woorden
- Schrijf voor mensen, niet voor zoekmachines

=== NLP-OPTIMALISATIE ===
- Gebruik volledige zinnen die vragen direct beantwoorden (voor featured snippets)
- Benoem getallen, percentages en concrete feiten: "gemiddeld 15-25% lagere stookkosten"
- Gebruik synoniemen en contextuele termen
- Schrijf alineas die als zelfstandig antwoord werken

=== E-E-A-T ===
- Toon vakkennis: benoem normen, technische begrippen (U-waarde, RC-waarde, profieldikte) en leg ze kort uit
- Geef eerlijk advies, ook als dat betekent dat iemand even moet wachten
- Schrijf als expert die de lezer echt helpt, niet als verkoper
- Verwijs naar concrete situaties en praktijkvoorbeelden

=== GEO (voor AI-zoekmachines) ===
- Begin elke sectie met een directe, feitelijke uitspraak die als citaat werkt
- Geef concrete antwoorden op impliciete vragen: wat kost het, hoe lang duurt het, voor- en nadelen
- Vermijd vage taal: wees stellig en concreet

=== INTERNE LINKS ===
- Verwerk VERPLICHT 4-6 interne links in de lopende blogtekst (niet alleen in CTA's of lijsten onderaan)
- Gebruik ALTIJD relatieve URLs: "kunststof-kozijnen.html", "kozijnen-almelo.html", "financiering.html" — NOOIT absolute URLs zoals "https://www.123kozijnenvergelijker.nl/..."
- Prioriteit: productpagina's (kunststof-kozijnen.html, kunststof-deuren.html, kunststof-schuifpuien.html, financiering.html), stadspagina's (kozijnen-[stad].html)
- Gebruik beschrijvende ankerteksten: "kunststof kozijnen vervangen" of "kozijnen in Almelo" — NOOIT "klik hier", "lees meer" of "deze pagina"
- Verwerk links organisch in lopende zinnen zodat ze als echte hyperlinks zichtbaar zijn
- Voeg onderaan een sectie <h2>Meer lezen</h2> toe met 3-4 relevante links als <ul><li><a href="...">tekst</a></li></ul>

=== CTA's ===
Verwerk EXACT 3 CTA's in de tekst op de volgende posities:
1. Direct na de intro (eerste alinea)
2. Halverwege het artikel (na sectie 5-6)
3. Voor de FAQ

Gebruik voor elke CTA dit exacte HTML:
<div class="blog-cta-inline">
<p>[Korte motiverende zin die aansluit op de context, max 15 woorden]</p>
<a href="https://123kozijnenvergelijker.nl/offerte-vergelijken#offerte-aanvragen" class="btn-primary">Vergelijk 3 gratis offertes</a>
</div>

=== STRUCTUUR EN OPMAAK ===
- Gebruik <h2> voor sectietitels (8-12 secties)
- Begin met sterke intro van 2-3 zinnen die het probleem/de vraag erkent
- Gebruik <ul><li> voor opsommingen
- Eindig met een FAQ-sectie (4-5 vragen) met dit exacte format:
<div class="faq">
<div class="faq-item">
<button class="faq-vraag" onclick="toggleFaq(this)">[Vraag]<span class="faq-icon">+</span></button>
<div class="faq-antwoord"><p>[Antwoord]</p></div>
</div>
</div>

=== OUTPUT FORMAT ===
Begin je output ALTIJD met deze regels (voor alle HTML):
SEO_TITEL: [Pakkende titel, 50-60 tekens, bevat hoofdzoekwoord]
META_DESC: [Meta beschrijving, 140-155 tekens, bevat zoekwoord + concrete belofte]
URL_SLUG: [url-slug-in-kleine-letters-met-koppeltekens]
FOCUS_KW: [Primair zoekwoord]
SAMENVATTING: [1-2 zinnen voor het blogoverzicht, max 120 tekens]

Dan een regel met precies: ---HTML---

Dan direct de HTML blog-content (GEEN <html>, <body>, <head> tags):
- Start met <p>[intro]</p>
- Dan CTA 1
- Dan <h2>secties</h2>
- Dan CTA 2 (halverwege)
- Dan meer secties
- Dan CTA 3 (voor FAQ)
- Dan FAQ-sectie
- Dan Meer lezen sectie
"""


def genereer_blog(titel: str, interne_links: list, recent_blogs: list) -> dict | None:
    """Genereert een volledig blog via Claude API. Geeft dict terug of None bij fout."""
    if not ANTHROPIC_KEY:
        log.error("ANTHROPIC_API_KEY niet ingesteld!")
        return None

    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
    categorie = bepaal_categorie(titel)

    # Selecteer relevante interne links (max 15 om prompt kort te houden)
    product_links = [l for l in interne_links if any(x in l["url"] for x in ["kunststof-", "schuifpuien", "financiering", "offerte"])]
    stad_links = [l for l in interne_links if l["url"].startswith("kozijnen-")]
    blog_links = [l for l in interne_links if l["url"].startswith("blog-") and not l["url"] == "blog-detail.html"]

    geselecteerde_links = product_links[:5]
    geselecteerde_links += random.sample(stad_links, min(5, len(stad_links)))
    if blog_links:
        geselecteerde_links += random.sample(blog_links, min(3, len(blog_links)))

    links_tekst = "\n".join([f"- {l['url']} ({l['naam']})" for l in geselecteerde_links])

    user_prompt = f"""Schrijf een complete SEO-blogpost over: "{titel}"

Categorie: {categorie}
Focus op de Nederlandse markt, met name Overijssel en omgeving.

Beschikbare interne links (gebruik er 4-6 in de tekst):
{links_tekst}

Relevante steden voor regionale vermelding: {', '.join(random.sample(STEDEN_SAMPLE, 4))}

Vergeet niet:
- Minimaal 1800 woorden
- Precies 3 CTA's op de juiste posities
- FAQ-sectie onderaan
- Geen emdashes
- je/jij toon
- Begin output met SEO_TITEL:, META_DESC:, URL_SLUG:, FOCUS_KW:, SAMENVATTING:
- Dan ---HTML---
- Dan de blog-content HTML"""

    log.info(f"Genereer blog: '{titel}'")
    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=8192,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        raw = message.content[0].text
        return verwerk_api_output(raw, titel, categorie)
    except Exception as e:
        log.error(f"API fout voor '{titel}': {e}")
        return None


def verwerk_api_output(raw: str, titel: str, categorie: str) -> dict | None:
    """Verwerkt Claude API output naar een blog-dict."""
    try:
        # Splits metadata van HTML
        if "---HTML---" not in raw:
            log.error("Geen ---HTML--- marker gevonden in output")
            return None

        meta_deel, html_deel = raw.split("---HTML---", 1)
        html_content = html_deel.strip()

        # Parse metadata
        def haal_meta(sleutel: str) -> str:
            match = re.search(rf"^{sleutel}:\s*(.+)$", meta_deel, re.MULTILINE)
            return match.group(1).strip() if match else ""

        seo_titel = haal_meta("SEO_TITEL") or titel
        meta_desc = haal_meta("META_DESC")
        url_slug   = haal_meta("URL_SLUG") or slugify(titel)
        focus_kw   = haal_meta("FOCUS_KW")
        samenvatting = haal_meta("SAMENVATTING")

        # Validaties
        url_slug = slugify(url_slug)  # Zorg dat het geldig is
        leestijd = schat_leestijd(html_content)

        # Datum: spreid over afgelopen 6 maanden (meest recent naar meest oud)
        # Wordt later ingesteld vanuit de loop

        return {
            "titel": seo_titel,
            "meta_desc": meta_desc,
            "slug": url_slug,
            "focus_kw": focus_kw,
            "samenvatting": samenvatting,
            "categorie": categorie,
            "leestijd": leestijd,
            "html_content": html_content,
        }
    except Exception as e:
        log.error(f"Verwerking mislukt: {e}")
        return None


def bouw_html_pagina(blog: dict, datum: datetime, recent_blogs: list) -> str:
    """Bouwt de volledige HTML-pagina op basis van blog-dict."""
    datum_str = format_datum(datum)
    datum_iso = datum.strftime("%Y-%m-%d")
    slug = blog["slug"]
    titel = blog["titel"]
    categorie = blog["categorie"]
    leestijd = blog["leestijd"]
    meta_desc = blog["meta_desc"]

    # Gerelateerde blogs (3 meest recente, niet zichzelf)
    gerelateerd = [b for b in recent_blogs if b["slug"] != slug][:3]
    gerelateerd_html = ""
    for rel in gerelateerd:
        gerelateerd_html += f"""
        <a href="{rel['slug']}.html" class="blog-related-item">
            <div class="blog-related-body">
                <span class="blog-cat-tag">{rel['categorie']}</span>
                <h4>{rel['titel']}</h4>
                <span class="blog-date">{rel['datum_display']}</span>
            </div>
        </a>"""
    if not gerelateerd_html:
        gerelateerd_html = '<a href="blog.html" class="blog-related-item"><div class="blog-related-body"><span class="blog-cat-tag">Kozijnen</span><h4>Bekijk alle artikelen</h4></div></a>'

    # Sidebar recente posts
    sidebar_posts_html = ""
    for rel in gerelateerd[:3]:
        sidebar_posts_html += f"""
        <a href="{rel['slug']}.html" class="sidebar-post">
            <div>
                <p>{rel['titel']}</p>
                <span>{rel['datum_display']}</span>
            </div>
        </a>"""
    if not sidebar_posts_html:
        sidebar_posts_html = '<a href="blog.html" class="sidebar-post"><div><p>Bekijk alle artikelen</p></div></a>'

    # Schema.org JSON-LD
    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": titel,
        "description": meta_desc,
        "datePublished": datum_iso,
        "dateModified": datum_iso,
        "author": {
            "@type": "Organization",
            "name": "123KozijnenVergelijker Redactie",
            "url": "https://123kozijnenvergelijker.nl"
        },
        "publisher": {
            "@type": "Organization",
            "name": "123KozijnenVergelijker.nl",
            "url": "https://123kozijnenvergelijker.nl"
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"https://123kozijnenvergelijker.nl/{slug}.html"
        }
    }, ensure_ascii=False, indent=2)

    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titel} | 123KozijnenVergelijker.nl</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="https://123kozijnenvergelijker.nl/{slug}.html">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="blog.css">
    <script type="application/ld+json">
{schema}
    </script>
</head>
<body>

<!-- HEADER -->
<header class="header">
    <div class="container header-inner">
        <div class="logo">
            <a href="index.html">
                <span class="logo-123">123</span><span class="logo-kozijnen">kozijnen</span><span class="logo-verg">vergelijker</span><span class="logo-nl">.nl</span>
            </a>
        </div>
        <nav class="nav">
            <a href="index.html#producten">Producten</a>
            <a href="index.html#voordelen">Voordelen</a>
            <a href="blog.html" style="color:#fff;font-weight:700;">Blog</a>
            <a href="index.html#contact">Contact</a>
            <a href="https://123kozijnenvergelijker.nl/offerte-vergelijken#offerte-aanvragen" class="btn-nav">Gratis offerte</a>
        </nav>
    </div>
</header>

<!-- BLOG DETAIL -->
<div class="blog-detail-wrap">
    <div class="container">

        <nav class="breadcrumb">
            <a href="index.html">Home</a>
            <span>&rsaquo;</span>
            <a href="blog.html">Blog</a>
            <span>&rsaquo;</span>
            <span>{titel}</span>
        </nav>

        <div class="blog-detail-layout">

            <!-- ARTIKEL -->
            <article class="blog-article">

                <div class="blog-article-meta">
                    <span class="blog-cat-tag">{categorie}</span>
                    <span class="blog-date">{datum_str}</span>
                    <span class="blog-readtime">{leestijd} min leestijd</span>
                </div>

                <h1>{titel}</h1>

                <div class="blog-content">
{blog['html_content']}
                </div>

                <div class="blog-author">
                    <div class="blog-author-avatar">KS</div>
                    <div class="blog-author-info">
                        <strong>123KozijnenVergelijker Redactie</strong>
                        <p>Specialist in kunststof kozijnen, deuren en verduurzaming van woningen.</p>
                    </div>
                </div>

                <div class="blog-related">
                    <h3>Meer artikelen</h3>
                    <div class="blog-related-grid">
{gerelateerd_html}
                    </div>
                </div>

            </article>

            <!-- SIDEBAR -->
            <aside class="blog-sidebar">

                <div class="sidebar-widget sidebar-offerte">
                    <h4>Gratis offertes vergelijken</h4>
                    <p>Ontvang 3 offertes van installateurs bij jou in de buurt. Gratis en vrijblijvend.</p>
                    <ul>
                        <li>&#10003; Geen aanbetaling</li>
                        <li>&#10003; 20 jaar garantie</li>
                        <li>&#10003; HR++ glas standaard</li>
                        <li>&#10003; Gratis horren</li>
                    </ul>
                    <a href="https://123kozijnenvergelijker.nl/offerte-vergelijken#offerte-aanvragen" class="btn-primary btn-full" style="margin-top:16px;">Vraag 3 offertes aan</a>
                </div>

                <div class="sidebar-widget">
                    <h4>Recente artikelen</h4>
                    <div class="sidebar-posts">
{sidebar_posts_html}
                    </div>
                </div>

                <div class="sidebar-widget">
                    <h4>Categorieen</h4>
                    <div class="sidebar-cats">
                        <a href="blog.html">Kozijnen</a>
                        <a href="blog.html">Deuren</a>
                        <a href="blog.html">Schuifpuien</a>
                        <a href="blog.html">Verduurzamen</a>
                        <a href="blog.html">Tips</a>
                        <a href="blog.html">Subsidie</a>
                    </div>
                </div>

                <div class="sidebar-widget">
                    <h4>Producten</h4>
                    <div class="sidebar-cats">
                        <a href="kunststof-kozijnen.html">Kunststof kozijnen</a>
                        <a href="kunststof-deuren.html">Kunststof deuren</a>
                        <a href="kunststof-schuifpuien.html">Schuifpuien</a>
                        <a href="offerte-vergelijken.html">Offertes vergelijken</a>
                    </div>
                </div>

            </aside>

        </div>
    </div>
</div>

<!-- FOOTER -->
<footer class="footer">
    <div class="container footer-inner">
        <div class="footer-logo">
            <span class="logo-123">123</span><span class="logo-kozijnen">kozijnen</span><span class="logo-verg">vergelijker</span><span class="logo-nl">.nl</span>
            <p>Kozijnen vergelijken &amp; laten plaatsen<br>Almelo &middot; Haarlem &middot; Bathmen</p>
        </div>
        <div class="footer-links">
            <h5>Producten</h5>
            <a href="kunststof-kozijnen.html">Kunststof kozijnen</a>
            <a href="kunststof-deuren.html">Kunststof deuren</a>
            <a href="kunststof-schuifpuien.html">Schuifpuien</a>
        </div>
        <div class="footer-links">
            <h5>Informatie</h5>
            <a href="over-ons.html">Over ons</a>
            <a href="blog.html">Blog</a>
            <a href="index.html#contact">Contact</a>
        </div>
        <div class="footer-contact">
            <h5>Contact</h5>
            <a href="tel:0541235222" class="footer-contact-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="15" height="15"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81a19.79 19.79 0 01-3.07-8.63A2 2 0 012 .18h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
                0541-23 52 22
            </a>
            <a href="mailto:info@123kozijnenvergelijker.nl" class="footer-contact-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="15" height="15"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                info@123kozijnenvergelijker.nl
            </a>
            <div class="footer-contact-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="15" height="15"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                Almelo &middot; Haarlem &middot; Bathmen
            </div>
        </div>
    </div>

    <div class="footer-werkgebied">
        <div class="container">
            <p class="footer-werkgebied-titel">Werkgebied</p>
            <div class="footer-werkgebied-steden">
                <a href="kozijnen-amsterdam.html">Amsterdam</a>
                <a href="kozijnen-rotterdam.html">Rotterdam</a>
                <a href="kozijnen-den-haag.html">Den Haag</a>
                <a href="kozijnen-utrecht.html">Utrecht</a>
                <a href="kozijnen-eindhoven.html">Eindhoven</a>
                <a href="kozijnen-tilburg.html">Tilburg</a>
                <a href="kozijnen-groningen.html">Groningen</a>
                <a href="kozijnen-almere.html">Almere</a>
                <a href="kozijnen-breda.html">Breda</a>
                <a href="kozijnen-nijmegen.html">Nijmegen</a>
                <a href="kozijnen-enschede.html">Enschede</a>
                <a href="kozijnen-haarlem.html">Haarlem</a>
                <a href="kozijnen-arnhem.html">Arnhem</a>
                <a href="kozijnen-zaandam.html">Zaandam</a>
                <a href="kozijnen-amersfoort.html">Amersfoort</a>
                <a href="kozijnen-apeldoorn.html">Apeldoorn</a>
                <a href="kozijnen-s-hertogenbosch.html">Den Bosch</a>
                <a href="kozijnen-zwolle.html">Zwolle</a>
                <a href="kozijnen-leiden.html">Leiden</a>
                <a href="kozijnen-dordrecht.html">Dordrecht</a>
                <a href="kozijnen-almelo.html">Almelo</a>
                <a href="kozijnen-deventer.html">Deventer</a>
                <a href="kozijnen-hengelo.html">Hengelo</a>
                <a href="kozijnen-assen.html">Assen</a>
                <a href="kozijnen-borne.html">Borne</a>
                <a href="kozijnen-oldenzaal.html">Oldenzaal</a>
                <a href="kozijnen-hardenberg.html">Hardenberg</a>
                <a href="kozijnen-rijssen.html">Rijssen</a>
                <a href="kozijnen-wierden.html">Wierden</a>
                <a href="kozijnen-vriezenveen.html">Vriezenveen</a>
            </div>
        </div>
    </div>

    <div class="footer-bottom">
        <div class="container">
            <p>&copy; 2026 123KozijnenVergelijker.nl &mdash; <a href="algemene-voorwaarden.html">Algemene voorwaarden</a></p>
        </div>
    </div>
</footer>

<script>
function toggleFaq(btn) {{
    var item = btn.parentElement;
    var antwoord = item.querySelector('.faq-antwoord');
    var icon = btn.querySelector('.faq-icon');
    var isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item.open').forEach(function(el) {{
        el.classList.remove('open');
        el.querySelector('.faq-antwoord').classList.remove('open');
        var ic = el.querySelector('.faq-icon');
        if (ic) ic.textContent = '+';
    }});
    if (!isOpen) {{
        item.classList.add('open');
        antwoord.classList.add('open');
        if (icon) icon.textContent = '-';
    }}
}}
</script>

</body>
</html>"""


# --- Blog overzicht (blog.html) opbouwen ---
def genereer_blog_overzicht(index: list) -> None:
    """Schrijft een volledig nieuw blog.html op basis van de index."""
    if not index:
        log.info("Geen blogs in index, blog.html niet bijgewerkt")
        return

    # Sorteer op datum (meest recent eerst)
    gesorteerd = sorted(index, key=lambda x: x.get("datum_iso", ""), reverse=True)

    uitgelicht = gesorteerd[0]
    overige = gesorteerd[1:]

    # Uitgelicht artikel HTML
    uitgelicht_html = f"""
                <a href="{uitgelicht['slug']}.html" class="blog-featured blog-featured-noimg" data-cat="{uitgelicht['categorie']}">
                    <div class="blog-featured-body">
                        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
                            <span class="blog-cat-tag">{uitgelicht['categorie']}</span>
                            <span style="background:#FF6500;color:#fff;font-size:11px;font-weight:700;padding:3px 10px;border-radius:12px;">Uitgelicht</span>
                        </div>
                        <p class="blog-featured-meta">{uitgelicht['datum_display']} &middot; {uitgelicht['leestijd']} min leestijd</p>
                        <h2>{uitgelicht['titel']}</h2>
                        <p>{uitgelicht.get('samenvatting', '')}</p>
                        <span class="blog-lees-meer">Lees meer &rarr;</span>
                    </div>
                </a>"""

    # Blog cards HTML
    cards_html = ""
    for blog in overige:
        cards_html += f"""
                    <a href="{blog['slug']}.html" class="blog-card" data-cat="{blog['categorie']}" style="text-decoration:none;color:inherit;">
                        <div class="blog-card-body">
                            <span class="blog-cat-tag" style="font-size:11px;margin-bottom:8px;display:inline-block;">{blog['categorie']}</span>
                            <p class="blog-card-meta">{blog['datum_display']} &middot; {blog['leestijd']} min</p>
                            <h3>{blog['titel']}</h3>
                            <p>{blog.get('samenvatting', '')}</p>
                            <span class="blog-lees-meer">Lees meer &rarr;</span>
                        </div>
                    </a>"""

    # Sidebar recente posts
    sidebar_recent_html = ""
    for blog in gesorteerd[:5]:
        sidebar_recent_html += f"""
                        <a href="{blog['slug']}.html" class="sidebar-post">
                            <div>
                                <p>{blog['titel']}</p>
                                <span>{blog['datum_display']}</span>
                            </div>
                        </a>"""

    # Categorie tellingen
    cat_counts = {}
    for b in index:
        cat = b.get("categorie", "Kozijnen")
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    cat_html = ""
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        cat_html += f'                        <a href="#">{cat} <span>{count}</span></a>\n'

    totaal = len(index)

    html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog &amp; Kennisbank | 123KozijnenVergelijker.nl</title>
    <meta name="description" content="Alles over kunststof kozijnen, deuren en schuifpuien. {totaal} artikelen vol praktisch advies, tips en subsidie-informatie.">
    <link rel="canonical" href="https://123kozijnenvergelijker.nl/blog.html">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="blog.css">
    <style>
        .blog-overview-wrap {{ padding: 60px 0 80px; background: #f8faf8; }}
        .blog-overview-header {{ text-align: center; margin-bottom: 48px; }}
        .blog-overview-header h1 {{ font-size: 40px; font-weight: 800; color: #1E5C2F; margin-bottom: 12px; }}
        .blog-overview-header p {{ color: #666; font-size: 17px; }}
        .blog-filter {{ display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-bottom: 48px; }}
        .filter-btn {{ padding: 8px 20px; border-radius: 20px; border: 2px solid #1E5C2F; background: transparent; color: #1E5C2F; font-family: 'Poppins', sans-serif; font-size: 14px; font-weight: 600; cursor: pointer; transition: all 0.2s; }}
        .filter-btn:hover, .filter-btn.active {{ background: #1E5C2F; color: #fff; }}
        .blog-overview-layout {{ display: grid; grid-template-columns: 1fr 300px; gap: 48px; align-items: start; }}
        .blog-featured {{ display: block; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 36px; transition: transform 0.2s; border-left: 5px solid #1E5C2F; text-decoration: none; color: inherit; }}
        .blog-featured:hover {{ transform: translateY(-3px); }}
        .blog-featured-body {{ padding: 32px 36px; display: flex; flex-direction: column; }}
        .blog-featured-body h2 {{ font-size: 24px; font-weight: 800; color: #1a1a1a; line-height: 1.3; margin-bottom: 12px; text-align: left; }}
        .blog-featured-body p {{ color: #666; font-size: 15px; margin-bottom: 20px; }}
        .blog-featured-meta {{ font-size: 13px; color: #aaa; margin-bottom: 8px; }}
        .blog-articles-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }}
        .blog-card {{ background: #fff; border-radius: 10px; box-shadow: 0 2px 12px rgba(0,0,0,0.07); transition: transform 0.2s, box-shadow 0.2s; border-top: 3px solid #1E5C2F; overflow: hidden; }}
        .blog-card:hover {{ transform: translateY(-3px); box-shadow: 0 8px 24px rgba(30,92,47,0.12); }}
        .blog-card-body {{ padding: 22px 24px; }}
        .blog-card-meta {{ font-size: 12px; color: #aaa; margin-bottom: 8px; }}
        .blog-card-body h3 {{ font-size: 16px; font-weight: 700; color: #1a1a1a; line-height: 1.35; margin-bottom: 8px; }}
        .blog-card-body p {{ font-size: 14px; color: #666; line-height: 1.55; margin-bottom: 14px; }}
        .blog-lees-meer {{ font-size: 13px; color: #1E5C2F; font-weight: 700; text-decoration: none; }}
        .blog-pagination {{ display: flex; justify-content: center; gap: 8px; margin-top: 48px; }}
        .page-btn {{ width: 40px; height: 40px; border-radius: 6px; border: 2px solid #e8e8e8; background: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Poppins', sans-serif; font-size: 15px; font-weight: 600; cursor: pointer; color: #333; transition: all 0.2s; }}
        .page-btn:hover, .page-btn.active {{ background: #1E5C2F; border-color: #1E5C2F; color: #fff; }}
        .blog-hero-cta {{ background: #1E5C2F; color: #fff; border-radius: 12px; padding: 32px 36px; margin-bottom: 40px; text-align: center; }}
        .blog-hero-cta h2 {{ font-size: 22px; font-weight: 800; margin-bottom: 10px; color: #fff; }}
        .blog-hero-cta p {{ color: rgba(255,255,255,0.85); margin-bottom: 20px; font-size: 15px; }}
        @media (max-width: 900px) {{ .blog-overview-layout {{ grid-template-columns: 1fr; }} }}
        @media (max-width: 600px) {{ .blog-articles-grid {{ grid-template-columns: 1fr; }} .blog-overview-header h1 {{ font-size: 28px; }} }}
    </style>
</head>
<body>

<!-- HEADER -->
<header class="header">
    <div class="container header-inner">
        <div class="logo">
            <a href="index.html">
                <span class="logo-123">123</span><span class="logo-kozijnen">kozijnen</span><span class="logo-verg">vergelijker</span><span class="logo-nl">.nl</span>
            </a>
        </div>
        <nav class="nav">
            <a href="index.html#producten">Producten</a>
            <a href="index.html#voordelen">Voordelen</a>
            <a href="blog.html" style="color:#fff;font-weight:700;">Blog</a>
            <a href="index.html#contact">Contact</a>
            <a href="https://123kozijnenvergelijker.nl/offerte-vergelijken#offerte-aanvragen" class="btn-nav">Gratis offerte</a>
        </nav>
    </div>
</header>

<div class="blog-overview-wrap">
    <div class="container">

        <div class="blog-overview-header">
            <h1>Kennisbank &amp; Blog</h1>
            <p>Alles over kunststof kozijnen, verduurzamen en energiebesparing &mdash; {totaal} artikelen</p>
        </div>

        <!-- CTA Banner -->
        <div class="blog-hero-cta">
            <h2>Klaar om offertes te vergelijken?</h2>
            <p>Ontvang gratis 3 offertes van gecertificeerde installateurs bij jou in de buurt.</p>
            <a href="https://123kozijnenvergelijker.nl/offerte-vergelijken#offerte-aanvragen" class="btn-primary" style="background:#FF6500;border-color:#FF6500;">Vraag 3 gratis offertes aan</a>
        </div>

        <!-- Categoriefilter -->
        <div class="blog-filter">
            <button class="filter-btn active">Alle artikelen</button>
            <button class="filter-btn">Kozijnen</button>
            <button class="filter-btn">Deuren</button>
            <button class="filter-btn">Schuifpuien</button>
            <button class="filter-btn">Verduurzamen</button>
            <button class="filter-btn">Tips</button>
            <button class="filter-btn">Subsidie</button>
        </div>

        <div class="blog-overview-layout">

            <!-- MAIN -->
            <div>

                <!-- Uitgelicht -->
{uitgelicht_html}

                <!-- Artikelen grid -->
                <div class="blog-articles-grid">
{cards_html}
                </div>

            </div>

            <!-- SIDEBAR -->
            <aside class="blog-sidebar">

                <div class="sidebar-widget sidebar-offerte">
                    <h4>Gratis offertes vergelijken</h4>
                    <p>Ontvang 3 offertes van installateurs bij jou in de buurt. Gratis en vrijblijvend.</p>
                    <ul>
                        <li>&#10003; Geen aanbetaling</li>
                        <li>&#10003; 20 jaar garantie</li>
                        <li>&#10003; HR++ glas standaard</li>
                        <li>&#10003; Gratis horren</li>
                    </ul>
                    <a href="https://123kozijnenvergelijker.nl/offerte-vergelijken#offerte-aanvragen" class="btn-primary btn-full" style="margin-top:16px;">Vraag 3 offertes aan</a>
                </div>

                <div class="sidebar-widget">
                    <h4>Recente artikelen</h4>
                    <div class="sidebar-posts">
{sidebar_recent_html}
                    </div>
                </div>

                <div class="sidebar-widget">
                    <h4>Categorieen</h4>
                    <div class="sidebar-cats">
{cat_html}
                    </div>
                </div>

            </aside>

        </div>
    </div>
</div>

<!-- FOOTER -->
<footer class="footer">
    <div class="container footer-inner">
        <div class="footer-logo">
            <span class="logo-123">123</span><span class="logo-kozijnen">kozijnen</span><span class="logo-verg">vergelijker</span><span class="logo-nl">.nl</span>
            <p>Kozijnen vergelijken &amp; laten plaatsen<br>Almelo &middot; Haarlem &middot; Bathmen</p>
        </div>
        <div class="footer-links">
            <h5>Producten</h5>
            <a href="kunststof-kozijnen.html">Kunststof kozijnen</a>
            <a href="kunststof-deuren.html">Kunststof deuren</a>
            <a href="kunststof-schuifpuien.html">Schuifpuien</a>
        </div>
        <div class="footer-links">
            <h5>Informatie</h5>
            <a href="over-ons.html">Over ons</a>
            <a href="blog.html">Blog</a>
            <a href="index.html#contact">Contact</a>
        </div>
        <div class="footer-contact">
            <h5>Contact</h5>
            <a href="tel:0541235222" class="footer-contact-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="15" height="15"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81a19.79 19.79 0 01-3.07-8.63A2 2 0 012 .18h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
                0541-23 52 22
            </a>
            <a href="mailto:info@123kozijnenvergelijker.nl" class="footer-contact-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="15" height="15"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                info@123kozijnenvergelijker.nl
            </a>
        </div>
    </div>
    <div class="footer-bottom">
        <div class="container">
            <p>&copy; 2026 123KozijnenVergelijker.nl &mdash; <a href="algemene-voorwaarden.html">Algemene voorwaarden</a></p>
        </div>
    </div>
</footer>

<script>
(function() {{
    var btns = document.querySelectorAll('.filter-btn');
    var featured = document.querySelector('.blog-featured');
    var cards = document.querySelectorAll('.blog-card');

    btns.forEach(function(btn) {{
        btn.addEventListener('click', function() {{
            btns.forEach(function(b) {{ b.classList.remove('active'); }});
            btn.classList.add('active');
            var cat = btn.textContent.trim();

            if (cat === 'Alle artikelen') {{
                if (featured) featured.style.display = '';
                cards.forEach(function(c) {{ c.style.display = ''; }});
            }} else {{
                if (featured) {{
                    featured.style.display = (featured.getAttribute('data-cat') === cat) ? '' : 'none';
                }}
                cards.forEach(function(c) {{
                    c.style.display = (c.getAttribute('data-cat') === cat) ? '' : 'none';
                }});
            }}
        }});
    }});
}})();
</script>

</body>
</html>"""

    blog_html_path = BASE_DIR / "blog.html"
    with open(blog_html_path, "w", encoding="utf-8") as f:
        f.write(html)
    log.info(f"blog.html bijgewerkt met {totaal} artikelen")


# --- Datum spreiding ---
def bereken_datums(aantal: int, huidige_index: list) -> list:
    """Berekent publicatiedata gespreid over de afgelopen 6 maanden."""
    if huidige_index:
        # Pak meest recente datum en ga verder terug
        meest_recent_iso = max(b.get("datum_iso", "2026-01-01") for b in huidige_index)
        laatste_datum = datetime.strptime(meest_recent_iso, "%Y-%m-%d")
    else:
        laatste_datum = datetime(2026, 3, 12)

    datums = []
    for i in range(aantal):
        # ~3-4 dagen tussenpoze per blog
        delta = timedelta(days=random.randint(2, 5))
        laatste_datum = laatste_datum - delta
        datums.append(laatste_datum)

    return datums


# --- Sitemap bijwerken ---
def voeg_blogs_toe_aan_sitemap(nieuwe_slugs: list[str]) -> None:
    if not SITEMAP_FILE.exists():
        log.warning("sitemap.xml niet gevonden, kan blogs niet toevoegen")
        return
    try:
        tree = ET.parse(SITEMAP_FILE)
        root = tree.getroot()
        NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
        ET.register_namespace("", NS)

        # Check welke slugs al bestaan
        bestaande_urls = {url_el.find(f"{{{NS}}}loc").text for url_el in root.findall(f"{{{NS}}}url") if url_el.find(f"{{{NS}}}loc") is not None}

        toegevoegd = 0
        for slug in nieuwe_slugs:
            url = f"https://123kozijnenvergelijker.nl/{slug}.html"
            if url in bestaande_urls:
                continue
            url_el = ET.SubElement(root, f"{{{NS}}}url")
            ET.SubElement(url_el, f"{{{NS}}}loc").text = url
            ET.SubElement(url_el, f"{{{NS}}}lastmod").text = "2026-03-12"
            ET.SubElement(url_el, f"{{{NS}}}changefreq").text = "monthly"
            ET.SubElement(url_el, f"{{{NS}}}priority").text = "0.6"
            toegevoegd += 1

        if toegevoegd > 0:
            tree.write(SITEMAP_FILE, xml_declaration=True, encoding="utf-8")
            log.info(f"sitemap.xml: {toegevoegd} blog-URLs toegevoegd")
    except Exception as e:
        log.warning(f"Sitemap bijwerken mislukt: {e}")


# --- Hoofd-loop ---
def main():
    parser = argparse.ArgumentParser(description="123KozijnenVergelijker blog generator")
    parser.add_argument("--aantal", type=int, default=BLOGS_PER_RUN, help="Aantal te genereren blogs")
    args = parser.parse_args()

    if not ANTHROPIC_KEY:
        log.error("ANTHROPIC_API_KEY niet gevonden in .env of omgevingsvariabelen!")
        sys.exit(1)

    # Laad bestanden
    onderwerpen = laad_json(ONDERWERPEN_FILE)
    index = laad_json(INDEX_FILE) if INDEX_FILE.exists() else []

    # Kies onderwerpen
    te_genereren = kies_onderwerpen(onderwerpen, args.aantal)
    if not te_genereren:
        log.info("Geen ongebruikte onderwerpen meer beschikbaar.")
        return

    log.info(f"Start generatie van {len(te_genereren)} blogs")

    # Haal interne links
    interne_links = haal_interne_links()
    log.info(f"{len(interne_links)} interne links geladen")

    # Voeg bestaande blog-URLs toe aan interne links
    for b in index:
        interne_links.append({"url": f"{b['slug']}.html", "naam": b["titel"]})

    # Bereken datums
    datums = bereken_datums(len(te_genereren), index)

    # Genereer blogs
    geslaagd = 0
    nieuwe_slugs = []

    for i, onderwerp in enumerate(te_genereren):
        titel = onderwerp["titel"]

        # Check of slug al bestaat
        slug_preview = slugify(titel)
        if any(b["slug"] == slug_preview for b in index):
            log.warning(f"Slug '{slug_preview}' bestaat al, sla over")
            # Markeer toch als gebruikt
            for o in onderwerpen:
                if o["titel"] == titel:
                    o["gebruikt"] = True
            continue

        blog = genereer_blog(titel, interne_links, index)
        if blog is None:
            log.error(f"Blog generatie mislukt voor '{titel}', sla over")
            time.sleep(3)
            continue

        datum = datums[i]
        blog["datum_iso"] = datum.strftime("%Y-%m-%d")
        blog["datum_display"] = format_datum(datum)

        # Sla HTML op
        bestandsnaam = f"{blog['slug']}.html"
        pad = OUTPUT_DIR / bestandsnaam

        # Voeg blog toe aan index VOOR het bouwen (voor gerelateerde links)
        index_entry = {
            "slug": blog["slug"],
            "titel": blog["titel"],
            "categorie": blog["categorie"],
            "datum_iso": blog["datum_iso"],
            "datum_display": blog["datum_display"],
            "leestijd": blog["leestijd"],
            "samenvatting": blog.get("samenvatting", ""),
            "meta_desc": blog.get("meta_desc", ""),
        }
        index.insert(0, index_entry)  # Nieuwste eerst

        # Bouw volledige HTML pagina
        html = bouw_html_pagina(blog, datum, index)

        with open(pad, "w", encoding="utf-8") as f:
            f.write(html)
        log.info(f"  Opgeslagen: {bestandsnaam}")

        # Markeer als gebruikt
        for o in onderwerpen:
            if o["titel"] == titel:
                o["gebruikt"] = True

        nieuwe_slugs.append(blog["slug"])

        # Voeg toe aan interne links voor volgende blogs
        interne_links.append({"url": bestandsnaam, "naam": blog["titel"]})

        geslaagd += 1

        # Sla tussentijds op
        sla_json_op(ONDERWERPEN_FILE, onderwerpen)
        sla_json_op(INDEX_FILE, index)

        # Kleine pauze
        if i < len(te_genereren) - 1:
            time.sleep(2)

    # Finaal opslaan
    sla_json_op(ONDERWERPEN_FILE, onderwerpen)
    sla_json_op(INDEX_FILE, index)

    # Sitemap bijwerken
    if nieuwe_slugs:
        voeg_blogs_toe_aan_sitemap(nieuwe_slugs)

    # Blog overzicht bijwerken
    genereer_blog_overzicht(index)

    log.info(f"Klaar! {geslaagd}/{len(te_genereren)} blogs succesvol gegenereerd.")


if __name__ == "__main__":
    main()
