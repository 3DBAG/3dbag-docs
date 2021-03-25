# Algemeen overzicht

Welkom bij de documentatie van de 3D BAG door de 3D geoinformation groep! De 3D BAG is de eerste open dataset met 3D gebouwmodellen op dit detailniveau die volledig automatisch is gegenereerd.

Op deze pagina vind je algemene informatie over de 3D BAG en hoe deze is ontwikkeld, een aantal praktische toepassingen waarvoor de data gebruikt kan worden en hoe de 3D BAG in relatie staat tot andere Nederlandse datasets.

- [Databronnen](overview/sources.md) beschrijft welke (delen van) andere datasets gebruikt zijn om de 3D BAG te ontwikkelen.
- [Schema](schema/concepts.md) geeft gedetailleerde informatie over de structuur van de 3D BAG.
- [Dataformaten](delivery/webservices.md) geeft uitleg over de formaten waarin de 3D BAG beschikbaar is en hoe deze gebruikt kunnen worden.
- [Gebruiksvoorwaarden](copyright.md) legt uit aan welke voorwaarden gebruikers van de 3D BAG moeten voldoen.
- [Contact](contact.md) geeft aan waar je vragen kunt stellen en hoe je ons kan contacteren voor andere opmerkingen.
- En in de [Viewer](https://3dbag.nl) kun je de 3D BAG zien vanuit je browser!

## Wat is de 3D BAG?

De 3D BAG is een up-to-date landsdekkende dataset met 3D gebouwmodellen van Nederland. De 3D BAG is open data. Het bevat 3D modellen op verscheidene detailniveaus welke zijn gegenereerd door de combinatie van twee open datasets: de pand-gegevens uit de [BAG](overview/sources.md#BAG) en de hoogtegegevens uit de [AHN](overview/sources.md#AHN). De 3D BAG wordt regelmatig geüpdatet met de meest recente openlijk beschikbare pand- en hoogtegegevens.

De 3D BAG is eveneens een plek voor experimenten. We gebruiken de data zelf ook om nieuwe ideeën te testen in onderzoek en onderwijs binnen de 3D geoinformation onderzoeksgroep. Gebaseerd op ervaringen met de data verbeteren we constant onze methoden, en door onze eigen service te ontwikkelen en in beheer te houden, behouden we de volledige controle over het gehele proces van invoerdata, voorbewerking en reconstructie tot querying en het gebruik van de gereconstrueerde 3D data voor stedelijke toepassingen.

## Belangrijkste kenmerken

- **Drie [levels of detail](schema/concepts.md#level-of-detail-lod)**.
Kies de meest geschikte LoD voor je toepassing: LoD1.2, LoD1.3 of LoD2.2.
- **Zowel 2D als 3D**.  
Naast de 3D modellen bieden we ook 2D projecties van de dakvormen met bijgevoegde hoogtereferenties aan.
- **Ondergrondse en met elkaar overlappende panden/panddelen niet meegenomen**. 
Zowel volledig ondergrondse als overlappende panden (wanneer een pand boven een ander zweeft) zijn niet meegenomen in de reconstructie. Van panden met delen onder het maaiveld zijn de ondergrondse delen afgesneden.
- **Terugval op simpele modellen bij problematische invoer**.
De punten van panden met glazen daken, voornamelijk kassen, zijn inconsistent in het AHN. Voor deze panden die doorgaans een zeer simpele vorm hebben, vallen we terug op een versimpeld 3D model om alsnog bruikbare modellen te verkrijgen, ook op hogere detailniveaus.
- **Geïntegreerde kwaliteitscontrole**.  
Tijdens het reconstructieproces worden alle 3D modellen gevalideerd met [val3dity](https://github.com/tudelft3d/val3dity) zodat je de 3D data niet zelf hoeft te valideren.
- **Beschikbaar in verscheidene formaten**.  
CityJSON, GeoPackage, Wavefront OBJ, PostgreSQL, WMS en WFS.

## Belangrijke toepassingen

Een aantal toepassingen van de dataset waar wij van weten:

- Toepassingen gerelateerd aan het energieverbruik in panden, zoals het voorspellen daarvan, retrofitkosten bepalen en geschikte daken identificeren voor zonnepanelen.
- Het simuleren van windstromen en de verspreiding van vervuilende stoffen in stedelijke gebieden (bijvoorbeeld [Simwind](https://3d.bk.tudelft.nl/projects/simwind/))
- Het berekenen van geluidsbelasting ten gevolge van verkeerslawaai (bijvoorbeeld [3D Noise](https://3d.bk.tudelft.nl/projects/noise3d/))
- Het analyseren van de stedelijke structuur en het evalueren van nieuwe stedelijke ontwikkelingen.

Heb je de 3D BAG gebruikt voor een interessante toepassing? [We horen er graag over!](contact.md)

<!-- this would fit under the LoD section at the Concepts -->
<!-- Het gewenste detailniveau waarin gebouwen gemodelleerd zijn hangt af van de data-eisen voor een specifieke toepassing. Een hogere LoD representeert de werkelijkheid beter, maar is ook complexer (en daarom duurder) om in te winnen en bij te houden. Daarnaast leidt een hogere LoD niet altijd tot betere resultaten, terwijl te veel detail een negatieve invloed kan hebben op de uitvoertijd van analyses en op de complexiteit van het implementeren daarvan. Het is daarom belangrijk om de juiste keuze te maken tussen de verschillende datasets die we aanbieden. -->

## Relatie tot andere datasets

### 3D Basisvoorziening

De [3D Basisvoorziening](https://www.pdok.nl/3d-basisvoorziening) is een verzameling van Nederlandse 3D datasets die gemaakt zijn in een samenwerking tussen het Kadaster en de 3D geoinformation onderzoeksgroep. De voorziening is beschikbaar gesteld in de zomer van 2020. Waar de 3D BAG zich beperkt tot 3D modellen van gebouwen uit de BAG, wordt in de 3D Basisvoorziening naast de BAG ook de Basisregistratie Grootschalige Topografie (BGT) meegenomen voor het modelleren van terreinobjecten in 3D. De 3D BAG bevat derhalve uitsluitend panden, terwijl de 3D Basisvoorziening een waterdicht 3D model van het hele land is, inclusief het terrein. Daarnaast gebruikt de 3D BAG alleen het AHN als hoogtebron, terwijl de 3D Basisvoorziening behalve het AHN ook een jaarlijks geüpdatete puntenwolk verkregen uit stereobeelden (van [Beeldmateriaal Nederland](https://www.beeldmateriaal.nl/)) gebruikt. Zowel de stereobeelden als de puntenwolk die eruit verkregen wordt zijn geen open data.

De tools en algoritmen die zijn gebruikt voor het genereren van de 3D Basisvoorziening zijn door de 3D geoinformation groep gemaakt. In feite zijn de LoD1.3 modellen in de 3D Basisvoorziening gegenereerd met een vorige, meer stabiele versie van dezelfde algoritmen die we gebruiken in de 3D BAG. Sindsdien hebben we het reconstructieproces verbeterd vooral gericht op een betere LoD2.2 reconstructie.

<!-- Jantien would leave the commented part underneath out, as she commented in the English version of this text. I wrote too many details, the focus should be on 3D BAG. -->

<!-- De gebouwen uit de BAG worden gebruikt in de 3D Basisvoorziening omdat de hoogtedata ingewonnen worden vanuit de lucht, en BAG-panden ook gebaseerd zijn op het bovenaanzicht van gebouwen. Deze kunnen dus accurater gereconstrueerd worden dan BGT-voetafdrukken, die gebaseerd zijn op het maaiveld. De panden uit de BAG sluiten echter niet perfect aan op de BGT, en daarom <a href=https://docs.geostandaarden.nl/3dbv/prod/#voorbewerking-van-bag-en-bgt>vindt er een voorbewerking</a> plaats om de twee datasets op elkaar aan te sluiten en ervoor te zorgen dat het resulterende 3D-model waterdicht is. -->

### 3D omgevingsmodel voor geluid

Het [3D omgevingsmodel voor geluid](https://www.pdok.nl/3d-input-data-voor-geluidssimulaties-versie-0.3.1) is gecreëerd in samenwerken met het RIVM, Rijkswaterstaat, Interprovinciaal Overleg, Kadaster en de 3D geoinformation onderzoeksgroep.

Zowel het 3D omgevingsmodel voor geluid als de 3D BAG gebruiken de BAG als basis voor de panden. Waar de 3D BAG uitsluitend het AHN gebruikt, is de 3D geluidsdata uitgebreid met LoD1.2 modellen die zijn gegenereerd met de actuele puntenwolk van het Kadaster voor panden die nieuwer zijn dan het AHN.

Naast gebouwmodellen, bevat de 3D geluidsdata twee aanvullende lagen, zowel voor de hoogte van het terrein als de geluidabsorptiewaarden van bodemvlakken. De gebouwmodellen in het 3D omgevingsmodel voor geluid zijn gemodelleerd als LoD1.3 modellen en in 2D beschikbaar (met de hoote-informatie als attribuutwaarden) omdat de huidige software voor geluidssimulatie alleen 2D gebouwen (+ hoogteattributen) ondersteunt.

## Toekomstplannen

- Een van de meest gewilde informatie gerelateerd aan pandhoogten is het exacte aantal verdiepingen in een pand. De bepaling hiervan blijkt ingewikkelder te zijn dan het standaard opdelen van de pandhoogte door een gemiddelde verdiepingshoogte (bijvoorbeeld 3 meter). We hebben momenteel dan ook een [een lopend MSc-onderzoek](https://3d.bk.tudelft.nl/education/#theses) over dit onderwerp.
- Adressen. Op dit moment voegen we de adressen uit de BAG niet toe aan de 3D BAG. Mogelijk zullen we dit in de toekomst wel doen.
- Orientatie van dakvlakken. In de viewer is het al mogelijk om de orientatie per dakvlak op te vragen. In de toekomst zullen we dit mogelijk als attribuut opslaan zodat deze informatie gebruikt kan worden in analyses, bijvoorbeeld bij het bepalen van de potentie van zonnepanelen.

## Financiering

![erc_logo](../images_common/erc_logo_small.png){ align=left } 

*Dit project heeft financiering ontvangen van de Europese Commissie (ERC) onder het European Unions Horizon2020 Research & Innovation Programme (grant agreement no. 677312 UMnD: Urban modelling in higher dimensions)*

