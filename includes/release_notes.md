## 2024.02.28 – beta

*Release date: 28 February 2024*

The most notable change with this release is the addition of the `b3_bouwlagen` attribute that estimates the number of floors of a building. This is based on the [work of Ellie Roy](https://repository.tudelft.nl/islandora/object/uuid%3A6de4255c-ab2b-49c2-a282-ed779de092a1), which was adapted for and integrated into the 3DBAG generation pipeline. For now only predictions up to 5 floors are available due to the reduced accuracy of the prediction model for higher buildings. Furthermore, due to certain constraints in the building features, predictions for the number of floors are missing for some lower-height buildings but they will become available in a future release.

A number of bug fixes is also included in this release. See below for the full details.

#### Changed / Fixed
+ Updated BAG source data. See the [Metadata for the details](https://3dbag.nl/en/download#metadata).
+ Fix polygons with duplicate vertices prior to triangulation, this reduces significantly the number missing faces for buildings in the OBJ output and in the 3D viewer.
+ Fix incorrect semantic labels for ground and roof surfaces in OBJ and GPKG outputs (`labels` attribute).
+ Update CityJSON outputs to CityJSON v2.0
+ Added the `PointOfContact` information, 3DBAG `version` and a link to the full metadata file in the metadata object of CityJSON outputs.
+ Old versions of 3DBAG are now more easily accessible

#### Added
+ New attribute `b3_bouwlagen`
+ New attribute `b3_kwaliteitsindicator`
+ New attribute `b3_azimut` for LoD 2.2 roofparts in GPKG 2D layers
+ New attribute `b3_hellingshoek` for LoD 2.2 roofparts in GPKG 2D layers
+ From now on each 3DBAG release will come with a quality report

#### Known issues
+ BAG date/time attributes in GPKG output are of the string type.
+ Attributes `b3_kwaliteitsindicator`, `b3_azimut`, `b3_hellingshoek` are currently missing from the CityJSON output
+ The following tiles have incomplete data in the GPKG format (missing layers): XX
+ The following tiles are completely missing: XX
+ A number of 3D models have invalid geometry. This affects less than 1% of the models.

## 2023.10.08 – beta

*Release date: 18 October 2023*

The most notable changes with this release are the addition of attributes with estimates for the area of various surfaces types (e.g. party wall, exterior wall, roof, floor), and the introduction of a new experimental RESTful API at [`api.3dbag.nl`](https://api.3dbag.nl). The new API returns the full 3D geometry as well as all the attributes in the [CityJSONFeatures format](https://www.cityjson.org/specs/2.0.0/#text-sequences-and-streaming-with-cityjsonfeature). The WFS/WMS api's will remain available as well. 

A number of bug fixes is also included in this release. See below for the full details.

#### Changed / Fixed

+ Updated BAG source data. See the [Metadata for the details](https://3dbag.nl/en/download#metadata).
+ Fix [an error](https://geoforum.nl/t/discrepancies-between-3d-bag-version-21-09-8-and-the-ahn3-dataset/8513/4?u=ylannl) with the `b3_mutatie_ahn3_ahn4` attribute due to an issue with our AHN3 input tiles. This only affects a small number of buildings.
+ Improve visual appearance of buildings that originate from overlapping BAG polygons.
+ Fix duplicate objects in the GPKG dump.
+ Added semantic surface labels back into the GPKG files (3D layers only) in the `labels` attribute. Previously this attribute was called `semantic_values`.
+ Removed old API endpoint `https://data.3dbag.nl/api/BAG3D_v2`

#### Added

+ New 3D API at [`api.3dbag.nl`](https://api.3dbag.nl) that returns [CityJSONFeatures](https://www.cityjson.org/specs/2.0.0/#text-sequences-and-streaming-with-cityjsonfeature) with 3D geometry. This beta version of the API is currently not OGC-compliant, but we aim for compliance in a later release. 
+ `b3_bag_bag_overlap` attribute, which is the area (m2) of overlap between BAG polygons
+ The following attributes were added in a project funded by the Rijksdienst voor Ondernemend Nederland (RVO). In this project, a method was implemented to calculate the volume of each 3DBAG building, as well as the areas of the wall-, roof- and ground floor- surfaces of each building. For the walls, a distinction was made between surfaces that are in contact with the outside air (outer walls, `buitenmuur`) and those that are not (party walls, `scheidingsmuur`). This was the most challenging part of the project as it required the generation of the geometry of those parts of the walls that are shared with another 3DBAG building. These calculations are all based on the LoD2.2 geometries and it should be noted that the areas refer only to those parts of the buildings that are above ground, as we have no elevation data for the underground parts.
  + `b3_opp_grond`
  + `b3_opp_dak_plat`
  + `b3_opp_dak_schuin`
  + `b3_opp_scheidingsmuur`
  + `b3_opp_buitenmuur`

#### Known issues
+ BAG date/time attributes in GPKG output are of the string type.
+ The following tiles have incomplete data in the GPKG format (missing layers): `9/336/672`, `8/560/352`.
+ The following tiles are completely missing: `7/480/912`, `8/488/560`, `9/476/592`, `10/498/592`, `8/720/344`, `9/424/692`, `10/364/472`, `7/672/192`, `8/256/536`, `7/544/720`, `9/1000/1068`, `9/1000/1072`.
+ Small number of 3D models have invalid geometry. This affects less than 1% of the models.

## 2023.08.09 – beta

*Release date: 9 August 2023*

With this release we fix an error with the attributes `h_dak_min `, `h_dak_50p`, `h_dak_70p`, `h_dak_max` in the GPKG and WFS formats. In 3DBAG version 2023.06.22 the values of these attributes were off by 15 meters. This is fixed in this release.

#### Changed / Fixed
+ Fix 15 meter offset in `h_dak_min `, `h_dak_50p`, `h_dak_70p`, `h_dak_max` attributes on roofparts in GPKG and WFS formats.

## 2023.06.22 – beta

*Release date: 22 June 2023*

This is the third public beta release of the 3DBAG. It's been a while since the second release. As it turns out it costs quite some work to properly maintain and update 3DBAG next to our busy day jobs. Fortunately we were able to receive funding from the ERC to bring the 3DBAG to a level where it can be maintained and developed reliably. The current release is the first of three that is financed by the ERC budget, and it paves the way towards a stable, open 3DBAG service. We are very happy to see that so many people found a use for 3DBAG to help them with their business, research or hobby projects. And we remain committed to keep maintaining 3DBAG into the future, of course as an open dataset. 

[The team behind 3DBAG](group.md) has changed in the sense that some people have moved on to other jobs, others are working on 3DBAG with a different affiliation ([3DGI](https://3dgi.xyz), a spinoff of the [tudelft3d](https://3d.bk.tudelft.nl/) research group) and we also have welcomed a [new member](http://3d.bk.tudelft.nl/gstavropoulou).

The biggest technical change is that the 3DBAG now uses the AHN4 pointcloud which was acquired between 2020 and 2022. This means that the building models are much more up-to-date, compared to the previous release which was based solely on AHN3 (acquired starting from 2014). For this new release we use a 'smart' combination of AHN3 and AHN4. We did not opt for a simple 'drop-in' replacement of AHN3 by AHN4 because of the quality issues that we discovered in AHN4. These issues affect a small, yet significant fraction of the buildings. The 'smart' combination entails that our algorithms automatically select the 'best' available point cloud on a per building basis. The selection is based primarily on point coverage, ie. how well the roof surface of a building is covered with AHN points and *most importantly* if there are any big gaps. Naturally, AHN3 is only considered when a building has not changed compared to the AHN4 data. AHN3 is used for ~8.5% of the buildings, the rest all uses AHN4.

There are also some changes in the BAG viewer and the download page. Most notably, the viewer now brings you to an interesting landmark that is randomly picked when you load the website, and all 3DBAG attributes are now visible in the viewer. The download page now also offers a metadata file about the dataset as a whole (including lineage) and the PostgreSQL dump was replaced by one big GPKG file (something that several people have asked for).

And last, but not least: behind the scenes *a lot of work* has been done to completely recreate our automatic building reconstruction pipeline. This helps us to reliably produce new 3DBAG releases from now on. A tangible benefit to the 3DBAG users is that we now have much fewer missing buildings compared to the previous releases. We will continue to work on our pipeline in the background and streamline our internal processes even further.

This release contains a record number of 10 383 384 builings. The overall geometric val3dity is also at a record at 99.15% (up from 98.25% in the previous release, counted on the LoD2.2 geometries).

Thank you for using the 3DBAG! As always our [feedback forms](https://forms.gle/NZg83heXM75pAmfVA) are available and we are reading all the emails that we receive at info@3dbag.nl.

-- The 3DBAG Team

#### Update 11-07-2023
* Regenerated 3D tiles to fix a number of display issues in the 3D BAG viewer, including incorrect placement of search result marker.

#### Added

+ The building part ID (`pand_deel_id`) to the 3D layers. Previously it was only part of the 2D layers.
+ Reconstruction algorithm
    + added procedure for automatic selection of pointcloud (AHN3 or 4) best suited for reconstruction on a per building basis
    + building areas are now calculated and outputted
    + changed the method for calculating the height attributes on roofparts
+ A metadata file is now available on the download page. The metadata contains information about the current release, including the versions of the source data sets and the versions of the software that were used for producing the release. The metadata file unifies some of the information that were previously scattered across different formats.
+ 3DBAG viewer
    + When opening the 3DBAG viewer you are brought to a random landmark
    + You can now view all attributes directly in the viewer
    + Clicking on the attribute name in the viewer attribute table now brings you to the corresponding section in the documentation
    + Update basemap to Luchfoto Actueel
+ Various quality attributes relating to the 'smart' point cloud selection algorithm.
+ 3DGI attribution
+ Created a [3DBAG twitter account](https://twitter.com/3D_BAG). Follow this to be notified about 3DBAG updates and other announcements.
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
+ 3DBAG version number is now a full date instead of a mix between date and minor version number.
+ All 3DBAG specific attributes are now preceded by the `b3_` prefix.
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
+ Missing tiles from download page: `7/1008/656`, `8/720/344`, `9/1000/1068`. The 3DBAG viewer may have some additional tiles missing.
+ Small number of 3D models have invalid geometry. This affects less than 1% of the models.
+ Some attributes are missing from the WMS/WFS layers.
+ The GPKG data dump has a small number of duplicate features.
+ The GPKG files have incorrect height attributes (`b3_h_*`)

## 21.09.8 – beta

*Release date: 29 September 2021*

This is the second public beta release of the renewed 3DBAG. Before addressing what has changed with this release we would like to take a moment to thank everyone that has been downloading and using the first release. It's very exciting to see how people from various disciplines found ways to apply 3DBAG for their use cases! (also see our new [In the media](media.md) page). A special thanks also to everyone that filled out our feedback forms or gave us feedback in other ways. This is much appreciated!

For this second release we focused primarily on improving the data quality and the way the data is disseminated. The overall geometric validity of the 3D models has risen to 98.25% (up from ~89% in the previous release). Another highlight is that the 3D outputs are no longer triangulated, as requested by several users. Altogether this should make it easier to use our models in other software. These and more changes are described below in more detail. 

This 3DBAG release contains 9 692 978 buildings. This is 7.72% less buildings than available in the BAG dataset, mostly due to outdated or otherwise insufficient input data. We hope to do a release based on the updated AHN4 soon, but this release is still based on AHN3.

Thank you for using 3DBAG!

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
