
## 21.09.1 (2021.09.XX) – beta

#### Added

+ The building part ID (`pand_deel_id`) to the 3D layers. Previously it was only part of the 2D layers.

#### Changed / Fixed

+ 3D geometries are **not triangulated** anymore in the CityJSON, GeoPackage, PostgreSQL formats. The OBJ format is triangulated.
+ The object ID in the OBJ files are the BAG ID (`identificatie`), instead of an integer sequence.
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
+ GPKG format: preserve the feature ID (`fid`) in the `pand` layer so it is possible to join the other layers on `fid`.
+ Fixed the duplicate / cloned objects in the output.

#### Removed

#### Known issues


## 21.03.1 (2021.03.26) – beta

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
