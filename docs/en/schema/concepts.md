# General Concepts

## Level of Detail (LoD)

All spatial models are abstractions of reality. Some are closer to the real thing, while others are less so. In 3D GIS, the Level of Detail (LoD) of a 3D model describes the amount of detail that is captured in the model, although a high LoD can still be an inaccurate approximation of reality.
For instance, consider a very simple building with four corners and a gabled roof. A very rough approximation of this building would be a cube. While on the other end, we could have individual surfaces in the model that follow the shape of the building exactly, each of them labelled with additional information like surface type, material etc.

Higher LoDs (LoD2 and above) can label the surfaces of the model based on their function in the real object.
These labels are called *semantics*, and accordingly we call the labelled surfaces **semantic surfaces**. For instance in case of building models, we can identify a *ground surface*, *wall surface*, *roof surface* etc.

In the 3DBAG, we use the so called [*improved LoD specification*](http://doi.org/10.1016/j.compenvurbsys.2016.04.005), as it is displayed in the figure below.

<figure>
  <img src="https://3d.bk.tudelft.nl/lod/lodtud.png" />
  <figcaption><b>An improved LOD specification for 3D building models.</b> Filip Biljecki, Hugo Ledoux, and Jantien Stoter. Computers, Environment and Urban Systems, 59: 25–37, 2016. <a href="http://doi.org/10.1016/j.compenvurbsys.2016.04.005">DOI</a></figcaption>
</figure>

For the 3DBAG the relevant LoDs are 1.2, 1.3, and 2.2. Note that apart from the amount of geometric detail, the key difference between LoD1 and LoD2 is the presence of *semantic surfaces*, to allow, for example, roof surfaces to be coloured red and wall surfaces to be coloured grey. Furthermore, the distinction between LoD1.2 and LoD1.3 is that LoD1.3 distinguishes between significant height differences within one building, while in case of LoD1.2 the whole model has a uniform height.

<!-- difficulties of modelling buildings in diff lod-s -->

<!-- highest lod is not always the best -->

## 3D geometric primitives

In 2D GIS, the geometry of objects can be represented by *points*, *lines*, *polygons* and their variations. There are standards that prescribe a set of rules for these primitives so that data can be exchanged in an interoperable manner (eg [Simple Feature Access](https://www.ogc.org/standards/sfa)). 

In 3D GIS, the geometric primitives and their rules need to be extended to the third dimension, so that their interactions can be described in a meaningful way. The figure below gives an overview of the commonly used primitives in 3D GIS.

<figure>
  <img src="https://val3dity.readthedocs.io/en/latest/_images/geomprimitives.svg" />
  <figcaption>3D primitives handled by val3dity. See: <b>Val3dity: validation of 3D GIS primitives according to the international standards.</b> Hugo Ledoux. Open Geospatial Data, Software and Standards 3 (1), 2018, pp. 1. <a href="http://dx.doi.org/10.1186/s40965-018-0043-x">DOI</a></figcaption>
</figure>

For the 3DBAG the most relevant primitive is the [Solid](https://val3dity.readthedocs.io/en/latest/definitions/#solid), as we treat the building models as Solids in our process. This distinction is important, because of the (stricter) rules that apply to Solids, compared to other 3D primitives.

!!! note "3D primitives and data formats"
    Not every data format supports the 3D primitives mentioned above. In fact, this applies to all our export formats except CityJSON. Therefore, in such formats we use the geometry types that are the closest equivalent to Solids. The PostgreSQL backup is a bit of an outlier here, because technically PostGIS can store Solids, but only with the [SFCGAL extension](http://www.sfcgal.org/). In order to cause the least friction for restoring the PostgreSQL backup, we store the 3D geometries as `MultiPolygonZ`.

## Valid 3D geometries

Having valid geometries is important for using the data in various applications. Standards help to define a common set of rules to which both data producers and consumers can adhere to, when working with data. [val3dity](https://val3dity.readthedocs.io/en/latest/) is a software that validates 3D primitives according to the international standard ISO19107.

We integrated val3dity into our process, and so we validate each 3D model after it is reconstructed. However, the building models are validated independently as they go through the reconstruction process. Therefore, we cannot detect errors in the interaction of multiple models (error codes above 500).

!!! note "b3_val3dity_lod12", "b3_val3dity_lod13", "b3_val3dity_lod22"
    The attributes starting with [`b3_val3dity_`](attributes.md##b3_val3dity_lod12) store the error codes from val3dity (if any) for a model.

<figure>
  <img src="https://val3dity.readthedocs.io/en/latest/_images/errorcodes.png" />
  <figcaption>val3dity error codes. See <a href="https://val3dity.readthedocs.io/en/latest/errors/">the full description of each code</a> in the val3dity documentation.</figcaption>
</figure>