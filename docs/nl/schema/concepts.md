# Algemene concepten

## Level of Detail (LoD)

Alle modellen zijn abstracties van de werkelijkheid. Sommige komen dichter bij het werkelijke, andere minder. In 3D GIS geeft het Level of Detail (LoD) van een 3D model aan welke mate van detail in het model is opgenomen.

Neem bijvoorbeeld een zeer simpel gebouw met vier hoeken en een puntdak. Een ruwe benadering van dit gebouw is een kubus. Dit terwijl we aan de andere kant ook individuele oppervlakken in het model kunnen hebben, die de vorm van het gebouw exact volgen, waarbij elk van deze gelabeld is met aanvullende informatie zoals het oppervlaktype, het materiaal et cetera.

Hogere LoDs (vanaf LoD2) kunnen de oppervlakken van het model labelen, gebaseerd op hun functie in het echte object. Deze labels heten *semantiek*, en derhalve noemen we gelabelde oppervlakken **semantische oppervlakken**. In het geval van gebouwmodellen spreken we bijvoorbeeld over een *grondoppervlak*, *muuroppervlak*, *dakoppervlak*, enzovoort.

In de 3D BAG gebruiken we de zogenaamde [*verbeterde LoD-specificatie*](http://doi.org/10.1016/j.compenvurbsys.2016.04.005), welke in de onderstaande figuur getoond wordt.

<figure>
  <img src="https://3d.bk.tudelft.nl/lod/lodtud.png" />
  <figcaption><b>An improved LOD specification for 3D building models.</b> Filip Biljecki, Hugo Ledoux, and Jantien Stoter. Computers, Environment and Urban Systems, 59: 25–37, 2016. <a href="http://doi.org/10.1016/j.compenvurbsys.2016.04.005">DOI</a></figcaption>
</figure>

Voor de 3D BAG zijn de relevante LoDs 1.2, 1.3 en 2.2. Merk op dat behalve het verschil in de mate van geometrische details, een belangrijk verschil tussen LoD1 en LoD2 de aanwezigheid van *semantische oppervlakken* is. Deze informatie zorgt er bijvoorbeeld voor dat dak- en muuroppervlakken respectievelijk rood en grijs gevisualiseerd kunnen worden. Verder is het verschil tussen LoD1.2 en LoD 1.3 dat laatstgenoemde onderscheid heeft tussen significante hoogteverschillen binnen een gebouw, terwijl het hele gebouw in LoD1.2 een uniforme hoogte heeft.

<!-- difficulties of modelling buildings in diff lod-s -->

<!-- highest lod is not always the best -->

## 3D geometrische primitieven

In 2D GIS kan de geometrie van objecten worden gerepresenteerd door *punten*, *lijnen*, *polygonen* en hun variaites. Er zijn standaarden die een verzameling regels voorschrijven voor deze primitieven, zodat data uitgewisseld kan worden op interoperabele wijze (bijvoorbeeld [Simple Feature Access](https://www.ogc.org/standards/sfa)).

Voor 3D GIS moeten deze geometrische primitieven en de bijbehorende regels uitgebreid worden naar de derde dimensie, zodat hun interacties op een betekenisvolle manier beschreven kunnen worden. De onderstaande figuur geeft een overzicht van de veelgebruikte primitieven in 3D GIS.

<figure>
  <img src="https://val3dity.readthedocs.io/en/latest/_images/geomprimitives.svg" />
  <figcaption>3D primitieven waar val3dity mee omgaat. Zie: <b>Val3dity: validation of 3D GIS primitives according to the international standards.</b> Hugo Ledoux. Open Geospatial Data, Software and Standards 3 (1), 2018, pp. 1. <a href="http://dx.doi.org/10.1186/s40965-018-0043-x">DOI</a></figcaption>
</figure>

<!-- I am unsure if there is a proper Dutch translation for Solid -->

Voor de 3D BAG is de meest relevante primitief de [Solid](https://val3dity.readthedocs.io/en/latest/definitions/#solid), aangezien we gebouwmodellen als zodanig beschouwen. Dit onderscheid is belangrijk omdat er andere regels voor Solids gelden, ten opzichte van andere 3D primitieven.

!!! note "3D primitieven en dataformaten"
    Niet ieder dataformaat ondersteunt de bovengenoemde 3D primitieven. Dat is eigenlijk zo voor al onze exportformaten, behalve CityJSON. Daarom gebruiken we in deze andere formaten de geometrietypes die meest gelijkwaardig zijn aan Solids. De PostgreSQL backup is hierbij een beetje een bijzonder geval, daar PostGIS technisch gezien Solids kan opslaan, maar alleen met de [SFCGAL-extensie](http://www.sfcgal.org/). Om het inladen van de PostgreSQL backup zo makkelijk mogelijk te maken, slaan we de 3D geometrieën op als `MultiPolygonZ`.

## Valide 3D geometrieën

De validiteit van geometrieën is belangrijk voor het gebruik van de data bij verschillende toepassingen. Standaarden helpen bij het definiëren van een algemene verzameling van regels waar zowel data-ontwikkelaars als -consumenten zich aan kunnen houden bij het werken met data. [val3dity](https://val3dity.readthedocs.io/en/latest/) is een software die 3D primitieven valideert aan de hand van de international standaard ISO19107.

We hebben val3dity in ons proces geïntegreerd, waarmee we ieder 3D model valideren na reconstructie. De gebouwmodellen worden echter individueel gevalideerd tijdens het reconstructieproces, waardoor we geen fouten kunnen detecteren in de interactie tussen verschillende modellen (foutcodes boven de 500).

!!! note "val3dity_codes"
    Het attribuut [`val3dity_codes`](attributes.md#val3dity_codes) geeft de foutcode van een model aan als deze invalide is.

<figure>
  <img src="https://val3dity.readthedocs.io/en/latest/_images/errorcodes.png" />
  <figcaption>val3dity foutcodes. Zie <a href="https://val3dity.readthedocs.io/en/latest/errors/">de volledige omschrijving van iedere code</a> in de documentatie van val3dity.</figcaption>
</figure>


