# Algemeen

Welkom bij de documentatie van de vernieuwde 3D BAG 2.0. De nieuwe data zijn beter dan ooit tevoren. Met automatisch gereconstrueerde dakvormen is het de eerste open 3D dataset op dit detailniveau!

Op deze pagina vind je algemene informatie over wat de 3D BAG is en hoe deze ontwikkeld is, voor welke praktische toepassing het gebruikt kan worden en hoe het in relatie staat tot andere datasets.

- <a href=/nl/overview/sources>Databronnen</a> beschrifjt welke (delen van) andere datasets gebruikt zijn om de 3D BAG te ontwikkelen.
- <a href=nl/schema/concepts/>Schema</a> geeft gedetailleerde informatie over de data.
- <a href=nl/delivery/webservices/>Datalevering</a> geeft uitleg over de formaten waarin de 3D BAG beschikbaar is en hoe deze gebruikt kunnen worden.
- <a href=nl/terms/>Gebruiksvoorwaarden</a> legt uit aan welke voorwaarden gebruikers van de 3D BAG moeten voldoen.
- <a href=nl/contact/>Contact</a> geeft aan hoe je ons kan contacteren voor vragen en andere opmerkingen.
- En in de <a href=https://3dbag.nl/>Viewer</a> kan je de 3D BAG zien vanuit je browser!

## Wat is de 3D BAG?

De 3D BAG omvat landsdekkende datasets met 3D geometrieën van Nederlandse gebouwen, gemodelleerd in verschillende detailniveaus. Deze zijn gecreëerd uit twee belangrijke datasets: de BAG en het AHN. De nieuwe versie is een doorontwikkeling van de 3D BAG 1.0, die slechts één detailniveau bevatte. Het is ons nu gelukt om ook dakvormen volledig automatisch te modelleren (<a href="https://3d.bk.tudelft.nl/lod/">LoD2.2</a>)!

De Basisregistratie Adressen en Gebouwen (BAG) is de meest gedetailleerde en open beschikbare dataset van gebouwen en adressen in Nederland. Het bevat informatie over ieder adres in een gebouw, zoals het huidige gebruik, constructiedatum of registratiestatus. De (2D) geometrieën in de BAG representeren de voetafdrukken van gebouwen als genomen van het bovenaanzicht.

Het Actueel Hoogtebestand Nederland (AHN) is het openlijk beschikbare digitale hoogtemodel van Nederland. Vanuit de lucht worden door middel van LiDAR-metingen precieze en gedetailleerde hoogtegegevens ingewonnen, resulterend in een dataset met gemiddeld 8 punten per vierkante meter.

Door de voetafdrukken van de BAG te combineren met de hoogtedata uit de AHN kunnen deze opgetrokken worden tot 3D modellen, en zo onstaat de 3D BAG.

## Dataomschrijving

Onderstaand een opsomming van de belangrijkste punten van de data:

- **Drie <a href="https://3d.bk.tudelft.nl/lod/">detailniveaus (LoDs)</a>**  
De vernieuwde 3D BAG omvat drie verschillende LoDs: LoD1.2, LoD1.3 en LoD2.2, ten opzichte van de vorige versie van de 3D BAG die alleen LoD1-modellen bevatte.
- **Zowel 2D als 3D**  
Naast de 3D-modellen stelt de 3D BAG de data ook beschikbaar met 2D geometrieën. Dat zijn de originele BAG-polygonen met hoogte-informatie in de attributen.
- **Kassen en warenhuizen**  
Deze zijn gemarkeerd in de BAG en uitsluitend gereconstrueerd in LoD2.2.
- **Ondergrondse en met elkaar overlappende gebouwen**  
Deze zijn eveneens gemarkeerd in de BAG, maar niet gereconstrueerd.
- **Onder- en bovengrondse gebouwdelen**  
De voetafdrukken uit de BAG zijn opgedeeld in bovengrondse delen, zoals een staande constructie, en delen die ondergronds danwel de grond (maaiveld) zelf zijn. We nemen alleen de bovengrondse delen mee voor de LoD1.3 en LoD2.2 reconstructie.
- **CityJSON, GeoPackage, WFS, WMS en PostgreSQL**  
Dit zijn de formaten waarin de data beschikbaar gesteld is.
- **Tegels**  
De data zijn opgedeeld in tegels, zodat deze niet meteen voor het hele land gedownload hoeven te worden. Tenzij je dat wel wil: daarvoor is er de PostgreSQL dump beschikbaar.
- **Aanvullende kwaliteitsstatistieken**  
We bepalen verscheidene statistische waarden die de kwaliteit van de reconstructie aanduiden. 

