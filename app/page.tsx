import Link from "next/link";
import { JsonLd } from "../components/JsonLd";
import { homePageSchema } from "../lib/schema";

const comparisonPoints = [
  ["Totaalprijs", "Vergelijk niet alleen de kozijnprijs, maar ook montage, afwerking en eventuele extra werkzaamheden."],
  ["Glas & isolatie", "Controleer welk type glas, profiel en isolatiewaarde daadwerkelijk in de offerte zijn opgenomen."],
  ["Garantie", "Bekijk waarop garantie geldt, hoe lang deze loopt en wie verantwoordelijk is voor service na plaatsing."],
  ["Planning & montage", "Vergelijk levertijd, montageduur, afvoer van oude kozijnen en de manier waarop de woning wordt opgeleverd."],
];

const knowledge = [
  ["Kunststof kozijnen", "Alles over profielen, glas, montage en levensduur.", "Lees over kozijnen", "/kunststof-kozijnen.html"],
  ["Kosten & prijzen", "Begrijp welke keuzes de totaalprijs van je project bepalen.", "Bekijk prijsinformatie", "/prijs-kunststof-kozijnen-berekend.html"],
  ["Deuren & schuifpuien", "Vergelijk mogelijkheden voor deuren en schuifpuien.", "Ontdek de mogelijkheden", "/kunststof-schuifpuien.html"],
];

const faqs = [
  ["Hoe werkt 123KozijnenVergelijker?", "Je geeft aan wat je wilt vervangen en waar je woont. Op basis daarvan kan je aanvraag worden gekoppeld aan passende aanbieders. Je vergelijkt vervolgens zelf prijs, uitvoering en voorwaarden."],
  ["Is vergelijken gratis?", "Ja. Het aanvragen en vergelijken is gratis en vrijblijvend. Je bepaalt zelf of je met een aanbieder verder wilt."],
  ["Waar moet ik offertes op vergelijken?", "Kijk naast de totaalprijs naar het type profiel, glas, montage, afwerking, planning, garantie en eventuele uitsluitingen in de offerte."],
  ["Kan ik ook deuren of een schuifpui meenemen?", "Ja. Je kunt kunststof kozijnen, deuren, een schuifpui of meerdere onderdelen binnen één aanvraag meenemen."],
];

const topicLinks = [
  ["Prijzen", "Hoe wordt de prijs van kunststof kozijnen berekend?", "Bekijk prijsfactoren, glas en montage.", "/prijs-kunststof-kozijnen-berekend.html"],
  ["Merken", "Welke kozijnenmerken kom je in Nederland tegen?", "Vergelijk profielmerken en kijk verder dan alleen het logo.", "/beste-kozijnenmerken-nederland.html"],
  ["Financiering", "Welke financieringsmogelijkheden zijn er?", "Lees over betalen, lening en subsidievoorwaarden.", "/financiering.html"],
  ["Kennisbank", "Alle artikelen over kozijnen op één plek", "Verdiep je in isolatie, onderhoud, montage en keuzes.", "/blog.html"],
];

