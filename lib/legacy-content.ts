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
      /Plan een vrijblijvend adviesgesprek aan huis\. We meten op, geven advies en sturen een offerte binnen 24 uur\./gi,
      "Vraag vrijblijvend offertes aan en vergelijk prijs, materiaal, glas, montage, planning en voorwaarden.",
    ],
    [
      /Onze monteurs werken schoon en zorgen dat je woning aan het eind van de dag wind- en waterdicht is\./gi,
      "Bespreek met de gekozen aanbieder hoe de montage wordt uitgevoerd en hoe de woning wordt opgeleverd.",
    ],
    [
      /Bij ieder kozijn ontvang je gratis horren in dezelfde kleur\./gi,
      "Vraag per offerte of horren zijn inbegrepen of als optie worden aangeboden.",
    ],
    [
      /RC2 inbraakwerende beslag standaard\. RC3 als optie\./gi,
      "Vergelijk welk veiligheidsbeslag standaard is inbegrepen en welke upgrades mogelijk zijn.",
    ],
    [
      /<tr><td>Profielmateriaal<\/td><td>VEKA PVC \(6-kamer profiel\)<\/td><\/tr>/gi,
      "<tr><td>Profielmateriaal</td><td>Vergelijk merk, materiaal en profielopbouw per offerte</td></tr>",
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
    [/HR\+\+ glas standaard inbegrepen/gi, "controleer welk glastype standaard is inbegrepen"],
    [/HR\+\+ glas standaard/gi, "HR++ glas: controleer wat is inbegrepen"],
    [/20 jaar garantie/gi, "garantie volgens de voorwaarden van de aanbieder"],
    [/KOMO-gecertificeerd/gi, "controleer relevante keurmerken per aanbieder"],
    [/Gratis horren/gi, "Horren als optie"],
    [/gratis horraam inbegrepen/gi, "vraag of een horraam is inbegrepen"],
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
  const rawDescription = getMeta(html, "description") || `Lees meer over ${h1.toLowerCase()} en vergelijk de mogelijkheden voor jouw woning.`;
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