## Belangrijke toepassingen

3D stadsmodellen worden steeds beter en gebouwen zijn hier prominente objecten in. Behalve voor visualiseringsdoeleinden kan de 3D BAG ook gebruikt worden voor verschillende soorten analyses.

Het gewenste detailniveau waarin gebouwen gemodelleerd zijn hangt af van de data-eisen voor een specifieke toepassing. Een hogere LoD representeert de werkelijkheid beter, maar is ook complexer (en daarom duurder) om in te winnen en bij te houden. Daarnaast leidt een hogere LoD niet altijd tot betere resultaten, terwijl te veel detail een negatieve invloed kan hebben op de uitvoertijd van analyses en de complexiteit van het implementeren daarvan. Het is derhalve belangrijk om de juiste keuze te maken tussen de verschillende datasets die we aanbieden.

<a href=https://www.mdpi.com/2220-9964/4/4/2842/pdf>Dit paper van Biljecki, Stoter, Ledoux, Zlatanova, & Çöltekin (2015)</a> (op pagina 2851) geeft een overzicht van toepassingen van 3D stadsmodellen. Een aantal belangrijke waar LoD1 nuttig is zijn geluidssimulaties, schaduw- en wind-analyses. LoD2 kan dankzij de dakvormen bijvoorbeeld gebruikt worden voor het bepalen van de potentie van zonnepanelen, én is een stap naar LoD3.

Heb je de 3D BAG gebruikt voor een interessante toepassing? [We horen er graag over!](/nl/contact)

## Relatie tot andere datasets

### 3D Basisvoorziening

<a href=https://www.pdok.nl/3d-basisvoorziening>De 3D Basisvoorziening</a> omvat eveneens nationale 3D-datasets en is door samenwerking van het Kadaster en de 3D Geoinformation groep (TU Delft) beschikbaar gesteld in de zomer van 2020. Waar de gebruikte voetafdrukken voor de 3D BAG uitsluitend uit de BAG komen, wordt in de 3D Basisvoorziening naast de BAG ook de Basisregistratie Grootschalige Topografie (BGT) meegenomen. In de 3D BAG worden dus uitsluitend gebouwen gemodelleerd, en in de 3D Basisvoorziening wordt de BAG gecombineerd met andere topografische objecten uit de BGT, resulterend in een waterdicht 3D-model van Nederland. Daarnaast gebruikt de 3D Basisvoorziening behalve het AHN ook een puntenwolk gegenereerd uit stereofoto's van <a href=https://www.beeldmateriaal.nl/>Beeldmateriaal Nederland</a> voor de reconstructie, aangezien deze jaarlijks opnieuw ingewonnen wordt in tegenstelling tot het AHN.

In de 3D Basisvoorziening zijn de gebouwen gemodelleerd in LoD1.3. Verder maakt de 3D BAG geen gebruik van de puntenwolk van Beeldmateriaal Nederland naast het AHN omdat dit geen open data zijn. De 3D Basisvoorziening kan gebruikt worden voor extra toepassingen die meer objecttypen nodig hebben dan gebouwen, zoals afwateringsberekeningen.

De gebouwen uit de BAG worden gebruikt in de 3D Basisvoorziening omdat de hoogtedata ingewonnen worden vanuit de lucht, en BAG-panden ook gebaseerd zijn op het bovenaanzicht van gebouwen. Deze kunnen dus accurater gereconstrueerd worden dan BGT-voetafdrukken, die gebaseerd zijn op het maaiveld. De panden uit de BAG sluiten echter niet perfect aan op de BGT, en daarom <a href=https://docs.geostandaarden.nl/3dbv/prod/#voorbewerking-van-bag-en-bgt>vindt er een voorbewerking</a> plaats om de twee datasets op elkaar aan te sluiten en ervoor te zorgen dat het resulterende 3D-model waterdicht is. 

De tools en algoritmen die we ontwikkelen voor de 3D Basisvoorziening worden ook gebruikt voor de 3D BAG. In zekere zin borduurt de 3D BAG dus voort op de 3D Basisvoorziening, aangezien we constant bezig zijn met het experimenteren met en verbeteren van onze methoden. Doordat we de data van de 3D BAG zelf bijhouden en beschikbaarstellen houden we de volledige controle over het proces en kunnen we gemakkelijk verbeteringen doorvoeren. Het duurt even voordat deze verbeteringen doorgevoerd kunnen worden in de 3D Basisvoorziening (als dat in de toekomst gebeurt), ook omdat het extra werk vereist.

### 3D Geluid



