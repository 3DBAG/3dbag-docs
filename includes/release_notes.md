## Unreleased (First full release)
These are the issues that we want to solve for the first full release of the 3D BAG.

+ issue
+ issue


## 21.03.1 (2021.03.26) – beta

#### Added

+ A brand new 3D viewer.
+ Multiple LoDs, LoD1.2, LoD1.3, LoD2.2.
+ 2D and 3D variants of all LoDs. The 3D models are triangulated.
+ More accurate height calculation, due to our new reconstruction method.
+ Underground buildings and floating buildings are removed, underground parts are cut off from the models. This means that we modify the incoming BAG footprints by removing the underground parts.
+ Buildings with an extremely noisy point cloud (eg. greenhouses) only have an extrusion as their 3D model, and they are not reconstructed in any of the three LoDs. Their BAG footprint is not modified either. Thus, these models are very similar to those in the previous 3D BAG version.
+ Integrated validation of the 3D models with val3dity.
+ OBJ and CityJSON data formats.
+ A completely re-worked documentation.
+ Report issues on individual buildings and provide general feedback with a form.

#### Changed

+ Downloads are available in tiles instead of the whole country. Except the PostgreSQL backup, which is only available for the whole country.
+ Switched to BAG 2.0.
+ Basically all the attributes have changed. Note that due to our new reconstruction method, the meaning of the building height percentiles `h_dak` have changed too. Previously we had multiple percentiles for the ground height, while there is only one `h_maaiveld` now.
+ All the URLs.
+ New contact information.

#### Removed

+ CSV data format.

#### Known issues

+ issue