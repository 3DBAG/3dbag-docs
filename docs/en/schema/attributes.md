# Data Attributes


## `_semantics_values`

Building surface semantics. This is an array of integers, where an integer refers to a surface type (0: `GroundSurface`, 1: `RoofSurface`, 2: `OuterWallSurface`, 3: `InnerWallSurface`). If a surface does not have a semantic value, NULL is used instead. Thus the length of the array equals the number of surfaces, and the order of values in the array corresponds to the order of surfaces.

*Data type*: list

*Unit*: -


## `begingeldigheid`

Relates to the building registration history and version.

*Data type*: date

*Unit*: `YYYY-MM-DD`

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `dak_type`

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
| `no planes` | Could not detect a roof surface, even though points were found. |

## `dd_id`

Dak Deel ID. Roofpart ID.

*Data type*: nominal number

*Unit*: -


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


## `fid`

Numeric ID of a building (feature).

*Data type*: nominal number

*Unit*: -


## `geconstateerd`

Indicates that the buildings has included in the BAG registration.

*Data type*: categorical

*Unit*: yes/no

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `gid`

Geometry ID.

*Data type*: nominal number

*Unit*: -


## `h_dak_50p`

Elevation above sea level (NAP) at rooflevel. Calculated as the median of all elevation points on the corresponding roofpart.

*Data type*: real number

*Unit*: metre


## `h_dak_70p`

Elevation above sea level (NAP) at rooflevel. Calculated as the 70th percentile of all elevation points on the corresponding roofpart.

*Data type*: real number

*Unit*: metre


## `h_dak_max`

Elevation above sea level (NAP) at rooflevel. Calculated as the maximum of all elevation points on the corresponding roofpart.

*Data type*: real number

*Unit*: metre


## `h_dak_min`

Elevation above sea level (NAP) at rooflevel. Calculated as the minimum of all elevation points on the corresponding roofpart.

*Data type*: real number

*Unit*: metre


## `h_maaiveld`

Elevation above sea level (Amsterdam Ordnance Datum) at the ground level of the building. Calculated as the 5th percentile of the ground points found within a 4 meter radius of the building.

*Data type*: real number

*Unit*: metre


## `identificatie`

ID of a building.

*Data type*: text

*Unit*: -

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `kas_warenhuis`

The building is greenhouse or warehouse (according to TOP10NL).

*Data type*: categorical

*Unit*: yes/no


## `lod11_replace`

Indicates whether the LoD1.3/LoD2.2 reconstruction was skipped for this feature (and also LoD1.1 reconstruction if `lod11_replace==false`). This can happen when there were no points found for the building.

*Data type*: categorical

*Unit*: yes/no


## `ondergronds_type`

Underground classification of the building or building part.

*Data type*: categorical

*Unit*: -

*Values*:

| Values | Description |
| :---- | :---------- |
| `floating` | Building or building part is floating above other objects. |
| `above ground` | Building or building part is completely above ground. |
| `underground` | Building or building part is completely under ground.  |

## `oorspronkelijk_bouwjaar`

Building construction year.

*Data type*: date

*Unit*: `YYYY`

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `pand_deel_id`

Buildingpart ID. A building can have multiple parts when it was cut into parts because of underground parts.

*Data type*: nominal number

*Unit*: -


## `pw_actueel`

Indicates that the point cloud is actual w.r.t. the age of the building.

*Data type*: categorical

*Unit*: -

*Values*:

| Values | Description |
| :---- | :---------- |
| `yes` | The point cloud was acquired after the construction date of the building. |
| `no` | The point cloud was acquired before the construction date of the building. |
| `uncertain` | The point cloud was acquired in the same year as the construction date of the building. |

## `pw_bron`

Source of the point cloud.

*Data type*: text

*Unit*: -


## `pw_datum`

Acquisition date of the point cloud. In case of the AHN3, this is an assumed acquisition date, which is computed as 1st of December in the year *before* the officially reported acquisition year (inwinjaar) of a particular AHN3 tile.

*Data type*: date

*Unit*: `YYYY-MM-DD`


## `reconstructie_methode`

Reconstruction method of the building model.

*Data type*: text

*Unit*: -


## `reconstruction_skipped`

Indicates whether full LoD1.2/LoD1.3/LoD2.2 reconstruction was skipped for this feature (and also LoD1.1 if lod11_replace==false).

*Data type*: categorical

*Unit*: yes/no


## `status`

The current fase in the buildings life-cycle.

*Data type*: categorical

*Unit*: -

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)

*Values*:

| Values | Description |
| :---- | :---------- |
| `Bouwvergunning verleend` |  |
| `Niet gerealiseerd pand` |  |
| `Bouw gestart` |  |
| `Pand in gebruik (niet ingemeten)` |  |
| `Pand in gebruik` |  |
| `Verbouwing pand` |  |
| `Sloopvergunning verleend` |  |
| `Pand gesloopt` |  |
| `Pand buiten gebruik` |  |
| `Pand ten onrechte opgevoerd` |  |

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


## `tijdstipregistratielv`

Relates to the building registration history and version.

*Data type*: date-time

*Unit*: `YYYY-MM-DDThh:mm:ss.sss`

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `val3dity_codes`

[Val3dity error codes](https://val3dity.readthedocs.io/en/latest/errors) for the 3D model. `Null` means valid geometry.

*Data type*: list

*Unit*: -


## `versie_methode`

Version of the building reconstruction method.

*Data type*: text

*Unit*: -


## `voorkomenidentificatie`

Relates to the building registration history and version.

*Data type*: ordinal number

*Unit*: -

*Source*: BAG. See [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)

