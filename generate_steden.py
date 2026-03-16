import os

steden = [
    ("amsterdam", "Amsterdam", "Noord-Holland"),
    ("rotterdam", "Rotterdam", "Zuid-Holland"),
    ("den-haag", "Den Haag", "Zuid-Holland"),
    ("utrecht", "Utrecht", "Utrecht"),
    ("eindhoven", "Eindhoven", "Noord-Brabant"),
    ("tilburg", "Tilburg", "Noord-Brabant"),
    ("groningen", "Groningen", "Groningen"),
    ("almere", "Almere", "Flevoland"),
    ("breda", "Breda", "Noord-Brabant"),
    ("nijmegen", "Nijmegen", "Gelderland"),
    ("enschede", "Enschede", "Overijssel"),
    ("haarlem", "Haarlem", "Noord-Holland"),
    ("arnhem", "Arnhem", "Gelderland"),
    ("zaandam", "Zaandam", "Noord-Holland"),
    ("amersfoort", "Amersfoort", "Utrecht"),
    ("apeldoorn", "Apeldoorn", "Gelderland"),
    ("den-bosch", "Den Bosch", "Noord-Brabant"),
    ("hoofddorp", "Hoofddorp", "Noord-Holland"),
    ("maastricht", "Maastricht", "Limburg"),
    ("leiden", "Leiden", "Zuid-Holland"),
    ("dordrecht", "Dordrecht", "Zuid-Holland"),
    ("zoetermeer", "Zoetermeer", "Zuid-Holland"),
    ("zwolle", "Zwolle", "Overijssel"),
    ("deventer", "Deventer", "Overijssel"),
    ("delft", "Delft", "Zuid-Holland"),
    ("alkmaar", "Alkmaar", "Noord-Holland"),
    ("heerlen", "Heerlen", "Limburg"),
    ("venlo", "Venlo", "Limburg"),
    ("leeuwarden", "Leeuwarden", "Friesland"),
    ("emmen", "Emmen", "Drenthe"),
    ("almelo", "Almelo", "Overijssel"),
    ("oss", "Oss", "Noord-Brabant"),
    ("hilversum", "Hilversum", "Noord-Holland"),
    ("hengelo", "Hengelo", "Overijssel"),
    ("roosendaal", "Roosendaal", "Noord-Brabant"),
    ("purmerend", "Purmerend", "Noord-Holland"),
    ("schiedam", "Schiedam", "Zuid-Holland"),
    ("helmond", "Helmond", "Noord-Brabant"),
    ("lelystad", "Lelystad", "Flevoland"),
    ("ede", "Ede", "Gelderland"),
]

