# Data Layers

![3dbag_layers](../images/3d_bag_layers_en.svg)

The diagram above shows the relation between a building in the real world and how is it modeled in the 3D BAG.
The BAG models buildings with their largest extent as viewed from above. In practice this means a single 2D polygon per building, as it is displayed by the black polygon in the figure. Therefore, the BAG polygon also includes parts of the building that are underground.

<!-- set font color to blue and red for the above ground and under ground texts to highlight the connection to the figure -->
In order to create an accurate model of the above ground parts of a building, we cut off the underground parts from the BAG polygon. We only consider the above ground parts, because we do not have data on the 3D extent of the underground parts.

From the above ground parts we then generate the 3D models in LoD1.2, 1.3 and 2.2. We realise that for some applications it is more suitable to read 2D polygons and the building height information from attributes. Therefore, we also provide a 2D counterpart in each LoD.

!!! lod11_replace
    In case of greenhouses and large warehouses we do not cut off any parts of the BAG model, but take the polygon as is, and only generate an LoD1.1 model. Thus, such buildings only have an LoD1.1 model and are marked with the attribute value `lod11_replace = true`.

<!-- link to h_dak_* attribute description --> 
In case of the 2D models, the polygons represent the 2D projection of the roof planes of the 3D model. For LoD1.2 and LoD1.3 the 3D model can be fully reconstructed from the 2D model, by taking the 2D polygons and extruding each to one of their `h_dak_*` height values. However, this is not true for the LoD2.2 models, since here we have slanted roof planes, which cannot be represented by a 2D polygon and a single height value.

conceptual relation between the layers

differences, similarities etc