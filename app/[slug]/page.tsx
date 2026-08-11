import type { Metadata } from "next";
import fs from "node:fs";
import path from "node:path";
import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import { CompareAside, InternalFooter, InternalHeader } from "../../components/InternalChrome";
import { getLegacyPage, legacyExists, listLegacyHtmlFiles, readLegacyHtml } from "../../lib/legacy-content";

type BlogItem = {
  slug: string;
  titel: string;
  categorie: string;
  datum_iso: string;
  datum_display: string;
  leestijd: number;
  samenvatting: string;
  meta_desc: string;
};

type ProjectItem = {
  titel: string;
  locatie: string;
  categorie: string;
  tags: string[];
  review: string;
  klant: string;
  sterren: string;
};

function readJson<T>(filename: string): T {
  return JSON.parse(fs.readFileSync(path.join(process.cwd(), filename), "utf8")) as T;
}

function blogs() {
  return readJson<BlogItem[]>("blogs_index.json");
}

function blogForSlug(slug: string) {
  return blogs().find((item) => `${item.slug}.html` === slug);
}

export function generateStaticParams() {
  return listLegacyHtmlFiles().map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  if (slug === "index.html") return { title: "123KozijnenVergelijker" };
  if (slug === "blog.html") {
    return {
      title: "Kennisbank kunststof kozijnen | 123KozijnenVergelijker",
      description: "Praktische informatie over kunststof kozijnen, prijzen, glas, montage, financiering en het vergelijken van offertes.",
      alternates: { canonical: "https://www.123kozijnenvergelijker.nl/blog.html" },
    };
  }
  if (slug === "projecten.html") {
    return {
      title: "Kozijnprojecten en voorbeelden | 123KozijnenVergelijker",
      description: "Bekijk voorbeelden van kozijn-, deur- en schuifpuiprojecten en ontdek welke keuzes bij verschillende woningen passen.",
    };
  }
  if (slug === "offerte-aanvragen.html") {
    return {
      title: "Kunststof kozijnen offertes vergelijken | Gratis aanvraag",
      description: "Start gratis en vrijblijvend je vergelijking voor kunststof kozijnen, deuren of een schuifpui.",
    };
  }
  const page = getLegacyPage(slug);
  if (!page) return {};
  return {
    title: page.title,
    description: page.description,
    alternates: page.canonical ? { canonical: page.canonical } : undefined,
  };
}

function Breadcrumbs({ current, parent }: { current: string; parent?: { label: string; href: string } }) {
  return (
    <nav className="internalBreadcrumb" aria-label="Broodkruimel">
      <Link href="/">Home</Link><span>›</span>
      {parent ? <><Link href={parent.href}>{parent.label}</Link><span>›</span></> : null}
      <span>{current}</span>
    </nav>
  );
}

function StandardHero({ label, title, description, location }: { label: string; title: string; description: string; location?: boolean }) {
  return (
    <section className={location ? "internalPageHero locationHero" : "internalPageHero"}>
      <div className="internalShell">
        <div className="internalHeroContent">
          <span className="internalEyebrow">{location ? "⌖ " : ""}{label}</span>
          <h1>{title}</h1>
          <p>{description}</p>
          <div className="internalHeroActions">
            <Link className="internalPrimaryButton" href="/offerte-aanvragen.html">Vergelijk offertes <span>→</span></Link>
            <Link className="internalSecondaryButton" href="/blog.html">Lees eerst de kennisbank</Link>
          </div>
          <div className="internalTrustLine"><span>✓ Gratis en vrijblijvend</span><span>✓ Vergelijk op inhoud en prijs</span><span>✓ Zelf beslissen</span></div>
        </div>
      </div>
    </section>
  );
}

