# Data Attributes


## `b3_dak_type`

Roof type of the building.

*Data type*: categorical

*Unit*: -

*Values*:

| Values | Description |
| :---- | :---------- |
| `slanted` | Roof with at least one slanted surface. |
| `multiple horizontal` | Roof with multiple, only horizontal surfaces. |
| `single horizontal` | Roof with a single horizontal surface. |
| `no points` | No point was found for the building. |
| `could not detect` | Could not detect a roof surface, even though points were found. |

## `b3_dd_id`

Dak Deel ID. Roofpart ID.

*Data type*: nominal number

*Unit*: -


## `b3_h_dak_50p`

Median elevation on roof surface based on reconstructed 3D model in LoD2.2. Given as elevation above sea level (NAP).

*Data type*: real number

*Unit*: metre


## `b3_h_dak_70p`

The 70th percentile elevation on roof surface based on reconstructed 3D model in LoD2.2. Given as elevation above sea level (NAP).

*Data type*: real number

*Unit*: metre


## `b3_h_dak_max`

Maximum elevation on roof surface based on reconstructed 3D model in LoD2.2. Given as elevation above sea level (NAP). Unit: metre.

*Data type*: real number

*Unit*: metre


## `b3_h_dak_min`

Minimum elevation on roof surface based on reconstructed 3D model in LoD2.2. Given as elevation above sea level (NAP).

*Data type*: real number

*Unit*: metre


## `b3_h_maaiveld`

Elevation above sea level (Amsterdam Ordnance Datum) at the ground level of the building. Calculated as the 5th percentile of the ground points found within a 4 meter radius of the building.

*Data type*: real number

*Unit*: metre


## `b3_kas_warenhuis`

The building is greenhouse or warehouse (according to TOP10NL) or has an area of over 70000 square meters.

*Data type*: categorical

*Unit*: yes/no


## `b3_mutatie_ahn3_ahn4`

`true` if there was a significant change detected in the building between the AHN3 and AHN4 pointclouds.

*Data type*: categorical

*Unit*: yes/no


## `b3_nodata_fractie_ahn3`

Fraction of the footprint area that has no point data in the AHN3 point cloud. Only points classified as building or ground are considered.

*Data type*: real number

*Unit*: -


## `b3_nodata_fractie_ahn4`

Fraction of the footprint area that has no point data in the AHN4 point cloud. Only points classified as building or ground are considered.

*Data type*: real number

*Unit*: -


## `b3_nodata_radius_ahn3`

Radius of the largest circle inside the BAG polygon without any AHN3 points. Only points classified as building or ground are considered.

*Data type*: real number

*Unit*: metre


## `b3_nodata_radius_ahn4`

Radius of the largest circle inside the BAG polygon without any AHN4 points. Only points classified as building or ground are considered.

*Data type*: real number

*Unit*: metre


## `b3_pand_deel_id`

Buildingpart ID. A building can have multiple parts when it was cut into parts because of underground parts.

*Data type*: nominal number

*Unit*: -


## `b3_puntdichtheid_ahn3`

Density of the AHN3 point cloud on BAG polygon. Only points classified as building or ground are considered.

*Data type*: nominal number

*Unit*: points per square metre


## `b3_puntdichtheid_ahn4`

Density of the AHN4 point cloud on BAG polygon. Only points classified as building or ground are considered. Unit: points per square metre.

*Data type*: nominal number

*Unit*: points per square metre


## `b3_pw_bron`

Source of the point cloud, eg. AHN3 or AHN4.

*Data type*: text

*Unit*: -


## `b3_pw_datum`

Acquisition year of the point cloud. This is determined by looking at the GPS timestamps on the AHN points for the building. In case good GPS timestamps are not available the file creation date of the point cloud file is used.

*Data type*: date

*Unit*: `YYYY`


## `b3_pw_selectie_reden`

Provides information about the pointcloud selection indicated in the `pw_bron` attribute.

*Data type*: categorical

*Unit*: -

*Values*:

| Values | Description |
| :---- | :---------- |
| ``PREFERRED_AND_LATEST`` | The selected point cloud has a good point coverage and there are no newer point clouds available that also have good point coverage. |
| ``PREFERRED_NOT_LATEST`` | The selected point cloud has a good point coverage and there is a newer point cloud available that also has good coverage. Newer pointcloud was not selected because no mutation was detected. |
| ``LATEST_WITH_MUTATION`` | The selected point cloud has a good point coverage and a mutation was detected compared to the older pointclouds. |
| ``_HIGHEST_YET_INSUFFICIENT_COVERAGE`` | The selected point cloud has possible poor point coverage. Nonetheless, it is the point cloud with the highest point coverage among all available point clouds. |
| ``_LATEST_BUT_OUTDATED`` | The selected pointcloud is the latest one available, but it may be outdated for this building. This happens when the year of construction is equal or later than the point cloud acquisition date. |

