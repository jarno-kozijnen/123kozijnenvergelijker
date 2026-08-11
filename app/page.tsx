const steps = [
  ["01", "Vertel wat je zoekt", "Geef aan welke kozijnen je wilt vervangen en in welke regio je woont."],
  ["02", "Ontvang passende offertes", "We koppelen je aanvraag aan aanbieders die passen bij jouw project."],
  ["03", "Vergelijk rustig", "Bekijk prijs, garantie, planning en voorwaarden voordat je kiest."],
];

const topics = [
  ["Kunststof kozijnen", "Kosten, profielen, glaskeuze en waar je op let bij een offerte."],
  ["Kunststof deuren", "Voordeuren, achterdeuren, veiligheid, isolatie en prijsverschillen."],
  ["Schuifpuien", "Meer licht en ruimte, inclusief uitleg over afmetingen en montage."],
  ["Kosten & besparen", "Heldere prijsinformatie, subsidie, financiering en terugverdientijd."],
];

export default function Home() {
  return (
    <main>
      <header className="siteHeader">
        <div className="shell navWrap">
          <a className="brand" href="#" aria-label="123KozijnenVergelijker home">
            <span className="brand123">123</span><span>Kozijnen</span><strong>Vergelijker</strong>
          </a>
          <nav className="navLinks" aria-label="Hoofdnavigatie">
            <a href="#hoe-werkt-het">Hoe werkt het?</a>
            <a href="#kennisbank">Kennisbank</a>
            <a href="#over">Over ons</a>
          </nav>
          <a className="button buttonSmall" href="#offerte">Vergelijk offertes</a>
        </div>
      </header>

      <section className="hero">
        <div className="shell heroGrid">
          <div className="heroCopy">
            <div className="eyebrow">Onafhankelijk vergelijken voor jouw woning</div>
            <h1>Vergelijk kunststof kozijnen zonder verkooppraat.</h1>
            <p className="heroLead">
              Krijg inzicht in prijzen, mogelijkheden en aanbieders. Eén aanvraag, meerdere opties en jij bepaalt zelf wat bij je woning past.
            </p>
            <div className="heroActions">
              <a className="button" href="#offerte">Start gratis vergelijking</a>
              <a className="textLink" href="#hoe-werkt-het">Bekijk hoe het werkt <span>→</span></a>
            </div>
            <div className="trustRow">
              <span>✓ Gratis en vrijblijvend</span>
              <span>✓ Geen aanbetaling via ons</span>
              <span>✓ Vergelijk op jouw tempo</span>
            </div>
          </div>

          <aside className="quoteCard" id="offerte">
            <div className="quoteTop">
              <span className="pill">Gratis vergelijking</span>
              <span className="time">± 2 minuten</span>
            </div>
            <h2>Wat wil je vergelijken?</h2>
            <p>Kies je project. In de volgende stap verfijnen we je aanvraag.</p>
            <div className="choiceList">
              <button>Kunststof kozijnen <span>→</span></button>
              <button>Kunststof deuren <span>→</span></button>
              <button>Schuifpui <span>→</span></button>
              <button>Meerdere onderdelen <span>→</span></button>
            </div>
            <small>Je zit nergens aan vast. We delen je aanvraag alleen met passende aanbieders.</small>
          </aside>
        </div>
      </section>

      <section className="proofStrip">
        <div className="shell proofGrid">
          <div><strong>100%</strong><span>vrijblijvend vergelijken</span></div>
          <div><strong>1 aanvraag</strong><span>voor meerdere opties</span></div>
          <div><strong>Landelijk</strong><span>aanbieders per regio</span></div>
          <div><strong>Duidelijk</strong><span>prijs, garantie en planning</span></div>
        </div>
      </section>

      <section className="section" id="hoe-werkt-het">
        <div className="shell">
          <div className="sectionHead">
            <div>
              <span className="sectionLabel">Zo werkt vergelijken</span>
              <h2>Van aanvraag naar een keuze die klopt.</h2>
            </div>
            <p>Geen onnodig ingewikkelde funnel. Eerst de juiste informatie verzamelen, daarna pas vergelijken.</p>
          </div>
          <div className="stepsGrid">
            {steps.map(([nr, title, body]) => (
              <article className="stepCard" key={nr}>
                <span className="stepNr">{nr}</span>
                <h3>{title}</h3>
                <p>{body}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="section soft" id="kennisbank">
        <div className="shell">
          <div className="sectionHead">
            <div>
              <span className="sectionLabel">Kennisbank</span>
              <h2>Eerst begrijpen. Dan vergelijken.</h2>
            </div>
            <p>De bestaande SEO-content blijft behouden en krijgt straks één rustige, vaste artikelopmaak.</p>
          </div>
          <div className="topicGrid">
            {topics.map(([title, body]) => (
              <a className="topicCard" href="#" key={title}>
                <div className="topicIcon">↗</div>
                <h3>{title}</h3>
                <p>{body}</p>
                <span>Bekijk onderwerp →</span>
              </a>
            ))}
          </div>
        </div>
      </section>

      <section className="section" id="over">
        <div className="shell splitBlock">
          <div>
            <span className="sectionLabel">Waarom 123KozijnenVergelijker</span>
            <h2>Een vergelijker moet je helpen kiezen, niet harder laten twijfelen.</h2>
          </div>
          <div className="checkList">
            <p><b>Heldere uitleg.</b> Geen pagina’s vol loze superlatieven, maar concrete informatie over prijs, materiaal, glas en montage.</p>
            <p><b>Vaste structuur.</b> Elk onderwerp krijgt een eigen plek zodat je snel van vraag naar antwoord en offerte kunt gaan.</p>
            <p><b>Gericht vergelijken.</b> De offertefunnel wordt straks gekoppeld aan het type project en de regio van de bezoeker.</p>
          </div>
        </div>
      </section>

      <section className="ctaSection">
        <div className="shell ctaBox">
          <div>
            <span>Start met vergelijken</span>
            <h2>Benieuwd wat kunststof kozijnen voor jouw woning kosten?</h2>
          </div>
          <a className="button buttonLight" href="#offerte">Vergelijk offertes</a>
        </div>
      </section>

      <footer className="footer">
        <div className="shell footerInner">
          <div className="brand footerBrand"><span className="brand123">123</span><span>Kozijnen</span><strong>Vergelijker</strong></div>
          <p>Onafhankelijke informatie en vergelijking voor kunststof kozijnen, deuren en schuifpuien.</p>
          <span>© 2026 123KozijnenVergelijker.nl</span>
        </div>
      </footer>
    </main>
  );
}
