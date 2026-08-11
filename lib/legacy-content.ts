import fs from "node:fs";
import path from "node:path";

export type LegacyPageType = "article" | "location" | "product" | "legal" | "standard";

export type LegacyPage = {
  slug: string;
  title: string;
  description: string;
  canonical?: string;
  h1: string;
  label: string;
  type: LegacyPageType;
  content: string;
};

const productSlugs = new Set([
  "kunststof-kozijnen.html",
  "kunststof-deuren.html",
  "kunststof-schuifpuien.html",
  "financiering.html",
  "calculator.html",
  "offerte-vergelijken.html",
  "offerte-kunststof-kozijnen.html",
  "lp-kozijnen.html",
  "lander.html",
]);

const legalSlugs = new Set([
  "privacyverklaring.html",
  "algemene-voorwaarden.html",
]);

const reservedSlugs = new Set([
  "index.html",
  "blog.html",
  "projecten.html",
  "offerte-aanvragen.html",
  "bedankt.html",
  "blog-detail.html",
]);

const descriptionOverrides: Record<string, string> = {
  "kunststof-kozijnen.html": "Kunststof kozijnen laten plaatsen? Vergelijk offertes op totaalprijs, profiel, glastype, montage, garantie en relevante keurmerken.",
  "kunststof-deuren.html": "Kunststof deuren vergelijken? Bekijk uitvoering, isolatie, veiligheid, montage, garantie en totaalprijs per aanbieder.",
  "kunststof-schuifpuien.html": "Kunststof schuifpui vergelijken? Let op profiel, glas, afmetingen, bediening, montage, garantie en totaalprijs.",
};

function rootFile(slug: string) {
  return path.join(process.cwd(), slug);
}

export function listLegacyHtmlFiles() {
  return fs
    .readdirSync(process.cwd())
    .filter((name) => name.endsWith(".html"))
    .filter((name) => name !== "index.html");
}

export function legacyExists(slug: string) {
  if (!slug.endsWith(".html")) return false;
  return fs.existsSync(rootFile(slug));
}

export function readLegacyHtml(slug: string) {
  return fs.readFileSync(rootFile(slug), "utf8");
}

function matchContent(html: string, pattern: RegExp) {
  const match = html.match(pattern);
  return match?.[1]?.trim() ?? "";
}

