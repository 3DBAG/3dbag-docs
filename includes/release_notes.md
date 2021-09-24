
## 21.09.8 – beta

*Release date: 22 September 2021*

This is the second public beta release of the renewed 3D BAG. Before addressing what has changed with this release we would like to take a moment to thank everyone that has been downloading and using the first release. It's very exciting to see how people from various discipplines found ways to apply 3D BAG for their use cases! (also see our new [In the media](media.md) page). A special thanks also to everyone that filled out our feedback forms or gave us feedback in other ways. This is much appreciated!

For this second release we focused primarily on improving the data quality and the way the data is disseminated. The overall geometric validity of the 3D models has risen to 98.25% (up from ~89% in the previous release). Another highlight is that the 3D outputs are no longer triangulated, as requested by several users. Alltogether this should make it easier to use our models in other software. These and more changes are described below in more detail. Thanks for using 3D BAG!

#### Added

+ The building part ID (`pand_deel_id`) to the 3D layers. Previously it was only part of the 2D layers.
+ A new layer (`ondergrond`) with parts of the building polygons that were cut off during the reconstruction, because they were detected as the ground.

#### Changed / Fixed

+ Update of the source data sets (BAG, BGT, Top10NL) to the version available on 2021-09-07.
+ 3D geometries are **not triangulated** anymore in the CityJSON, GeoPackage, PostgreSQL formats. The OBJ format remains triangulated.
+ The CityJSON exporter was rewritten
    - The semantic surfaces of type `WallSurface` now have an additional boolean attribute `on_footprint` which indicates if a WallSurface is on a footprint edge or not.
    - The original BAG footprint is now include for each object
    - CityObject ID's are now the BAG identificatie
+ Improvements in the reconstruction algorithm
    + Added new triangulation-based snapping node. The goal of this node is to remove (near) duplicate vertices in the 2D roof partition without introducing topological problems. This fixes problems with e.g. spikes (due vertices with invalid coordinates) and missing faces in the final 3D models. With this improvement we have >98% valid geometries, up from 89% in the previous version. We checked this with [val3dity](https://github.com/tudelft3d/val3dity).
    + Added a nearest neighbor interpolation for no-data pixels in the heightfield that is used during optimisation. This interpolation picks the lowest value in the neighborhood (with radius of 10 cm at the moment) of the nodata pixel of interest. This should reduce the occurence of erroneous thin vertical 'screens' in building models (several still remain however).
    + Several other smaller bugfixes and improvements.

+ The object ID in the OBJ files is now the BAG ID (`identificatie`) instead of an integer sequence.
+ Attribute name changes:

| From                    | To                     |
|-------------------------|------------------------|
| _lod11_replace          | lod11_replace          |
| _semantics_values       | semantics_values       |
| _tile_id                | tile_id                |
| _reconstruction_skipped | reconstruction_skipped |
| _t_run                  | q_t_run                |
| _roofplane_cnt          | q_roofplane_cnt        |
| _data_area              | q_data_area            |
| _nodata_area            | q_nodata_area          |
| _data_coverage          | q_data_coverage        |
| _roof_pt_cnt            | q_roof_pt_cnt          |
| _wall_pt_cnt            | q_wall_pt_cnt          |
| _unsegmented_pt_cnt     | q_unsegmented_pt_cnt   |
| _pc2m_error_hist        | q_pc2m_error_hist      |
| _m2pc_error_hist        | q_m2pc_error_hist      |
| _m2pc_error_max         | q_m2pc_error_max       |
| _rmse                   | q_rmse                 |

+ The roofpart ID (`dd_id`) starts with 0. Previously it started with 1.
+ The value `could not detect` of the `dak_type` attribute has been changed to `no planes`.
+ GPKG format: preserve the feature ID (`fid`) in the `pand` layer so it is possible to join the other layers on `fid`.
+ Fixed the duplicate / cloned objects in the output.
+ Improve 3D tiles export and rendering in the Viewer

#### Known issues
+ Artificial vertical 'screens' still occur in some building models.
+ 1.75% of the buildings is geometrically invalid, consult the `val3dity_codes` attribute to find out which ones.
+ Missing tiles (in all formats): 10, 41, 42, 117, 143, 228, 301, 381, 776, 1485, 1876, 2178, 2333, 2436, 2511, 2662, 2713, 5158, 5186, 5228, 6813, 7364
+ Self intersection on buildings that have a roofplane detected that extends below `h_maaiveld`.

## 21.03.1 – beta

*Release date: 26 March 2021*

#### Added

+ A brand new 3D viewer.
+ Multiple LoDs, LoD1.2, LoD1.3, LoD2.2.
+ 2D and 3D variants of all LoDs. The 3D models are triangulated.
+ More accurate height calculation, due to our new reconstruction method.
+ Underground buildings and floating buildings are removed, underground parts are cut off from the models. This means that we modify the incoming BAG footprints by removing the underground parts.
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

+ Some buildings have a 'spike': a large deviation in the building geometry due to one vertex with an erroneous coordinate (3D models only).
+ Not all buildings are geometrically valid (eg. missing face). Note that this should be evident from the val3dity_codes attribute (3D models only).
+ Missing tiles (in all formats): 6, 8, 10, 20, 42, 50, 51, 52, 53, 57, 309, 736, 1389, 2178, 3647. On the top of the previous list, the following tiles are missing a CityJSON format: 19, 251, 298, 365, 381, 702, 1051, 1812, 2535, 2700, 2962, 2996, 3173, 3324, 3381, 3796, 4248, 4511, 4615, 4729, 5316, 5411, 6237, 6690, 6986, 7290, 7470, 7597, 8061.
