# General Concepts

## Level of Detail (LoD)

All models are abstractions of the reality, some are closer to the real thing, while others are less so. In 3D GIS, the Level of Detail (LoD) of a 3D model tells the amount of approximation that the model has. For instance, consider a very simple building with four corners and a gabled roof. A very rough approximation of this building would be a cube. While on the other end, we could have individual surfaces in the model that follow the shape of the building exactly, each of them labelled with additional information like surface type, material etc.

Higher LoDs (LoD2 and above) require that the surfaces of the model are labelled based on their function in the real object. These labels are called *semantics*, and accordingly we call the labelled surfaces *semantic surfaces*. For instance in case of building models, we can talk about a *ground surface*, *wall surface*, *roof surface* etc.

In the 3D BAG we use the so called [*improved LoD specification*](http://doi.org/10.1016/j.compenvurbsys.2016.04.005), as it is displayed in the figure below.

![improved_lod](https://3d.bk.tudelft.nl/lod/lodtud.png)

For the 3D BAG the relevant LoDs are 1.2, 1.3, and 2.2. Note that apart from the amount of geometric detail, the key difference between LoD1 and LoD2 is the presence of *semantic surfaces*, as roof surfaces are coloured red, wall surfaces are grey. Furthermore, the distinction between LoD1.2 and LoD1.3 is that LoD1.3 distinguishes between the significant height differences in the building, while in case of LoD1.2 the whole model has a uniform height.



difficulties of modelling buildings in diff lod-s

highest lod is not always the best

geometric validity

...