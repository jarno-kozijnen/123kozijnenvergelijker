import { SITE_ALTERNATE_NAME, SITE_NAME, SITE_URL, absoluteUrl } from "./seo";

const organizationId = `${SITE_URL}/#organization`;
const websiteId = `${SITE_URL}/#website`;

export function globalSchema() {
  return {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Organization",
        "@id": organizationId,
        name: SITE_NAME,
        alternateName: SITE_ALTERNATE_NAME,
        url: SITE_URL,
        logo: {
          "@type": "ImageObject",
          url: `${SITE_URL}/icon.svg`,
          width: 512,
          height: 512,
        },
      },
      {
        "@type": "WebSite",
        "@id": websiteId,
        url: SITE_URL,
        name: SITE_NAME,
        alternateName: SITE_ALTERNATE_NAME,
        inLanguage: "nl-NL",
        publisher: { "@id": organizationId },
      },
    ],
  };
}

type Breadcrumb = { name: string; url?: string };

type PageSchemaOptions = {
  url: string;
  name: string;
  description: string;
  breadcrumbs: Breadcrumb[];
  type?: "article" | "location" | "product" | "standard" | "legal";
  published?: string;
  category?: string;
  locationName?: string;
};

export function pageSchema(options: PageSchemaOptions) {
  const url = absoluteUrl(options.url);
  const breadcrumbId = `${url}#breadcrumb`;
  const pageId = `${url}#webpage`;

  const breadcrumb = {
    "@type": "BreadcrumbList",
    "@id": breadcrumbId,
    itemListElement: options.breadcrumbs.map((item, index) => ({
      "@type": "ListItem",
      position: index + 1,
      name: item.name,
      ...(item.url ? { item: absoluteUrl(item.url) } : {}),
    })),
  };

  const webpage = {
    "@type": "WebPage",
    "@id": pageId,
    url,
    name: options.name,
    description: options.description,
    inLanguage: "nl-NL",
    isPartOf: { "@id": websiteId },
    breadcrumb: { "@id": breadcrumbId },
    about: { "@id": organizationId },
  };

  const graph: Record<string, unknown>[] = [breadcrumb, webpage];

  if (options.type === "article" && options.published) {
    graph.push({
      "@type": "BlogPosting",
      "@id": `${url}#article`,
      headline: options.name,
      description: options.description,
      datePublished: options.published,
      dateModified: options.published,
      articleSection: options.category,
      inLanguage: "nl-NL",
      mainEntityOfPage: { "@id": pageId },
      author: { "@id": organizationId },
      publisher: { "@id": organizationId },
    });
  }

  if (options.type === "product" || options.type === "location") {
    graph.push({
      "@type": "Service",
      "@id": `${url}#service`,
      name: options.locationName ? `Kunststof kozijnen vergelijken in ${options.locationName}` : options.name,
      serviceType: "Vergelijken van offertes voor kunststof kozijnen",
      provider: { "@id": organizationId },
      areaServed: options.locationName
        ? { "@type": "City", name: options.locationName }
        : { "@type": "Country", name: "Nederland" },
      url,
      mainEntityOfPage: { "@id": pageId },
    });
  }

  return { "@context": "https://schema.org", "@graph": graph };
}

export function homePageSchema(faqs: string[][]) {
  const pageId = `${SITE_URL}/#webpage`;
  return {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebPage",
        "@id": pageId,
        url: SITE_URL,
        name: "Kunststof kozijnen vergelijken | 123KozijnenVergelijker",
        description: "Vergelijk kunststof kozijnen, deuren en schuifpuien op prijs, kwaliteit, montage, garantie en voorwaarden.",
        inLanguage: "nl-NL",
        isPartOf: { "@id": websiteId },
      },
      {
        "@type": "Service",
        "@id": `${SITE_URL}/#comparison-service`,
        name: "Kunststof kozijnen vergelijken",
        serviceType: "Vergelijken van offertes voor kunststof kozijnen, deuren en schuifpuien",
        provider: { "@id": organizationId },
        areaServed: { "@type": "Country", name: "Nederland" },
        url: SITE_URL,
        mainEntityOfPage: { "@id": pageId },
      },
      {
        "@type": "FAQPage",
        "@id": `${SITE_URL}/#faq`,
        mainEntity: faqs.map(([question, answer]) => ({
          "@type": "Question",
          name: question,
          acceptedAnswer: { "@type": "Answer", text: answer },
        })),
      },
    ],
  };
}
