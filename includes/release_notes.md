## 2023.06.16 – beta

*Release date: X juni 2023*

This is the third public beta release of the 3D BAG. 

AHN4

+ Revamped reconstruction pipeline, deployed on new server.

+ several viewer improvements

3dgi

nr of buildings, validity percentage

Thank you for using 3D BAG!

#### Added

+ The building part ID (`pand_deel_id`) to the 3D layers. Previously it was only part of the 2D layers.
+ Improvements in the reconstruction algorithm
    + added procedure for automatic selection of the pointcloud (AHN3 or 4) best suited for reconstruction on a per building basis.
    + building volumes are now calculated and outputted
+ When opening the 3D BAG viewer you are brought to a random landmark
+ A metadata file is now available on the download page
+ You can now view all attributes directly in the viewer
+ Clicking on the attribute name in the viewer attribute table now brings you to the corresponding section in the documentation

#### Changed / Fixed

+ Update of the source vector data sets (BAG, Top10NL) to the version available on 2023-06-05 (TOP10NL) and 2023-06-08 (BAG).
+ Update of the source point cloud data sets. Now AHN3 and AHN4 are used.
+ New tiling scheme for downloads
+ New file naming
+ 3D BAG version number is now a full date instead of a mix between date and minor version number.
+ All 3D BAG specific attributes are now preceded by the `b3_` prefix.
+ The postgres database dump was replaced by one big gpkg file zipped into a [seek-optimized ZIP (SOZip)](https://gdal.org/programs/sozip.html#sozip) file.
+ Improvements in the reconstruction algorithm
    + new procedure for overlap detection between buildings. In this procedure it is guaranteed that points on areas of overlap are only assigned to one of the overlapping buildings.
    + fine tuning of snapping thresholds to achieve better geomtric validity
    + various small improvements
+ The layer `ondergrond` was removed.
+ Changed WFS/WMS endpoint from BAG3D_ to BAG3D
+ Attribute changes:

| v21.09                          |v2023.06 (release) |
|---------------------------------|------------------------|
| gid                             |- |
| fid                             |- |
| pand_deel_id                    |b3_pand_deel_id |
| dd_id                           |b3_dd_id |
| -                               |tijdstipregistratie |
| -                               |eindregistratie |
| h_maaiveld                      |b3_h_maaiveld |
| dak_type                        |b3_dak_type |
| pw_datum                        |b3_pw_datum |
| pw_actueel                      |- |
| pw_bron                         |b3_pw_bron |
| reconstructie_methode           |- |
| versie_methode                  |- |
| kas_warenhuis                   |b3_kas_warenhuis |
| ondergronds_type                |- |
| reconstruction_skipped          |b3_reconstructie_onvolledig |
| lod11_replace                   |- |
| h_dak_min                       |b3_h_dak_min |
| h_dak_50p                       |b3_h_dak_50p |
| h_dak_70p                       |b3_h_dak_70p |
| h_dak_max                       |b3_h_dak_max |
| val3dity_codes_lod12            |b3_val3dity_lod12 |
| val3dity_codes_lod13            |b3_val3dity_lod13 |
| val3dity_codes_lod22            |b3_val3dity_lod22 |
| semantics_values                | - |
| rmse_lod12                      |b3_rmse_lod12 |
| rmse_lod13                      |b3_rmse_lod13 |
| rmse_lod22                      |b3_rmse_lod22 |
| rn                              |- |
| -                               |b3_mutatie_ahn3_ahn4 |
| -                               |b3_nodata_fractie_ahn3 |
| -                               |b3_nodata_fractie_ahn4 |
| -                               |b3_nodata_radius_ahn3 |
| -                               |b3_nodata_radius_ahn4 |
| -                               |b3_pw_selectie_reden |
| -                               |b3_puntdichtheid_ahn3 |
| -                               |b3_puntdichtheid_ahn4 |
| -                               |b3_volume_lod12 |
| -                               |b3_volume_lod13 |
| -                               |b3_volume_lod22 |

#### Known issues
+ BAG date/time attributes in GPKG output are of the string type
+ missing tiles/buildings??
+ b3_pw_datum is always set to 2014 for AHN3 and 2020 for AHN4, instead of AHN metadata values??


## 21.09.8 – beta

*Release date: 29 September 2021*

This is the second public beta release of the renewed 3D BAG. Before addressing what has changed with this release we would like to take a moment to thank everyone that has been downloading and using the first release. It's very exciting to see how people from various disciplines found ways to apply 3D BAG for their use cases! (also see our new [In the media](media.md) page). A special thanks also to everyone that filled out our feedback forms or gave us feedback in other ways. This is much appreciated!

For this second release we focused primarily on improving the data quality and the way the data is disseminated. The overall geometric validity of the 3D models has risen to 98.25% (up from ~89% in the previous release). Another highlight is that the 3D outputs are no longer triangulated, as requested by several users. Altogether this should make it easier to use our models in other software. These and more changes are described below in more detail. 

This 3D BAG release contains 9 692 978 buildings. This is 7.72% less buildings than available in the BAG dataset, mostly due to outdated or otherwise insufficient input data. We hope to do a release based on the updated AHN4 soon, but this release is still based on AHN3.

Thank you for using 3D BAG!

#### Added

+ The building part ID (`pand_deel_id`) to the 3D layers. Previously it was only part of the 2D layers.
+ A new layer (`ondergrond`) with parts of the building polygons that were cut off during the reconstruction, because they were detected as the ground.

#### Changed / Fixed

+ Update of the source data sets (BAG, BGT, Top10NL) to the version available on 2021-09-07.
+ 3D geometries are **not triangulated** anymore in the CityJSON, GeoPackage, PostgreSQL formats. The OBJ format remains triangulated.
+ The CityJSON exporter was rewritten
    - The semantic surfaces of type `WallSurface` now have an additional boolean attribute `on_footprint` which indicates if a WallSurface is on a footprint edge or not.
    - The original BAG footprint is now included for each object
    - CityObject ID's are now based on the BAG `identificatie` attribute
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
+ Missing tiles for download (in all formats): 10, 41, 42, 117, 143, 228, 301, 381, 776, 1485, 1876, 2178, 2333, 2436, 2511, 2662, 2713, 5158, 5186, 5228, 6813, 7364. In the 3D viewer some additional tiles may be missing.
+ Self-intersection on buildings that have a roofplane detected that extends below `h_maaiveld`.
+ Possibly incaccurate building geometry for buildings with glass roofs.
+ Intersecting 3D geometries in case the input BAG footprints overlap.
+ Possible duplicate vertices in CityJSON files.

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
