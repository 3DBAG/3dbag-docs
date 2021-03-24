[CityJSON](https://www.cityjson.org/) is an open data format for distributing 3D city models (also known as digital twins), and a JSON-encoding of the [CityGML](https://www.ogc.org/standards/citygml) data model. CityJSON is in the process of becoming a [community standard](https://www.ogc.org/standards/community) of the Open Geospatial Consortium.

The CityJSON specification prescribes how to store the 3D geometry as well as the semantics of common objects in a city, eg. buildings, vegetation, roads, waterways and bridges. This makes the the data model optimal for spatial analysis.

The three guiding principles for the format are compactness, simplicity and ease of use for software development. CityJSON has approximately a 6x smaller size than CityGML due to the JSON-encoding. Furthermore, there are already [several open software that work with CityJSON](https://www.cityjson.org/software/) files. We present a few of them below. Try them out!

The CityJSON files of the 3D BAG contain all the [3D layers](../../schema/layers/#data-layers) (LoD1.2, LoD1.3, LoD2.2), but only the attributes that apply to the whole building.

## ninja and azul

[ninja](http://ninja.cityjson.org/) is a drag-and-drop web application for visualising and editing CityJSON files.

On macOS [azul](https://github.com/tudelft3d/azul) can visualise several data formats, including CityJSON.

<figure>
  <img src="../../../images_common/ninja.jpg" />
  <figcaption>A portion of the 3D BAG visualised in ninja.</figcaption>
</figure>


## QGIS CityJSON Loader plugin

With the [CityJSON loader plugin](https://github.com/cityjson/cityjson-qgis-plugin) it is possible to load CityJSON files into QGIS 3, and view them in 3D. You can open the 3D viewer by selecting `View` -> `New 3D Map View`. For QGIS 3 versions older than 3.2, there is an [extra step necessary](https://github.com/cityjson/cityjson-qgis-plugin#3d-view-in-qgis-30).

<figure>
  <img src="../../../images_common/qgis.jpg" />
  <figcaption>A portion of the 3D BAG visualised in QGIS, with the 3D Map View on the left and the attributes on the right.</figcaption>
</figure>

## cjio

[cjio](https://github.com/cityjson/cjio) is tool with a command-line-interface for working with CityJSON files. For instance, you can get information about the file contents, subset and merge files, convert them to other formats etc.

List all the attributes (and more) in a 3D BAG file:

```shell
cjio 3dbag_<version>_<tile ID>.json info --long
```

Extract only the LoD2.2 from a 3D BAG file:

```shell
cjio 3dbag_<version>_<tile ID>.json extract_lod 2 save out.json
```
