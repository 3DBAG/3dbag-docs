Webservices make it possible to specify via an URL exactly which models to download from the 3D BAG. All major GIS software supports these services.

From the 3D BAG we serve the [2D layers](../schema/layers.md#data-layers) and the tile set that we use for distributing the data in various formats. You can find the respective links in the [Downloads](https://3dbag.nl/en/download) page.

## WFS

The [Web Feature Service](https://www.ogc.org/standards/wfs) (WFS) is an Open Geospatial Consortium standard, and it describes how to query, create and modify geospatial data through the internet.

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

[Here](https://www.youtube.com/watch?v=dWTGOm3Emw4&list=PL4POqt8zsiXFJEEF88f6uAnfuOQSAoG6l) you find a tutorial on using webservices in QGIS, created by one of our colleagues of the 3D geoinformation research group. At `3:18` in the video you can see how to load the webservices of the previous 3D BAG version. The process is almost the same for the current 3D BAG version.

The video also refers to the [PDOK services plugin](https://plugins.qgis.org/plugins/pdokservicesplugin/), which is very handy for loading base layers.
