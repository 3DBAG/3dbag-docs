De webservices geven de mogelijkheid om in de vorm van een URL exact te specificeren welke 3D BAG gebouwen je wilt downloaden. Alle belangrijke GIS-software heeft ondersteuning voor deze services.

Van de 3D BAG bieden we zowel de [2D lagen](../schema/layers.md#data-layers) aan, als de tegelset die we gebruiken voor het verspreiden van de data in de verschillende formaten. De links naar de webservices staan op de 3D BAG [Downloads](https://3dbag.nl/nl/download) pagina.

## WFS

[Web Feature Service (WFS)](https://www.ogc.org/standards/wfs) is een OGC-standaard die beschrijft hoe geografische vectordata opgevraagd, gecreëerd en bewerkt kan worden via internet.

<figure>
  <a href="../../../images_common/wfs.png">
    <img src="../../../images_common/wfs.png" width="600" />
  </a>
  <figcaption>LoD1.3 2D laag van de WFS gevisualiseerd in QGIS, met de BRT Achtergrondkaart van PDOK op de achtergrond.</figcaption>
</figure>

## WMS

Ook [Web Map Service (WMS)](https://www.ogc.org/standards/wms) is een OGC-standaard, maar dan om kaarten als afbeelding op te vragen.

<figure>
  <a href="../../../images_common/wms.png">
    <img src="../../../images_common/wms.png" width="600" />
  </a>
  <figcaption>LoD1.3 2D laag van de WMS gevisualiseerd in QGIS, met de BRT Achtergrondkaart van PDOK op de achtergrond.</figcaption>
</figure>

## Webservices in QGIS

[Hier](https://www.youtube.com/watch?v=dWTGOm3Emw4&list=PL4POqt8zsiXFJEEF88f6uAnfuOQSAoG6l) vind je een QGIS tutorial over webservices van een van onze 3D geoinformation groep collega's. Op 3:18 in de video laat hij specifiek zien hoe je de webservices van de vorige versie van de 3D BAG gebruikt. Het grootste verschil met de nieuwe 3D BAG is dat je nu kunt specificeren welke laag van de data je wilt gebruiken (de tileset of een van de LoDs).

In die video wordt eveneens de [PDOK services plugin](https://plugins.qgis.org/plugins/pdokservicesplugin/) geïntroduceerd, met handige webservices die kunnen fungeren als referentiekaart.
