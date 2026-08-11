import Link from "next/link";

export function InternalHeader() {
  return (
    <>
      <div className="internalUtility">
        <div className="internalShell internalUtilityInner">
          <span>Gratis en vrijblijvend vergelijken</span>
          <div><span>✓ Aanbieders uit jouw regio</span><span>✓ Eén aanvraag</span><span>✓ Zelf vergelijken</span></div>
        </div>
      </div>
      <header className="internalHeader">
        <div className="internalShell internalNav">
          <Link className="internalBrand" href="/" aria-label="123KozijnenVergelijker home">
            <span className="internalBrandMark">123</span>
            <span><strong>Kozijnen</strong><b>Vergelijker</b></span>
          </Link>
          <nav aria-label="Hoofdnavigatie">
            <Link href="/kunststof-kozijnen.html">Kozijnen</Link>
            <Link href="/kunststof-deuren.html">Deuren</Link>
            <Link href="/kunststof-schuifpuien.html">Schuifpuien</Link>
            <Link href="/financiering.html">Financiering</Link>
            <Link href="/blog.html">Kennisbank</Link>
          </nav>
          <Link className="internalNavCta" href="/offerte-aanvragen.html">Start vergelijking</Link>
        </div>
      </header>
    </>
  );
}

export function CompareAside({ compact = false }: { compact?: boolean }) {
  return (
    <aside className={compact ? "internalAside compactAside" : "internalAside"}>
      <span className="internalAsideLabel">Vrijblijvend vergelijken</span>
      <h3>Benieuwd wat jouw project kost?</h3>
      <p>Vergelijk prijs, materiaal, glas, montage en voorwaarden van passende opties.</p>
      <ul>
        <li><span>✓</span> Gratis aanvraag</li>
        <li><span>✓</span> Geen verplichting</li>
        <li><span>✓</span> Gericht op jouw project</li>
      </ul>
      <Link className="internalPrimaryButton" href="/offerte-aanvragen.html">Start gratis vergelijking <span>→</span></Link>
      <small>Je bepaalt altijd zelf of je met een aanbieder verder gaat.</small>
    </aside>
  );
}

export function InternalFooter() {
  return (
    <footer className="internalFooter">
      <div className="internalShell internalFooterGrid">
        <div className="internalFooterBrand">
          <Link className="internalBrand" href="/">
            <span className="internalBrandMark">123</span>
            <span><strong>Kozijnen</strong><b>Vergelijker</b></span>
          </Link>
          <p>Informatie en vergelijking voor kunststof kozijnen, deuren en schuifpuien.</p>
        </div>
        <div><strong>Vergelijken</strong><Link href="/kunststof-kozijnen.html">Kunststof kozijnen</Link><Link href="/kunststof-deuren.html">Kunststof deuren</Link><Link href="/kunststof-schuifpuien.html">Schuifpuien</Link><Link href="/offerte-aanvragen.html">Offertes vergelijken</Link></div>
        <div><strong>Kennis</strong><Link href="/blog.html">Kennisbank</Link><Link href="/financiering.html">Financiering</Link><Link href="/calculator.html">Kosten berekenen</Link><Link href="/projecten.html">Voorbeelden</Link></div>
        <div><strong>Over ons</strong><Link href="/over-ons.html">Over 123KozijnenVergelijker</Link><Link href="/privacyverklaring.html">Privacy</Link><Link href="/algemene-voorwaarden.html">Voorwaarden</Link></div>
      </div>
      <div className="internalShell internalFooterBottom"><span>© 2026 123KozijnenVergelijker.nl</span><span>Onafhankelijke informatie om beter te kunnen vergelijken.</span></div>
    </footer>
  );
}