## `b3_reconstructie_onvolledig`

Indicates whether full LoD1.2/LoD1.3/LoD2.2 reconstruction was skipped for this feature.

*Data type*: None

*Unit*: None


## `b3_rmse_lod12`

Root Mean Square Error of the 3D distances between the point cloud and the LoD1.2 model. Unit: metre.

*Data type*: real number

*Unit*: metre


## `b3_rmse_lod13`

Root Mean Square Error of the 3D distances between the point cloud and the LoD1.3 model. Unit: metre.

*Data type*: real number

*Unit*: metre


## `b3_rmse_lod22`

Root Mean Square Error of the 3D distances between the point cloud and the LoD2.2 model. Unit: metre.

*Data type*: real number

*Unit*: metre


## `b3_val3dity_lod12`

[Val3dity error codes](https://val3dity.readthedocs.io/en/latest/errors) for the LoD1.2 3D model. Empty list means valid geometry.

*Data type*: list

*Unit*: -


## `b3_val3dity_lod13`

[Val3dity error codes](https://val3dity.readthedocs.io/en/latest/errors) for the LoD1.3 3D model. Empty list means valid geometry.

*Data type*: list

*Unit*: -


## `b3_val3dity_lod22`

[Val3dity error codes](https://val3dity.readthedocs.io/en/latest/errors) for the LoD2.2 3D model. Empty list means valid geometry.

*Data type*: list

*Unit*: -


## `b3_volume_lod12`

Volume of the LoD1.2 model. Unit: cubic metre.

*Data type*: real number

*Unit*: cubic metre


## `b3_volume_lod13`

Volume of the LoD1.3 model. Unit: cubic metre.

*Data type*: real number

*Unit*: cubic metre


## `b3_volume_lod22`

Volume of the LoD2.2 model. Unit: cubic metre.

*Data type*: real number

*Unit*: cubic metre


## `begingeldigheid`

Relates to the building registration history and version.

*Data type*: date

*Unit*: `YYYY-MM-DD`

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `documentdatum`

Building registration date.

*Data type*: date

*Unit*: `YYYY-MM-DD`

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `documentnummer`

Document number.

*Data type*: text

*Unit*: `YYYY-MM-DD`

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `eindgeldigheid`

Relates to the building registration history and version.

*Data type*: date

*Unit*: `YYYY-MM-DD`

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `eindregistratie`

Relates to the building registration history and version.

*Data type*: date-time

*Unit*: `YYYY-MM-DDThh:mm:ss.sss`

*Source*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `geconstateerd`

Indicates that the buildings has included in the BAG registration.

*Data type*: categorical

*Unit*: yes/no

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `identificatie`

ID of a building.

*Data type*: text

*Unit*: -

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `oorspronkelijkbouwjaar`

Building construction year.

*Data type*: date

*Unit*: `YYYY`


## `status`

The current fase in the buildings life-cycle.

*Data type*: categorical

*Unit*: -

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `tijdstipeindregistratielv`

Relates to the building registration history and version.

*Data type*: date-time

*Unit*: `YYYY-MM-DDThh:mm:ss.sss`

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `tijdstipinactief`

Relates to the building registration history and version.

*Data type*: date-time

*Unit*: `YYYY-MM-DDThh:mm:ss.sss`

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `tijdstipinactieflv`

Relates to the building registration history and version.

*Data type*: date-time

*Unit*: `YYYY-MM-DDThh:mm:ss.sss`

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `tijdstipnietbaglv`

Relates to the building registration history and version.

*Data type*: date-time

*Unit*: `YYYY-MM-DDThh:mm:ss.sss`

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `tijdstipregistratie`

Relates to the building registration history and version.

*Data type*: date-time

*Unit*: `YYYY-MM-DDThh:mm:ss.sss`

*Source*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `tijdstipregistratielv`

Relates to the building registration history and version.

*Data type*: date-time

*Unit*: `YYYY-MM-DDThh:mm:ss.sss`

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `voorkomenidentificatie`

Relates to the building registration history and version.

*Data type*: ordinal number

*Unit*: -

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)

