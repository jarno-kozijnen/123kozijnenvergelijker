import type { Metadata } from "next";
import type { LegacyPage } from "./legacy-content";

export const SITE_URL = "https://www.123kozijnenvergelijker.nl";
export const SITE_NAME = "123KozijnenVergelijker";
export const SITE_ALTERNATE_NAME = "123 Kozijnen Vergelijker";

export type ArticleSeo = {
  titel: string;
  meta_desc: string;
  datum_iso: string;
  categorie: string;
};

const titleOverrides: Record<string, string> = {
  "kunststof-kozijnen.html": "Kunststof kozijnen vergelijken | Prijzen, glas & montage",
  "kunststof-deuren.html": "Kunststof deuren vergelijken | Prijzen & mogelijkheden",
  "kunststof-schuifpuien.html": "Kunststof schuifpui vergelijken | Prijzen & opties",
  "financiering.html": "Kunststof kozijnen financieren | Subsidie & mogelijkheden",
  "calculator.html": "Kosten kunststof kozijnen berekenen | Prijsindicatie",
  "offerte-vergelijken.html": "Kozijnenoffertes vergelijken | Prijs, kwaliteit & voorwaarden",
  "offerte-kunststof-kozijnen.html": "Offerte kunststof kozijnen | Vergelijk aanbieders",
  "over-ons.html": "Over 123KozijnenVergelijker | Zo werkt vergelijken",
  "privacyverklaring.html": "Privacyverklaring | 123KozijnenVergelijker",
  "algemene-voorwaarden.html": "Algemene voorwaarden | 123KozijnenVergelijker",
};

const descriptionOverrides: Record<string, string> = {
  "kunststof-kozijnen.html": "Vergelijk kunststof kozijnen op prijs, profiel, glas, montage en garantie. Lees de belangrijkste keuzes en vraag vrijblijvend offertes aan.",
  "kunststof-deuren.html": "Vergelijk kunststof deuren op uitvoering, isolatie, veiligheid, montage en totaalprijs. Bekijk de mogelijkheden en vraag vrijblijvend offertes aan.",
  "kunststof-schuifpuien.html": "Vergelijk kunststof schuifpuien op afmetingen, glas, profiel, montage en prijs. Lees waar je op let en vraag vrijblijvend offertes aan.",
  "financiering.html": "Lees welke mogelijkheden er zijn om kunststof kozijnen te financieren en waar je op let bij subsidie, lening, rente en voorwaarden.",
  "calculator.html": "Bereken een eerste prijsindicatie voor kunststof kozijnen en ontdek welke keuzes de totaalprijs beïnvloeden, van glas tot montage en afwerking.",
  "over-ons.html": "Lees hoe 123KozijnenVergelijker consumenten helpt om kunststof kozijnen, deuren en schuifpuien beter te vergelijken op prijs en voorwaarden.",
};

const noIndexSlugs = new Set(["bedankt.html", "lander.html", "lp-kozijnen.html", "blog-detail.html"]);

function stripBrand(title: string) {
  return title
    .replace(/\s*[|–-]\s*123\s*Kozijnen\s*Vergelijker(?:\.nl)?/gi, "")
    .replace(/\s*[|–-]\s*123KozijnenVergelijker(?:\.nl)?/gi, "")
    .trim();
}

export function cityFromSlug(slug: string) {
  if (!/^kozijnen-[a-z0-9-]+\.html$/i.test(slug)) return "";
  const raw = slug.replace(/^kozijnen-/, "").replace(/\.html$/, "");
  return raw
    .split("-")
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");
}

function titleFor(slug: string, page: LegacyPage, article?: ArticleSeo) {
  if (article) {
    const core = stripBrand(article.titel);
    return core.length > 58 ? core : `${core} | ${SITE_NAME}`;
  }
  const city = page.type === "location" ? cityFromSlug(slug) : "";
  if (city) return `Kunststof kozijnen ${city} | Prijzen & offertes vergelijken`;
  if (titleOverrides[slug]) return titleOverrides[slug];
  const core = stripBrand(page.title || page.h1);
  return core.length > 60 ? core : `${core} | ${SITE_NAME}`;
}

function descriptionFor(slug: string, page: LegacyPage, article?: ArticleSeo) {
  if (article?.meta_desc) return article.meta_desc;
  const city = page.type === "location" ? cityFromSlug(slug) : "";
  if (city) {
    return `Kunststof kozijnen in ${city}? Lees over prijzen, glas, montage en belangrijke aandachtspunten en vergelijk vrijblijvend offertes van passende aanbieders.`;
  }
  return descriptionOverrides[slug] || page.description;
}

export function metadataForLegacy(slug: string, page: LegacyPage, article?: ArticleSeo): Metadata {
  const title = titleFor(slug, page, article);
  const description = descriptionFor(slug, page, article);
  const canonical = page.canonical || `${SITE_URL}/${slug}`;
  const shouldIndex = !noIndexSlugs.has(slug);

  const metadata: Metadata = {
    title,
    description,
    alternates: { canonical },
    robots: shouldIndex
      ? { index: true, follow: true, googleBot: { index: true, follow: true, "max-image-preview": "large", "max-snippet": -1, "max-video-preview": -1 } }
      : { index: false, follow: false },
    openGraph: {
      type: article ? "article" : "website",
      locale: "nl_NL",
      siteName: SITE_NAME,
      url: canonical,
      title,
      description,
      images: [{ url: "/opengraph-image", width: 1200, height: 630, alt: `${SITE_NAME} – kunststof kozijnen vergelijken` }],
      ...(article ? { publishedTime: article.datum_iso } : {}),
    },
    twitter: {
      card: "summary_large_image",
      title,
      description,
      images: ["/twitter-image"],
    },
  };

  return metadata;
}

export function absoluteUrl(pathname: string) {
  if (/^https?:\/\//i.test(pathname)) return pathname;
  return `${SITE_URL}${pathname.startsWith("/") ? pathname : `/${pathname}`}`;
}
