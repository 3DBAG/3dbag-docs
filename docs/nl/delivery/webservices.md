De webservices geven de mogelijkheid om in de vorm van een URL exact te specificeren welke 3D BAG gebouwen je wil downloaden. Alle belangrijke GIS-software heeft ondersteuning voor deze services.

Van de 3D BAG bieden we de [2D lagen](../schema/layers.md#data-layers) aan, en de tegelset die we gebruiken voor het verspreiden van de data in de verschillende formaten.

### WFS

<a href=https://www.ogc.org/standards/wfs>Web Feature Service (WFS)</a> is een OGC-standaard die beschrijft hoe geografische vectordata opgevraagd, gecreëerd en bewerkt kan worden via internet.

<figure>
  <img src="../../../images_common/wfs.png" />
  <figcaption>LoD1.3 2D laag van de WFS gevisualiseerd in QGIS, met de BRT Achtergrondkaart van PDOK op de achtergrond.</figcaption>
</figure>

### WMS

Ook <a href=https://www.ogc.org/standards/wms>Web Map Service (WMS)</a> is een OGC-standaard, maar dan om kaarten als afbeelding op te vragen.

<figure>
  <img src="../../../images_common/wms.png" />
  <figcaption>LoD1.3 2D laag van de WMS gevisualiseerd in QGIS, met de BRT Achtergrondkaart van PDOK op de achtergrond.</figcaption>
</figure>

### Webservices in QGIS

[Hier](https://www.youtube.com/watch?v=dWTGOm3Emw4) vind je een QGIS tutorial over webservices van een van onze 3D geoinformation groep collega's. Op 3:18 in de video laat hij specifiek zien hoe je de webservices van de vorige versie van de 3D BAG gebruikt. Het grootste verschil met de nieuwe 3D BAG is dat je nu kan specificeren welke laag van de data je wil gebruiken (de tileset of een van de LoDs).

In die video wordt eveneens de [PDOK services plugin](https://plugins.qgis.org/plugins/pdokservicesplugin/) geïntroduceerd, met handige webservices die kunnen fungeren als referentiekaart.