export default function Home() {
  return (
    <main>
      <JsonLd data={homePageSchema(faqs)} />

      <div className="utilityBar">
        <div className="shell utilityInner">
          <span>Gratis en vrijblijvend vergelijken</span>
          <div className="utilityBenefits">
            <span>✓ Aanbieders uit jouw regio</span>
            <span>✓ Eén aanvraag</span>
            <span>✓ Zelf rustig vergelijken</span>
          </div>
        </div>
      </div>

      <header className="siteHeader">
        <div className="shell navWrap">
          <Link className="brand" href="/" aria-label="123KozijnenVergelijker home">
            <span className="brandMark">123</span>
            <span className="brandWords"><strong>Kozijnen</strong><b>Vergelijker</b></span>
          </Link>
          <nav className="navLinks" aria-label="Hoofdnavigatie">
            <Link href="/kunststof-kozijnen.html">Kozijnen</Link>
            <Link href="/kunststof-deuren.html">Deuren</Link>
            <Link href="/kunststof-schuifpuien.html">Schuifpuien</Link>
            <Link href="/financiering.html">Financiering</Link>
            <Link href="/blog.html">Kennisbank</Link>
          </nav>
          <Link className="button buttonSmall" href="/offerte-aanvragen.html">Start vergelijking</Link>
        </div>
      </header>

      <section className="hero" id="vergelijken">
        <div className="heroGlow heroGlowOne" />
        <div className="heroGlow heroGlowTwo" />
        <div className="shell heroGrid">
          <div className="heroCopy">
            <div className="eyebrow"><span /> Vergelijk op wat écht telt</div>
            <h1>Vergelijk kunststof kozijnen op prijs, kwaliteit en voorwaarden.</h1>
            <p className="heroLead">
              Ontvang opties van passende aanbieders en krijg grip op de keuzes die jouw project bepalen. Van glas en profielen tot montage, garantie en totaalprijs.
            </p>
            <div className="heroActions">
              <Link className="button buttonLarge" href="/offerte-aanvragen.html">Start gratis vergelijking <span>→</span></Link>
              <a className="quietLink" href="#hoe-werkt-het">Zo werkt het in 3 stappen</a>
            </div>
            <div className="heroTrust">
              <div><span className="trustIcon">✓</span><p><strong>Gratis aanvraag</strong><small>Geen kosten voor vergelijken</small></p></div>
              <div><span className="trustIcon">✓</span><p><strong>Geen verplichting</strong><small>Jij kiest of je verder gaat</small></p></div>
              <div><span className="trustIcon">✓</span><p><strong>Gericht vergelijken</strong><small>Op meer dan alleen prijs</small></p></div>
            </div>
          </div>

          <aside className="comparePanel" id="aanvraag">
            <div className="panelHeader">
              <div>
                <span className="panelKicker">Start je vergelijking</span>
                <h2>Wat wil je laten vervangen?</h2>
              </div>
              <span className="stepBadge">Stap 1 van 3</span>
            </div>
            <div className="progress"><span /></div>
            <p className="panelIntro">Kies wat het beste bij jouw project past.</p>
            <div className="projectOptions">
              <Link href="/offerte-aanvragen.html?project=kozijnen"><span className="optionIcon">▦</span><span><strong>Kunststof kozijnen</strong><small>Ramen en vaste kozijnen</small></span><b>→</b></Link>
              <Link href="/offerte-aanvragen.html?project=deuren"><span className="optionIcon">▯</span><span><strong>Kunststof deuren</strong><small>Voor- en achterdeuren</small></span><b>→</b></Link>
              <Link href="/offerte-aanvragen.html?project=schuifpui"><span className="optionIcon">▥</span><span><strong>Schuifpui</strong><small>Meer licht en doorgang</small></span><b>→</b></Link>
              <Link href="/offerte-aanvragen.html?project=combinatie"><span className="optionIcon">＋</span><span><strong>Combinatie</strong><small>Meerdere onderdelen</small></span><b>→</b></Link>
            </div>
            <div className="panelFoot">
              <span className="lockIcon">◇</span>
              <p><strong>Vrijblijvend aanvragen</strong><small>Je gegevens worden alleen gebruikt voor je aanvraag.</small></p>
            </div>
          </aside>
        </div>
      </section>

      <section className="confidenceBar">
        <div className="shell confidenceInner">
          <p>Een goede vergelijking kijkt verder dan de laagste prijs.</p>
          <div className="confidenceItems">
            <span>Profiel & materiaal</span><i />
            <span>Glas & isolatie</span><i />
            <span>Montage & afwerking</span><i />
            <span>Garantie & service</span>
          </div>
        </div>
      </section>

      <section className="section howSection" id="hoe-werkt-het">
        <div className="shell">
          <div className="sectionIntro centered">
            <span className="sectionLabel">Zo werkt het</span>
            <h2>In drie stappen van vraag naar een duidelijke vergelijking.</h2>
            <p>We houden de aanvraag kort. Daarna heb jij de informatie om offertes inhoudelijk naast elkaar te leggen.</p>
          </div>
          <div className="processRail">
            <div className="processLine" />
            <article><span className="processNumber">01</span><div className="processIcon">⌂</div><h3>Vertel wat je wilt vervangen</h3><p>Kies het type project en geef de belangrijkste kenmerken van je woning door.</p></article>
            <article><span className="processNumber">02</span><div className="processIcon">◎</div><h3>Ontvang passende opties</h3><p>Je aanvraag kan worden gekoppeld aan aanbieders die passen bij jouw regio en project.</p></article>
            <article><span className="processNumber">03</span><div className="processIcon">≡</div><h3>Vergelijk de offertes</h3><p>Bekijk totaalprijs, materiaal, glas, montage, garantie en voorwaarden voordat je kiest.</p></article>
          </div>
        </div>
      </section>

      <section className="section compareSection" id="waarom">
        <div className="shell compareLayout">
          <div className="compareCopy">
            <span className="sectionLabel lightLabel">Slim vergelijken</span>
            <h2>Voorkom dat je appels met peren vergelijkt.</h2>
            <p>Een offerte kan goedkoper lijken terwijl glas, afwerking of werkzaamheden anders zijn opgenomen. Daarom draait een goede vergelijking om de volledige aanbieding.</p>
            <Link className="button buttonWhite" href="/offerte-aanvragen.html">Vergelijk jouw project <span>→</span></Link>
          </div>
          <div className="comparisonTable">
            <div className="tableHead"><span>Waar let je op?</span><b>Waarom het telt</b></div>
            {comparisonPoints.map(([title, text]) => (
              <div className="comparisonRow" key={title}><div><span className="rowCheck">✓</span><strong>{title}</strong></div><p>{text}</p></div>
            ))}
          </div>
        </div>
      </section>

      <section className="section knowledgeSection" id="kennisbank">
        <div className="shell">
          <div className="sectionIntro knowledgeHead">
            <div><span className="sectionLabel">Kennisbank</span><h2>Lees je eerst in. Vergelijk daarna met meer zekerheid.</h2></div>
            <p>Van kosten en isolatie tot montage en garantie. De kennisbank helpt je begrijpen welke keuzes in een offerte daadwerkelijk verschil maken.</p>
          </div>
          <div className="knowledgeLayout">
            <Link className="featuredKnowledge" href="/kunststof-kozijnen.html">
              <span className="featuredLabel">Startpunt</span>
              <div className="windowVisual" aria-hidden="true"><div className="windowFrame"><span /><span /></div><div className="windowLight" /></div>
              <div className="featuredContent"><span>Kunststof kozijnen</span><h3>Waar moet je op letten bij het vergelijken van kunststof kozijnen?</h3><p>Een praktisch startpunt voor profielen, glas, montage, keurmerken en garantie.</p><b>Lees de complete uitleg →</b></div>
            </Link>
            <div className="knowledgeList">
              {knowledge.map(([title, body, label, href], index) => (
                <Link href={href} key={title}><span className="knowledgeIndex">0{index + 1}</span><div><h3>{title}</h3><p>{body}</p><b>{label} →</b></div></Link>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="homepageTopicLinks">
        <div className="shell clusterLinksInner">
          <div className="clusterLinksHead">
            <div><span>Verder lezen</span><h2>Belangrijke onderwerpen binnen het kozijnencluster.</h2></div>
            <p>Deze pagina’s vormen de belangrijkste route van oriënteren naar prijzen begrijpen en uiteindelijk offertes vergelijken.</p>
          </div>
          <div className="clusterLinksGrid">
            {topicLinks.map(([label, title, text, href]) => <Link className="clusterLink" href={href} key={href}><span>{label}</span><strong>{title}</strong><small>{text}</small></Link>)}
          </div>
        </div>
      </section>

      <section className="section decisionSection">
        <div className="shell decisionGrid">
          <div className="decisionCopy"><span className="sectionLabel">Meer grip op je keuze</span><h2>Niet de meeste informatie. Wel de informatie die je nodig hebt.</h2><p>123KozijnenVergelijker brengt de belangrijkste keuzes samen op één plek. Zo kun je gerichter vragen stellen en offertes beter beoordelen.</p></div>
          <div className="decisionStats"><div><strong>01</strong><span>Project bepalen</span><p>Kozijnen, deuren, schuifpui of een combinatie.</p></div><div><strong>02</strong><span>Specificaties begrijpen</span><p>Materiaal, glas, montage en afwerking.</p></div><div><strong>03</strong><span>Voorwaarden vergelijken</span><p>Prijs, planning, garantie en service.</p></div><div><strong>04</strong><span>Zelf beslissen</span><p>Jij bepaalt met welke partij je verder gaat.</p></div></div>
        </div>
      </section>

      <section className="section faqSection">
        <div className="shell faqGrid">
          <div className="faqIntro"><span className="sectionLabel">Veelgestelde vragen</span><h2>Nog iets onduidelijk?</h2><p>De belangrijkste vragen over vergelijken, aanvragen en het beoordelen van offertes.</p></div>
          <div className="faqList">{faqs.map(([question, answer]) => <details key={question}><summary>{question}<span>+</span></summary><p>{answer}</p></details>)}</div>
        </div>
      </section>

      <section className="finalCta">
        <div className="shell finalCtaBox">
          <div className="finalCtaCopy"><span className="sectionLabel lightLabel">Klaar om te vergelijken?</span><h2>Ontdek welke opties passen bij jouw woning en project.</h2><p>Start vrijblijvend en vergelijk daarna zelf de offertes en voorwaarden.</p></div>
          <Link className="button buttonWhite buttonCta" href="/offerte-aanvragen.html">Start gratis vergelijking <span>→</span></Link>
        </div>
      </section>

      <footer className="footer">
        <div className="shell footerTop">
          <div className="footerBrandBlock"><Link className="brand footerBrand" href="/"><span className="brandMark">123</span><span className="brandWords"><strong>Kozijnen</strong><b>Vergelijker</b></span></Link><p>Informatie en vergelijking voor kunststof kozijnen, deuren en schuifpuien.</p></div>
          <div className="footerCol"><strong>Vergelijken</strong><Link href="/kunststof-kozijnen.html">Kunststof kozijnen</Link><Link href="/kunststof-deuren.html">Kunststof deuren</Link><Link href="/kunststof-schuifpuien.html">Schuifpuien</Link><Link href="/offerte-aanvragen.html">Offertes vergelijken</Link></div>
          <div className="footerCol"><strong>Kennis</strong><Link href="/blog.html">Kennisbank</Link><Link href="/prijs-kunststof-kozijnen-berekend.html">Kosten & prijzen</Link><Link href="/financiering.html">Financiering</Link><Link href="/calculator.html">Kosten berekenen</Link></div>
          <div className="footerCol"><strong>123KozijnenVergelijker</strong><Link href="/over-ons.html">Over ons</Link><Link href="/projecten.html">Voorbeelden</Link><Link href="/privacyverklaring.html">Privacy</Link><Link href="/algemene-voorwaarden.html">Voorwaarden</Link></div>
        </div>
        <div className="shell footerBottom"><span>© 2026 123KozijnenVergelijker.nl</span><div><Link href="/privacyverklaring.html">Privacy</Link><Link href="/algemene-voorwaarden.html">Voorwaarden</Link></div></div>
      </footer>
    </main>
  );
}
