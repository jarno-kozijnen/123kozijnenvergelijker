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
  return rewriteLinks(fragment)
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
    .replace(/<\/button>/gi, "</span>")
    .trim();
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
  const description = getMeta(html, "description") || `Lees meer over ${h1.toLowerCase()} en vergelijk de mogelijkheden voor jouw woning.`;
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
