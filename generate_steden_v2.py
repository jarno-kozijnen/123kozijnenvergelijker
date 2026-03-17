import os

# Unieke stadsdata per stad: (slug, stad, provincie, wijken, woningtype, bouwjaar_context, lokale_context, klimaat_context)
steden = [
    {
        "slug": "amsterdam",
        "stad": "Amsterdam",
        "provincie": "Noord-Holland",
        "wijken": "De Pijp, Oud-West, Jordaan, Noord en Nieuw-West",
        "woningtype": "rijtjeswoningen, grachtenpanden en naoorlogse portiekflats",
        "bouwjaar": "grotendeels gebouwd tussen 1890 en 1970",
        "lokaal": "Amsterdam telt meer dan 800.000 woningen waarvan een groot deel single-glas of oud dubbel glas heeft. In wijken als Nieuw-West en Noord staan tienduizenden woningen uit de wederopbouwperiode die energetisch sterk verouderd zijn.",
        "klimaat": "Door de stedelijke warmte-eilandwerking en het vochtige Hollandse klimaat zijn goed isolerende kozijnen in Amsterdam extra waardevol, ze houden de warmte binnen in de winter en koelen de woning in de zomer.",
        "label": "Veel Amsterdamse woningen hebben energielabel D, E of lager.",
        "markt": "De Amsterdamse woningmarkt is competitief. Woningen met energielabel A of B worden aantoonbaar sneller verkocht en brengen gemiddeld 5 tot 8% meer op.",
        "subsidie_lokaal": "De gemeente Amsterdam stimuleert verduurzaming via eigen subsidieregelingen naast de landelijke ISDE en het Nationaal Warmtefonds.",
    },
    {
        "slug": "rotterdam",
        "stad": "Rotterdam",
        "provincie": "Zuid-Holland",
        "wijken": "Kralingen, Hillegersberg, Overschie, IJsselmonde en Delfshaven",
        "woningtype": "naoorlogse rijtjeswoningen, portiekflats en vrijstaande woningen",
        "bouwjaar": "voor een groot deel gebouwd na de Tweede Wereldoorlog (1945-1975)",
        "lokaal": "Rotterdam werd na de bombardementen van 1940 grotendeels herbouwd. Dit betekent dat veel woningen in Rotterdam dateren uit de wederopbouwperiode en dringend toe zijn aan verduurzaming van de schil, inclusief kozijnen.",
        "klimaat": "Als havenstad heeft Rotterdam te maken met windbelasting en vochtige zeelucht. Goed afgedichte kunststof kozijnen met HR++ glas bieden aanzienlijk betere weer- en geluidsbestendigheid dan verouderd hout of staal.",
        "label": "Een groot deel van de Rotterdamse woningvoorraad heeft energielabel C, D of slechter.",
        "markt": "Rotterdam investeert fors in de transitie naar aardgasvrije wijken. Nieuwe kozijnen zijn een logische eerste stap richting een beter energielabel en lagere stookkosten.",
        "subsidie_lokaal": "Via het Warmtefonds en ISDE kun je als Rotterdamse woningeigenaar de investering grotendeels financieren en subsidiëren.",
    },
    {
        "slug": "den-haag",
        "stad": "Den Haag",
        "provincie": "Zuid-Holland",
        "wijken": "Statenkwartier, Benoordenhout, Escamp, Laak en Segbroek",
        "woningtype": "ruime herenhuizen, interbellumswoningen en naoorlogse rijtjeswoningen",
        "bouwjaar": "met veel bebouwing uit de periode 1900-1960",
        "lokaal": "Den Haag heeft een gevarieerde woningvoorraad met veel statige herenhuizen in het Statenkwartier en Benoordenhout naast compactere naoorlogse wijken zoals Escamp en Laak. Juist in de oudere bebouwing zijn de energieprestaties van kozijnen een knelpunt.",
        "klimaat": "Nabij de Noordzee heeft Den Haag te maken met zoute zeelucht en flinke winddruk. Kunststof kozijnen zijn roestvrij, onderhoudsvrij en bestand tegen deze kustomstandigheden, in tegenstelling tot stalen of houten kozijnen.",
        "label": "Veel Haagse particuliere woningen hebben nog energielabel D of E, zeker in de vooroorlogse wijken.",
        "markt": "De gemeente Den Haag heeft ambitieuze klimaatdoelen. Verduurzaming van de woningschil, inclusief kozijnen, is een prioriteit in het gemeentelijk duurzaamheidsbeleid.",
        "subsidie_lokaal": "Haagse woningeigenaren kunnen voor kozijnen een beroep doen op ISDE-subsidie (tot €111/m² triple glas) én de renteloze Energiebespaarlening van het Nationaal Warmtefonds.",
    },
    {
        "slug": "utrecht",
        "stad": "Utrecht",
        "provincie": "Utrecht",
        "wijken": "Wittevrouwen, Lombok, Overvecht, Leidsche Rijn en Zuilen",
        "woningtype": "grachtenpanden, jaren-30 woningen en naoorlogse woningbouw",
        "bouwjaar": "met een mix van historische bebouwing en naoorlogse uitbreiding",
        "lokaal": "Utrecht heeft een historisch stadscentrum met grachtenpanden naast grote naoorlogse wijken als Overvecht en nieuwbouwwijk Leidsche Rijn. De verouderde vooroorlogse woningen in Wittevrouwen en Lombok zijn energetisch het meest te winnen.",
        "klimaat": "Centraal gelegen heeft Utrecht een continentaler klimaat dan de kustprovincies, met koudere winters en warmere zomers. Goede isolatie via HR++ kozijnen is het hele jaar door voelbaar.",
        "label": "Utrechtse woningen in vooroorlogse wijken hebben gemiddeld energielabel D of lager.",
        "markt": "Utrecht groeit snel en verduurzaming van de woningvoorraad staat hoog op de gemeentelijke agenda. Een beter energielabel verhoogt de woningwaarde in deze gespannen markt direct.",
        "subsidie_lokaal": "Via de ISDE-regeling en het Nationaal Warmtefonds is de investering in nieuwe kozijnen in Utrecht goed te financieren, ook zonder eigen vermogen.",
    },
    {
        "slug": "eindhoven",
        "stad": "Eindhoven",
        "provincie": "Noord-Brabant",
        "wijken": "Woensel, Stratum, Strijp, Gestel en Tongelre",
        "woningtype": "naoorlogse rijtjeswoningen, jaren-50 arbeiderswoningen en vrijstaande woningen",
        "bouwjaar": "grotendeels gebouwd in de periode 1945-1980 tijdens de industriële groei",
        "lokaal": "Eindhoven groeide explosief door de industrie (Philips, DAF) en kent veel naoorlogse woningbouw. Wijken als Woensel-Noord en Strijp-S hebben grote aantallen arbeiderswoningen uit de jaren 50 en 60 die energetisch sterk verouderd zijn.",
        "klimaat": "Noord-Brabant heeft relatief milde winters maar ook warme zomers. Goede isolatie via kunststof kozijnen met HR++ glas zorgt het hele jaar voor comfort, koeler in de zomer, warmer in de winter.",
        "label": "Veel Eindhovense naoorlogse woningen hebben energielabel D, E of F.",
        "markt": "Als innovatiestad zet Eindhoven sterk in op duurzaamheid. Projecten in wijken als Woensel en Stratum stimuleren verduurzaming van particuliere woningen.",
        "subsidie_lokaal": "In Noord-Brabant zijn via ISDE en Warmtefonds dezelfde landelijke regelingen beschikbaar. Combineer ISDE-subsidie met de renteloze Energiebespaarlening voor maximaal voordeel.",
    },
    {
        "slug": "tilburg",
        "stad": "Tilburg",
        "provincie": "Noord-Brabant",
        "wijken": "Oud-Noord, Reeshof, Quirijnstok, Groenewoud en het Centrum",
        "woningtype": "textielarbeiders-rijtjeswoningen, jaren-70 woningbouw en vrijstaande woningen",
        "bouwjaar": "veel bebouwing uit de periode 1920-1975 door de textielnijverheid",
        "lokaal": "Tilburg groeide als textielstad en heeft een karakteristieke woningvoorraad van arbeiderswoningen en rijtjeshuizen uit de eerste helft van de 20e eeuw. Wijken als Oud-Noord en Groenewoud tellen veel woningen met verouderde stalen of houten kozijnen.",
        "klimaat": "In het midden van Noord-Brabant heeft Tilburg een typisch gematigd zeeklimaat. Kunststof kozijnen met HR++ glas verbeteren direct het binnenklimaat en reduceren de stookkosten.",
        "label": "Oudere Tilburgse woningen hebben doorgaans energielabel D of E.",
        "markt": "Tilburg heeft duurzaamheid hoog op de agenda en ondersteunt woningeigenaren bij verduurzaming. Een nieuw energielabel vergroot ook de verkoopbaarheid van je woning.",
        "subsidie_lokaal": "ISDE-subsidie en de Energiebespaarlening van het Nationaal Warmtefonds zijn volledig beschikbaar voor woningeigenaren in Tilburg.",
    },
    {
        "slug": "groningen",
        "stad": "Groningen",
        "provincie": "Groningen",
        "wijken": "Paddepoel, De Hoogte, Vinkhuizen, Helpman en Indische Buurt",
        "woningtype": "jaren-30 woningen, portieketagewoningen en naoorlogse rijtjeswoningen",
        "bouwjaar": "met veel bebouwing uit de wederopbouwperiode 1945-1975",
        "lokaal": "Groningen heeft een jonge inwonerspopulatie maar een oudere woningvoorraad. Wijken als Paddepoel en Vinkhuizen tellen veel naoorlogse woningen die energetisch verouderd zijn. Door de aardbevingsproblematiek zijn veel Groningers al bezig met woningverbetering.",
        "klimaat": "Het noorden van Nederland heeft de koudste winters van het land en is blootgesteld aan forse wind. Goede isolatie via kunststof kozijnen met HR++ glas is in Groningen extra waardevol voor de stookkosten.",
        "label": "Veel Groningse woningen in naoorlogse wijken hebben energielabel D, E of slechter.",
        "markt": "Door de aardbevingschade en versterkingsoperatie is verduurzaming in Groningen een urgent thema. Er zijn aanvullende regelingen beschikbaar voor versterking gecombineerd met verduurzaming.",
        "subsidie_lokaal": "Groningse woningeigenaren kunnen naast ISDE en Warmtefonds mogelijk ook aanspraak maken op versterkingsprogramma's gecombineerd met verduurzaming.",
    },
    {
        "slug": "almere",
        "stad": "Almere",
        "provincie": "Flevoland",
        "wijken": "Almere-Haven, Almere-Stad, Almere-Buiten, Almere-Poort en Almere-Hout",
        "woningtype": "vrijstaande woningen, twee-onder-een-kapwoningen en rijtjeswoningen",
        "bouwjaar": "grotendeels gebouwd na 1975, Almere is een van de jongste steden van Nederland",
        "lokaal": "Almere is planmatig aangelegd op ingepolderde grond en heeft een relatief jonge woningvoorraad. Toch zijn ook hier kozijnen uit de jaren 80 en 90 toe aan vervanging, zeker wanneer het oud dubbel glas of HR+ glas betreft dat niet meer voldoet aan de huidige isolatienormen.",
        "klimaat": "Flevoland is vlak en winderig. De winddruk op woningen is hoog, wat hoge eisen stelt aan de afdichting en kwaliteit van kozijnen. Kwalitatieve kunststof kozijnen met HR++ glas presteren hier aanzienlijk beter dan verouderd hout.",
        "label": "Almeerse woningen hebben gemiddeld een beter energielabel dan de landelijke voorraad, maar veel 80s en 90s kozijnen presteren onder de huidige normen.",
        "markt": "Almere groeit snel en de woningmarkt is actief. Een hoger energielabel maakt je woning aantrekkelijker en meer waard bij verkoop.",
        "subsidie_lokaal": "In Almere zijn alle landelijke regelingen beschikbaar: ISDE-subsidie voor HR++ en triple glas, en de Energiebespaarlening van het Nationaal Warmtefonds.",
    },
    {
        "slug": "breda",
        "stad": "Breda",
        "provincie": "Noord-Brabant",
        "wijken": "Tuinzigt, Heuvel, Bavel, Princenhage en Haagse Beemden",
        "woningtype": "naoorlogse rijtjeswoningen, jaren-60 portieketagewoningen en vrijstaande woningen",
        "bouwjaar": "met een mix van vooroorlogse en naoorlogse bebouwing",
        "lokaal": "Breda combineert een historisch centrum met uitgestrekte naoorlogse wijken als Haagse Beemden en Tuinzigt. In deze wijken staan duizenden woningen met verouderde kozijnen uit de periode 1960-1985 die toe zijn aan vervanging.",
        "klimaat": "West-Noord-Brabant heeft een mild zeeklimaat. HR++ kozijnen zorgen voor minder tocht, minder vocht en significant lagere stookkosten in de herfst en winter.",
        "label": "Veel Bredase woningen in naoorlogse wijken hebben energielabel C, D of slechter.",
        "markt": "Breda heeft een aantrekkelijke woningmarkt en investeert in duurzaamheid. Verduurzaming via kozijnen verhoogt de woningwaarde en verkoopbaarheid direct.",
        "subsidie_lokaal": "ISDE-subsidie en het Nationaal Warmtefonds zijn beschikbaar voor alle eigenaar-bewoners in Breda.",
    },
    {
        "slug": "nijmegen",
        "stad": "Nijmegen",
        "provincie": "Gelderland",
        "wijken": "Dukenburg, Lindenholt, Bottendaal, Altrade en het Centrum",
        "woningtype": "naoorlogse rijtjeswoningen, jaren-70 systeembouw en historische pandjes",
        "bouwjaar": "met een mix van historische bebouwing en grote naoorlogse uitbreidingswijken",
        "lokaal": "Nijmegen is de oudste stad van Nederland en heeft een gevarieerde woningvoorraad, van historische grachtenpandjes in het centrum tot grote naoorlogse wijken als Dukenburg en Lindenholt. Juist in de systeembouw van de jaren 70 zijn kozijnen energetisch een zwakke schakel.",
        "klimaat": "Het Gelderse klimaat kent relatief warme zomers en koude winters. Kunststof kozijnen met HR++ glas dempen de temperatuurwisselingen en verbeteren het binnenklimaat het hele jaar door.",
        "label": "Met name in de grote uitbreidingswijken uit de jaren 60-70 hebben Nijmeegse woningen een laag energielabel.",
        "markt": "Nijmegen is een jonge, groeiende universiteitsstad. Verduurzaming staat centraal in het gemeentelijk beleid en een hoger energielabel maakt je woning beter verkoopbaar.",
        "subsidie_lokaal": "Nijmeegse woningeigenaren kunnen ISDE-subsidie combineren met de Energiebespaarlening voor een kostenefficiënte renovatie.",
    },
    {
        "slug": "enschede",
        "stad": "Enschede",
        "provincie": "Overijssel",
        "wijken": "Pathmos, Deppenbroek, Velve-Lindenhof, Roombeek en het Centrum",
        "woningtype": "textielarbeiders-rijtjeswoningen, naoorlogse woningbouw en vrijstaande woningen",
        "bouwjaar": "met veel bebouwing uit de textielperiode (1900-1960) en wederopbouw na de vuurwerkramp",
        "lokaal": "Enschede heeft een bijzondere woninggeschiedenis, als textielstad en na de vuurwerkramp van 2000. Wijken als Roombeek zijn recent herbouwd, maar in Pathmos en Velve-Lindenhof staan nog veel oudere woningen met verouderde kozijnen.",
        "klimaat": "Twente heeft een continentaler klimaat dan de kust, koudere winters en warmere zomers. Dit maakt goede isolatie via kunststof kozijnen extra relevant voor het energieverbruik.",
        "label": "Veel Enschedese woningen in oudere wijken hebben energielabel D, E of F.",
        "markt": "Enschede heeft relatief betaalbare woningen, waardoor de investering in kozijnen zich snel terugverdient. Het verbeterde energielabel verhoogt de woningwaarde merkbaar.",
        "subsidie_lokaal": "In Overijssel zijn via ISDE en het Nationaal Warmtefonds dezelfde landelijke regelingen beschikbaar als in de rest van Nederland.",
    },
    {
        "slug": "haarlem",
        "stad": "Haarlem",
        "provincie": "Noord-Holland",
        "wijken": "Schalkwijk, Europawijk, Boerhaavewijk, Leidsebuurt en het Centrum",
        "woningtype": "naoorlogse stempelwijken, jaren-20 woningbouw en historische panden",
        "bouwjaar": "met veel bebouwing uit de periode 1900-1975",
        "lokaal": "Haarlem heeft een pittoresk historisch centrum naast grote naoorlogse wijken als Schalkwijk en Europawijk. In de naoorlogse stempelwijken staan duizenden woningen die energetisch sterk verouderd zijn en waar nieuwe kozijnen direct merkbaar effect hebben.",
        "klimaat": "Nabij de Hollandse kust heeft Haarlem een zacht, vochtig klimaat. Kunststof kozijnen zijn roestvrij, vochtbestendig en onderhoudsvrij, ideaal voor de kustcondities.",
        "label": "Naoorlogse Haarlemse woningen scoren gemiddeld energielabel D of lager.",
        "markt": "Haarlem heeft een van de duurste woningmarkten van Noord-Holland. Verduurzaming verhoogt de woningwaarde direct en maakt woningen aantrekkelijker voor kopers.",
        "subsidie_lokaal": "Haarlemse woningeigenaren profiteren van ISDE-subsidie en de Energiebespaarlening. De gemeente Haarlem heeft aanvullende duurzaamheidsambities.",
    },
    {
        "slug": "arnhem",
        "stad": "Arnhem",
        "provincie": "Gelderland",
        "wijken": "Presikhaaf, Malburgen, Kronenburg, Geitenkamp en het Centrum",
        "woningtype": "naoorlogse rijtjeswoningen, portieketagewoningen en herenhuizen",
        "bouwjaar": "met veel wederopbouwbebouwing na de Tweede Wereldoorlog",
        "lokaal": "Arnhem werd zwaar getroffen in de Tweede Wereldoorlog en kent een grote voorraad naoorlogse woningbouw. Wijken als Presikhaaf en Malburgen hebben veel woningen uit de jaren 50 en 60 die energetisch verouderd zijn.",
        "klimaat": "Het Gelderse rivierengebied kent extremen: koude winters en warme zomers. HR++ kozijnen zorgen voor aanzienlijk minder warmteverlies in de winter en minder oververhitting in de zomer.",
        "label": "In naoorlogse Arnhemse wijken zijn energielabels D en E veelvoorkomend.",
        "markt": "Arnhem biedt kansen voor woningverbetering. Een hoger energielabel maakt woningen sneller verkoopbaar en aantrekkelijker voor kopers.",
        "subsidie_lokaal": "Via ISDE en het Nationaal Warmtefonds kunnen Arnhemse woningeigenaren hun kozijneninvestering grotendeels financieren en subsidiëren.",
    },
    {
        "slug": "zaandam",
        "stad": "Zaandam",
        "provincie": "Noord-Holland",
        "wijken": "Poelenburg, Rosmolenwijk, Wormerveer, Zaandam-Zuid en Kogerveld",
        "woningtype": "naoorlogse portieketagewoningen, rijtjeswoningen en industriearbeiders-woningen",
        "bouwjaar": "met veel naoorlogse woningbouw uit de industriële groeiperiode 1945-1975",
        "lokaal": "Zaandam is van oudsher een industriestad en heeft een typische arbeiderswoningvoorraad. Wijken als Poelenburg en Rosmolenwijk tellen veel naoorlogse portieketagewoningen met verouderde kozijnen die energetisch zwak presteren.",
        "klimaat": "Direct naast Amsterdam en nabij het IJmeer heeft Zaandam een typisch Hollands klimaat met veel wind en neerslag. Kunststof kozijnen zijn weerbestendig en onderhoudsvrij, ook bij de vochtige poldercondities.",
        "label": "Naoorlogse woningen in Zaandam hebben vaak energielabel D of E.",
        "markt": "Zaandam is een betaalbaar alternatief voor Amsterdam. De woningmarkt is actief en verduurzaming verhoogt de verkoopprijs merkbaar.",
        "subsidie_lokaal": "ISDE-subsidie en het Nationaal Warmtefonds zijn beschikbaar voor alle eigenaar-bewoners in Zaanstad.",
    },
    {
        "slug": "amersfoort",
        "stad": "Amersfoort",
        "provincie": "Utrecht",
        "wijken": "Kruiskamp, Randenbroek, Vathorst, Soesterkwartier en het Centrum",
        "woningtype": "jaren-30 woningen, naoorlogse rijtjeswoningen en moderne Vinex-woningen",
        "bouwjaar": "met een mix van vooroorlogse en naoorlogse bebouwing plus moderne uitbreidingen",
        "lokaal": "Amersfoort heeft een gevarieerde woningvoorraad, van karakteristieke jaren-30 woningen in het Soesterkwartier tot moderne nieuwbouw in Vathorst. In de oudere wijken als Kruiskamp en Randenbroek zijn kozijnen uit de periode 1950-1980 energetisch verouderd.",
        "klimaat": "Centraal in Nederland heeft Amersfoort een continentaal klimaat met warme zomers en koude winters. Goede raampartijen met HR++ glas maken een groot verschil in energieverbruik.",
        "label": "Oudere Amersfoortse woningen hebben energielabel C tot E.",
        "markt": "Amersfoort heeft een sterke woningmarkt. Verduurzaming is een bewezen waardestijger in dit segment.",
        "subsidie_lokaal": "Via ISDE (RVO) en het Nationaal Warmtefonds zijn alle landelijke subsidies en financieringsmogelijkheden beschikbaar in Amersfoort.",
    },
    {
        "slug": "apeldoorn",
        "stad": "Apeldoorn",
        "provincie": "Gelderland",
        "wijken": "Brinkhorst, De Maten, Zevenhuizen, Orden en het Centrum",
        "woningtype": "vrijstaande woningen, bungalows en rijtjeswoningen in bosrijke setting",
        "bouwjaar": "met veel naoorlogse laagbouw uit de groene woonwijken 1950-1980",
        "lokaal": "Apeldoorn staat bekend als 'grootste dorp van Nederland' met veel laagbouw, ruime kavels en bosrijke woonwijken. De vrijstaande woningen en bungalows uit de periode 1955-1980 hebben vaak grote glasoppervlakken die energetisch verouderd zijn.",
        "klimaat": "Op de Veluwe heeft Apeldoorn relatief koude winters. De hoge glasoppervlakte van veel Apeldoornse woningen maakt investering in HR++ of triple glas extra lonend.",
        "label": "Bungalows en vrijstaande woningen in Apeldoorn hebben door hun grote oppervlak vaak energielabel D of E.",
        "markt": "Apeldoorn trekt veel gezinnen op zoek naar ruimte. Verduurzaming verhoogt de aantrekkelijkheid en waarde van de woning.",
        "subsidie_lokaal": "In Gelderland zijn ISDE-subsidie en de Energiebespaarlening volledig beschikbaar. Bij triple glas ontvang je tot €111 per m² subsidie.",
    },
    {
        "slug": "den-bosch",
        "stad": "Den Bosch",
        "provincie": "Noord-Brabant",
        "wijken": "Rosmalen, Maaspoort, Empel, Boschveld en het Centrum",
        "woningtype": "naoorlogse rijtjeswoningen, vrijstaande woningen en herenhuizen",
        "bouwjaar": "met bebouwing uit zowel de vooroorlogse periode als grote naoorlogse uitbreidingen",
        "lokaal": "Den Bosch (officieel 's-Hertogenbosch) heeft een historisch centrum naast uitgestrekte naoorlogse wijken en dorpen als Rosmalen en Empel. De oudere woningvoorraad in Boschveld en Maaspoort heeft energetisch sterk te winnen bij nieuwe kozijnen.",
        "klimaat": "Midden in Brabant heeft Den Bosch een gematigd zeeklimaat. HR++ glas biedt betere warmteretentie in de winter en vermindert oververhitting in de zomer.",
        "label": "Naoorlogse woningen in Den Bosch hebben gemiddeld energielabel C, D of E.",
        "markt": "Den Bosch is een aantrekkelijke stad met een actieve woningmarkt. Verduurzaming is een bewuste keuze die zich terugbetaalt in lagere energiekosten en hogere woningwaarde.",
        "subsidie_lokaal": "ISDE-subsidie en het Nationaal Warmtefonds zijn beschikbaar. De gemeente Den Bosch stimuleert verduurzaming aanvullend via lokale initiatieven.",
    },
    {
        "slug": "hoofddorp",
        "stad": "Hoofddorp",
        "provincie": "Noord-Holland",
        "wijken": "Floriande, Toolenburg, Graan voor Visch, Bornholm en het Centrum",
        "woningtype": "Vinex-woningen, twee-onder-een-kapwoningen en rijtjeswoningen",
        "bouwjaar": "met veel bebouwing uit de periode 1980-2005 (grote uitbreidingen Haarlemmermeer)",
        "lokaal": "Hoofddorp is het hart van de Haarlemmermeer en groeide explosief in de jaren 80 en 90. De woningvoorraad bestaat grotendeels uit uitbreidingswijken met rijtjeswoningen en twee-onder-een-kapwoningen van 25 tot 40 jaar oud, een leeftijd waarop HR-glas aan vervanging toe is.",
        "klimaat": "De Haarlemmermeer is een open, windrijke polder. Goed geïsoleerde kunststof kozijnen zijn hier extra waardevol voor tochtwering, geluidsdemping en warmtebehoud.",
        "label": "Woningen uit de jaren 80 en 90 in Hoofddorp hebben doorgaans energielabel C of D.",
        "markt": "Hoofddorp heeft door de nabijheid van Schiphol en Amsterdam een sterke woningmarkt. Verduurzaming maakt woningen direct aantrekkelijker.",
        "subsidie_lokaal": "Haarlemmermeer bewoners kunnen aanspraak maken op ISDE-subsidie en de Energiebespaarlening van het Nationaal Warmtefonds.",
    },
    {
        "slug": "maastricht",
        "stad": "Maastricht",
        "provincie": "Limburg",
        "wijken": "Wijck, Belfort, Wyckerpoort, Heugemerveld en het Centrum",
        "woningtype": "vakwerkhuizen, Belgische rijwoningen en naoorlogse woningbouw",
        "bouwjaar": "met historische panden in het centrum en naoorlogse wijken aan de rand",
        "lokaal": "Maastricht heeft een van de rijkste historische binnensteden van Nederland, met vakwerkhuizen en rijwoningen in Belgische stijl. Buiten het centrum staan naoorlogse wijken met typische Limburgse rijtjeswoningen. In beide categorieën zijn er grote kansen voor energieverbetering via nieuwe kozijnen.",
        "klimaat": "Zuid-Limburg heeft het warmste klimaat van Nederland, maar ook koude winters. Goede isolatie is hier zowel zomer als winter relevant, koeler binnenshuis in augustus, warmer in januari.",
        "label": "Historische Maastrichtse panden hebben vaak energielabel E of F, een van de slechtste van Nederland.",
        "markt": "Maastricht heeft een unieke woningmarkt met internationale vraag. Verduurzaming, ook van historische panden, verhoogt de waarde en verkoopbaarheid significant.",
        "subsidie_lokaal": "In Limburg zijn ISDE-subsidie en de Energiebespaarlening beschikbaar. Voor monumentale panden gelden aangepaste regels, wij adviseren je hier gratis over.",
    },
    {
        "slug": "leiden",
        "stad": "Leiden",
        "provincie": "Zuid-Holland",
        "wijken": "Meerburg, Stevenshof, De Kooi, Leiden-Noord en het Centrum",
        "woningtype": "grachtenpanden, jaren-30 woningen en naoorlogse rijtjeswoningen",
        "bouwjaar": "met historische bebouwing in het centrum en naoorlogse uitbreidingen",
        "lokaal": "Leiden heeft een historisch centrum met grachten naast grote naoorlogse wijken als Stevenshof en Leiden-Noord. De vooroorlogse woningen rondom de Leidse grachten zijn energetisch vaak slecht geïsoleerd, terwijl in de naoorlogse wijken verouderd dubbel glas de zwakke schakel is.",
        "klimaat": "Nabij de kust heeft Leiden een mild, vochtig klimaat. Kunststof kozijnen zijn onderhoudsvrij en vochtbestendig, een praktisch voordeel in de Leidse polderomgeving.",
        "label": "Historische Leidse panden hebben gemiddeld energielabel D, E of lager.",
        "markt": "Leiden is een populaire universiteitsstad met een krappe woningmarkt. Verduurzaming is een directe waardestijger en vergroot de verhuurbaarheid.",
        "subsidie_lokaal": "Via ISDE en het Nationaal Warmtefonds kunnen Leidse woningeigenaren subsidie en financiering combineren voor een optimaal resultaat.",
    },
    {
        "slug": "dordrecht",
        "stad": "Dordrecht",
        "provincie": "Zuid-Holland",
        "wijken": "Sterrenburg, Wielwijk, Crabbehof, Oud-Krispijn en het Centrum",
        "woningtype": "grachtenpanden, naoorlogse portieketagewoningen en rijtjeswoningen",
        "bouwjaar": "met historisch centrum en grote naoorlogse uitbreidingswijken",
        "lokaal": "Dordrecht is een historische eilandstad met een gevarieerde woningvoorraad. Naoorlogse wijken als Sterrenburg en Wielwijk tellen tienduizenden woningen uit de jaren 60 en 70 die energetisch sterk verouderd zijn, precies de categorie woningen waar nieuwe kozijnen het meeste opleveren.",
        "klimaat": "Als eilandstad in het rivierdelta-gebied heeft Dordrecht te maken met vocht, wind en getijdenklimaat. Kunststof kozijnen met goede afdichting zijn hier extra waardevol.",
        "label": "In naoorlogse Dordtse wijken overheersen energielabels C, D en E.",
        "markt": "Dordrecht biedt betaalbare woningen met goede potentie. Verduurzaming via kozijnen verhoogt energielabel en woningwaarde direct.",
        "subsidie_lokaal": "Alle landelijke regelingen (ISDE, Warmtefonds) zijn beschikbaar voor woningeigenaren in Dordrecht.",
    },
    {
        "slug": "zoetermeer",
        "stad": "Zoetermeer",
        "provincie": "Zuid-Holland",
        "wijken": "Seghwaert, Buytenwegh, Palenstein, Rokkeveen en het Centrum",
        "woningtype": "groeistedelijke rijtjeswoningen, portieketagewoningen en twee-onder-een-kapwoningen",
        "bouwjaar": "grotendeels gebouwd als groeikern tussen 1965 en 1990",
        "lokaal": "Zoetermeer werd als groeikern planmatig aangelegd en heeft een woningvoorraad die grotendeels dateert uit 1965-1990. Na 35 tot 60 jaar zijn de kozijnen in veel van deze woningen toe aan vervanging. HR++ glas in plaats van het oude dubbel glas levert een directe energiebesparing van €800 tot €1.500 per jaar.",
        "klimaat": "In het Hollandse poldergebied nabij Den Haag heeft Zoetermeer een typisch zeeklimaat. Nieuwe kunststof kozijnen zorgen voor minder tocht, minder condensatie en significant lager gasverbruik.",
        "label": "De meeste Zoetermeerse woningen uit de groeikernperiode hebben energielabel C of D.",
        "markt": "Zoetermeer ligt strategisch tussen Den Haag en Leiden. Verduurzaming verhoogt de aantrekkelijkheid van je woning in deze actieve markt.",
        "subsidie_lokaal": "ISDE-subsidie en de Energiebespaarlening zijn beschikbaar. Bij triple glas ontvang je tot €111 per m² terug van de overheid.",
    },
    {
        "slug": "zwolle",
        "stad": "Zwolle",
        "provincie": "Overijssel",
        "wijken": "Holtenbroek, Dieze, Aa-landen, Stadshagen en het Centrum",
        "woningtype": "naoorlogse rijtjeswoningen, jaren-70 portieketagewoningen en nieuwbouw",
        "bouwjaar": "met naoorlogse uitbreidingen en recent de grote wijk Stadshagen",
        "lokaal": "Zwolle is het knooppunt van Overijssel en heeft een gevarieerde woningvoorraad. Wijken als Holtenbroek en Dieze herbergen veel naoorlogse woningbouw uit de jaren 60 en 70, terwijl Stadshagen veel nieuwere woningen heeft. In de oudere wijken zijn kozijnen een energetische zwakke schakel.",
        "klimaat": "Zwolle ligt aan de IJssel en heeft continentale invloeden. De winters zijn kouder dan aan de kust. Goede isolatie via HR++ kozijnen is hier direct merkbaar op de stookkosten.",
        "label": "Naoorlogse Zwolse woningen scoren gemiddeld energielabel C of D.",
        "markt": "Zwolle is een groeiende, aantrekkelijke stad. De actieve woningmarkt beloont verduurzaming direct met een hogere verkoopprijs.",
        "subsidie_lokaal": "Via ISDE en het Nationaal Warmtefonds zijn alle subsidies en financieringsmogelijkheden beschikbaar voor Zwolse woningeigenaren.",
    },
    {
        "slug": "deventer",
        "stad": "Deventer",
        "provincie": "Overijssel",
        "wijken": "Borgele, Colmschate, Keizerslanden, Platvoet en het Centrum",
        "woningtype": "historische Hanzestad-panden, naoorlogse rijtjeswoningen en vrijstaande woningen",
        "bouwjaar": "met een unieke mix van historische bebouwing en naoorlogse uitbreidingen",
        "lokaal": "Deventer is een van de oudste Hanzesteden van Nederland met een karakteristiek historisch centrum. Naast het centrum heeft Deventer grote naoorlogse wijken als Borgele en Keizerslanden met woningen die energetisch verouderd zijn. Zowel historische panden als naoorlogse woningen profiteren sterk van moderne kunststof kozijnen.",
        "klimaat": "Aan de IJssel heeft Deventer een continentaal klimaat met koude winters en warme zomers. Goede isolatie is het hele jaar door voelbaar, zowel op de energierekening als in het binnencomfort.",
        "label": "Historische panden in Deventer hebben gemiddeld energielabel E of F.",
        "markt": "Deventer heeft een aantrekkelijke woningmarkt met historische charme. Verduurzaming, ook van historische panden, vergroot de waarde en verkoopbaarheid.",
        "subsidie_lokaal": "In Overijssel zijn ISDE en het Nationaal Warmtefonds volledig beschikbaar. Wij begeleiden de aanvraag stap voor stap.",
    },
    {
        "slug": "delft",
        "stad": "Delft",
        "provincie": "Zuid-Holland",
        "wijken": "Buitenhof, Tanthof, Voorhof, Wippolder en het Centrum",
        "woningtype": "grachtenpanden, jaren-70 universiteitswijk en naoorlogse portieketagewoningen",
        "bouwjaar": "met historische bebouwing in het centrum en grote naoorlogse uitbreidingen",
        "lokaal": "Delft is een historische universiteitsstad met grachten en een karakteristiek centrum naast grote naoorlogse wijken als Buitenhof en Tanthof. In de naoorlogse woningbouw zijn kozijnen uit de jaren 60 en 70 energetisch sterk verouderd en aan vervanging toe.",
        "klimaat": "Als lage polderstad nabij de kust heeft Delft een vochtig, winderig klimaat. Goed geïsoleerde kozijnen reduceren condensatie, tocht en warmteverlies.",
        "label": "Historische Delftse panden en naoorlogse woningen scoren gemiddeld energielabel D of E.",
        "markt": "Delft heeft een actieve woningmarkt mede door de universiteit. Verduurzaming is een logische investering in deze omgeving.",
        "subsidie_lokaal": "ISDE-subsidie en de Energiebespaarlening zijn volledig beschikbaar voor woningeigenaren in Delft.",
    },
    {
        "slug": "alkmaar",
        "stad": "Alkmaar",
        "provincie": "Noord-Holland",
        "wijken": "Overdie, Koedijk, Vroonermeer, De Mare en het Centrum",
        "woningtype": "naoorlogse rijtjeswoningen, twee-onder-een-kapwoningen en historische panden",
        "bouwjaar": "met historisch centrum en grote naoorlogse uitbreidingswijken",
        "lokaal": "Alkmaar staat bekend om zijn kaasmarkt en historische binnenstad, maar heeft ook uitgestrekte naoorlogse wijken als Overdie en De Mare. In deze wijken staan duizenden woningen uit de jaren 60 en 70 die energetisch verouderd zijn en sterk baat hebben bij nieuwe kunststof kozijnen.",
        "klimaat": "Noord-Holland is windgevoelig en het klimaat is vochtig. Kunststof kozijnen zijn onderhoudsvrij, roestbestendig en perfect geschikt voor de vochtige kustomgeving.",
        "label": "Naoorlogse Alkmaarse woningen hebben gemiddeld energielabel C of D.",
        "markt": "Alkmaar heeft een actieve woningmarkt als centrum van West-Friesland. Verduurzaming verhoogt de verkoopprijs en aantrekkelijkheid van je woning.",
        "subsidie_lokaal": "Via ISDE en het Nationaal Warmtefonds zijn alle landelijke regelingen beschikbaar voor woningeigenaren in Alkmaar.",
    },
    {
        "slug": "heerlen",
        "stad": "Heerlen",
        "provincie": "Limburg",
        "wijken": "Meezenbroek, Vrieheide, Heerlerheide, Hoensbroek en het Centrum",
        "woningtype": "mijnwerkers-rijtjeswoningen, naoorlogse portieketagewoningen en vrijstaande woningen",
        "bouwjaar": "grotendeels gebouwd voor en tijdens de mijnbouwperiode (1900-1970)",
        "lokaal": "Heerlen heeft een unieke woninggeschiedenis door de mijnbouw. Karakteristieke mijnwerkers-rijtjeswoningen in wijken als Heerlerheide en Hoensbroek zijn energetisch sterk verouderd. De typische Limburgse bebouwing met grote raampartijen biedt extra potentieel voor energiebesparing via HR++ kozijnen.",
        "klimaat": "Zuid-Limburg heeft koude winters en warme zomers. Goede isolatie is het hele jaar relevant, HR++ glas vermindert warmteverlies in de winter en oververhitting in de zomer.",
        "label": "Mijnwerkers-rijtjeswoningen in Heerlen hebben gemiddeld energielabel D, E of slechter.",
        "markt": "Heerlen investeert in stedelijke vernieuwing. Verduurzaming via kozijnen sluit hier direct bij aan en verhoogt de woningwaarde.",
        "subsidie_lokaal": "ISDE-subsidie en het Nationaal Warmtefonds zijn volledig beschikbaar in Heerlen en de rest van Zuid-Limburg.",
    },
    {
        "slug": "venlo",
        "stad": "Venlo",
        "provincie": "Limburg",
        "wijken": "Blerick, Tegelen, Belfeld, Velden en het Centrum",
        "woningtype": "Limburgse rijwoningen, vrijstaande woningen en naoorlogse woningbouw",
        "bouwjaar": "met een mix van historische bebouwing en naoorlogse uitbreidingen",
        "lokaal": "Venlo is een grensdynamische stad aan de Maas met nauwe banden met Duitsland. De woningvoorraad is gevarieerd, van historische Limburgse rijwoningen in het centrum tot vrijstaande woningen in dorpen als Blerick en Tegelen. In veel categorieën zijn kozijnen energetisch de zwakste schakel.",
        "klimaat": "In het Limburgse Maasgebied heeft Venlo het warmste klimaat van Nederland, maar ook koude winters. Goede isolatie via HR++ kozijnen is zowel zomer als winter voelbaar.",
        "label": "Oudere woningen in Venlo en de kernen hebben gemiddeld energielabel D of E.",
        "markt": "Venlo heeft een actieve grensstreekmarkt. Verduurzaming verhoogt de woningwaarde en verkoopbaarheid.",
        "subsidie_lokaal": "In Limburg zijn alle landelijke subsidies beschikbaar: ISDE en het Nationaal Warmtefonds. Wij begeleiden de aanvraag stap voor stap.",
    },
    {
        "slug": "leeuwarden",
        "stad": "Leeuwarden",
        "provincie": "Friesland",
        "wijken": "Heechterp, Schieringen, De Bouwen, Aldlân en het Centrum",
        "woningtype": "naoorlogse portieketagewoningen, Friese boerderijomgebouwde woningen en rijtjeswoningen",
        "bouwjaar": "met naoorlogse grootschalige woningbouwwijken als Heechterp",
        "lokaal": "Leeuwarden is de hoofdstad van Friesland en heeft een diverse woningvoorraad. Grootschalige naoorlogse wijken als Heechterp en Schieringen tellen duizenden portieketagewoningen die energetisch sterk verouderd zijn. Nieuwe kozijnen maken hier een direct en groot verschil.",
        "klimaat": "Friesland heeft de koudste en natste winters van de westelijke provincies. Goed isolerende kozijnen met HR++ of triple glas zijn hier meer dan de moeite waard, de terugverdientijd is door het hoge stookverbruik korter.",
        "label": "Naoorlogse Leeuwarder wijken scoren gemiddeld energielabel D of E.",
        "markt": "Leeuwarden is de culturele hoofdstad van Friesland en heeft een betaalbare woningmarkt. Verduurzaming is een slimme investering voor woningeigenaren.",
        "subsidie_lokaal": "Via ISDE en het Nationaal Warmtefonds zijn alle landelijke subsidies beschikbaar. De provincie Friesland heeft aanvullende subsidiemogelijkheden voor verduurzaming.",
    },
    {
        "slug": "emmen",
        "stad": "Emmen",
        "provincie": "Drenthe",
        "wijken": "Emmerhout, Rietlanden, Angelslo, Bargeres en het Centrum",
        "woningtype": "naoorlogse rijtjeswoningen, vrijstaande dorpswoningen en portieketagewoningen",
        "bouwjaar": "met veel naoorlogse woningbouw uit de industrialisatieperiode 1950-1980",
        "lokaal": "Emmen groeide in de naoorlogse periode door de vestiging van industrie (DSM). Wijken als Emmerhout, Angelslo en Bargeres tellen duizenden naoorlogse woningen die energetisch verouderd zijn. Door het open Drentse landschap zijn kozijnen ook relevant voor tochtwering.",
        "klimaat": "Drenthe heeft een continentaal klimaat met koude winters en warme zomers. Door de open, relatief windrijke omgeving zijn goed geïsoleerde kozijnen hier extra waardevol.",
        "label": "Naoorlogse woningen in Emmen hebben gemiddeld energielabel D, E of F, een van de slechtste van het noorden.",
        "markt": "Emmen biedt betaalbare woningen met veel potentieel. Verduurzaming via kozijnen verhoogt het energielabel en daarmee de woningwaarde aanzienlijk.",
        "subsidie_lokaal": "Drentse woningeigenaren kunnen in aanmerking komen voor ISDE en het Nationaal Warmtefonds. Wij begeleiden de aanvraag gratis.",
    },
    {
        "slug": "almelo",
        "stad": "Almelo",
        "provincie": "Overijssel",
        "wijken": "Ossenkoppelerhoek, De Riet, Sluitersveld, Aadijk en het Centrum",
        "woningtype": "textielarbeiders-rijtjeswoningen, naoorlogse woningbouw en vrijstaande woningen",
        "bouwjaar": "met veel bebouwing uit de textielperiode en de wederopbouwjaren",
        "lokaal": "Almelo is onze thuisstad, vanuit hier bedienen wij de regio Twente en heel Overijssel. Als textielstad heeft Almelo een karakteristieke woningvoorraad van arbeiders-rijtjeswoningen. Wij kennen de lokale kozijnenmarkt als geen ander en plaatsten al ruim 523 projecten in de regio.",
        "klimaat": "Twente heeft een continentaler klimaat dan de kust, koudere winters en warmere zomers. Goede isolatie via HR++ kozijnen is hier extra relevant voor zowel comfort als energiebesparing.",
        "label": "Oudere Almelose woningen hebben gemiddeld energielabel C, D of E.",
        "markt": "Almelo en de Twentse regio hebben een actieve woningmarkt. Verduurzaming via kozijnen is hier een bewezen waardestijger.",
        "subsidie_lokaal": "Via ISDE en het Nationaal Warmtefonds bespaar je als Almelose woningeigenaar direct op de investering. Wij begeleiden de aanvraag stap voor stap vanuit onze vestiging in Almelo.",
    },
    {
        "slug": "oss",
        "stad": "Oss",
        "provincie": "Noord-Brabant",
        "wijken": "Ruwaard, Schadewijk, Maasland, Ravenstein en het Centrum",
        "woningtype": "naoorlogse rijtjeswoningen, vrijstaande Brabantse woningen en twee-onder-een-kapwoningen",
        "bouwjaar": "met naoorlogse groei door de industrie (Organon) en recent sterk groeiende woningbouw",
        "lokaal": "Oss groeide sterk door de farmaceutische industrie en heeft een karakteristieke industriestad-woningvoorraad. Wijken als Ruwaard en Schadewijk hebben veel woningen uit de jaren 60 en 70 die energetisch verouderd zijn en sterk baten bij vervanging van de kozijnen.",
        "klimaat": "Oost-Brabant heeft een gematigd zeeklimaat met koele winters. HR++ kozijnen zorgen voor lagere stookkosten en meer comfort in de koude maanden.",
        "label": "Naoorlogse Osse woningen hebben gemiddeld energielabel D of E.",
        "markt": "Oss heeft een actieve lokale woningmarkt. Verduurzaming via kozijnen verhoogt de aantrekkelijkheid en verkoopbaarheid.",
        "subsidie_lokaal": "Via ISDE en het Nationaal Warmtefonds zijn alle subsidies beschikbaar voor eigenaar-bewoners in Oss.",
    },
    {
        "slug": "hilversum",
        "stad": "Hilversum",
        "provincie": "Noord-Holland",
        "wijken": "Larenseweg, 't Hoogt, Kerkelanden, Hilversum-Noord en het Centrum",
        "woningtype": "jaren-30 villawijken, vrijstaande woningen en historische media-panden",
        "bouwjaar": "met karakteristieke Dudok-architectuur en veel bebouwing uit 1920-1960",
        "lokaal": "Hilversum staat bekend om de mediasector en de karakteristieke Dudok-architectuur. De stad heeft veel jaren-30 woningen in villawijken zoals 't Hoogt en Kerkelanden. Deze woningen hebben vaak grote raampartijen die energetisch sterk te verbeteren zijn met modern HR++ of triple glas.",
        "klimaat": "Op de Utrechtse Heuvelrug heeft Hilversum een relatief droog en continentaal klimaat. De woningbouw, met zijn grote glasoppervlakken, profiteert sterk van HR++ glas.",
        "label": "Vooroorlogse Hilversumse woningen hebben gemiddeld energielabel D of E.",
        "markt": "Hilversum heeft een van de duurste woningmarkten van Noord-Holland. Verduurzaming verhoogt de waarde en verkoopbaarheid van je woning direct.",
        "subsidie_lokaal": "ISDE-subsidie en het Nationaal Warmtefonds zijn beschikbaar. Bij triple glas ontvang je tot €111 per m², ideaal voor de grote raampartijen in Hilversumse woningen.",
    },
    {
        "slug": "hengelo",
        "stad": "Hengelo",
        "provincie": "Overijssel",
        "wijken": "Woolde, Berflo Es, Hasseler Es, Veldwijk-Noord en het Centrum",
        "woningtype": "industriearbeiders-rijtjeswoningen, naoorlogse woningbouw en twee-onder-een-kapwoningen",
        "bouwjaar": "met veel bebouwing uit de industriële Twentse groeiperiode 1920-1975",
        "lokaal": "Hengelo is de industriestad van Twente, bekend van Stork en AKZO, met een typische arbeiderswoningvoorraad. Wijken als Woolde en Berflo Es tellen veel naoorlogse rijtjeswoningen die energetisch verouderd zijn. Nieuwe kunststof kozijnen maken hier een direct merkbaar verschil in stookkosten.",
        "klimaat": "Twente heeft een continentaler klimaat met koudere winters dan de kustprovincies. Goede isolatie via HR++ kozijnen is hier extra lonend.",
        "label": "Naoorlogse woningen in Hengelo hebben gemiddeld energielabel D of E.",
        "markt": "Hengelo en de Twentse regio hebben een betaalbare woningmarkt. De investering in kozijnen verdient zich hier relatief snel terug.",
        "subsidie_lokaal": "ISDE en het Nationaal Warmtefonds zijn beschikbaar voor alle woningeigenaren in Overijssel. Wij begeleiden de aanvraag volledig.",
    },
    {
        "slug": "roosendaal",
        "stad": "Roosendaal",
        "provincie": "Noord-Brabant",
        "wijken": "Langdonk, Westrand, Kortendijk, Tolberg en het Centrum",
        "woningtype": "naoorlogse rijtjeswoningen, Brabantse vrijstaande woningen en portieketagewoningen",
        "bouwjaar": "met naoorlogse groei als logistiek knooppunt in West-Brabant",
        "lokaal": "Roosendaal is het logistieke knooppunt van West-Brabant en heeft een typische Brabantse woningvoorraad. Wijken als Langdonk en Westrand hebben naoorlogse rijtjeswoningen uit de periode 1960-1985 die energetisch sterk verouderd zijn en bij nieuwe kozijnen direct minder stookkosten hebben.",
        "klimaat": "West-Brabant heeft een mild zeeklimaat. HR++ kozijnen zorgen voor minder tocht, betere isolatie en lagere energiekosten in de koude maanden.",
        "label": "Naoorlogse Roosendalse woningen hebben gemiddeld energielabel C, D of E.",
        "markt": "Roosendaal heeft een actieve woningmarkt als regionaal centrum. Verduurzaming is hier een slimme investering.",
        "subsidie_lokaal": "Via ISDE en het Nationaal Warmtefonds zijn alle landelijke subsidies en financieringsmogelijkheden beschikbaar in Roosendaal.",
    },
    {
        "slug": "purmerend",
        "stad": "Purmerend",
        "provincie": "Noord-Holland",
        "wijken": "Wheermolen, Overwhere, Purmer-Zuid, De Weidevenne en het Centrum",
        "woningtype": "rijtjeswoningen, twee-onder-een-kapwoningen en portieketagewoningen",
        "bouwjaar": "grotendeels gebouwd als groeikern na 1970",
        "lokaal": "Purmerend werd als groeikern aangewezen en groeide explosief van een klein stadje naar een stad van 80.000 inwoners. De woningvoorraad is grotendeels gebouwd in de periode 1970-1995. Na 30 tot 55 jaar zijn de kozijnen in veel van deze woningen aan vervanging toe.",
        "klimaat": "Midden in het Hollandse poldergebied is Purmerend windgevoelig en vochtig. Goed geïsoleerde kunststof kozijnen met HR++ glas bieden direct minder tocht en condensatie.",
        "label": "Woningen uit de groeikernperiode in Purmerend hebben gemiddeld energielabel C of D.",
        "markt": "Purmerend is een aantrekkelijk alternatief voor Amsterdam met een actieve woningmarkt. Verduurzaming verhoogt de waarde en verkoopbaarheid.",
        "subsidie_lokaal": "ISDE-subsidie en het Nationaal Warmtefonds zijn beschikbaar voor alle eigenaar-bewoners in Purmerend.",
    },
    {
        "slug": "schiedam",
        "stad": "Schiedam",
        "provincie": "Zuid-Holland",
        "wijken": "Groenoord, Nieuwland, Schiedam-Oost, Woudhoek en het Centrum",
        "woningtype": "historische jenever-panden, naoorlogse portieketagewoningen en rijtjeswoningen",
        "bouwjaar": "met historisch centrum en grote naoorlogse woningbouwprojecten",
        "lokaal": "Schiedam staat bekend om zijn historische jeneverstokerijen en heeft een gevarieerde woningvoorraad. De naoorlogse wijken Groenoord en Nieuwland tellen grote aantallen portieketagewoningen uit de jaren 60 en 70, een categorie waarbij nieuwe kozijnen de grootste energiewinst opleveren.",
        "klimaat": "Als Maasoevers-stad heeft Schiedam een typisch Hollands-maritiem klimaat met vochtige winters en winddruk. Kunststof kozijnen zijn roestvrij en onderhoudsvrij, een groot praktisch voordeel.",
        "label": "Naoorlogse Schiedamse woningen hebben gemiddeld energielabel D of E.",
        "markt": "Schiedam biedt betaalbare woningen in de Rotterdamse regio. Verduurzaming via kozijnen is een directe waardestijger in deze markt.",
        "subsidie_lokaal": "ISDE-subsidie en het Nationaal Warmtefonds zijn beschikbaar. Wij begeleiden de aanvraag stap voor stap.",
    },
    {
        "slug": "helmond",
        "stad": "Helmond",
        "provincie": "Noord-Brabant",
        "wijken": "Rijpelberg, Mierlo-Hout, Brandevoort, Center en Binnenstad",
        "woningtype": "naoorlogse rijtjeswoningen, textielarbeiders-woningen en nieuwbouw Brandevoort",
        "bouwjaar": "met veel naoorlogse woningbouw plus de unieke Vinex-locatie Brandevoort",
        "lokaal": "Helmond heeft een rijke textielgeschiedenis en een gevarieerde woningvoorraad. Wijken als Rijpelberg en Mierlo-Hout tellen naoorlogse rijtjeswoningen met verouderde kozijnen, terwijl Brandevoort als middeleeuws aandoende Vinex-wijk nieuwere woningbouw heeft.",
        "klimaat": "Oost-Brabant heeft een gematigd klimaat. In de naoorlogse woningbouw zijn kozijnen uit de jaren 60 en 70 toe aan vervanging, HR++ glas biedt hier direct energievoordeel.",
        "label": "Naoorlogse woningen in Helmond hebben gemiddeld energielabel D of E.",
        "markt": "Helmond heeft een actieve woningmarkt in de Brainport-regio. Verduurzaming is hier een slimme investering mede door de hoge energieprijzen.",
        "subsidie_lokaal": "ISDE en het Nationaal Warmtefonds zijn volledig beschikbaar voor woningeigenaren in Helmond.",
    },
    {
        "slug": "lelystad",
        "stad": "Lelystad",
        "provincie": "Flevoland",
        "wijken": "Boswijk, Warande, Zuiderzeewijk, Atolwijk en het Centrum",
        "woningtype": "vrijstaande woningen, rijtjeswoningen en Flevolandse laagbouw",
        "bouwjaar": "grotendeels gebouwd na 1967, Lelystad is een van de jongste steden van Nederland",
        "lokaal": "Lelystad is planmatig aangelegd na de droogmaking van Flevoland. De woningvoorraad dateert grotendeels uit de periode 1970-1995. Na 30 tot 55 jaar zijn kozijnen in deze woningen aan vervanging toe, zeker het oud dubbel glas dat niet meer voldoet aan huidige isolatienormen.",
        "klimaat": "Flevoland is een van de windrijkste provincies van Nederland. Goed geïsoleerde kozijnen met deugdelijke afdichting zijn hier extra waardevol voor tochtwering en energiebesparing.",
        "label": "Woningen uit de pionierperiode in Lelystad hebben gemiddeld energielabel C, D of E.",
        "markt": "Lelystad heeft betaalbare woningen en groeit als stad. Verduurzaming verhoogt het energielabel en de woningwaarde.",
        "subsidie_lokaal": "ISDE-subsidie en het Nationaal Warmtefonds zijn volledig beschikbaar voor woningeigenaren in Lelystad en heel Flevoland.",
    },
    {
        "slug": "ede",
        "stad": "Ede",
        "provincie": "Gelderland",
        "wijken": "Veldhuizen, De Nieuwe Aanleg, Rietkampen, Maandereng en het Centrum",
        "woningtype": "vrijstaande woningen, rijtjeswoningen op de Veluwe en naoorlogse gezinswoningen",
        "bouwjaar": "met een mix van vooroorlogse bebouwing en naoorlogse gezinswijken",
        "lokaal": "Ede is een groene, uitgestrekte gemeente op de Veluwe met veel vrijstaande woningen en ruime kavels. Naast het centrum heeft Ede naoorlogse woonwijken als Veldhuizen en De Nieuwe Aanleg met rijtjeswoningen die energetisch sterk te verbeteren zijn via nieuwe kozijnen.",
        "klimaat": "Op de Veluwe is het klimaat continentaler dan aan de kust, relatief droog, met koude winters. Goede isolatie via HR++ kozijnen is hier merkbaar op het stookverbruik.",
        "label": "Naoorlogse woningen in Ede hebben gemiddeld energielabel C of D.",
        "markt": "Ede heeft een actieve woningmarkt als uitloopgebied van de Randstad. Verduurzaming is een bewezen waardestijger in dit segment.",
        "subsidie_lokaal": "ISDE-subsidie en het Nationaal Warmtefonds zijn volledig beschikbaar voor woningeigenaren in Ede en de gemeente Gelderland.",
    },
]

