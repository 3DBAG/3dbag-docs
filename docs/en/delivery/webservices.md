Webservices make it possible to specify via a URL exactly which models to download from the 3DBAG. All major GIS software supports these services.From the 3DBAG we serve the [2D layers](../schema/layers.md#data-layers) and the tile set that we use for distributing the data in various formats. 

Additionally, an experimental version of a 3D API is available which can be used to retrieve 3D buildings with all the available attributes in a [CityJSONFeatures](https://www.cityjson.org/specs/2.0.0/#text-sequences-and-streaming-with-cityjsonfeature) format.

You can find the webservice and API links on the 3DBAG [Downloads](https://3dbag.nl/en/download) page.

## WFS

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

## WMS

The [Web Map Service](https://www.ogc.org/standards/wms) is an Open Geospatial Consortium standard to retrieve maps as images through the internet.

<figure>
  <a href="../../../images_common/wms.png">
    <img src="../../../images_common/wms.png" width="600" />
  </a>
  <figcaption>LoD1.3 2D WMS layer visualised in QGIS, with the BRT Baselayer from PDOK in the background.</figcaption>
</figure>

## Webservices in QGIS

[Here](https://www.youtube.com/watch?v=dWTGOm3Emw4&list=PL4POqt8zsiXFJEEF88f6uAnfuOQSAoG6l) you find a tutorial on using webservices in QGIS, created by one of our colleagues of the 3D geoinformation research group. At `3:18` in the video you can see how to load the webservices of the previous 3DBAG version. The process is almost the same for the current 3DBAG version.

The video also refers to the [PDOK services plugin](https://plugins.qgis.org/plugins/pdokservicesplugin/), which is very handy for loading base layers.


## 3D API 
(beta)
The API's base URL is  `api.3dbag.nl` and more information about the available endpoints can be found [in the documentation](https://api.3dbag.nl/api.html). It can be used to retrieve a single building or all buildings within a certain bounding box with all the available attributes in a [CityJSONFeatures](https://www.cityjson.org/specs/2.0.0/#text-sequences-and-streaming-with-cityjsonfeature) format. 

In order to save the response to a `.jsonl` file you need to get both metadata and the features. You can do this manually or you could use a script like the one below:

```python
import urllib.request
import json

myurl = "https://api.3dbag.nl//collections/pand/items/NL.IMBAG.Pand.1655100000500568"
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

This is a beta version and currently it is not OGC-compliant, but we aim for compliance in a later release. At the moment the only supported CRS is Amersfoort / RD New + NAP height (EPSG:7415).