function KnowledgeIndex() {
  const items = blogs().sort((a, b) => b.datum_iso.localeCompare(a.datum_iso));
  const categories = Array.from(new Set(items.map((item) => item.categorie)));
  return (
    <>
      <StandardHero label="Kennisbank" title="Alles wat je wilt weten vóór je kozijnen vergelijkt." description="Van prijzen en isolatiewaarden tot montage, onderhoud, subsidie en financiering. Gebruik de kennisbank om offertes inhoudelijk beter te beoordelen." />
      <section className="internalSection">
        <div className="internalShell">
          <div className="knowledgeToolbar"><div><strong>{items.length} artikelen</strong><span>Praktische uitleg zonder onnodig jargon</span></div><div className="categoryPills">{categories.map((category) => <span key={category}>{category}</span>)}</div></div>
          <div className="articleGrid">
            {items.map((item, index) => (
              <Link className={index === 0 ? "articleCard featuredArticleCard" : "articleCard"} href={`/${item.slug}.html`} key={item.slug}>
                <div className="articleCardTop"><span>{item.categorie}</span><small>{item.leestijd} min leestijd</small></div>
                <h2>{item.titel}</h2>
                <p>{item.samenvatting}</p>
                <div className="articleCardBottom"><span>{item.datum_display}</span><b>Lees artikel →</b></div>
              </Link>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}

function ProjectsIndex() {
  const data = readJson<{ projecten: ProjectItem[] }>("_data/projecten.json");
  return (
    <>
      <StandardHero label="Inspiratie & voorbeelden" title="Bekijk hoe verschillende kozijnprojecten kunnen worden aangepakt." description="Van een paar nieuwe kozijnen tot een complete gevel. Gebruik de voorbeelden om te bepalen wat je in offertes wilt laten opnemen." />
      <section className="internalSection">
        <div className="internalShell projectPageGrid">
          {data.projecten.map((project, index) => (
            <article className="projectExample" key={`${project.titel}-${index}`}>
              <div className="projectVisual"><span>0{index + 1}</span><b>{project.locatie}</b></div>
              <div className="projectBody"><span className="projectCategory">{project.categorie}</span><h2>{project.titel}</h2><div className="projectTags">{project.tags.map((tag) => <span key={tag}>{tag}</span>)}</div><blockquote>“{project.review}”</blockquote><small>{project.klant}</small></div>
            </article>
          ))}
        </div>
      </section>
    </>
  );
}

function QuotePage() {
  return (
    <section className="quotePage">
      <div className="internalShell quotePageGrid">
        <div className="quotePageCopy">
          <span className="internalEyebrow">Start je vergelijking</span>
          <h1>Vergelijk kunststof kozijnen op wat écht telt.</h1>
          <p>Geef aan wat je wilt laten vervangen. Zo krijg je een gerichtere vergelijking op totaalprijs, glas, profiel, montage, garantie en voorwaarden.</p>
          <div className="quoteSteps"><div><span>01</span><p><strong>Vertel wat je zoekt</strong><small>Kozijnen, deuren, schuifpui of een combinatie.</small></p></div><div><span>02</span><p><strong>Geef je situatie door</strong><small>Een paar basisgegevens over woning en regio.</small></p></div><div><span>03</span><p><strong>Vergelijk de opties</strong><small>Jij bepaalt zelf met wie je verder wilt.</small></p></div></div>
          <div className="quoteTrust"><span>✓ Gratis aanvraag</span><span>✓ Geen verplichting</span><span>✓ Zelf rustig vergelijken</span></div>
        </div>
        <div className="quoteFormCard">
          <div className="quoteFormHead"><span>Vergelijking aanvragen</span><b>± 2 minuten</b></div>
          <form action="/bedankt.html" method="get">
            <fieldset><legend>Wat wil je vergelijken?</legend><div className="quoteChoices"><label><input type="radio" name="project" value="kozijnen" defaultChecked /><span>Kunststof kozijnen</span></label><label><input type="radio" name="project" value="deuren" /><span>Kunststof deuren</span></label><label><input type="radio" name="project" value="schuifpui" /><span>Schuifpui</span></label><label><input type="radio" name="project" value="combinatie" /><span>Combinatie</span></label></div></fieldset>
            <div className="quoteFields"><label>Naam<input name="naam" placeholder="Voor- en achternaam" required /></label><label>Postcode<input name="postcode" placeholder="1234 AB" required /></label><label>E-mailadres<input type="email" name="email" placeholder="jouw@email.nl" required /></label><label>Telefoon<input type="tel" name="telefoon" placeholder="06 12 34 56 78" required /></label></div>
            <button type="submit" className="quoteSubmit">Start gratis vergelijking <span>→</span></button>
            <small>Door verder te gaan vraag je vrijblijvend een vergelijking aan. Je zit nergens aan vast.</small>
          </form>
        </div>
      </div>
    </section>
  );
}

function ThanksPage() {
  return (
    <section className="thanksPage"><div className="internalShell"><div className="thanksCard"><span>✓</span><h1>Bedankt voor je aanvraag.</h1><p>Je gegevens zijn ingevuld. Zodra de definitieve leadkoppeling is aangesloten, kan de aanvraag automatisch worden verwerkt.</p><div><Link className="internalPrimaryButton" href="/">Terug naar de homepage</Link><Link className="internalSecondaryButton" href="/blog.html">Bekijk de kennisbank</Link></div></div></div></section>
  );
}

export default async function LegacyRoute({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  if (slug === "index.html") redirect("/");
  if (slug === "blog.html") return <><InternalHeader /><KnowledgeIndex /><InternalFooter /></>;
  if (slug === "projecten.html") return <><InternalHeader /><ProjectsIndex /><InternalFooter /></>;
  if (slug === "offerte-aanvragen.html") return <><InternalHeader /><QuotePage /><InternalFooter /></>;
  if (slug === "bedankt.html") return <><InternalHeader /><ThanksPage /><InternalFooter /></>;
  if (!legacyExists(slug)) notFound();

  const page = getLegacyPage(slug);
  if (!page) {
    if (slug === "blog-detail.html") redirect("/blog.html");
    notFound();
  }
  const articleMeta = blogForSlug(slug);
  const parent = page.type === "article" ? { label: "Kennisbank", href: "/blog.html" } : page.type === "location" ? { label: "Kunststof kozijnen", href: "/kunststof-kozijnen.html" } : undefined;
  const noAside = page.type === "legal";

  return (
    <>
      <InternalHeader />
      <div className="internalShell"><Breadcrumbs current={page.h1} parent={parent} /></div>
      <StandardHero label={page.label} title={page.h1} description={page.description} location={page.type === "location"} />
      {articleMeta ? <div className="internalShell articleMetaBar"><span>{articleMeta.categorie}</span><span>{articleMeta.datum_display}</span><span>{articleMeta.leestijd} min leestijd</span></div> : null}
      <section className="internalSection contentSection">
        <div className={noAside ? "internalShell legalLayout" : "internalShell internalContentGrid"}>
          <article className="legacyContent" dangerouslySetInnerHTML={{ __html: page.content }} />
          {!noAside ? <CompareAside /> : null}
        </div>
      </section>
      {!noAside ? <section className="internalBottomCta"><div className="internalShell"><div><span>Vrijblijvend vergelijken</span><h2>Maak van je onderzoek een duidelijke vergelijking.</h2><p>Leg offertes naast elkaar op prijs, glas, profiel, montage, planning en garantie.</p></div><Link className="internalPrimaryButton lightButton" href="/offerte-aanvragen.html">Start gratis vergelijking →</Link></div></section> : null}
      <InternalFooter />
    </>
  );
}