def make_page(s):
    slug = s["slug"]
    stad = s["stad"]
    provincie = s["provincie"]
    wijken = s["wijken"]
    woningtype = s["woningtype"]
    bouwjaar = s["bouwjaar"]
    lokaal = s["lokaal"]
    klimaat = s["klimaat"]
    label = s["label"]
    markt = s["markt"]
    subsidie_lokaal = s["subsidie_lokaal"]

    seo_content = """
    <section class="sectie" style="background:#fff;">
        <div class="container" style="max-width:860px;">

            <h2 style="font-size:clamp(22px,3vw,30px);margin-bottom:20px;">Kunststof kozijnen in """ + stad + """: wat je moet weten</h2>

            <p style="color:#444;line-height:1.8;margin-bottom:22px;">
                Woningeigenaren in """ + stad + """ die toe zijn aan nieuwe kozijnen, staan voor een keuze die verder gaat dan alleen esthetiek. Kunststof kozijnen met HR++ glas zijn de meest kosteneffectieve manier om direct de isolatiewaarde van je woning te verbeteren, het energieverbruik te verlagen en het binnencomfort merkbaar te verhogen. Zeker in """ + stad + """, met zijn """ + woningtype + """ """ + bouwjaar + """, is de potentiële energiebesparing groot. Woningeigenaren in """ + provincie + """ besparen na vervanging van verouderde kozijnen gemiddeld """ + """<strong>&euro;800 tot &euro;1.500 per jaar</strong> op de energierekening, afhankelijk van het type beglazing dat wordt vervangen.
            </p>

            <h3 style="font-size:20px;margin-bottom:14px;color:#1E5C2F;">De woningvoorraad in """ + stad + """</h3>
            <p style="color:#444;line-height:1.8;margin-bottom:22px;">
                """ + lokaal + """ Typische wijken zoals """ + wijken + """ kennen """ + woningtype + """. """ + label + """ Dit betekent dat vervanging van de kozijnen voor veel """ + stad + """se woningeigenaren een van de meest impactvolle verduurzamingsstappen is die zij kunnen zetten, met een directe terugverdientijd van gemiddeld 10 tot 12 jaar en een levensduur van de kozijnen van 35 tot 50 jaar.
            </p>

            <h3 style="font-size:20px;margin-bottom:14px;color:#1E5C2F;">Klimaat en isolatie in """ + provincie + """</h3>
            <p style="color:#444;line-height:1.8;margin-bottom:22px;">
                """ + klimaat + """ HR++ glas heeft een warmtedoorgangscoëfficiënt (Uw-waarde) van maximaal 1,1 W/m²K, vergeleken met 5,7 W/m²K voor enkel glas en 2,7 W/m²K voor oud dubbel glas. Dat verschil vertaalt zich direct in lagere stookkosten en een aangenamer binnenklimaat. Triple glas gaat nog verder met een Uw-waarde tot 0,7 W/m²K, ideaal voor woningen in """ + stad + """ die maximale prestatie willen combineren met de beschikbare ISDE-subsidie.
            </p>

            <h3 style="font-size:20px;margin-bottom:14px;color:#1E5C2F;">Subsidie en financiering voor kozijnen in """ + stad + """</h3>
            <p style="color:#444;line-height:1.8;margin-bottom:22px;">
                """ + subsidie_lokaal + """ Via de <a href="financiering.html" style="color:#1E5C2F;font-weight:600;">ISDE-subsidieregeling</a> van de Rijksoverheid ontvang je bij HR++ glas &euro;25 per m² en bij triple glas tot &euro;111 per m² directe subsidie, dit wordt verrekend op je factuur. Combineer dit met de <strong>Energiebespaarlening</strong> van het Nationaal Warmtefonds: lenen van &euro;1.000 tot &euro;28.000, bij een verzamelinkomen tot &euro;60.000 volledig rentevrij. Zo financier je de investering met je eigen toekomstige energiebesparing.
            </p>

            <h3 style="font-size:20px;margin-bottom:14px;color:#1E5C2F;">Waarom offertes vergelijken in """ + stad + """?</h3>
            <p style="color:#444;line-height:1.8;margin-bottom:22px;">
                """ + markt + """ De prijs van kunststof kozijnen in """ + stad + """ varieert sterk per kozijnbedrijf, soms wel 20 tot 30% verschil voor hetzelfde product. Via 123KozijnenVergelijker ontvang je geheel vrijblijvend 3 offertes van gerenommeerde kozijnbedrijven actief in jouw regio. Zo weet je zeker dat je de beste prijs betaalt, zonder zelf uren te besteden aan het zoeken en vergelijken. Bekijk ook onze pagina's over <a href="kunststof-kozijnen.html" style="color:#1E5C2F;font-weight:600;">kunststof kozijnen</a>, <a href="kunststof-deuren.html" style="color:#1E5C2F;font-weight:600;">kunststof deuren</a> en <a href="kunststof-schuifpuien.html" style="color:#1E5C2F;font-weight:600;">kunststof schuifpuien</a> voor meer informatie over de opties.
            </p>

            <h3 style="font-size:20px;margin-bottom:14px;color:#1E5C2F;">Wat je mag verwachten van het proces</h3>
            <p style="color:#444;line-height:1.8;margin-bottom:22px;">
                Na je aanvraag via 123KozijnenVergelijker neemt een adviseur binnen 24 uur contact op. Je ontvangt vervolgens 3 gedetailleerde offertes op maat, inclusief kosten voor montage, afvoer van oude kozijnen en eventueel stucwerk. Onze adviseurs lopen het subsidietraject (ISDE via RVO) en de financieringsaanvraag (Nationaal Warmtefonds) met je door. Van eerste contact tot gemonteerde kozijnen duurt het gemiddeld 3 tot 6 weken. Bekijk onze <a href="projecten.html" style="color:#1E5C2F;font-weight:600;">gerealiseerde projecten</a> voor inspiratie en bewijs van onze werkwijze.
            </p>

            <h3 style="font-size:20px;margin-bottom:14px;color:#1E5C2F;">Onze garanties en kwaliteitsborging</h3>
            <p style="color:#444;line-height:1.8;margin-bottom:22px;">
                Alle kozijnen die via 123KozijnenVergelijker worden geplaatst, worden geleverd met <strong>20 jaar garantie</strong> op het kozijnprofiel en 10 jaar op het isolatieglas. We werken uitsluitend met VEKA-kwaliteitsprofielen en HR++ glas dat voldoet aan de huidige Rc-waarde-eisen. Er is geen aanbetaling vereist, je betaalt pas na volledige en correcte oplevering. In """ + stad + """ hebben we inmiddels tientallen woningeigenaren geholpen aan energiezuinige kozijnen. Lees wat klanten zeggen of <a href="offerte-vergelijken.html" style="color:#1E5C2F;font-weight:600;">vraag direct je offerte aan</a>.
            </p>

            <div class="stad-cta-blok">
                <div class="stad-cta-blok-tekst">
                    <h3>Klaar om te vergelijken in """ + stad + """?</h3>
                    <p>Ontvang geheel vrijblijvend <strong>3 offertes op maat</strong> van kozijnbedrijven actief in """ + stad + """ en omgeving. Geen aanbetaling, ISDE-subsidie geregeld en 20 jaar garantie.</p>
                    <div class="stad-cta-blok-usps">
                        <span>&#10003; Vrijblijvend</span>
                        <span>&#10003; Gratis</span>
                        <span>&#10003; Binnen 24 uur reactie</span>
                        <span>&#10003; Geen aanbetaling</span>
                    </div>
                </div>
                <div class="stad-cta-blok-acties">
                    <a href="https://123kozijnenvergelijker.nl/offerte-vergelijken#offerte-aanvragen" class="btn-primary btn-pulse">Vraag 3 gratis offertes aan</a>
                </div>
            </div>

        </div>
    </section>"""

    schema = """{
      "@context": "https://schema.org",
      "@type": "Service",
      "name": "Kunststof kozijnen """ + stad + """",
      "description": "Kunststof kozijnen laten plaatsen in """ + stad + """. Gratis offertes vergelijken, HR++ glas standaard, 20 jaar garantie.",
      "areaServed": {
        "@type": "City",
        "name": \"""" + stad + """\",
        "containedInPlace": {
          "@type": "State",
          "name": \"""" + provincie + """\"
        }
      },
      "provider": {
        "@type": "LocalBusiness",
        "name": "123KozijnenVergelijker.nl",
        "url": "https://www.123kozijnenvergelijker.nl",
        "telephone": "0541-23 52 22",
        "email": "info@123kozijnenvergelijker.nl",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Almelo",
          "addressRegion": "Overijssel",
          "addressCountry": "NL"
        },
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": "9.3",
          "reviewCount": "149"
        }
      },
      "offers": {
        "@type": "Offer",
        "description": "Gratis offertes aanvragen voor kunststof kozijnen in """ + stad + """",
        "price": "0",
        "priceCurrency": "EUR"
      }
    }"""

    return """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kunststof Kozijnen """ + stad + """ | Gratis 3 Offertes Vergelijken | 123KozijnenVergelijker.nl</title>
    <meta name="description" content="Kunststof kozijnen laten plaatsen in """ + stad + """? Vergelijk 3 gratis offertes, profiteer van ISDE-subsidie (tot &euro;111/m&sup2;) en 0% rente via Warmtefonds. HR++ standaard, 20 jaar garantie, geen aanbetaling.">
    <link rel="canonical" href="https://www.123kozijnenvergelijker.nl/kozijnen-""" + slug + """.html">
    <link rel="icon" href="favicon.svg" type="image/svg+xml">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <script type="application/ld+json">
""" + schema + """
    </script>
</head>
<body>

<header class="header">
    <div class="container header-inner">
        <div class="logo">
            <a href="index.html" style="text-decoration:none;">
                <span class="logo-123">123</span><span class="logo-kozijnen">kozijnen</span><span class="logo-verg">vergelijker</span><span class="logo-nl">.nl</span>
            </a>
        </div>
        <nav class="nav" id="navLinks">
            <a href="kunststof-kozijnen.html">Kozijnen</a>
            <a href="kunststof-deuren.html">Deuren</a>
            <a href="kunststof-schuifpuien.html">Schuifpuien</a>
            <a href="projecten.html">Projecten</a>
            <a href="financiering.html">Financiering</a>
            <a href="index.html#contact">Contact</a>
            <a href="offerte-vergelijken.html" class="btn-nav">3 Offertes vergelijken</a>
        </nav>
        <button class="hamburger" id="hamburger" aria-label="Menu openen" onclick="document.getElementById('navLinks').classList.toggle('open');this.classList.toggle('open')">
            <span></span><span></span><span></span>
        </button>
    </div>
</header>

<div class="container">
    <nav class="breadcrumb">
        <a href="index.html">Home</a>
        <span>&rsaquo;</span>
        <a href="kunststof-kozijnen.html">Kozijnen</a>
        <span>&rsaquo;</span>
        <span>Kozijnen """ + stad + """</span>
    </nav>
</div>

<section class="hero" style="background:linear-gradient(135deg,#1E5C2F 0%,#2d7a42 100%);padding:60px 0 50px;">
    <div class="container">
        <div style="max-width:700px;">
            <div class="hero-label" style="background:rgba(255,255,255,0.15);color:#fff;display:inline-block;padding:6px 14px;border-radius:20px;font-size:13px;font-weight:600;margin-bottom:16px;">
                &#128205; """ + stad + """ &middot; """ + provincie + """
            </div>
            <h1 style="font-size:clamp(28px,4.5vw,48px);font-weight:800;color:#fff;line-height:1.15;margin-bottom:16px;">
                Kunststof kozijnen laten plaatsen in """ + stad + """
            </h1>
            <p style="font-size:17px;color:rgba(255,255,255,0.88);line-height:1.65;margin-bottom:28px;max-width:600px;">
                Vergelijk vrijblijvend 3 offertes van kozijnbedrijven actief in """ + stad + """ en omgeving. HR++ glas standaard, ISDE-subsidie geregeld, geen aanbetaling en 20 jaar garantie.
            </p>
            <div style="display:flex;gap:12px;flex-wrap:wrap;">
                <a href="https://123kozijnenvergelijker.nl/offerte-vergelijken#offerte-aanvragen" class="btn-primary btn-pulse">Vraag 3 gratis offertes aan</a>
                <a href="#inhoud" class="btn-secondary">Meer informatie</a>
            </div>
            <div style="margin-top:24px;display:flex;gap:24px;flex-wrap:wrap;">
                <span style="color:rgba(255,255,255,0.8);font-size:13px;">&#11088; 9.3 gemiddeld (149 reviews)</span>
                <span style="color:rgba(255,255,255,0.8);font-size:13px;">&#10003; Geen aanbetaling</span>
                <span style="color:rgba(255,255,255,0.8);font-size:13px;">&#10003; 20 jaar garantie</span>
                <span style="color:rgba(255,255,255,0.8);font-size:13px;">&#10003; ISDE-subsidie geregeld</span>
            </div>
        </div>
    </div>
</section>

<div style="background:linear-gradient(135deg,#FF6500,#e85500);padding:14px 0;text-align:center;">
    <div class="container">
        <span style="color:#fff;font-weight:700;font-size:15px;">&#127873; Gratis horren bij aanvraag in maart &middot; Actie geldig t/m 31 maart 2026</span>
    </div>
</div>

<section style="background:#f8f9fa;padding:32px 0;" id="inhoud">
    <div class="container">
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;text-align:center;">
            <div>
                <div style="font-size:28px;font-weight:800;color:#FF6500;">523+</div>
                <div style="font-size:13px;color:#666;">Tevreden huishoudens</div>
            </div>
            <div>
                <div style="font-size:28px;font-weight:800;color:#FF6500;">20 jaar</div>
                <div style="font-size:13px;color:#666;">Garantie op kozijnen</div>
            </div>
            <div>
                <div style="font-size:28px;font-weight:800;color:#FF6500;">&euro;800-&euro;1.500</div>
                <div style="font-size:13px;color:#666;">Besparing per jaar</div>
            </div>
            <div>
                <div style="font-size:28px;font-weight:800;color:#FF6500;">9.3</div>
                <div style="font-size:13px;color:#666;">Gemiddeld cijfer</div>
            </div>
        </div>
    </div>
</section>

<section class="sectie sectie-licht">
    <div class="container">
        <div style="text-align:center;margin-bottom:48px;">
            <span class="sectie-tag">Kozijnen in """ + stad + """</span>
            <h2>Waarom kiezen voor nieuwe kozijnen in """ + stad + """?</h2>
            <p class="section-sub">Woningeigenaren in """ + provincie + """ besparen gemiddeld &euro;800 tot &euro;1.500 per jaar na plaatsing van nieuwe kozijnen</p>
        </div>
        <div class="voordelen-grid">
            <div class="voordeel-item">
                <div class="voordeel-icon">
                    <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="#1E5C2F" stroke-width="2" fill="#f0f6f1"/><path d="M13 20l5 5 9-10" stroke="#1E5C2F" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <h4>Lagere energierekening</h4>
                <p>HR++ glas isoleert tot 30% beter dan enkel glas. Bespaar &euro;800 tot &euro;1.500 per jaar op stookkosten in """ + stad + """.</p>
            </div>
            <div class="voordeel-item">
                <div class="voordeel-icon">
                    <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="#1E5C2F" stroke-width="2" fill="#f0f6f1"/><text x="20" y="26" text-anchor="middle" font-size="16" font-weight="800" fill="#1E5C2F" font-family="Arial">&euro;</text></svg>
                </div>
                <h4>Geen aanbetaling</h4>
                <p>Betalen pas na oplevering. 0% rente via Nationaal Warmtefonds bij inkomen tot &euro;60.000. ISDE-subsidie tot &euro;111/m&sup2;.</p>
            </div>
            <div class="voordeel-item">
                <div class="voordeel-icon">
                    <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="#1E5C2F" stroke-width="2" fill="#f0f6f1"/><path d="M20 12v8l5 3" stroke="#1E5C2F" stroke-width="2.5" stroke-linecap="round"/></svg>
                </div>
                <h4>Snel geregeld</h4>
                <p>Offerte binnen 24 uur. Kozijnbedrijven actief in """ + stad + """ plannen het gratis adviesgesprek bij jou thuis.</p>
            </div>
            <div class="voordeel-item">
                <div class="voordeel-icon">
                    <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="#1E5C2F" stroke-width="2" fill="#f0f6f1"/><path d="M20 8v2M20 30v2M8 20h2M30 20h2" stroke="#1E5C2F" stroke-width="2"/><circle cx="20" cy="20" r="6" fill="#1E5C2F"/></svg>
                </div>
                <h4>Subsidie geregeld</h4>
                <p>Via de ISDE-regeling ontvang je tot &euro;111 per m&sup2; subsidie op HR++ en triple glas. Wij begeleiden de aanvraag bij RVO.</p>
            </div>
        </div>
    </div>
</section>

<section class="sectie" style="background:#fff;">
    <div class="container">
        <div style="text-align:center;margin-bottom:48px;">
            <h2>Ons aanbod in """ + stad + """ en omgeving</h2>
            <p class="section-sub">Op maat gemaakt, inclusief HR++ glas, gratis horren en 20 jaar garantie</p>
        </div>
        <div class="producten-grid">
            <div class="product-cat">
                <div class="product-cat-img placeholder-green">
                    <svg class="prod-icon-svg" viewBox="0 0 64 64" fill="none"><rect x="6" y="8" width="52" height="48" rx="3" stroke="rgba(255,255,255,0.9)" stroke-width="3" fill="none"/><line x1="32" y1="8" x2="32" y2="56" stroke="rgba(255,255,255,0.6)" stroke-width="2"/><line x1="6" y1="32" x2="58" y2="32" stroke="rgba(255,255,255,0.6)" stroke-width="2"/></svg>
                    <span class="prod-title">Kunststof Kozijnen</span>
                </div>
                <div class="product-cat-body">
                    <h3><a href="kunststof-kozijnen.html" style="color:inherit;text-decoration:none;">Kunststof Kozijnen """ + stad + """</a></h3>
                    <p class="prod-desc">Op maat voor jouw woning in """ + stad + """. Onderhoudsvrij, 40 tot 60 jaar mee en HR++ glas altijd standaard inbegrepen.</p>
                    <ul class="prod-voordelen">
                        <li>HR++ isolatieglas standaard</li>
                        <li>200+ kleuren en structuren</li>
                        <li>20 jaar garantie</li>
                        <li>Gratis horren inbegrepen</li>
                    </ul>
                    <div class="product-cat-footer">
                        <a href="offerte-vergelijken.html" class="btn-primary btn-sm">Gratis offerte aanvragen</a>
                    </div>
                </div>
            </div>
            <div class="product-cat">
                <div class="product-cat-img placeholder-green">
                    <svg class="prod-icon-svg" viewBox="0 0 64 64" fill="none"><rect x="12" y="4" width="36" height="56" rx="3" stroke="rgba(255,255,255,0.9)" stroke-width="3" fill="none"/><circle cx="40" cy="32" r="3.5" fill="rgba(255,255,255,0.9)"/></svg>
                    <span class="prod-title">Kunststof Deuren</span>
                </div>
                <div class="product-cat-body">
                    <h3><a href="kunststof-deuren.html" style="color:inherit;text-decoration:none;">Kunststof Deuren """ + stad + """</a></h3>
                    <p class="prod-desc">Veiliger, stiller en energiezuiniger. RC2 inbraakwering en meerpuntssluiting standaard inbegrepen.</p>
                    <ul class="prod-voordelen">
                        <li>RC2 inbraakwering standaard</li>
                        <li>Uitstekende isolatie</li>
                        <li>Op maat gemaakt</li>
                        <li>20 jaar garantie</li>
                    </ul>
                    <div class="product-cat-footer">
                        <a href="offerte-vergelijken.html" class="btn-primary btn-sm">Gratis offerte aanvragen</a>
                    </div>
                </div>
            </div>
            <div class="product-cat">
                <div class="product-cat-img placeholder-green">
                    <svg class="prod-icon-svg" viewBox="0 0 64 64" fill="none"><rect x="4" y="8" width="56" height="48" rx="3" stroke="rgba(255,255,255,0.9)" stroke-width="3" fill="none"/><line x1="32" y1="8" x2="32" y2="56" stroke="rgba(255,255,255,0.6)" stroke-width="2"/></svg>
                    <span class="prod-title">Schuifpuien</span>
                </div>
                <div class="product-cat-body">
                    <h3><a href="kunststof-schuifpuien.html" style="color:inherit;text-decoration:none;">Schuifpuien """ + stad + """</a></h3>
                    <p class="prod-desc">Tot 6 meter breed, energiezuinig en RC2 beslag standaard. Verbind woonkamer met tuin.</p>
                    <ul class="prod-voordelen">
                        <li>HR++ glas standaard</li>
                        <li>Tot 6 meter breedte</li>
                        <li>RC2 inbraakwering</li>
                        <li>Lichte bediening</li>
                    </ul>
                    <div class="product-cat-footer">
                        <a href="offerte-vergelijken.html" class="btn-primary btn-sm">Gratis offerte aanvragen</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="sectie sectie-licht">
    <div class="container">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;">
            <div>
                <span class="sectie-tag">Financiering en subsidie</span>
                <h2>Kozijnen in """ + stad + """ financieren met 0% rente</h2>
                <p style="color:#555;line-height:1.7;margin-bottom:20px;">Via de <a href="financiering.html" style="color:#1E5C2F;font-weight:600;">Energiebespaarlening</a> van het Nationaal Warmtefonds leen je tot &euro;28.000 tegen 0% rente bij een verzamelinkomen tot &euro;60.000. Combineer dit met ISDE-subsidie tot &euro;111 per m&sup2; glas.</p>
                <ul style="list-style:none;padding:0;margin-bottom:28px;">
                    <li style="padding:8px 0;border-bottom:1px solid #eee;color:#444;">&#10003; &nbsp;0% rente bij verzamelinkomen tot &euro;60.000</li>
                    <li style="padding:8px 0;border-bottom:1px solid #eee;color:#444;">&#10003; &nbsp;Lening van &euro;1.000 tot &euro;28.000</li>
                    <li style="padding:8px 0;border-bottom:1px solid #eee;color:#444;">&#10003; &nbsp;ISDE-subsidie tot &euro;111 per m&sup2;</li>
                    <li style="padding:8px 0;color:#444;">&#10003; &nbsp;Wij begeleiden beide aanvragen</li>
                </ul>
                <a href="financiering.html" class="btn-primary">Meer over financiering</a>
            </div>
            <div style="background:#1E5C2F;border-radius:16px;padding:36px;color:#fff;">
                <div style="font-size:13px;font-weight:600;letter-spacing:1px;opacity:0.7;margin-bottom:16px;">REKENVOORBEELD """ + stad.upper() + """</div>
                <div style="font-size:15px;opacity:0.85;margin-bottom:8px;">Investering nieuwe kozijnen</div>
                <div style="font-size:32px;font-weight:800;margin-bottom:20px;">&euro; 12.000</div>
                <div style="background:rgba(255,255,255,0.1);border-radius:10px;padding:16px;margin-bottom:12px;">
                    <div style="font-size:13px;opacity:0.7;">Maandlast (120 mnd, 0% rente)</div>
                    <div style="font-size:24px;font-weight:700;color:#FF6500;">&euro; 100 / mnd</div>
                </div>
                <div style="font-size:13px;opacity:0.75;">Terwijl jij al snel &euro;800 tot &euro;1.500 per jaar bespaart op je energierekening.</div>
            </div>
        </div>
    </div>
</section>

<section class="sectie" style="background:linear-gradient(135deg,#1E5C2F 0%,#2d7a42 100%);text-align:center;">
    <div class="container" style="max-width:700px;">
        <h2 style="color:#fff;font-size:clamp(24px,3.5vw,38px);margin-bottom:16px;">Vergelijk offertes van kozijnbedrijven in """ + stad + """</h2>
        <p style="color:rgba(255,255,255,0.85);font-size:16px;margin-bottom:32px;line-height:1.65;">
            Vul het formulier in en ontvang geheel vrijblijvend 3 offertes van gerenommeerde bedrijven in jouw buurt. Gratis, snel en zonder verplichtingen.
        </p>
        <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-bottom:24px;">
            <a href="https://123kozijnenvergelijker.nl/offerte-vergelijken#offerte-aanvragen" class="btn-primary btn-pulse" style="font-size:17px;padding:16px 32px;">Vraag 3 gratis offertes aan</a>
            <a href="index.html#contact" class="btn-secondary">Direct contact</a>
        </div>
        <div style="display:flex;gap:20px;justify-content:center;flex-wrap:wrap;">
            <span style="color:rgba(255,255,255,0.75);font-size:13px;">&#10003; Vrijblijvend</span>
            <span style="color:rgba(255,255,255,0.75);font-size:13px;">&#10003; Gratis</span>
            <span style="color:rgba(255,255,255,0.75);font-size:13px;">&#10003; Binnen 24 uur reactie</span>
            <span style="color:rgba(255,255,255,0.75);font-size:13px;">&#10003; Geen aanbetaling</span>
        </div>
    </div>
</section>

""" + seo_content + """

<section class="sectie sectie-licht">
    <div class="container" style="max-width:800px;">
        <h2 style="text-align:center;margin-bottom:40px;">Veelgestelde vragen over kozijnen in """ + stad + """</h2>
        <div class="faq-list">
            <div class="faq-item">
                <button class="faq-vraag" onclick="toggleFaq(this)">
                    Wat kost het laten plaatsen van kunststof kozijnen in """ + stad + """?
                    <span class="faq-icon">+</span>
                </button>
                <div class="faq-antwoord">
                    <p>De kosten voor kunststof kozijnen in """ + stad + """ hangen af van het aantal kozijnen, de maten en het glastype. Een standaard tussenwoning rekent gemiddeld &euro;8.000 tot &euro;18.000 voor een volledige vervanging inclusief HR++ glas en montage. Via <a href="offerte-vergelijken.html" style="color:#1E5C2F;">onze vergelijker</a> ontvang je 3 vrijblijvende offertes voor de beste prijs in """ + stad + """.</p>
                </div>
            </div>
            <div class="faq-item">
                <button class="faq-vraag" onclick="toggleFaq(this)">
                    Kan ik ISDE-subsidie krijgen voor kozijnen in """ + stad + """?
                    <span class="faq-icon">+</span>
                </button>
                <div class="faq-antwoord">
                    <p>Ja. Via de ISDE-regeling van de Rijksoverheid ontvang je bij HR++ glas &euro;25 per m&sup2; en bij triple glas tot &euro;111 per m&sup2; directe subsidie. Bij een gemiddelde tussenwoning (circa 12 m&sup2; glas) is dat al snel &euro;300 tot &euro;1.300 subsidie. Wij verzorgen de aanvraag bij RVO namens jou. Meer informatie via onze <a href="financiering.html" style="color:#1E5C2F;">financieringspagina</a>.</p>
                </div>
            </div>
            <div class="faq-item">
                <button class="faq-vraag" onclick="toggleFaq(this)">
                    Wat is de terugverdientijd van kozijnen in """ + stad + """?
                    <span class="faq-icon">+</span>
                </button>
                <div class="faq-antwoord">
                    <p>De gemiddelde terugverdientijd van kunststof kozijnen is 10 tot 12 jaar. Met ISDE-subsidie kan dat dalen tot 9 tot 10 jaar. Kozijnen gaan 35 tot 50 jaar mee, dus daarna is het puur rendement. Via de Energiebespaarlening (0% rente bij inkomen tot &euro;60.000) zijn je maandlasten direct lager dan je energiebesparing.</p>
                </div>
            </div>
            <div class="faq-item">
                <button class="faq-vraag" onclick="toggleFaq(this)">
                    Hoe lang duurt de plaatsing van kozijnen in """ + stad + """?
                    <span class="faq-icon">+</span>
                </button>
                <div class="faq-antwoord">
                    <p>De plaatsing in een gemiddelde woning in """ + stad + """ duurt 1 tot 3 werkdagen. Na het gratis adviesgesprek aan huis wordt de levertijd ingepland, gemiddeld 3 tot 6 weken na opdracht. Bekijk onze <a href="projecten.html" style="color:#1E5C2F;">gerealiseerde projecten</a> voor een indruk van onze werkwijze.</p>
                </div>
            </div>
            <div class="faq-item">
                <button class="faq-vraag" onclick="toggleFaq(this)">
                    Heb ik een vergunning nodig voor nieuwe kozijnen in """ + stad + """?
                    <span class="faq-icon">+</span>
                </button>
                <div class="faq-antwoord">
                    <p>In de meeste gevallen niet. Bij vervanging in dezelfde maat en stijl is een omgevingsvergunning doorgaans niet nodig (vergunningsvrij bouwen). Bij monumentale panden in """ + stad + """ of bij wijziging van de gevelindeling kan een vergunning vereist zijn. Wij adviseren je hier gratis over tijdens het adviesgesprek aan huis.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="sectie" style="background:#fff;">
    <div class="container">
        <h2 style="text-align:center;margin-bottom:8px;">Wat klanten zeggen</h2>
        <p class="section-sub" style="text-align:center;margin-bottom:40px;">&#11088;&#11088;&#11088;&#11088;&#11088; Gemiddeld 9.3 op basis van 149 beoordelingen</p>
        <div class="reviews-grid">
            <div class="review-item">
                <div class="review-stars">&#11088;&#11088;&#11088;&#11088;&#11088;</div>
                <p>"Drie offertes ontvangen, de beste was 20% goedkoper dan wat ik zelf had gevonden. Heel tevreden met het resultaat en de begeleiding van begin tot eind."</p>
                <strong>Sandra K., """ + stad + """</strong>
            </div>
            <div class="review-item">
                <div class="review-stars">&#11088;&#11088;&#11088;&#11088;&#11088;</div>
                <p>"ISDE-subsidieaanvraag volledig verzorgd. Kozijnen er nu 6 weken in en het huis is merkbaar warmer, stiller en minder tochtig. Absoluut een aanrader."</p>
                <strong>Peter V., """ + provincie + """</strong>
            </div>
            <div class="review-item">
                <div class="review-stars">&#11088;&#11088;&#11088;&#11088;&#11088;</div>
                <p>"Snel geregeld, netjes gemonteerd en de horren zaten er gratis bij. Energierekening al direct omlaag na de eerste maand. Uitstekende service."</p>
                <strong>M. de Boer, """ + stad + """</strong>
            </div>
        </div>
    </div>
</section>

<footer class="footer">
    <div class="container footer-inner">
        <div class="footer-logo">
            <span class="logo-123">123</span><span class="logo-kozijnen">kozijnen</span><span class="logo-verg">vergelijker</span><span class="logo-nl">.nl</span>
            <p>Kozijnen vergelijken &amp; laten plaatsen<br>Almelo &middot; Haarlem &middot; Bathmen</p>
        </div>
        <div class="footer-links">
            <h5>Producten</h5>
            <a href="kunststof-kozijnen.html">Kunststof kozijnen</a>
            <a href="kunststof-deuren.html">Kunststof deuren</a>
            <a href="kunststof-schuifpuien.html">Schuifpuien</a>
        </div>
        <div class="footer-links">
            <h5>Informatie</h5>
            <a href="over-ons.html">Over ons</a>
            <a href="projecten.html">Projecten</a>
            <a href="financiering.html">Financiering</a>
            <a href="blog.html">Blog</a>
            <a href="offerte-vergelijken.html">Offertes vergelijken</a>
        </div>
        <div class="footer-contact">
            <h5>Contact</h5>
            <p>info@123kozijnenvergelijker.nl</p>
            <p>0541-23 52 22</p>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; 2026 123KozijnenVergelijker.nl &middot; <a href="privacyverklaring.html">Privacyverklaring</a> &middot; <a href="algemene-voorwaarden.html">Algemene voorwaarden</a></p>
    </div>
</footer>

<script>
function toggleFaq(btn) {
    btn.classList.toggle('open');
    btn.nextElementSibling.classList.toggle('open');
}
</script>

</body>
</html>"""

output_dir = "C:/Users/knusl/Downloads/kozijnstunter"
generated = []
for s in steden:
    filename = "kozijnen-" + s["slug"] + ".html"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(make_page(s))
    generated.append(filename)

print("Aangemaakt: " + str(len(generated)) + " paginas")
for f in generated:
    print("  " + f)
