<a href=https://www.cityjson.org/>CityJSON</a> is een open bestandsformaat voor 3D stadsmodellen (ook wel digital twins genoemd) en een JSON-codering van het datamodel van CityGML. De standaard zit in het proces om een <a href=https://www.ogc.org/standards/community>community standard</a> te worden van het Open Geospatial Consortium (OGC).

De specificaties van CityJSON beschrijven de manier van het opslaan van zowel de geometrie als semantiek van veelvoorkomende 3D objecten, waaronder gebouwen, vegetatie, wegen, waterlichamen en bruggen. Dit maakt het geschikt voor 3D geografische analyse.

De drie leidende principes van het formaat zijn compactheid, eenvoud en makkelijk te gebruiken door ontwikkelaars. CityJSON is gemiddeld 6 maal zo compact als CityGML door de JSON-codering. Daarnaast zijn er door het gemakkelijke formaat al <a href=https://www.cityjson.org/software/>verscheidene tools</a> ontwikkeld voor het verwerken, bewerken en visualiseren van CityJSON-bestanden. Een aantal van die tools is hieronder uitgelicht, probeer het uit!

De CityJSON-bestanden van de 3D BAG bevatten alle [3D lagen](../../schema/layers/#data-layers) (LoD1.2, LoD1.3, LoD2.2), maar alleen de attributen die betrekking hebben op het gehele gebouw.

### ninja en azul

<a href=http://ninja.cityjson.org/>ninja</a> is een webapplicatie voor het visualiseren én bewerken van CityJSON-bestanden.

Voor macOS is er <a href=https://github.com/tudelft3d/azul>azul</a>, een 3D viewer voor verscheidene formaten waaronder CityJSON.

<figure>
  <img src="../../../images_common/ninja.jpg" />
  <figcaption>Een 3D BAG tegel gevisualiseerd met ninja.</figcaption>
</figure>


### QGIS CityJSON Loader plugin

De <a href=https://github.com/cityjson/cityjson-qgis-plugin>CityJSON Loader plugin</a> voor QGIS 3 maakt het mogelijk om CityJSON-bestanden in te laden in QGIS, inclusief 3D visualisering. Je kan de 3D visualisatie openen door naar `View` -> `New 3D Map View` te gaan. Voor versies van QGIS 3 ouder dan 3.2 is er daarvoor echter <a href=https://github.com/cityjson/cityjson-qgis-plugin#3d-view-in-qgis-30>een extra stap vereist</a>.

<figure>
  <img src="../../../images_common/qgis.jpg" />
  <figcaption>Een 3D BAG tegel geopend in QGIS, met de 3D Map View links en de attributen rechts.</figcaption>
</figure>

### cjio

<a href=https://github.com/cityjson/cjio>cjio</a> is een command-line-interface voor het verwerken van CityJSON-bestanden. Je kan er bijvoorbeeld data mee valideren, bestanden opdelen of samenvoegen en converteren naar andere formaten.

Om alle attributen (en meer) te zien in een 3D BAG bestand:

`cjio 3dbag_<version>_<tile ID>.json info --long`

Om de LoD2.2 uit een 3D BAG bestand te halen en die op te slaan:

`cjio 3dbag_<version>_<tile ID>.json extract_lod 2 save out.json`