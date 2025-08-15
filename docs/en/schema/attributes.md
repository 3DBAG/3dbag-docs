# Data Attributes

Attributes specification file and schema: [https://downloads.3dbag.nl](https://downloads.3dbag.nl)

## `b3_pand_deel_id`

| Property      | Value                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------|
| Description   | Buildingpart ID. A building can have multiple parts when it was cut into parts because of underground parts. |
| Source        | roofer                                                                                                       |
| Data Type     | INT                                                                                                          |
| Unit          | -                                                                                                            |
| Scale         | nominal number                                                                                               |
| Precision     | -                                                                                                            |
| Value Format  | `-`                                                                                                          |
| Nullable      | False                                                                                                        |
| Semantic Type | identifier                                                                                                   |

**Data Format Specifications**

| Data Format   | Property   | Value                                                      |
|---------------|------------|------------------------------------------------------------|
| GeoPackage    | Locations  | lod13_3d, lod12_2d, lod22_2d, lod22_3d, lod13_2d, lod12_3d |
| GeoPackage    | Data Type  | INTEGER                                                    |

## `b3_dd_id`

| Property      | Value                     |
|---------------|---------------------------|
| Description   | Dak Deel ID. Roofpart ID. |
| Source        | roofer                    |
| Data Type     | INT                       |
| Unit          | -                         |
| Scale         | nominal number            |
| Precision     | -                         |
| Value Format  | `-`                       |
| Nullable      | False                     |
| Semantic Type | identifier                |

**Data Format Specifications**

| Data Format   | Property   | Value                        |
|---------------|------------|------------------------------|
| GeoPackage    | Locations  | lod22_2d, lod12_2d, lod13_2d |
| GeoPackage    | Data Type  | INTEGER                      |

## `identificatie`

| Property      | Value             |
|---------------|-------------------|
| Description   | ID of a building. |
| Source        | BAG,roofer        |
| Data Type     | STRING            |
| Unit          | -                 |
| Scale         | text              |
| Precision     | -                 |
| Value Format  | `-`               |
| Nullable      | False             |
| Semantic Type | identifier        |

**Data Format Specifications**

| Data Format   | Property   | Value                                                            |
|---------------|------------|------------------------------------------------------------------|
| CityJSON      | Locations  | Building                                                         |
| CityJSON      | Data Type  | string                                                           |
| GeoPackage    | Locations  | lod13_3d, lod12_2d, pand, lod22_2d, lod22_3d, lod13_2d, lod12_3d |
| GeoPackage    | Data Type  | TEXT                                                             |

## `oorspronkelijkbouwjaar`

| Property      | Value                       |
|---------------|-----------------------------|
| Description   | Building construction year. |
| Source        | BAG                         |
| Data Type     | INT                         |
| Unit          | -                           |
| Scale         | interval                    |
| Precision     | -                           |
| Value Format  | `YYYY`                      |
| Nullable      | True                        |
| Semantic Type | year                        |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | INTEGER  |

## `status`

| Property      | Value                                         |
|---------------|-----------------------------------------------|
| Description   | The current fase in the buildings life-cycle. |
| Source        | BAG                                           |
| Data Type     | STRING                                        |
| Unit          | -                                             |
| Scale         | categorical                                   |
| Precision     | -                                             |
| Value Format  | `-`                                           |
| Nullable      | -                                             |
| Semantic Type | category                                      |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | TEXT     |

## `geconstateerd`

| Property      | Value                                                              |
|---------------|--------------------------------------------------------------------|
| Description   | Indicates that the buildings has included in the BAG registration. |
| Source        | -                                                                  |
| Data Type     | STRING                                                             |
| Unit          | -                                                                  |
| Scale         | nominal                                                            |
| Precision     | -                                                                  |
| Value Format  | `-`                                                                |
| Nullable      | -                                                                  |
| Semantic Type | flag                                                               |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | TEXT     |

## `documentdatum`

| Property      | Value                       |
|---------------|-----------------------------|
| Description   | Building registration date. |
| Source        | -                           |
| Data Type     | DATE                        |
| Unit          | -                           |
| Scale         | interval                    |
| Precision     | -                           |
| Value Format  | `YYYY-MM-DD`                |
| Nullable      | -                           |
| Semantic Type | day                         |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | DATE     |

## `documentnummer`

| Property      | Value            |
|---------------|------------------|
| Description   | Document number. |
| Source        | -                |
| Data Type     | STRING           |
| Unit          | -                |
| Scale         | text             |
| Precision     | -                |
| Value Format  | `-`              |
| Nullable      | -                |
| Semantic Type | identifier       |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | TEXT     |

## `voorkomenidentificatie`

| Property      | Value                                                     |
|---------------|-----------------------------------------------------------|
| Description   | Relates to the building registration history and version. |
| Source        | BAG                                                       |
| Data Type     | INT                                                       |
| Unit          | -                                                         |
| Scale         | ordinal number                                            |
| Precision     | -                                                         |
| Value Format  | `-`                                                       |
| Nullable      | -                                                         |
| Semantic Type | identifier                                                |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | INTEGER  |

## `begingeldigheid`

| Property      | Value                                                     |
|---------------|-----------------------------------------------------------|
| Description   | Relates to the building registration history and version. |
| Source        | BAG                                                       |
| Data Type     | DATE                                                      |
| Unit          | -                                                         |
| Scale         | interval                                                  |
| Precision     | -                                                         |
| Value Format  | `YYYY-MM-DD`                                              |
| Nullable      | -                                                         |
| Semantic Type | day                                                       |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | DATE     |

## `eindgeldigheid`

| Property      | Value                                                     |
|---------------|-----------------------------------------------------------|
| Description   | Relates to the building registration history and version. |
| Source        | BAG                                                       |
| Data Type     | DATE                                                      |
| Unit          | -                                                         |
| Scale         | interval                                                  |
| Precision     | -                                                         |
| Value Format  | `YYYY-MM-DD`                                              |
| Nullable      | -                                                         |
| Semantic Type | day                                                       |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | DATE     |

## `tijdstipregistratie`

| Property      | Value                                                     |
|---------------|-----------------------------------------------------------|
| Description   | Relates to the building registration history and version. |
| Source        | BAG                                                       |
| Data Type     | DATETIME                                                  |
| Unit          | -                                                         |
| Scale         | interval                                                  |
| Precision     | -                                                         |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                 |
| Nullable      | -                                                         |
| Semantic Type | millisecond                                               |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | DATETIME |

## `eindregistratie`

| Property      | Value                                                     |
|---------------|-----------------------------------------------------------|
| Description   | Relates to the building registration history and version. |
| Source        | BAG                                                       |
| Data Type     | DATETIME                                                  |
| Unit          | -                                                         |
| Scale         | interval                                                  |
| Precision     | -                                                         |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                 |
| Nullable      | -                                                         |
| Semantic Type | millisecond                                               |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | DATETIME |

## `tijdstipinactief`

| Property      | Value                                                     |
|---------------|-----------------------------------------------------------|
| Description   | Relates to the building registration history and version. |
| Source        | BAG                                                       |
| Data Type     | DATETIME                                                  |
| Unit          | -                                                         |
| Scale         | interval                                                  |
| Precision     | -                                                         |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                 |
| Nullable      | -                                                         |
| Semantic Type | millisecond                                               |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | DATETIME |

## `tijdstipregistratielv`

| Property      | Value                                                     |
|---------------|-----------------------------------------------------------|
| Description   | Relates to the building registration history and version. |
| Source        | BAG                                                       |
| Data Type     | DATETIME                                                  |
| Unit          | -                                                         |
| Scale         | interval                                                  |
| Precision     | -                                                         |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                 |
| Nullable      | -                                                         |
| Semantic Type | millisecond                                               |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | DATETIME |

## `tijdstipeindregistratielv`

| Property      | Value                                                     |
|---------------|-----------------------------------------------------------|
| Description   | Relates to the building registration history and version. |
| Source        | BAG                                                       |
| Data Type     | DATETIME                                                  |
| Unit          | -                                                         |
| Scale         | interval                                                  |
| Precision     | -                                                         |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                 |
| Nullable      | -                                                         |
| Semantic Type | millisecond                                               |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | DATETIME |

## `tijdstipinactieflv`

| Property      | Value                                                     |
|---------------|-----------------------------------------------------------|
| Description   | Relates to the building registration history and version. |
| Source        | BAG                                                       |
| Data Type     | DATETIME                                                  |
| Unit          | -                                                         |
| Scale         | interval                                                  |
| Precision     | -                                                         |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                 |
| Nullable      | -                                                         |
| Semantic Type | millisecond                                               |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | DATETIME |

## `tijdstipnietbaglv`

| Property      | Value                                                     |
|---------------|-----------------------------------------------------------|
| Description   | Relates to the building registration history and version. |
| Source        | BAG                                                       |
| Data Type     | DATETIME                                                  |
| Unit          | -                                                         |
| Scale         | interval                                                  |
| Precision     | -                                                         |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                 |
| Nullable      | -                                                         |
| Semantic Type | millisecond                                               |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | DATETIME |

## `b3_h_maaiveld`

| Property      | Value                                                                                                                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Elevation above sea level (Amsterdam Ordnance Datum) at the ground level of the building. Calculated as the 5th percentile of the ground points found within a 4 meter radius of the building. |
| Source        | -                                                                                                                                                                                              |
| Data Type     | FLOAT                                                                                                                                                                                          |
| Unit          | metre                                                                                                                                                                                          |
| Scale         | ratio                                                                                                                                                                                          |
| Precision     | -                                                                                                                                                                                              |
| Value Format  | `-`                                                                                                                                                                                            |
| Nullable      | -                                                                                                                                                                                              |
| Semantic Type | elevation                                                                                                                                                                                      |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_dak_type`

| Property      | Value                      |
|---------------|----------------------------|
| Description   | Roof type of the building. |
| Source        | -                          |
| Data Type     | STRING                     |
| Unit          | -                          |
| Scale         | categorical                |
| Precision     | -                          |
| Value Format  | `-`                        |
| Nullable      | -                          |
| Semantic Type | category                   |

**Attribute Values**

| Attribute Value       | Description                                                     |
|-----------------------|-----------------------------------------------------------------|
| `slanted`             | Roof with at least one slanted surface.                         |
| `multiple horizontal` | Roof with multiple, only horizontal surfaces.                   |
| `single horizontal`   | Roof with a single horizontal surface.                          |
| `no points`           | No point was found for the building.                            |
| `could not detect`    | Could not detect a roof surface, even though points were found. |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | TEXT     |

## `b3_pw_datum`

| Property      | Value                                                                                                                                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Acquisition year of the point cloud. This is determined by looking at the GPS timestamps on the AHN points for the building. In case good GPS timestamps are not available the file creation date of the point cloud file is used. |
| Source        | -                                                                                                                                                                                                                                  |
| Data Type     | INT                                                                                                                                                                                                                                |
| Unit          | -                                                                                                                                                                                                                                  |
| Scale         | interval                                                                                                                                                                                                                           |
| Precision     | -                                                                                                                                                                                                                                  |
| Value Format  | `YYYY`                                                                                                                                                                                                                             |
| Nullable      | False                                                                                                                                                                                                                              |
| Semantic Type | year                                                                                                                                                                                                                               |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | INTEGER  |

## `b3_pw_bron`

| Property      | Value                                        |
|---------------|----------------------------------------------|
| Description   | Source of the point cloud, eg. AHN3 or AHN4. |
| Source        | -                                            |
| Data Type     | STRING                                       |
| Unit          | -                                            |
| Scale         | text                                         |
| Precision     | -                                            |
| Value Format  | `-`                                          |
| Nullable      | -                                            |
| Semantic Type | text                                         |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | TEXT     |

## `b3_kas_warenhuis`

| Property      | Value                                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------|
| Description   | The building is greenhouse or warehouse (according to TOP10NL) or has an area of over 70000 square meters. |
| Source        | -                                                                                                          |
| Data Type     | BOOL                                                                                                       |
| Unit          | -                                                                                                          |
| Scale         | nominal                                                                                                    |
| Precision     | -                                                                                                          |
| Value Format  | `-`                                                                                                        |
| Nullable      | -                                                                                                          |
| Semantic Type | flag                                                                                                       |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | boolean  |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | BOOLEAN  |

## `b3_reconstructie_onvolledig`

| Property      | Value                                                                                    |
|---------------|------------------------------------------------------------------------------------------|
| Description   | Indicates whether full LoD1.2/LoD1.3/LoD2.2 reconstruction was skipped for this feature. |
| Source        | -                                                                                        |
| Data Type     | BOOL                                                                                     |
| Unit          | -                                                                                        |
| Scale         | nominal                                                                                  |
| Precision     | -                                                                                        |
| Value Format  | `-`                                                                                      |
| Nullable      | -                                                                                        |
| Semantic Type | flag                                                                                     |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | boolean  |

## `b3_h_dak_min`

| Property      | Value                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------|
| Description   | Minimum elevation on roof surface based on reconstructed 3D model in LoD2.2. Given as elevation above sea level (NAP). |
| Source        | -                                                                                                                      |
| Data Type     | FLOAT                                                                                                                  |
| Unit          | metre                                                                                                                  |
| Scale         | ratio                                                                                                                  |
| Precision     | -                                                                                                                      |
| Value Format  | `-`                                                                                                                    |
| Nullable      | -                                                                                                                      |
| Semantic Type | elevation                                                                                                              |

**Data Format Specifications**

| Data Format   | Property   | Value                 |
|---------------|------------|-----------------------|
| CityJSON      | Locations  | RoofSurface, Building |
| CityJSON      | Data Type  | number                |

## `b3_h_dak_50p`

| Property      | Value                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------|
| Description   | Median elevation on roof surface based on reconstructed 3D model in LoD2.2. Given as elevation above sea level (NAP). |
| Source        | -                                                                                                                     |
| Data Type     | FLOAT                                                                                                                 |
| Unit          | metre                                                                                                                 |
| Scale         | ratio                                                                                                                 |
| Precision     | -                                                                                                                     |
| Value Format  | `-`                                                                                                                   |
| Nullable      | -                                                                                                                     |
| Semantic Type | elevation                                                                                                             |

**Data Format Specifications**

| Data Format   | Property   | Value                 |
|---------------|------------|-----------------------|
| CityJSON      | Locations  | RoofSurface, Building |
| CityJSON      | Data Type  | number                |

## `b3_h_dak_70p`

| Property      | Value                                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------|
| Description   | The 70th percentile elevation on roof surface based on reconstructed 3D model in LoD2.2. Given as elevation above sea level (NAP). |
| Source        | -                                                                                                                                  |
| Data Type     | FLOAT                                                                                                                              |
| Unit          | metre                                                                                                                              |
| Scale         | ratio                                                                                                                              |
| Precision     | -                                                                                                                                  |
| Value Format  | `-`                                                                                                                                |
| Nullable      | -                                                                                                                                  |
| Semantic Type | elevation                                                                                                                          |

**Data Format Specifications**

| Data Format   | Property   | Value                 |
|---------------|------------|-----------------------|
| CityJSON      | Locations  | RoofSurface, Building |
| CityJSON      | Data Type  | number                |

## `b3_h_dak_max`

| Property      | Value                                                                                                                               |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Maximum elevation on roof surface based on reconstructed 3D model in LoD2.2. Given as elevation above sea level (NAP). Unit: metre. |
| Source        | -                                                                                                                                   |
| Data Type     | FLOAT                                                                                                                               |
| Unit          | metre                                                                                                                               |
| Scale         | ratio                                                                                                                               |
| Precision     | -                                                                                                                                   |
| Value Format  | `-`                                                                                                                                 |
| Nullable      | -                                                                                                                                   |
| Semantic Type | elevation                                                                                                                           |

**Data Format Specifications**

| Data Format   | Property   | Value                 |
|---------------|------------|-----------------------|
| CityJSON      | Locations  | RoofSurface, Building |
| CityJSON      | Data Type  | number                |

## `b3_val3dity_lod12`

| Property      | Value                                                                                                                                 |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Description   | [Val3dity error codes](https://val3dity.readthedocs.io/2.5.1/errors.html) for the LoD1.2 3D model. An empty list means valid geometry. |
| Source        | -                                                                                                                                     |
| Data Type     | ARRAY<INT>                                                                                                                            |
| Unit          | -                                                                                                                                     |
| Scale         | -                                                                                                                                     |
| Precision     | -                                                                                                                                     |
| Value Format  | `-`                                                                                                                                   |
| Nullable      | False                                                                                                                                 |
| Semantic Type | list                                                                                                                                  |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | array    |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | TEXT     |

## `b3_val3dity_lod13`

| Property      | Value                                                                                                                                 |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Description   | [Val3dity error codes](https://val3dity.readthedocs.io/2.5.1/errors.html) for the LoD1.3 3D model. An empty list means valid geometry. |
| Source        | -                                                                                                                                     |
| Data Type     | ARRAY<INT>                                                                                                                            |
| Unit          | -                                                                                                                                     |
| Scale         | -                                                                                                                                     |
| Precision     | -                                                                                                                                     |
| Value Format  | `-`                                                                                                                                   |
| Nullable      | False                                                                                                                                 |
| Semantic Type | list                                                                                                                                  |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | array    |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | TEXT     |

## `b3_val3dity_lod22`

| Property      | Value                                                                                                                                 |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Description   | [Val3dity error codes](https://val3dity.readthedocs.io/2.5.1/errors.html) for the LoD2.2 3D model. An empty list means valid geometry. |
| Source        | -                                                                                                                                     |
| Data Type     | ARRAY<INT>                                                                                                                            |
| Unit          | -                                                                                                                                     |
| Scale         | -                                                                                                                                     |
| Precision     | -                                                                                                                                     |
| Value Format  | `-`                                                                                                                                   |
| Nullable      | False                                                                                                                                 |
| Semantic Type | list                                                                                                                                  |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | array    |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | TEXT     |

## `b3_rmse_lod12`

| Property      | Value                                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------|
| Description   | Root Mean Square Error of the 3D distances between the point cloud and the LoD1.2 model. Unit: metre. |
| Source        | -                                                                                                     |
| Data Type     | FLOAT                                                                                                 |
| Unit          | metre                                                                                                 |
| Scale         | ratio                                                                                                 |
| Precision     | -                                                                                                     |
| Value Format  | `-`                                                                                                   |
| Nullable      | -                                                                                                     |
| Semantic Type | error                                                                                                 |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_rmse_lod13`

| Property      | Value                                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------|
| Description   | Root Mean Square Error of the 3D distances between the point cloud and the LoD1.3 model. Unit: metre. |
| Source        | -                                                                                                     |
| Data Type     | FLOAT                                                                                                 |
| Unit          | metre                                                                                                 |
| Scale         | ratio                                                                                                 |
| Precision     | -                                                                                                     |
| Value Format  | `-`                                                                                                   |
| Nullable      | -                                                                                                     |
| Semantic Type | error                                                                                                 |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_rmse_lod22`

| Property      | Value                                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------|
| Description   | Root Mean Square Error of the 3D distances between the point cloud and the LoD2.2 model. Unit: metre. |
| Source        | -                                                                                                     |
| Data Type     | FLOAT                                                                                                 |
| Unit          | metre                                                                                                 |
| Scale         | ratio                                                                                                 |
| Precision     | -                                                                                                     |
| Value Format  | `-`                                                                                                   |
| Nullable      | -                                                                                                     |
| Semantic Type | error                                                                                                 |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_mutatie_ahn3_ahn4`

| Property      | Value                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------|
| Description   | `true` if there was a significant change detected in the building between the AHN3 and AHN4 pointclouds. |
| Source        | -                                                                                                        |
| Data Type     | BOOL                                                                                                     |
| Unit          | -                                                                                                        |
| Scale         | nominal                                                                                                  |
| Precision     | -                                                                                                        |
| Value Format  | `-`                                                                                                      |
| Nullable      | -                                                                                                        |
| Semantic Type | flag                                                                                                     |

**Attribute Values**

| Attribute Value   | Description                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------|
| `true`            | There was a significant change detected in the building between the AHN3 and AHN4 pointclouds.  |
| `false`           | There was no significant change detected in the building between the AHN3 and AHN4 pointclouds. |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | boolean  |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | BOOLEAN  |

## `b3_nodata_fractie_ahn3`

| Property      | Value                                                                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Fraction of the footprint area that has no point data in the AHN3 point cloud. Only points classified as building or ground are considered. |
| Source        | -                                                                                                                                           |
| Data Type     | FLOAT                                                                                                                                       |
| Unit          | -                                                                                                                                           |
| Scale         | ratio                                                                                                                                       |
| Precision     | -                                                                                                                                           |
| Value Format  | `-`                                                                                                                                         |
| Nullable      | -                                                                                                                                           |
| Semantic Type | fraction                                                                                                                                    |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_nodata_fractie_ahn4`

| Property      | Value                                                                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Fraction of the footprint area that has no point data in the AHN4 point cloud. Only points classified as building or ground are considered. |
| Source        | -                                                                                                                                           |
| Data Type     | FLOAT                                                                                                                                       |
| Unit          | -                                                                                                                                           |
| Scale         | ratio                                                                                                                                       |
| Precision     | -                                                                                                                                           |
| Value Format  | `-`                                                                                                                                         |
| Nullable      | -                                                                                                                                           |
| Semantic Type | fraction                                                                                                                                    |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_nodata_radius_ahn3`

| Property      | Value                                                                                                                                     |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Radius of the largest circle inside the BAG polygon without any AHN3 points. Only points classified as building or ground are considered. |
| Source        | -                                                                                                                                         |
| Data Type     | FLOAT                                                                                                                                     |
| Unit          | metre                                                                                                                                     |
| Scale         | ratio                                                                                                                                     |
| Precision     | -                                                                                                                                         |
| Value Format  | `-`                                                                                                                                       |
| Nullable      | -                                                                                                                                         |
| Semantic Type | length                                                                                                                                    |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_nodata_radius_ahn4`

| Property      | Value                                                                                                                                     |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Radius of the largest circle inside the BAG polygon without any AHN4 points. Only points classified as building or ground are considered. |
| Source        | -                                                                                                                                         |
| Data Type     | FLOAT                                                                                                                                     |
| Unit          | metre                                                                                                                                     |
| Scale         | ratio                                                                                                                                     |
| Precision     | -                                                                                                                                         |
| Value Format  | `-`                                                                                                                                       |
| Nullable      | -                                                                                                                                         |
| Semantic Type | length                                                                                                                                    |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_pw_selectie_reden`

| Property      | Value                                                                                     |
|---------------|-------------------------------------------------------------------------------------------|
| Description   | Provides information about the pointcloud selection indicated in the `pw_bron` attribute. |
| Source        | -                                                                                         |
| Data Type     | STRING                                                                                    |
| Unit          | -                                                                                         |
| Scale         | categorical                                                                               |
| Precision     | -                                                                                         |
| Value Format  | `-`                                                                                       |
| Nullable      | -                                                                                         |
| Semantic Type | category                                                                                  |

**Attribute Values**

| Attribute Value                      | Description                                                                                                                                                                                        |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PREFERRED_AND_LATEST`               | The selected point cloud has a good point coverage and there are no newer point clouds available that also have good point coverage.                                                               |
| `PREFERRED_NOT_LATEST`               | The selected point cloud has a good point coverage and there is a newer point cloud available that also has good coverage. Newer pointcloud was not selected because no mutation was detected.     |
| `LATEST_WITH_MUTATION`               | The selected point cloud has a good point coverage and a mutation was detected compared to the older pointclouds.                                                                                  |
| `_HIGHEST_YET_INSUFFICIENT_COVERAGE` | The selected point cloud has possible poor point coverage. Nonetheless, it is the point cloud with the highest point coverage among all available point clouds.                                    |
| `_LATEST_BUT_OUTDATED`               | The selected pointcloud is the latest one available, but it may be outdated for this building. This happens when the year of construction is equal or later than the point cloud acquisition date. |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | string   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | TEXT     |

## `b3_puntdichtheid_ahn3`

| Property      | Value                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------|
| Description   | Density of the AHN3 point cloud on BAG polygon. Only points classified as building or ground are considered. |
| Source        | -                                                                                                            |
| Data Type     | INT                                                                                                          |
| Unit          | points per square metre                                                                                      |
| Scale         | ratio                                                                                                        |
| Precision     | -                                                                                                            |
| Value Format  | `-`                                                                                                          |
| Nullable      | -                                                                                                            |
| Semantic Type | density                                                                                                      |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | INTEGER  |

## `b3_puntdichtheid_ahn4`

| Property      | Value                                                                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Density of the AHN4 point cloud on BAG polygon. Only points classified as building or ground are considered. Unit: points per square metre. |
| Source        | -                                                                                                                                           |
| Data Type     | INT                                                                                                                                         |
| Unit          | points per square metre                                                                                                                     |
| Scale         | ratio                                                                                                                                       |
| Precision     | -                                                                                                                                           |
| Value Format  | `-`                                                                                                                                         |
| Nullable      | -                                                                                                                                           |
| Semantic Type | density                                                                                                                                     |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | INTEGER  |

## `b3_volume_lod12`

| Property      | Value                                          |
|---------------|------------------------------------------------|
| Description   | Volume of the LoD1.2 model. Unit: cubic metre. |
| Source        | -                                              |
| Data Type     | FLOAT                                          |
| Unit          | cubic metre                                    |
| Scale         | ratio                                          |
| Precision     | -                                              |
| Value Format  | `-`                                            |
| Nullable      | -                                              |
| Semantic Type | volume                                         |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_volume_lod13`

| Property      | Value                                          |
|---------------|------------------------------------------------|
| Description   | Volume of the LoD1.3 model. Unit: cubic metre. |
| Source        | -                                              |
| Data Type     | FLOAT                                          |
| Unit          | cubic metre                                    |
| Scale         | ratio                                          |
| Precision     | -                                              |
| Value Format  | `-`                                            |
| Nullable      | -                                              |
| Semantic Type | volume                                         |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_volume_lod22`

| Property      | Value                                          |
|---------------|------------------------------------------------|
| Description   | Volume of the LoD2.2 model. Unit: cubic metre. |
| Source        | -                                              |
| Data Type     | FLOAT                                          |
| Unit          | cubic metre                                    |
| Scale         | ratio                                          |
| Precision     | -                                              |
| Value Format  | `-`                                            |
| Nullable      | -                                              |
| Semantic Type | volume                                         |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_bag_bag_overlap`

| Property      | Value                                                                              |
|---------------|------------------------------------------------------------------------------------|
| Description   | The total overlap area of BAG polygon with other BAG polygons. Unit: square metre. |
| Source        | -                                                                                  |
| Data Type     | FLOAT                                                                              |
| Unit          | square metre                                                                       |
| Scale         | ratio                                                                              |
| Precision     | -                                                                                  |
| Value Format  | `-`                                                                                |
| Nullable      | -                                                                                  |
| Semantic Type | area                                                                               |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_opp_grond`

| Property      | Value                                        |
|---------------|----------------------------------------------|
| Description   | Total ground floor area. Unit: square metre. |
| Source        | -                                            |
| Data Type     | FLOAT                                        |
| Unit          | square metre                                 |
| Scale         | ratio                                        |
| Precision     | -                                            |
| Value Format  | `-`                                          |
| Nullable      | -                                            |
| Semantic Type | area                                         |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_opp_dak_plat`

| Property      | Value                                                         |
|---------------|---------------------------------------------------------------|
| Description   | Total area of the flat parts of the roof. Unit: square metre. |
| Source        | -                                                             |
| Data Type     | FLOAT                                                         |
| Unit          | square metre                                                  |
| Scale         | ratio                                                         |
| Precision     | -                                                             |
| Value Format  | `-`                                                           |
| Nullable      | -                                                             |
| Semantic Type | area                                                          |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_opp_dak_schuin`

| Property      | Value                                                           |
|---------------|-----------------------------------------------------------------|
| Description   | Total area of the sloped parts of the roof. Unit: square metre. |
| Source        | -                                                               |
| Data Type     | FLOAT                                                           |
| Unit          | square metre                                                    |
| Scale         | ratio                                                           |
| Precision     | -                                                               |
| Value Format  | `-`                                                             |
| Nullable      | -                                                               |
| Semantic Type | area                                                            |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_opp_scheidingsmuur`

| Property      | Value                                              |
|---------------|----------------------------------------------------|
| Description   | Total area of the party walls. Unit: square metre. |
| Source        | -                                                  |
| Data Type     | FLOAT                                              |
| Unit          | square metre                                       |
| Scale         | ratio                                              |
| Precision     | -                                                  |
| Value Format  | `-`                                                |
| Nullable      | -                                                  |
| Semantic Type | area                                               |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `b3_opp_buitenmuur`

| Property      | Value                                                 |
|---------------|-------------------------------------------------------|
| Description   | Total area of the exterior walls. Unit: square metre. |
| Source        | -                                                     |
| Data Type     | FLOAT                                                 |
| Unit          | square metre                                          |
| Scale         | ratio                                                 |
| Precision     | -                                                     |
| Value Format  | `-`                                                   |
| Nullable      | -                                                     |
| Semantic Type | area                                                  |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | FLOAT    |

## `labels`

| Property      | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Building surface semantics. Only available in the GPKG 3D layers. This is an array of integers, where an integer refers to a surface type (0: `GroundSurface`, 1: `RoofSurface`, 2: `OuterWallSurface`, 3: `InnerWallSurface`). If a surface does not have a semantic value, NULL is used instead. Thus the length of the array equals the number of 3D polygons in the geometry, and the order of values in the array corresponds to the order of polygons. |
| Source        | -                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Data Type     | ARRAY<INT>                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Unit          | -                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Scale         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Precision     | -                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Value Format  | `-`                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Nullable      | -                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Semantic Type | list                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

**Data Format Specifications**

| Data Format   | Property   | Value                        |
|---------------|------------|------------------------------|
| GeoPackage    | Locations  | lod22_3d, lod13_3d, lod12_3d |
| GeoPackage    | Data Type  | TEXT                         |

## `b3_bouwlagen`

| Property      | Value                                                                                                                                |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Description   | An estimation of the number of floors in the building. Estimates are only are available for buildings with up to 5 estimated floors. |
| Source        | -                                                                                                                                    |
| Data Type     | INT                                                                                                                                  |
| Unit          | -                                                                                                                                    |
| Scale         | ratio                                                                                                                                |
| Precision     | -                                                                                                                                    |
| Value Format  | `-`                                                                                                                                  |
| Nullable      | -                                                                                                                                    |
| Semantic Type | count                                                                                                                                |

**Data Format Specifications**

| Data Format   | Property   | Value    |
|---------------|------------|----------|
| CityJSON      | Locations  | Building |
| CityJSON      | Data Type  | number   |
| GeoPackage    | Locations  | pand     |
| GeoPackage    | Data Type  | INTEGER  |

## `b3_kwaliteitsindicator`

| Property      | Value                                                                                                                                                                                                                                                                    |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Indication of the reliability of the building reconstruction. `b3_kwaliteitsindicator = (b3_bag_bag_overlap == 0) AND (b3_val3dity_lod22 == []) AND ( (b3_pw_selectie_reden != _HIGHEST_YET_INSUFFICIENT_COVERAGE) AND (b3_pw_selectie_reden != _LATEST_BUT_OUTDATED) )` |
| Source        | -                                                                                                                                                                                                                                                                        |
| Data Type     | STRING                                                                                                                                                                                                                                                                   |
| Unit          | -                                                                                                                                                                                                                                                                        |
| Scale         | nominal                                                                                                                                                                                                                                                                  |
| Precision     | -                                                                                                                                                                                                                                                                        |
| Value Format  | `-`                                                                                                                                                                                                                                                                      |
| Nullable      | -                                                                                                                                                                                                                                                                        |
| Semantic Type | flag                                                                                                                                                                                                                                                                     |

**Attribute Values**

| Attribute Value   | Description                               |
|-------------------|-------------------------------------------|
| `true`            | The reconstruction is correct.            |
| `false`           | The reconstruction is possibly incorrect. |

**Data Format Specifications**

| Data Format   | Property   | Value   |
|---------------|------------|---------|
| GeoPackage    | Locations  | pand    |
| GeoPackage    | Data Type  | TEXT    |

## `b3_azimut`

| Property      | Value                                                                       |
|---------------|-----------------------------------------------------------------------------|
| Description   | Azimuth of roofpart. Available for the LoD 2.2 roofparts in GPKG 2D layers. |
| Source        | -                                                                           |
| Data Type     | FLOAT                                                                       |
| Unit          | degrees                                                                     |
| Scale         | ratio                                                                       |
| Precision     | -                                                                           |
| Value Format  | `-`                                                                         |
| Nullable      | -                                                                           |
| Semantic Type | angle                                                                       |

**Data Format Specifications**

| Data Format   | Property   | Value       |
|---------------|------------|-------------|
| CityJSON      | Locations  | RoofSurface |
| CityJSON      | Data Type  | number      |
| GeoPackage    | Locations  | lod22_2d    |
| GeoPackage    | Data Type  | FLOAT       |

## `b3_hellingshoek`

| Property      | Value                                                                     |
|---------------|---------------------------------------------------------------------------|
| Description   | Slope of roofpart. Available for the LoD 2.2 roofparts in GPKG 2D layers. |
| Source        | -                                                                         |
| Data Type     | FLOAT                                                                     |
| Unit          | degrees                                                                   |
| Scale         | ratio                                                                     |
| Precision     | -                                                                         |
| Value Format  | `-`                                                                       |
| Nullable      | -                                                                         |
| Semantic Type | angle                                                                     |

**Data Format Specifications**

| Data Format   | Property   | Value       |
|---------------|------------|-------------|
| CityJSON      | Locations  | RoofSurface |
| CityJSON      | Data Type  | number      |
| GeoPackage    | Locations  | lod22_2d    |
| GeoPackage    | Data Type  | FLOAT       |