def make_page(slug, stad, provincie):
    return """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kunststof Kozijnen """ + stad + """ | Gratis Offertes Vergelijken | 123KozijnenVergelijker.nl</title>
    <meta name="description" content="Kunststof kozijnen laten plaatsen in """ + stad + """? Vergelijk vrijblijvend 3 offertes van kozijnbedrijven in """ + provincie + """. HR++ glas standaard, 20 jaar garantie, geen aanbetaling.">
    <link rel="canonical" href="https://www.123kozijnenvergelijker.nl/kozijnen-""" + slug + """.html">
    <link rel="icon" href="favicon.svg" type="image/svg+xml">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>

<header class="header">
    <div class="container header-inner">
        <div class="logo">
            <a href="index.html" style="text-decoration:none;">
                <span class="logo-123">123</span><span class="logo-kozijnen">kozijnen</span><span class="logo-verg">vergelijker</span><span class="logo-nl">.nl</span>
            </a>
        </div>
        <nav class="nav" id="navLinks">
            <a href="kunststof-kozijnen.html">Kozijnen</a>
            <a href="kunststof-deuren.html">Deuren</a>
            <a href="kunststof-schuifpuien.html">Schuifpuien</a>
            <a href="projecten.html">Projecten</a>
            <a href="financiering.html">Financiering</a>
            <a href="index.html#contact">Contact</a>
            <a href="offerte-vergelijken.html" class="btn-nav">3 Offertes vergelijken</a>
        </nav>
        <button class="hamburger" id="hamburger" aria-label="Menu openen" onclick="document.getElementById('navLinks').classList.toggle('open');this.classList.toggle('open')">
            <span></span><span></span><span></span>
        </button>
    </div>
</header>

<div class="container">
    <nav class="breadcrumb">
        <a href="index.html">Home</a>
        <span>&rsaquo;</span>
        <span>Kozijnen """ + stad + """</span>
    </nav>
</div>

<section class="hero" style="background:linear-gradient(135deg,#1E5C2F 0%,#2d7a42 100%);padding:60px 0 50px;">
    <div class="container">
        <div style="max-width:700px;">
            <div class="hero-label" style="background:rgba(255,255,255,0.15);color:#fff;display:inline-block;padding:6px 14px;border-radius:20px;font-size:13px;font-weight:600;margin-bottom:16px;">
                &starf; """ + stad + """ &middot; """ + provincie + """
            </div>
            <h1 style="font-size:clamp(28px,4.5vw,48px);font-weight:800;color:#fff;line-height:1.15;margin-bottom:16px;">
                Kunststof kozijnen laten plaatsen in """ + stad + """
            </h1>
            <p style="font-size:17px;color:rgba(255,255,255,0.88);line-height:1.65;margin-bottom:28px;max-width:600px;">
                Vergelijk vrijblijvend offertes van kozijnbedrijven actief in """ + stad + """ en omgeving. HR++ glas standaard inbegrepen, geen aanbetaling, 20 jaar garantie.
            </p>
            <div style="display:flex;gap:12px;flex-wrap:wrap;">
                <a href="offerte-vergelijken.html" class="btn-primary btn-pulse">Vraag 3 gratis offertes aan</a>
                <a href="#waarom" class="btn-secondary">Meer informatie</a>
            </div>
            <div style="margin-top:24px;display:flex;gap:24px;flex-wrap:wrap;">
                <span style="color:rgba(255,255,255,0.8);font-size:13px;">&#9733; 9.3 gemiddeld (149 reviews)</span>
                <span style="color:rgba(255,255,255,0.8);font-size:13px;">&#10003; Geen aanbetaling</span>
                <span style="color:rgba(255,255,255,0.8);font-size:13px;">&#10003; 20 jaar garantie</span>
            </div>
        </div>
    </div>
</section>

<div style="background:linear-gradient(135deg,#FF6500,#e85500);padding:14px 0;text-align:center;">
    <div class="container">
        <span style="color:#fff;font-weight:700;font-size:15px;">&#127873; Gratis horren bij aanvraag in maart &middot; Actie geldig t/m 31 maart 2026</span>
    </div>
</div>

<section style="background:#f8f9fa;padding:32px 0;">
    <div class="container">
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;text-align:center;">
            <div>
                <div style="font-size:28px;font-weight:800;color:#FF6500;">523+</div>
                <div style="font-size:13px;color:#666;">Tevreden huishoudens</div>
            </div>
            <div>
                <div style="font-size:28px;font-weight:800;color:#FF6500;">20 jaar</div>
                <div style="font-size:13px;color:#666;">Garantie op kozijnen</div>
            </div>
            <div>
                <div style="font-size:28px;font-weight:800;color:#FF6500;">&euro;800-&euro;1.500</div>
                <div style="font-size:13px;color:#666;">Besparing per jaar</div>
            </div>
            <div>
                <div style="font-size:28px;font-weight:800;color:#FF6500;">9.3</div>
                <div style="font-size:13px;color:#666;">Gemiddeld cijfer</div>
            </div>
        </div>
    </div>
</section>

<section class="sectie sectie-licht" id="waarom">
    <div class="container">
        <div style="text-align:center;margin-bottom:48px;">
            <span class="sectie-tag">Kozijnen in """ + stad + """</span>
            <h2>Waarom kiezen voor nieuwe kozijnen in """ + stad + """?</h2>
            <p class="section-sub">Woningeigenaren in """ + provincie + """ besparen gemiddeld &euro;800 tot &euro;1.500 per jaar na plaatsing van nieuwe kozijnen</p>
        </div>
        <div class="voordelen-grid">
            <div class="voordeel-item">
                <div class="voordeel-icon">
                    <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="#1E5C2F" stroke-width="2" fill="#f0f6f1"/><path d="M13 20l5 5 9-10" stroke="#1E5C2F" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <h4>Lagere energierekening</h4>
                <p>HR++ glas isoleert tot 30% beter dan enkel glas. Bespaar &euro;800 tot &euro;1.500 per jaar op je energiekosten in """ + stad + """.</p>
            </div>
            <div class="voordeel-item">
                <div class="voordeel-icon">
                    <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="#1E5C2F" stroke-width="2" fill="#f0f6f1"/><text x="20" y="26" text-anchor="middle" font-size="16" font-weight="800" fill="#1E5C2F" font-family="Arial">&euro;</text></svg>
                </div>
                <h4>Geen aanbetaling</h4>
                <p>Je betaalt pas na oplevering. Vrijblijvende offertes zonder verplichtingen. 0% rente via Nationaal Warmtefonds bij inkomen tot &euro;60.000.</p>
            </div>
            <div class="voordeel-item">
                <div class="voordeel-icon">
                    <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="#1E5C2F" stroke-width="2" fill="#f0f6f1"/><path d="M20 12v8l5 3" stroke="#1E5C2F" stroke-width="2.5" stroke-linecap="round"/></svg>
                </div>
                <h4>Snel geregeld</h4>
                <p>Offerte binnen 24 uur na aanvraag. Kozijnbedrijven actief in """ + stad + """ plannen het adviesgesprek bij jou thuis.</p>
            </div>
            <div class="voordeel-item">
                <div class="voordeel-icon">
                    <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="#1E5C2F" stroke-width="2" fill="#f0f6f1"/><path d="M20 10a10 10 0 010 20 10 10 0 010-20z" fill="#1E5C2F"/></svg>
                </div>
                <h4>Subsidie geregeld</h4>
                <p>Via de ISDE-regeling ontvang je tot &euro;111 per m&sup2; subsidie op HR++ en triple glas. Wij begeleiden de aanvraag bij RVO.</p>
            </div>
        </div>
    </div>
</section>

<section class="sectie" style="background:#fff;">
    <div class="container">
        <div style="text-align:center;margin-bottom:48px;">
            <h2>Ons aanbod in """ + stad + """ en omgeving</h2>
            <p class="section-sub">Op maat gemaakt, inclusief HR++ glas, gratis horren en 20 jaar garantie</p>
        </div>
        <div class="producten-grid">
            <div class="product-cat">
                <div class="product-cat-img placeholder-green">
                    <svg class="prod-icon-svg" viewBox="0 0 64 64" fill="none"><rect x="6" y="8" width="52" height="48" rx="3" stroke="rgba(255,255,255,0.9)" stroke-width="3" fill="none"/><line x1="32" y1="8" x2="32" y2="56" stroke="rgba(255,255,255,0.6)" stroke-width="2"/><line x1="6" y1="32" x2="58" y2="32" stroke="rgba(255,255,255,0.6)" stroke-width="2"/></svg>
                    <span class="prod-title">Kunststof Kozijnen</span>
                </div>
                <div class="product-cat-body">
                    <h3>Kunststof Kozijnen """ + stad + """</h3>
                    <p class="prod-desc">Op maat gemaakt voor jouw woning in """ + stad + """. Onderhoudsvrij, 40 tot 60 jaar mee en HR++ glas altijd standaard inbegrepen.</p>
                    <ul class="prod-voordelen">
                        <li>HR++ isolatieglas standaard</li>
                        <li>200+ kleuren en structuren</li>
                        <li>20 jaar garantie</li>
                        <li>Gratis horren inbegrepen</li>
                    </ul>
                    <div class="product-cat-footer">
                        <a href="offerte-vergelijken.html" class="btn-primary btn-sm">Gratis offerte aanvragen</a>
                    </div>
                </div>
            </div>
            <div class="product-cat">
                <div class="product-cat-img placeholder-green">
                    <svg class="prod-icon-svg" viewBox="0 0 64 64" fill="none"><rect x="12" y="4" width="36" height="56" rx="3" stroke="rgba(255,255,255,0.9)" stroke-width="3" fill="none"/><circle cx="40" cy="32" r="3.5" fill="rgba(255,255,255,0.9)"/></svg>
                    <span class="prod-title">Kunststof Deuren</span>
                </div>
                <div class="product-cat-body">
                    <h3>Kunststof Deuren """ + stad + """</h3>
                    <p class="prod-desc">Veiliger, stiller en energiezuiniger. RC2 inbraakwering en meerpuntssluiting standaard inbegrepen.</p>
                    <ul class="prod-voordelen">
                        <li>RC2 inbraakwering standaard</li>
                        <li>Uitstekende isolatie</li>
                        <li>Op maat gemaakt</li>
                        <li>20 jaar garantie</li>
                    </ul>
                    <div class="product-cat-footer">
                        <a href="offerte-vergelijken.html" class="btn-primary btn-sm">Gratis offerte aanvragen</a>
                    </div>
                </div>
            </div>
            <div class="product-cat">
                <div class="product-cat-img placeholder-green">
                    <svg class="prod-icon-svg" viewBox="0 0 64 64" fill="none"><rect x="4" y="8" width="56" height="48" rx="3" stroke="rgba(255,255,255,0.9)" stroke-width="3" fill="none"/><line x1="32" y1="8" x2="32" y2="56" stroke="rgba(255,255,255,0.6)" stroke-width="2"/></svg>
                    <span class="prod-title">Schuifpuien</span>
                </div>
                <div class="product-cat-body">
                    <h3>Schuifpuien """ + stad + """</h3>
                    <p class="prod-desc">Verbind jouw woonkamer met de tuin. Tot 6 meter breed, energiezuinig en RC2 beslag standaard inbegrepen.</p>
                    <ul class="prod-voordelen">
                        <li>HR++ glas standaard</li>
                        <li>Tot 6 meter breedte</li>
                        <li>RC2 inbraakwering</li>
                        <li>Lichte bediening</li>
                    </ul>
                    <div class="product-cat-footer">
                        <a href="offerte-vergelijken.html" class="btn-primary btn-sm">Gratis offerte aanvragen</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="sectie sectie-licht">
    <div class="container">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;">
            <div>
                <span class="sectie-tag">Financiering en subsidie</span>
                <h2>Kozijnen in """ + stad + """ financieren met 0% rente</h2>
                <p style="color:#555;line-height:1.7;margin-bottom:20px;">Via de <strong>Energiebespaarlening</strong> van het Nationaal Warmtefonds leen je tot &euro;28.000 tegen 0% rente bij een verzamelinkomen tot &euro;60.000. Combineer dit met ISDE-subsidie tot &euro;111 per m&sup2; glas.</p>
                <ul style="list-style:none;padding:0;margin-bottom:28px;">
                    <li style="padding:8px 0;border-bottom:1px solid #eee;color:#444;">&#10003; &nbsp;0% rente bij verzamelinkomen tot &euro;60.000</li>
                    <li style="padding:8px 0;border-bottom:1px solid #eee;color:#444;">&#10003; &nbsp;Lening van &euro;1.000 tot &euro;28.000</li>
                    <li style="padding:8px 0;border-bottom:1px solid #eee;color:#444;">&#10003; &nbsp;ISDE-subsidie tot &euro;111 per m&sup2; glas</li>
                    <li style="padding:8px 0;color:#444;">&#10003; &nbsp;Wij begeleiden beide aanvragen</li>
                </ul>
                <a href="financiering.html" class="btn-primary">Meer over financiering</a>
            </div>
            <div style="background:#1E5C2F;border-radius:16px;padding:36px;color:#fff;">
                <div style="font-size:13px;font-weight:600;letter-spacing:1px;opacity:0.7;margin-bottom:16px;">REKENVOORBEELD """ + stad.upper() + """</div>
                <div style="font-size:15px;opacity:0.85;margin-bottom:8px;">Investering nieuwe kozijnen</div>
                <div style="font-size:32px;font-weight:800;margin-bottom:20px;">&euro; 12.000</div>
                <div style="background:rgba(255,255,255,0.1);border-radius:10px;padding:16px;margin-bottom:12px;">
                    <div style="font-size:13px;opacity:0.7;">Maandlast (120 mnd, 0% rente)</div>
                    <div style="font-size:24px;font-weight:700;color:#FF6500;">&euro; 100 / mnd</div>
                </div>
                <div style="font-size:13px;opacity:0.75;">Terwijl jij al snel &euro;800 tot &euro;1.500 per jaar bespaart op je energierekening.</div>
            </div>
        </div>
    </div>
</section>

<section class="sectie" style="background:linear-gradient(135deg,#1E5C2F 0%,#2d7a42 100%);text-align:center;">
    <div class="container" style="max-width:700px;">
        <h2 style="color:#fff;font-size:clamp(24px,3.5vw,38px);margin-bottom:16px;">Vergelijk offertes van kozijnbedrijven in """ + stad + """</h2>
        <p style="color:rgba(255,255,255,0.85);font-size:16px;margin-bottom:32px;line-height:1.65;">
            Vul het formulier in en ontvang geheel vrijblijvend 3 offertes van gerenommeerde bedrijven in jouw buurt. Gratis, snel en zonder verplichtingen.
        </p>
        <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-bottom:24px;">
            <a href="offerte-vergelijken.html" class="btn-primary btn-pulse" style="font-size:17px;padding:16px 32px;">Vraag 3 gratis offertes aan</a>
            <a href="index.html#contact" class="btn-secondary">Direct contact</a>
        </div>
        <div style="display:flex;gap:20px;justify-content:center;flex-wrap:wrap;">
            <span style="color:rgba(255,255,255,0.75);font-size:13px;">&#10003; Vrijblijvend</span>
            <span style="color:rgba(255,255,255,0.75);font-size:13px;">&#10003; Gratis</span>
            <span style="color:rgba(255,255,255,0.75);font-size:13px;">&#10003; Binnen 24 uur reactie</span>
            <span style="color:rgba(255,255,255,0.75);font-size:13px;">&#10003; Geen aanbetaling</span>
        </div>
    </div>
</section>

<section class="sectie sectie-licht">
    <div class="container" style="max-width:800px;">
        <h2 style="text-align:center;margin-bottom:40px;">Veelgestelde vragen over kozijnen in """ + stad + """</h2>
        <div class="faq-list">
            <div class="faq-item">
                <button class="faq-vraag" onclick="toggleFaq(this)">
                    Wat kost het laten plaatsen van kunststof kozijnen in """ + stad + """?
                    <span class="faq-icon">+</span>
                </button>
                <div class="faq-antwoord">
                    <p>De kosten voor kunststof kozijnen in """ + stad + """ hangen af van het aantal kozijnen, de maten en het glastype. Een standaard tussenwoning rekent gemiddeld &euro;8.000 tot &euro;18.000 voor een volledige vervanging inclusief HR++ glas en montage. Vraag vrijblijvend 3 offertes aan om de beste prijs in """ + stad + """ te vergelijken.</p>
                </div>
            </div>
            <div class="faq-item">
                <button class="faq-vraag" onclick="toggleFaq(this)">
                    Kan ik subsidie krijgen voor kozijnen in """ + stad + """?
                    <span class="faq-icon">+</span>
                </button>
                <div class="faq-antwoord">
                    <p>Ja. Via de ISDE-regeling van de Rijksoverheid ontvang je tot &euro;111 per m&sup2; voor HR++ of triple glas. Bij een gemiddelde woning is dat al snel &euro;300 tot &euro;1.300 directe subsidie. Wij verzorgen de aanvraag bij RVO namens jou.</p>
                </div>
            </div>
            <div class="faq-item">
                <button class="faq-vraag" onclick="toggleFaq(this)">
                    Hoe lang duurt de plaatsing van nieuwe kozijnen in """ + stad + """?
                    <span class="faq-icon">+</span>
                </button>
                <div class="faq-antwoord">
                    <p>De plaatsing in een gemiddelde woning in """ + stad + """ duurt doorgaans 1 tot 3 werkdagen. Na het adviesgesprek aan huis wordt de levertijd ingepland, gemiddeld 3 tot 6 weken na opdracht.</p>
                </div>
            </div>
            <div class="faq-item">
                <button class="faq-vraag" onclick="toggleFaq(this)">
                    Wat is de terugverdientijd van kozijnen in """ + stad + """?
                    <span class="faq-icon">+</span>
                </button>
                <div class="faq-antwoord">
                    <p>De gemiddelde terugverdientijd van kunststof kozijnen is 10 tot 12 jaar. Met ISDE-subsidie kan dat dalen tot 9 tot 10 jaar. Kozijnen gaan 35 tot 50 jaar mee, dus daarna is het pure winst. Via de Energiebespaarlening (0% rente bij inkomen tot &euro;60.000) zijn je maandlasten direct lager dan je energiebesparing.</p>
                </div>
            </div>
            <div class="faq-item">
                <button class="faq-vraag" onclick="toggleFaq(this)">
                    Heb ik een vergunning nodig voor nieuwe kozijnen in """ + stad + """?
                    <span class="faq-icon">+</span>
                </button>
                <div class="faq-antwoord">
                    <p>In de meeste gevallen niet. Bij vervanging in dezelfde maat en stijl is een omgevingsvergunning doorgaans niet nodig. Bij monumentale panden in """ + stad + """ kan dat anders zijn. Wij adviseren je hier gratis over tijdens het adviesgesprek aan huis.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="sectie" style="background:#fff;">
    <div class="container">
        <h2 style="text-align:center;margin-bottom:8px;">Wat klanten zeggen</h2>
        <p class="section-sub" style="text-align:center;margin-bottom:40px;">&#9733;&#9733;&#9733;&#9733;&#9733; Gemiddeld 9.3 op basis van 149 beoordelingen</p>
        <div class="reviews-grid">
            <div class="review-item">
                <div class="review-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
                <p>"Drie offertes ontvangen, de beste was 20% goedkoper dan wat ik zelf had gevonden. Heel tevreden met het resultaat en de begeleiding."</p>
                <strong>Sandra K., """ + stad + """</strong>
            </div>
            <div class="review-item">
                <div class="review-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
                <p>"Subsidieaanvraag helemaal verzorgd. Kozijnen er nu 6 weken in en het huis is merkbaar warmer en stiller. Aanrader!"</p>
                <strong>Peter V., """ + provincie + """</strong>
            </div>
            <div class="review-item">
                <div class="review-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
                <p>"Snel geregeld, netjes gemonteerd en de horren zaten er gratis bij. Energierekening al flink omlaag in de eerste maand."</p>
                <strong>M. de Boer, """ + stad + """</strong>
            </div>
        </div>
    </div>
</section>

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
            <a href="projecten.html">Projecten</a>
            <a href="financiering.html">Financiering</a>
            <a href="offerte-vergelijken.html">Offertes vergelijken</a>
        </div>
        <div class="footer-contact">
            <h5>Contact</h5>
            <p>info@123kozijnenvergelijker.nl</p>
            <p>0546-23 20 66</p>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; 2026 123KozijnenVergelijker.nl &middot; <a href="privacyverklaring.html">Privacyverklaring</a> &middot; <a href="algemene-voorwaarden.html">Algemene voorwaarden</a></p>
    </div>
</footer>

<script>
function toggleFaq(btn) {
    btn.classList.toggle('open');
    btn.nextElementSibling.classList.toggle('open');
}
</script>

</body>
</html>"""

output_dir = "C:/Users/knusl/Downloads/kozijnstunter"
generated = []
for slug, stad, provincie in steden:
    filename = "kozijnen-" + slug + ".html"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(make_page(slug, stad, provincie))
    generated.append(filename)

print("Aangemaakt: " + str(len(generated)) + " paginas")
for f in generated:
    print("  " + f)