function textOnly(value: string) {
  return value
    .replace(/<[^>]+>/g, " ")
    .replace(/&nbsp;/gi, " ")
    .replace(/&amp;/gi, "&")
    .replace(/&quot;/gi, '"')
    .replace(/&#39;/gi, "'")
    .replace(/&euro;/gi, "€")
    .replace(/\s+/g, " ")
    .trim();
}

export function neutralizeComparisonCopy(value: string) {
  const replacements: Array<[RegExp, string]> = [
    [
      /Bij 123KozijnenVergelijker is HR\+\+ glas altijd standaard inbegrepen en geldt er 20 jaar garantie\./gi,
      "Controleer per offerte welk glastype is inbegrepen en welke garantie geldt op materiaal en montage.",
    ],
    [
      /Onze kozijnen worden gemaakt van hoogwaardig VEKA PVC-profiel en worden op maat geproduceerd voor jouw woning\. HR\+\+ glas is standaard inbegrepen\./gi,
      "Kunststof kozijnen worden op maat geproduceerd en zijn verkrijgbaar met verschillende profielmerken en glastypen. Controleer per offerte welk profiel en glas zijn inbegrepen.",
    ],
    [
      /Onze adviseurs helpen je bij de aanvraag zodat je geen geld laat liggen\./gi,
      "Controleer de actuele voorwaarden bij RVO en vraag indien nodig hulp bij de subsidieaanvraag.",
    ],
    [
      /Onze adviseurs helpen je hier graag bij\./gi,
      "Vraag de gekozen aanbieder indien nodig om hulp bij de aanvraag.",
    ],
    [
      /een adviseur van de gekozen aanbieder helpen je hier graag bij\./gi,
      "Een adviseur van de gekozen aanbieder kan je hier indien nodig bij helpen.",
    ],
    [
      /Plan een vrijblijvend adviesgesprek aan huis\. We meten op, geven advies en sturen een offerte binnen 24 uur\./gi,
      "Vraag vrijblijvend offertes aan en vergelijk prijs, materiaal, glas, montage, planning en voorwaarden.",
    ],
    [
      /Onze monteurs werken schoon en zorgen dat je woning aan het eind van de dag wind- en waterdicht is\./gi,
      "Bespreek met de gekozen aanbieder hoe de montage wordt uitgevoerd en hoe de woning wordt opgeleverd.",
    ],
    [
      /Onze VEKA-profielen bevatten UV-stabilisatoren die dit sterk vertragen\./gi,
      "De UV-bestendigheid verschilt per profiel; vraag naar productspecificaties en garantie op verkleuring.",
    ],
    [
      /Wij adviseren je hierover tijdens het adviesgesprek\./gi,
      "Controleer bij twijfel de regels bij je gemeente of via het Omgevingsloket.",
    ],
    [
      /Bij ieder kozijn ontvang je gratis horren in dezelfde kleur\./gi,
      "Vraag per offerte of horren zijn inbegrepen of als optie worden aangeboden.",
    ],
    [
      /Hiermee bespaar je tot 30% op je stookkosten ten opzichte van enkel glas\./gi,
      "De uiteindelijke energiebesparing hangt af van het huidige glas, de woning en het complete kozijn.",
    ],
    [
      /Bij vervanging van enkel glas bespaar je gemiddeld €800 tot €1\.500 per jaar op je energierekening\./gi,
      "De besparing verschilt sterk per woning, glasoppervlak, huidige beglazing en energiegebruik.",
    ],
    [
      /In vergelijking met houten kozijnen bespaar je zo al gauw <strong>€300 tot €600 per jaar<\/strong> aan onderhoud en schilderwerk\./gi,
      "In vergelijking met houten kozijnen vervalt periodiek schilderwerk, waardoor de onderhoudslast doorgaans lager is.",
    ],
    [
      /<strong>€ 1\.150<\/strong>\s*<span>gemiddelde besparing per jaar<\/span>/gi,
      "<strong>Per woning verschillend</strong><span>laat besparing onderbouwen voor jouw situatie</span>",
    ],
    [
      /<h3>ISDE-subsidie in 2026: tot €111 per m²<\/h3>/gi,
      "<h3>ISDE-subsidie: controleer de actuele voorwaarden</h3>",
    ],
    [
      /Via de <strong>ISDE-subsidie<\/strong> ontvang je in 2026 bij vervanging naar <strong>HR\+\+ glas €25 per m²<\/strong> en bij <strong>triple glas zelfs €111 per m²<\/strong>\. Minimum is 3 m², maximum 45 m²\. Combineer je de kozijnen met een warmtepomp of zonneboiler\? Dan worden de bedragen verdubbeld\. Naast ISDE is er ook het <strong>Nationaal Warmtefonds<\/strong> met 0% rente bij een inkomen onder €60\.000\. Controleer de actuele voorwaarden bij RVO en vraag indien nodig hulp bij de subsidieaanvraag\./gi,
      "Voor isolerend glas en kozijnmaatregelen kunnen subsidiemogelijkheden gelden. Bedragen en voorwaarden kunnen wijzigen; controleer daarom altijd de actuele informatie bij RVO en het Nationaal Warmtefonds voordat je rekent met een voordeel.",
    ],
    [
      /<div class="subsidie-rij"><span>HR\+\+ glas<\/span><strong>€ 25 per m²<\/strong><\/div>/gi,
      "<div class=\"subsidie-rij\"><span>HR++ glas</span><strong>Controleer actueel bedrag</strong></div>",
    ],
    [
      /<div class="subsidie-rij highlight"><span>Triple glas \(HR\+\+\+\)<\/span><strong>€ 111 per m²<\/strong><\/div>/gi,
      "<div class=\"subsidie-rij highlight\"><span>Triple glas (HR+++)</span><strong>Controleer actueel bedrag</strong></div>",
    ],
    [
      /<div class="subsidie-rij"><span>Combinatie met warmtepomp<\/span><strong>bedragen x2<\/strong><\/div>/gi,
      "<div class=\"subsidie-rij\"><span>Combineren van maatregelen</span><strong>Voorwaarden kunnen verschillen</strong></div>",
    ],
    [
      /Hoeveel ISDE-subsidie krijg ik in 2026 voor nieuwe kozijnen\?/gi,
      "Hoe werkt ISDE-subsidie voor nieuwe kozijnen?",
    ],
    [
      /Via de ISDE-subsidie ontvang je in 2026 bij vervanging naar <strong>HR\+\+ glas €25 per m²<\/strong> en bij <strong>triple glas €111 per m²<\/strong>\. De subsidie geldt bij minimaal 3 m² en maximaal 45 m² glas\. Combineer je de kozijnen met een warmtepomp of zonneboiler, dan worden de subsidiebedragen verdubbeld\. Je vraagt de subsidie aan via RVO\.nl, uiterlijk 24 maanden na de eerste werkzaamheden\. [^<]*<\/p>/gi,
      "Voor isolerend glas en kozijnmaatregelen kan ISDE beschikbaar zijn. De bedragen, oppervlaktegrenzen en combinatieregels kunnen wijzigen. Controleer daarom de actuele voorwaarden en aanvraagtermijn rechtstreeks bij RVO.</p>",
    ],
    [
      /Naast ISDE kun je ook gebruikmaken van het <strong>Nationaal Warmtefonds<\/strong>: 0% rente bij een verzamelinkomen onder €60\.000, leningen vanaf €1\.000 tot €28\.000 met looptijd tot 20 jaar\./gi,
      "Naast subsidie kan financiering via het Nationaal Warmtefonds een mogelijkheid zijn. Controleer de actuele rente, inkomensvoorwaarden, bedragen en looptijden voordat je een keuze maakt.",
    ],
    [
      /RC2 inbraakwerende beslag standaard\. RC3 als optie\./gi,
      "Vergelijk welk veiligheidsbeslag standaard is inbegrepen en welke upgrades mogelijk zijn.",
    ],
    [
      /<strong>200\+ kleuren<\/strong>\s*<p>Wit, antraciet, houtlook, crème en meer\. Binnen en buiten verschillende kleur mogelijk\.<\/p>/gi,
      "<strong>Kleuren en afwerking</strong><p>Vergelijk beschikbare kleuren, folies en combinaties voor binnen- en buitenzijde per aanbieder.</p>",
    ],
    [
      /<strong>100% recyclebaar<\/strong>\s*<p>PVC is volledig recyclebaar\. Duurzame keuze voor het milieu\.<\/p>/gi,
      "<strong>Recycling en circulariteit</strong><p>Vraag naar materiaalopbouw, gerecycled aandeel en verwerking aan het einde van de levensduur.</p>",
    ],
    [
      /Ug-waarde 1,0 W\/m²K\. Optioneel HR\+\+\+ \(Ug 0,7\) beschikbaar\./gi,
      "Vergelijk de Ug-waarde van het glas en de Uw-waarde van het complete kozijn per offerte.",
    ],
    [
      /<tr><td>Profielmateriaal<\/td><td>VEKA PVC \(6-kamer profiel\)<\/td><\/tr>/gi,
      "<tr><td>Profielmateriaal</td><td>Vergelijk merk, materiaal en profielopbouw per offerte</td></tr>",
    ],
    [
      /<tr><td>Glastype standaard<\/td><td>HR\+\+ \(Ug = 1,0 W\/m²K\)<\/td><\/tr>/gi,
      "<tr><td>Glastype</td><td>Controleer per offerte welk glas is inbegrepen en welke isolatiewaarde geldt</td></tr>",
    ],
    [
      /<tr><td>Glastype optioneel<\/td><td>HR\+\+\+ \(Ug = 0,7 W\/m²K\)<\/td><\/tr>/gi,
      "<tr><td>Glasopties</td><td>Vergelijk HR++ en triple glas op isolatiewaarde en meerprijs</td></tr>",
    ],
    [
      /<tr><td>Profilerbreedte<\/td><td>70 mm \/ 82 mm<\/td><\/tr>/gi,
      "<tr><td>Profielopbouw</td><td>Verschilt per merk en systeem; vergelijk specificaties</td></tr>",
    ],
    [
      /<tr><td>Maximale hoogte<\/td><td>2\.500 mm<\/td><\/tr>/gi,
      "<tr><td>Afmetingen</td><td>Maximale maten verschillen per systeem en toepassing</td></tr>",
    ],
    [
      /<tr><td>Maximale breedte<\/td><td>2\.400 mm<\/td><\/tr>/gi,
      "",
    ],
    [
      /<tr><td>Inbraakweerstand<\/td><td>RC2 \(standaard\), RC3 \(optioneel\)<\/td><\/tr>/gi,
      "<tr><td>Inbraakwering</td><td>Vergelijk veiligheidsklasse, beslag en certificering per offerte</td></tr>",
    ],
    [
      /<tr><td>Garantie kozijn<\/td><td>20 jaar<\/td><\/tr>/gi,
      "<tr><td>Garantie kozijn</td><td>Verschilt per aanbieder en product</td></tr>",
    ],
    [
      /<tr><td>Garantie isolatieglas<\/td><td>10 jaar dichting<\/td><\/tr>/gi,
      "<tr><td>Garantie isolatieglas</td><td>Controleer de voorwaarden per offerte</td></tr>",
    ],
    [
      /<tr><td>Kleuren<\/td><td>200\+ RAL kleuren en foliekleur<\/td><\/tr>/gi,
      "<tr><td>Kleuren</td><td>Kleur- en folieaanbod verschilt per aanbieder</td></tr>",
    ],
    [
      /<tr><td>Certificering<\/td><td>KOMO, SKG<\/td><\/tr>/gi,
      "<tr><td>Certificering</td><td>Controleer relevante keurmerken en certificaten per aanbieder</td></tr>",
    ],
    [/Inclusief gratis horraam/gi, "Vraag of een horraam is inbegrepen"],
    [/HR\+\+ glas standaard inbegrepen/gi, "controleer welk glastype standaard is inbegrepen"],
    [/HR\+\+ glas standaard/gi, "HR++ glas: controleer wat is inbegrepen"],
    [/20 jaar garantie/gi, "garantie volgens de voorwaarden van de aanbieder"],
    [/KOMO-gecertificeerd/gi, "controleer relevante keurmerken per aanbieder"],
    [/Gratis horren/gi, "Horren als optie"],
    [/gratis horraam inbegrepen/gi, "vraag of een horraam is inbegrepen"],
    [/Populairste keuze/gi, "Veelgekozen optie"],
    [/De meest gekozen variant/gi, "Een veelgekozen variant"],
    [/onze kunststof kozijnen/gi, "kunststof kozijnen"],
    [/onze kozijnen/gi, "kunststof kozijnen"],
    [/onze kunststof deuren/gi, "kunststof deuren"],
    [/onze deuren/gi, "kunststof deuren"],
    [/onze kunststof schuifpuien/gi, "kunststof schuifpuien"],
    [/onze schuifpuien/gi, "kunststof schuifpuien"],
    [/onze producten/gi, "de mogelijkheden"],
    [/onze adviseurs/gi, "een adviseur van de gekozen aanbieder"],
    [/onze adviseur/gi, "een adviseur van de gekozen aanbieder"],
    [/onze monteurs/gi, "de monteurs van de gekozen aanbieder"],
    [/onze vakmensen/gi, "de vakmensen van de gekozen aanbieder"],
    [/onze installateurs/gi, "de installateurs die je vergelijkt"],
    [/wij leveren alles op maat/gi, "veel aanbieders leveren maatwerk"],
    [/wij leveren/gi, "aanbieders leveren"],
    [/wij plaatsen/gi, "installateurs plaatsen"],
    [/wij monteren/gi, "installateurs monteren"],
    [/wij komen/gi, "de gekozen aanbieder komt"],
    [/we komen/gi, "de gekozen aanbieder komt"],
    [/we meten op/gi, "de gekozen aanbieder meet op"],
    [/we geven advies/gi, "je bespreekt de mogelijkheden"],
    [/we sturen een offerte/gi, "je ontvangt een offerte"],
    [/neem contact met ons op/gi, "start een vrijblijvende vergelijking"],
    [/bel ons voor/gi, "vraag informatie aan over"],
    [/>Maak een afspraak</gi, ">Vergelijk offertes<"],
  ];

  return replacements.reduce((result, [pattern, replacement]) => result.replace(pattern, replacement), value);
}

function getMeta(html: string, name: string) {
  const first = new RegExp(`<meta[^>]+name=["']${name}["'][^>]+content=["']([^"']*)["'][^>]*>`, "i");
  const second = new RegExp(`<meta[^>]+content=["']([^"']*)["'][^>]+name=["']${name}["'][^>]*>`, "i");
  return html.match(first)?.[1] ?? html.match(second)?.[1] ?? "";
}

function getCanonical(html: string) {
  return html.match(/<link[^>]+rel=["']canonical["'][^>]+href=["']([^"']+)["'][^>]*>/i)?.[1];
}

function getTitle(html: string) {
  return textOnly(matchContent(html, /<title[^>]*>([\s\S]*?)<\/title>/i));
}

function getH1(html: string) {
  return textOnly(matchContent(html, /<h1[^>]*>([\s\S]*?)<\/h1>/i));
}

function rewriteLinks(fragment: string) {
  return fragment
    .replace(/href=["']index\.html#contact["']/gi, 'href="/offerte-aanvragen.html"')
    .replace(/href=["']index\.html#[^"']*["']/gi, 'href="/"')
    .replace(/href=["']index\.html["']/gi, 'href="/"')
    .replace(/href=["']([a-z0-9-]+\.html)(#[^"']*)?["']/gi, (_full, page, hash = "") => `href="/${page}${hash}"`);
}

function sanitize(fragment: string) {
  const cleaned = rewriteLinks(fragment)
    .replace(/<script\b[\s\S]*?<\/script>/gi, "")
    .replace(/<style\b[\s\S]*?<\/style>/gi, "")
    .replace(/<noscript\b[\s\S]*?<\/noscript>/gi, "")
    .replace(/<header\b[\s\S]*?<\/header>/gi, "")
    .replace(/<footer\b[\s\S]*?<\/footer>/gi, "")
    .replace(/<nav\b[\s\S]*?<\/nav>/gi, "")
    .replace(/<svg\b[\s\S]*?<\/svg>/gi, "")
    .replace(/<img\b[^>]*>/gi, "")
    .replace(/\sonclick=["'][^"']*["']/gi, "")
    .replace(/\sstyle=["'][^"']*["']/gi, "")
    .replace(/\sdata-netlify=["'][^"']*["']/gi, "")
    .replace(/<button([^>]*)>/gi, '<span class="legacyButton"$1>')
    .replace(/<\/button>/gi, "</span>");

  return neutralizeComparisonCopy(cleaned).trim();
}

function articleContent(html: string) {
  const startMarker = '<div class="blog-content">';
  const start = html.indexOf(startMarker);
  if (start >= 0) {
    const articleEnd = html.indexOf("</article>", start);
    const raw = html.slice(start + startMarker.length, articleEnd > start ? articleEnd : undefined);
    return sanitize(raw);
  }
  return standardContent(html);
}

function productContent(html: string) {
  const wrap = html.indexOf('<div class="product-content-wrap">');
  const mainStart = html.indexOf("<main", wrap >= 0 ? wrap : 0);
  const openEnd = html.indexOf(">", mainStart);
  const mainEnd = html.indexOf("</main>", openEnd);
  if (mainStart >= 0 && openEnd >= 0 && mainEnd > openEnd) {
    return sanitize(html.slice(openEnd + 1, mainEnd));
  }
  return standardContent(html);
}

function locationContent(html: string) {
  const heroStart = html.search(/<section[^>]+class=["'][^"']*\bhero\b[^"']*["']/i);
  if (heroStart >= 0) {
    const heroEnd = html.indexOf("</section>", heroStart);
    if (heroEnd > heroStart) {
      const footerStart = html.search(/<footer\b/i);
      return sanitize(html.slice(heroEnd + 10, footerStart > heroEnd ? footerStart : undefined));
    }
  }
  return standardContent(html);
}

function standardContent(html: string) {
  const body = matchContent(html, /<body[^>]*>([\s\S]*?)<\/body>/i) || html;
  let cleaned = sanitize(body);
  cleaned = cleaned.replace(/<h1[^>]*>[\s\S]*?<\/h1>/i, "");
  return cleaned;
}

export function pageTypeFor(slug: string, html: string): LegacyPageType {
  if (legalSlugs.has(slug)) return "legal";
  if (/^kozijnen-[a-z0-9-]+\.html$/i.test(slug) && !slug.includes("vervangen") && !slug.includes("isoleren") && !slug.includes("kopen") && !slug.includes("buiten-of-binnen") && !slug.includes("geintegreerde")) return "location";
  if (productSlugs.has(slug)) return "product";
  if (html.includes('class="blog-article"') || html.includes('class="blog-content"')) return "article";
  return "standard";
}

function labelFor(type: LegacyPageType, slug: string) {
  if (type === "location") return "Kozijnen in jouw regio";
  if (type === "article") return "Kennisbank";
  if (type === "product") return "Vergelijken & kiezen";
  if (type === "legal") return "123KozijnenVergelijker";
  if (slug === "over-ons.html") return "Over 123KozijnenVergelijker";
  return "Praktische informatie";
}

export function getLegacyPage(slug: string): LegacyPage | null {
  if (!legacyExists(slug) || reservedSlugs.has(slug)) return null;
  const html = readLegacyHtml(slug);
  const type = pageTypeFor(slug, html);
  const title = getTitle(html) || getH1(html) || slug.replace(/\.html$/, "").replace(/-/g, " ");
  const h1 = getH1(html) || title.split("|")[0].trim();
  const rawDescription = descriptionOverrides[slug] || getMeta(html, "description") || `Lees meer over ${h1.toLowerCase()} en vergelijk de mogelijkheden voor jouw woning.`;
  const description = neutralizeComparisonCopy(rawDescription);
  const content = type === "article" ? articleContent(html) : type === "location" ? locationContent(html) : type === "product" ? productContent(html) : standardContent(html);

  return {
    slug,
    title,
    description,
    canonical: getCanonical(html),
    h1,
    label: labelFor(type, slug),
    type,
    content,
  };
}
