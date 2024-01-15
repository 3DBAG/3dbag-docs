Webservices make it possible to specify via a URL exactly which models to download from the 3DBAG. We offer traditional 2D webservices (WFS and WMS) and an experimental 3D webservice that we call the 3DBAG API.

The 2D webservices are supported by all major GIS software packages. They serve directly the [2D layers](../schema/layers.md#data-layers) of the 3DBAG and a tile-index that corresponds to the 3DBAG tiles that are available for download in various formats. 

Additionally, an experimental version of a 3D API is available which can be used to retrieve 3DBAG buildings with their 3D geometry and all the available attributes in the [CityJSONFeatures](https://www.cityjson.org/specs/2.0.0/#text-sequences-and-streaming-with-cityjsonfeature) format.

You can find the webservice links on the 3DBAG [Downloads](https://3dbag.nl/en/download) page.


## 2D webservices

### WFS (2D)

The [Web Feature Service](https://www.ogc.org/standards/wfs) (WFS) is an Open Geospatial Consortium standard, and it describes how to query, create and modify geospatial data through the internet.

Available layers:

- lod12
- lod13
- lod22
- tiles

<figure>
  <a href="../../../images_common/wfs.png">
    <img src="../../../images_common/wfs.png" width="600" />
  </a>
  <figcaption>LoD1.3 2D WFS layer visualised in QGIS, with the BRT Baselayer from PDOK in the background.</figcaption>
</figure>

### WMS (2D)

The [Web Map Service](https://www.ogc.org/standards/wms) is an Open Geospatial Consortium standard to retrieve maps as images through the internet.

<figure>
  <a href="../../../images_common/wms.png">
    <img src="../../../images_common/wms.png" width="600" />
  </a>
  <figcaption>LoD1.3 2D WMS layer visualised in QGIS, with the BRT Baselayer from PDOK in the background.</figcaption>
</figure>

### 2D webservices in QGIS

[Here](https://www.youtube.com/watch?v=dWTGOm3Emw4&list=PL4POqt8zsiXFJEEF88f6uAnfuOQSAoG6l) you find a tutorial on using webservices in QGIS, created by one of our colleagues of the 3D geoinformation research group. At `3:18` in the video you can see how to load the webservices of the previous 3DBAG version. The process is almost the same for the current 3DBAG version.

The video also refers to the [PDOK services plugin](https://plugins.qgis.org/plugins/pdokservicesplugin/), which is very handy for loading base layers.


## 3DBAG API (3D)

The base URL of the experimental 3DBAG API is [api.3dbag.nl](https://api.3dbag.nl) and more information about the available endpoints can be found on its [embedded documentation page](https://api.3dbag.nl/api.html). As opposed to the 2D webservices described above, the 3DBAG API returns 3D geometries. It can be used to retrieve [a single building](https://api.3dbag.nl/collections/pand/items/NL.IMBAG.Pand.1655100000500568) (using the BAG `identificatie` code) or [all buildings within a certain bounding box](https://api.3dbag.nl//collections/pand/items?bbox=75900.011,447000.034,76000.011,447200.034) with all the available attributes in [CityJSONFeature objects](https://www.cityjson.org/specs/2.0.0/#text-sequences-and-streaming-with-cityjsonfeature).  

The CityJSONFeature objects can be stored in a [CityJSONSeq](https://www.cityjson.org/cityjsonseq/) file with the suffix `city.jsonl`, using the python snippet below. However, for queries that return more than 10 buildings the results are paginated and you will need to write your own script to retrieve them.

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

To convert from CityJSONSeq to CityJSON, you can use the tool [cjio](https://github.com/cityjson/cjio) as follows:

```bash
cat <path-to>output.city.jsonl | cjio stdin save <path-to>output.city.json
```

The 3DBAG API is currently in an experimental beta state. It is currently not OGC-compliant, but we aim for full compliance with the [OGC API Features specification](https://ogcapi.ogc.org/features/) in a later release. At the moment the only supported CRS is Amersfoort / RD New + NAP height (EPSG:7415).

