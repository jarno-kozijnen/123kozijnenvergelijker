# 123KozijnenVergelijker Next.js migration

Deze branch vervangt de bestaande content **niet**. De huidige statische HTML-bestanden blijven voorlopig onaangeroerd en vormen de bron voor de migratie.

## Uitgangspunten

- bestaande SEO-teksten behouden;
- bestaande slugs en zoekwoordkeuzes behouden tenzij er bewust een redirectplan wordt gemaakt;
- design loskoppelen van content;
- één vaste Next.js-componentenbibliotheek voor home, money pages, artikelen en locatiepagina's;
- redirects pas activeren nadat alle oude URL's in een URL-mapping staan;
- geen automatische herschrijving tijdens de technische migratie.

## Fasen

1. Nieuwe homepage en design system opzetten.
2. Alle bestaande HTML-content inventariseren.
3. Content per URL extraheren naar een gestructureerd formaat.
4. Eén vast ArticleTemplate maken en eerste 3 artikelen migreren voor controle.
5. Money pages en locatiepagina's een eigen template geven.
6. Interne links en canonicals controleren.
7. URL-mapping + 301 redirects maken waar nodig.
8. Vercel preview controleren voordat main of het domein wordt omgezet.

## Eerste designkeuze

De nieuwe voorkant is bewust rustiger dan de bestaande AI-achtige pagina's: veel witruimte, donkerblauw, één groen accent, weinig decoratieve effecten en vaste kaarten/CTA's. De vergelijkfunnel blijft een centraal conversie-element.
