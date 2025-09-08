Webservices maken het mogelijk om via een URL exact te specificeren welke 3DBAG gebouwen je wilt downloaden. Wij bieden traditionele 2D webservices (WFS/WMS) en een 3D webservice aan (3DBAG API).

De 2D webservices worden ondersteund door de meeste GIS software pakketten. Ze bevatten zowel de [2D lagen](../schema/layers.md#data-layers), als de tegel-index die we gebruiken voor het verspreiden van de data in de verschillende formaten.

Daarnaast is er ook een 3DBAG 3D API beschikbaar. Hiermee kunnen alle 3DBAG gebouwen met 3D geometrie en alle beschikbare attributen in het [CityJSONFeatures](https://www.cityjson.org/specs/2.0.0/#text-sequences-and-streaming-with-cityjsonfeature) formaat gedownload worden.

De links naar de webservices staan op de 3DBAG [Downloads](https://3dbag.nl/nl/download) pagina.

## 2D webservices

### WFS (2D)

[Web Feature Service (WFS)](https://www.ogc.org/standards/wfs) is een OGC-standaard die beschrijft hoe geografische vectordata opgevraagd, gecreëerd en bewerkt kan worden via internet.

Beschikbare lagen:

- lod12
- lod13
- lod22
- tiles

<figure>
  <a href="../../../images_common/wfs.png">
    <img src="../../../images_common/wfs.png" width="600" />
  </a>
  <figcaption>LoD1.3 2D laag van de WFS gevisualiseerd in QGIS, met de BRT Achtergrondkaart van PDOK op de achtergrond.</figcaption>
</figure>

Om de WFS-laag correct te filteren in Python, kun je [ons script](https://github.com/3DBAG/3dbag-scripts/blob/main/wfs_filtering.py) raadplegen.

### WMS (2D)

Ook [Web Map Service (WMS)](https://www.ogc.org/standards/wms) is een OGC-standaard, maar dan om kaarten als afbeelding op te vragen.

<figure>
  <a href="../../../images_common/wms.png">
    <img src="../../../images_common/wms.png" width="600" />
  </a>
  <figcaption>LoD1.3 2D laag van de WMS gevisualiseerd in QGIS, met de BRT Achtergrondkaart van PDOK op de achtergrond.</figcaption>
</figure>

### 2D webservices in QGIS

[Hier](https://www.youtube.com/watch?v=dWTGOm3Emw4&list=PL4POqt8zsiXFJEEF88f6uAnfuOQSAoG6l) vind je een QGIS tutorial over webservices van een van onze 3D geoinformation groep collega's. Op 3:18 in de video laat hij specifiek zien hoe je de webservices van de vorige versie van de 3DBAG gebruikt. Het grootste verschil met de nieuwe 3DBAG is dat je nu kunt specificeren welke laag van de data je wilt gebruiken (de tegel-index of een van de LoDs).

In die video wordt eveneens de [PDOK services plugin](https://plugins.qgis.org/plugins/pdokservicesplugin/) geïntroduceerd, met handige webservices die kunnen fungeren als referentiekaart.

## 3DBAG API (3D)

De 3DBAG API is beschikbaar via [api.3dbag.nl](https://api.3dbag.nl). Gedetailleerde informatie over de werking kan gevonden worden op de [ingebedde documentatie pagina](https://api.3dbag.nl/api.html). In tegenstelling tot de 2D webservices hierboven, wordt er 3D geometrie geleverd. De 3DBAG API kan gebruikt worden om een enkel gebouw binnen te halen (op basis van de BAG `identificatie` code) of om alle gebouwen binnen een bounding box binnen te halen. De 3DBAG objecten worden teruggegeven in het [CityJSONFeatures](https://www.cityjson.org/specs/2.0.0/#text-sequences-and-streaming-with-cityjsonfeature) formaat.

Hieronder staat een korte python code die laat zijn hoe je een [`.city.jsonl` bestand](https://www.cityjson.org/specs/2.0.0/#text-sequences-and-streaming-with-cityjsonfeature) kan maken van een  verzoek aan de 3DBAG API:

```python
import urllib.request
import json

myurl = "https://api.3dbag.nl/collections/pand/items/NL.IMBAG.Pand.1655100000500568"
with urllib.request.urlopen(myurl) as response:

    j = json.loads(response.read().decode('utf-8'))
    with open("output.city.jsonl", "w") as my_file:
        my_file.write(json.dumps(j["metadata"]) + "\n")
        if "feature" in j:
            my_file.write(json.dumps(j["feature"]) + "\n")
        if "features" in j:
            for f in j["features"]:
                my_file.write(json.dumps(f) + "\n")
```

Als je je data in CityJSON-formaat nodig hebt, kun je van CityJSONSeq naar CityJSON converteren met het gereedschap [cjio](https://github.com/cityjson/cjio) als volgt:

```bash
cat <path-to>output.city.jsonl | cjio stdin save <path-to>output.city.json
```

Let op: Voor verzoeken die meer dan 10 gebouwen retourneren, worden de resultaten door de 3DBAG API gepagineerd. We raden aan om [ons script te gebruiken om gepagineerde responses om te zetten naar één CityJSON-bestand](https://github.com/3DBAG/3dbag-scripts/blob/main/api_to_cityjson.py).

Momenteel is de 3DBAG API nog niet OGC-compliant, maar het is wel ons doel om in een latere versie van de 3DBAG volledig compliant te zijn met de [OGC API Features specificatie](https://ogcapi.ogc.org/features/). Momenteel wordt alleen het CRS Amersfoort / RD New + NAP height (EPSG:7415) ondersteund.

## 3D Tiles

[3D Tiles](https://www.ogc.org/standards/3dtiles/) is een Open Geospatial Consortium community standaard voor het streamen van enorme heterogene 3D geospatial datasets.
Wij gebruiken 3D Tiles voor het streamen van de gebouwmodellen naar onze 3D Viewer en we stellen dezelfde set 3D Tiles ook beschikbaar voor extern gebruik.

De drie LoD-s (LoD1.2, LoD1.3, LoD2.2) worden als aparte tegelsets aangeboden.
De link naar de tegelsets is te vinden op onze [Downloads pagina](https://3dbag.nl/nl/download).

Er zijn momenteen geen beperkingen in kwa gebruiksvolume, maar dit kan in de toekomst veranderen.
De [Copyright notice](https://docs.3dbag.nl/nl/copyright/) is verplicht.

Details van de 3D-tegels:

- Maakt gebruik van 3D Tiles v1.1.
- De tileset en content CRS is EPSG:4978.
- De content van de tileset is binair glTF (.glb).
- De glTF-assets bevatten metadata attributen (per Gebouw), met behulp van de [EXT_mesh_features](https://github.com/CesiumGS/glTF/tree/3d-tiles-next/extensions/2.0/Vendor/EXT_mesh_features) en [EXT_structural_metadata](https://github.com/CesiumGS/glTF/tree/3d-tiles-next/extensions/2.0/Vendor/EXT_structural_metadata) extensies.
- De gebouwen zijn in een uniforme kleur gekleurd.
- De glTF-bestanden zijn gecomprimeerd, met behulp van de [KHR_mesh_quantization](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_mesh_quantization) en [EXT_meshopt_compression](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Vendor/EXT_meshopt_compression) extensies.
- De tileset gebruikt _explicit tiling_ en is opgesplitst in meerdere [External tilesets](https://docs.ogc.org/cs/22-025r4/22-025r4.html#core-external-tilesets).

Onze 3D Tiles worden gemaakt met [Tyler](https://github.com/3DGI/tyler).

Hieronder vind je een voorbeeld script om de 3DBAG 3D-tegels in een Cesium viewer op te nemen.
Merk op dat je `<YOUR CESIUM ION TOKEN>` moet vervangen met je eigen [Cesium Ion access token](https://ion.cesium.com/signup/).

```html
<!DOCTYPE html>

<html lang="en">

<head>

  <meta charset="utf-8">

  <!-- Include the CesiumJS JavaScript and CSS files -->
  <script src="https://cesium.com/downloads/cesiumjs/releases/1.133/Build/Cesium/Cesium.js"></script>
  <link href="https://cesium.com/downloads/cesiumjs/releases/1.133/Build/Cesium/Widgets/widgets.css"
        rel="stylesheet">

</head>

<body>

<div id="cesiumContainer"></div>

<script type="module">
    // Your access token can be found at: https://ion.cesium.com/tokens.
    // Replace `your_access_token` with your Cesium ion access token.
    Cesium.Ion.defaultAccessToken = '<YOUR CESIUM ION TOKEN>';

    // Initialize the Cesium Viewer in the HTML element with the `cesiumContainer` ID.
    const viewer = new Cesium.Viewer('cesiumContainer', {
        terrain: Cesium.Terrain.fromWorldTerrain(),
    });


    try {
        const tileset = await Cesium.Cesium3DTileset.fromUrl(
            'https://data.3dbag.nl/v20250903/cesium3dtiles/lod22/tileset.json'
        );
        viewer.scene.primitives.add(tileset)
        viewer.zoomTo(
            tileset,
            new Cesium.HeadingPitchRange(
                0.5,
                -0.5,
                tileset.boundingSphere.radius * 0.05
            )
        );
    } catch (error) {
        // Handle errors
        console.log(`There was an error while creating the 3D tileset. ${error}`);
    }

</script>

</div>

</body>

</html>
```
