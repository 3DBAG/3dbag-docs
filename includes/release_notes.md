## Unreleased

#### Changed / Fixed

+ Fix duplicates in the GeoPackage dump.

## 2023.08.09 – beta

*Release date: 9 August 2023*

With this release we fix an error with the attributes `h_dak_min `, `h_dak_50p`, `h_dak_70p`, `h_dak_max` in the GPKG and WFS formats. In 3DBAG version 2023.06.22 the values of these attributes were off by 15 meters. This is fixed in this release.

#### Changed / Fixed
+ Fix 15 meter offset in `h_dak_min `, `h_dak_50p`, `h_dak_70p`, `h_dak_max` attributes on roofparts in GPKG and WFS formats.

## 2023.06.22 – beta

*Release date: 22 June 2023*

This is the third public beta release of the 3D BAG. It's been a while since the second release. As it turns out it costs quite some work to properly maintain and update 3D BAG next to our busy day jobs. Fortunately we were able to receive funding from the ERC to bring the 3D BAG to a level where it can be maintained and developed reliably. The current release is the first of three that is financed by the ERC budget, and it paves the way towards a stable, open 3D BAG service. We are very happy to see that so many people found a use for 3D BAG to help them with their business, research or hobby projects. And we remain committed to keep maintaining 3D BAG into the future, of course as an open dataset. 

[The team behind 3D BAG](group.md) has changed in the sense that some people have moved on to other jobs, others are working on 3D BAG with a different affiliation ([3DGI](https://3dgi.xyz), a spinoff of the [tudelft3d](https://3d.bk.tudelft.nl/) research group) and we also have welcomed a [new member](http://3d.bk.tudelft.nl/gstavropoulou).

The biggest technical change is that the 3D BAG now uses the AHN4 pointcloud which was acquired between 2020 and 2022. This means that the building models are much more up-to-date, compared to the previous release which was based solely on AHN3 (acquired starting from 2014). For this new release we use a 'smart' combination of AHN3 and AHN4. We did not opt for a simple 'drop-in' replacement of AHN3 by AHN4 because of the quality issues that we discovered in AHN4. These issues affect a small, yet significant fraction of the buildings. The 'smart' combination entails that our algorithms automatically select the 'best' available point cloud on a per building basis. The selection is based primarily on point coverage, ie. how well the roof surface of a building is covered with AHN points and *most importantly* if there are any big gaps. Naturally, AHN3 is only considered when a building has not changed compared to the AHN4 data. AHN3 is used for ~8.5% of the buildings, the rest all uses AHN4.

There are also some changes in the BAG viewer and the download page. Most notably, the viewer now brings you to an interesting landmark that is randomly picked when you load the website, and all 3D BAG attributes are now visible in the viewer. The download page now also offers a metadata file about the dataset as a whole (including lineage) and the PostgreSQL dump was replaced by one big GPKG file (something that several people have asked for).

And last, but not least: behind the scenes *a lot of work* has been done to completely recreate our automatic building reconstruction pipeline. This helps us to reliably produce new 3D BAG releases from now on. A tangible benefit to the 3DBAG users is that we now have much fewer missing buildings compared to the previous releases. We will continue to work on our pipeline in the background and streamline our internal processes even further.

This release contains a record number of 10 383 384 builings. The overall geometric val3dity is also at a record at 99.15% (up from 98.25% in the previous release, counted on the LoD2.2 geometries).

Thank you for using the 3D BAG! As always our [feedback forms](https://forms.gle/NZg83heXM75pAmfVA) are available and we are reading all the emails that we receive at info@3dbag.nl.

-- The 3D BAG Team

#### Update 11-07-2023
* Regenerated 3D tiles to fix a number of disply issues in the 3D BAG viewer, including incorrect placement of search result marker.

#### Added

+ The building part ID (`pand_deel_id`) to the 3D layers. Previously it was only part of the 2D layers.
+ Reconstruction algorithm
    + added procedure for automatic selection of pointcloud (AHN3 or 4) best suited for reconstruction on a per building basis
    + building volumes are now calculated and outputted
    + changed the method for calculating the height attributes on roofparts
+ A metadata file is now available on the download page. The metadata contains information about the current release, including the versions of the source data sets and the versions of the software that were used for producing the release. The metadata file unifies some of the information that were previously scattered across different formats.
+ 3D BAG viewer
    + When opening the 3D BAG viewer you are brought to a random landmark
    + You can now view all attributes directly in the viewer
    + Clicking on the attribute name in the viewer attribute table now brings you to the corresponding section in the documentation
    + Update basemap to Luchfoto Actueel
+ Various quality attributes relating to the 'smart' point cloud selection algorithm.
+ 3DGI attribution
+ Created a [3D BAG twitter account](https://twitter.com/3D_BAG). Follow this to be notified about 3D BAG updates and other announcements.
+ SHA-256 hashes for the downloadable files (included on the `tiles` WMS/WFS layer).
+ Download link for each format (included on the `tiles` WMS/WFS layer).
+ Extended testing of all data formats (included on the `tiles` WMS/WFS layer).

#### Changed / Fixed

+ Update of the source vector data sets (BAG, Top10NL) to the version available on 2023-06-05 (TOP10NL) and 2023-06-08 (BAG).
+ Update of the source point cloud data sets. Now AHN3 and AHN4 are used.
+ Significantly fewer missing buildings, due to revamped processing pipeline.
+ Improved geometric validity. Now 99.15% of buildings are geometrically valid.
+ New tiling scheme for downloads.
+ New file naming.
+ 3D BAG version number is now a full date instead of a mix between date and minor version number.
+ All 3D BAG specific attributes are now preceded by the `b3_` prefix.
+ The postgres database dump was replaced by one big gpkg file zipped into a [seek-optimized ZIP (SOZip)](https://gdal.org/programs/sozip.html#sozip) file.
+ Improvements in the reconstruction algorithm
    + new procedure for overlap detection between buildings. In this procedure it is guaranteed that points on areas of overlap are only assigned to one of the overlapping buildings.
    + fine tuning of snapping thresholds to achieve better geomtric validity
    + various small improvements
+ The layer `ondergrond` was removed.
+ Changed WFS/WMS namespace from `BAG3D_v2` to `BAG3D`.
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
+ BAG date/time attributes in GPKG output are of the string type.
+ Missing tiles from download page: `7/1008/656`, `8/720/344`, `9/1000/1068`. The 3D BAG viewer may have some additional tiles missing.
+ Small number of 3D models have invalid geometry. This affects less than 1% of the models.

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
