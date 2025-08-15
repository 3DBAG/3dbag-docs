# Data Attributen

Attribuut specificatie bestand en schema: [https://downloads.3dbag.nl](https://downloads.3dbag.nl)

## `b3_pand_deel_id`

| Eigenschap    | Waarde                                                                                               |
|---------------|------------------------------------------------------------------------------------------------------|
| Description   | Panddeel ID. Een pand kan meerdere delen hebben wanneer het is opgedeeld vanwege ondergrondse delen. |
| Source        | roofer                                                                                               |
| Data Type     | INT                                                                                                  |
| Unit          | -                                                                                                    |
| Scale         | nominaal getal                                                                                       |
| Precision     | -                                                                                                    |
| Value Format  | `-`                                                                                                  |
| Nullable      | False                                                                                                |
| Semantic Type | identifier                                                                                           |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde                                                     |
|-------------------|--------------|------------------------------------------------------------|
| GeoPackage        | Locations    | lod13_3d, lod12_2d, lod22_2d, lod22_3d, lod13_2d, lod12_3d |
| GeoPackage        | Data Type    | INTEGER                                                    |

## `b3_dd_id`

| Eigenschap    | Waarde         |
|---------------|----------------|
| Description   | Dakdeel ID.    |
| Source        | roofer         |
| Data Type     | INT            |
| Unit          | -              |
| Scale         | nominaal getal |
| Precision     | -              |
| Value Format  | `-`            |
| Nullable      | False          |
| Semantic Type | identifier     |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde                       |
|-------------------|--------------|------------------------------|
| GeoPackage        | Locations    | lod22_2d, lod12_2d, lod13_2d |
| GeoPackage        | Data Type    | INTEGER                      |

## `identificatie`

| Eigenschap    | Waarde                                 |
|---------------|----------------------------------------|
| Description   | De unieke BAG aanduiding van een pand. |
| Source        | BAG,roofer                             |
| Data Type     | STRING                                 |
| Unit          | -                                      |
| Scale         | tekst                                  |
| Precision     | -                                      |
| Value Format  | `-`                                    |
| Nullable      | False                                  |
| Semantic Type | identifier                             |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde                                                           |
|-------------------|--------------|------------------------------------------------------------------|
| CityJSON          | Locations    | Building                                                         |
| CityJSON          | Data Type    | string                                                           |
| GeoPackage        | Locations    | lod13_3d, lod12_2d, pand, lod22_2d, lod22_3d, lod13_2d, lod12_3d |
| GeoPackage        | Data Type    | TEXT                                                             |

## `oorspronkelijkbouwjaar`

| Eigenschap    | Waarde                                                                                                       |
|---------------|--------------------------------------------------------------------------------------------------------------|
| Description   | De aanduiding van het jaar waarin een pand oorspronkelijk als bouwkundig gereed is of zal worden opgeleverd. |
| Source        | BAG                                                                                                          |
| Data Type     | INT                                                                                                          |
| Unit          | -                                                                                                            |
| Scale         | interval                                                                                                     |
| Precision     | -                                                                                                            |
| Value Format  | `YYYY`                                                                                                       |
| Nullable      | True                                                                                                         |
| Semantic Type | year                                                                                                         |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | INTEGER  |

## `status`

| Eigenschap    | Waarde                                                                              |
|---------------|-------------------------------------------------------------------------------------|
| Description   | De fase van de levenscyclus van een pand, waarin het betreffende pand zich bevindt. |
| Source        | BAG                                                                                 |
| Data Type     | STRING                                                                              |
| Unit          | -                                                                                   |
| Scale         | categorisch                                                                         |
| Precision     | -                                                                                   |
| Value Format  | `-`                                                                                 |
| Nullable      | -                                                                                   |
| Semantic Type | category                                                                            |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | TEXT     |

## `geconstateerd`

| Eigenschap    | Waarde                                                                                                                                                                                                                                 |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Een aanduiding waarmee kan worden aangegeven dat een pand in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake was van een regulier brondocument voor deze opname. |
| Source        | -                                                                                                                                                                                                                                      |
| Data Type     | STRING                                                                                                                                                                                                                                 |
| Unit          | -                                                                                                                                                                                                                                      |
| Scale         | nominaal                                                                                                                                                                                                                               |
| Precision     | -                                                                                                                                                                                                                                      |
| Value Format  | `-`                                                                                                                                                                                                                                    |
| Nullable      | -                                                                                                                                                                                                                                      |
| Semantic Type | flag                                                                                                                                                                                                                                   |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | TEXT     |

## `documentdatum`

| Eigenschap    | Waarde                                                                                                                                                                |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | De datum waarop het brondocument is vastgesteld, op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van een pand heeft plaatsgevonden. |
| Source        | -                                                                                                                                                                     |
| Data Type     | DATE                                                                                                                                                                  |
| Unit          | -                                                                                                                                                                     |
| Scale         | interval                                                                                                                                                              |
| Precision     | -                                                                                                                                                                     |
| Value Format  | `YYYY-MM-DD`                                                                                                                                                          |
| Nullable      | -                                                                                                                                                                     |
| Semantic Type | day                                                                                                                                                                   |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | DATE     |

## `documentnummer`

| Eigenschap    | Waarde                                                                                                                                                                              |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | De unieke aanduiding van het brondocument op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van een pand heeft plaatsgevonden, binnen een gemeente. |
| Source        | -                                                                                                                                                                                   |
| Data Type     | STRING                                                                                                                                                                              |
| Unit          | -                                                                                                                                                                                   |
| Scale         | tekst                                                                                                                                                                               |
| Precision     | -                                                                                                                                                                                   |
| Value Format  | `-`                                                                                                                                                                                 |
| Nullable      | -                                                                                                                                                                                   |
| Semantic Type | identifier                                                                                                                                                                          |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | TEXT     |

## `voorkomenidentificatie`

| Eigenschap    | Waarde                                                                 |
|---------------|------------------------------------------------------------------------|
| Description   | Houdt verband met de geschiedenis van de pandregistratie en de versie. |
| Source        | BAG                                                                    |
| Data Type     | INT                                                                    |
| Unit          | -                                                                      |
| Scale         | ordinaal getal                                                         |
| Precision     | -                                                                      |
| Value Format  | `-`                                                                    |
| Nullable      | -                                                                      |
| Semantic Type | identifier                                                             |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | INTEGER  |

## `begingeldigheid`

| Eigenschap    | Waarde                                                                                                                                                                                                                                                                                          |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | De datum waarop een versie van een BAG-object geldig is in de werkelijkheid conform de ingangsdatum in het brondocument. Dit tijdstip wordt vastgelegd in de beginGeldigheid. Als er geen expliciete ingangsdatum van geldigheid is opgenomen, wordt de datum van het brondocument overgenomen. |
| Source        | BAG                                                                                                                                                                                                                                                                                             |
| Data Type     | DATE                                                                                                                                                                                                                                                                                            |
| Unit          | -                                                                                                                                                                                                                                                                                               |
| Scale         | interval                                                                                                                                                                                                                                                                                        |
| Precision     | -                                                                                                                                                                                                                                                                                               |
| Value Format  | `YYYY-MM-DD`                                                                                                                                                                                                                                                                                    |
| Nullable      | -                                                                                                                                                                                                                                                                                               |
| Semantic Type | day                                                                                                                                                                                                                                                                                             |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | DATE     |

## `eindgeldigheid`

| Eigenschap    | Waarde                                                                                                                                                                                                                                                                              |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | De datum waarop de periode van geldigheid van een versie van een BAG-object eindigt. Bijvoorbeeld als gevolg van de vaststelling van een nieuw brondocument. Wanneer er geen tijdstip is ingevuld, dan is de versie nog geldig. Dit tijdstip wordt vastgelegd in de eindGeldigheid. |
| Source        | BAG                                                                                                                                                                                                                                                                                 |
| Data Type     | DATE                                                                                                                                                                                                                                                                                |
| Unit          | -                                                                                                                                                                                                                                                                                   |
| Scale         | interval                                                                                                                                                                                                                                                                            |
| Precision     | -                                                                                                                                                                                                                                                                                   |
| Value Format  | `YYYY-MM-DD`                                                                                                                                                                                                                                                                        |
| Nullable      | -                                                                                                                                                                                                                                                                                   |
| Semantic Type | day                                                                                                                                                                                                                                                                                 |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | DATE     |

## `tijdstipregistratie`

| Eigenschap    | Waarde                                                                 |
|---------------|------------------------------------------------------------------------|
| Description   | Houdt verband met de geschiedenis van de pandregistratie en de versie. |
| Source        | BAG                                                                    |
| Data Type     | DATETIME                                                               |
| Unit          | -                                                                      |
| Scale         | interval                                                               |
| Precision     | -                                                                      |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                              |
| Nullable      | -                                                                      |
| Semantic Type | millisecond                                                            |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | DATETIME |

## `eindregistratie`

| Eigenschap    | Waarde                                                                 |
|---------------|------------------------------------------------------------------------|
| Description   | Houdt verband met de geschiedenis van de pandregistratie en de versie. |
| Source        | BAG                                                                    |
| Data Type     | DATETIME                                                               |
| Unit          | -                                                                      |
| Scale         | interval                                                               |
| Precision     | -                                                                      |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                              |
| Nullable      | -                                                                      |
| Semantic Type | millisecond                                                            |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | DATETIME |

## `tijdstipinactief`

| Eigenschap    | Waarde                                                                 |
|---------------|------------------------------------------------------------------------|
| Description   | Houdt verband met de geschiedenis van de pandregistratie en de versie. |
| Source        | BAG                                                                    |
| Data Type     | DATETIME                                                               |
| Unit          | -                                                                      |
| Scale         | interval                                                               |
| Precision     | -                                                                      |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                              |
| Nullable      | -                                                                      |
| Semantic Type | millisecond                                                            |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | DATETIME |

## `tijdstipregistratielv`

| Eigenschap    | Waarde                                                                                                                                                                      |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Dit is het tijdstip waarop een versie van een BAG-object is opgenomen in de registratie van de landelijke voorziening. De gegevens komen daarmee beschikbaar voor afnemers. |
| Source        | BAG                                                                                                                                                                         |
| Data Type     | DATETIME                                                                                                                                                                    |
| Unit          | -                                                                                                                                                                           |
| Scale         | interval                                                                                                                                                                    |
| Precision     | -                                                                                                                                                                           |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                                                                                                                                   |
| Nullable      | -                                                                                                                                                                           |
| Semantic Type | millisecond                                                                                                                                                                 |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | DATETIME |

## `tijdstipeindregistratielv`

| Eigenschap    | Waarde                                                                 |
|---------------|------------------------------------------------------------------------|
| Description   | Houdt verband met de geschiedenis van de pandregistratie en de versie. |
| Source        | BAG                                                                    |
| Data Type     | DATETIME                                                               |
| Unit          | -                                                                      |
| Scale         | interval                                                               |
| Precision     | -                                                                      |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                              |
| Nullable      | -                                                                      |
| Semantic Type | millisecond                                                            |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | DATETIME |

## `tijdstipinactieflv`

| Eigenschap    | Waarde                                                                 |
|---------------|------------------------------------------------------------------------|
| Description   | Houdt verband met de geschiedenis van de pandregistratie en de versie. |
| Source        | BAG                                                                    |
| Data Type     | DATETIME                                                               |
| Unit          | -                                                                      |
| Scale         | interval                                                               |
| Precision     | -                                                                      |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                              |
| Nullable      | -                                                                      |
| Semantic Type | millisecond                                                            |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | DATETIME |

## `tijdstipnietbaglv`

| Eigenschap    | Waarde                                                                 |
|---------------|------------------------------------------------------------------------|
| Description   | Houdt verband met de geschiedenis van de pandregistratie en de versie. |
| Source        | BAG                                                                    |
| Data Type     | DATETIME                                                               |
| Unit          | -                                                                      |
| Scale         | interval                                                               |
| Precision     | -                                                                      |
| Value Format  | `YYYY-MM-DDThh:mm:ss.sss`                                              |
| Nullable      | -                                                                      |
| Semantic Type | millisecond                                                            |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | DATETIME |

## `b3_h_maaiveld`

| Eigenschap    | Waarde                                                                                                                                                                       |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Elevatie boven zeeniveau (NAP) op het maaiveldniveau van het pand. Berekend als het 5e percentiel van de maaiveldpunten gevonden binnen een radius van 4 meter van het pand. |
| Source        | -                                                                                                                                                                            |
| Data Type     | FLOAT                                                                                                                                                                        |
| Unit          | meter                                                                                                                                                                        |
| Scale         | ratio                                                                                                                                                                        |
| Precision     | -                                                                                                                                                                            |
| Value Format  | `-`                                                                                                                                                                          |
| Nullable      | -                                                                                                                                                                            |
| Semantic Type | elevation                                                                                                                                                                    |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_dak_type`

| Eigenschap    | Waarde                |
|---------------|-----------------------|
| Description   | Daktype van het pand. |
| Source        | -                     |
| Data Type     | STRING                |
| Unit          | -                     |
| Scale         | categorisch           |
| Precision     | -                     |
| Value Format  | `-`                   |
| Nullable      | -                     |
| Semantic Type | category              |

**Attribuutwaarden**

| Attribuutwaarde       | Omschrijving                                                            |
|-----------------------|-------------------------------------------------------------------------|
| `slanted`             | Dat met ten minste één schuin oppervlak.                                |
| `multiple horizontal` | Dak met meerdere, uitsluitend horizontale oppervlakken.                 |
| `single horizontal`   | Dak met een enkel horizontaal oppervlak.                                |
| `no points`           | Er was geen punt gevonden voor het gebouw.                              |
| `could not detect`    | Kon geen dakoppervlak detecteren, ondanks dat er punten gevonden waren. |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | TEXT     |

## `b3_pw_datum`

| Eigenschap    | Waarde                                                                                                                                                                                                                  |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Inwinjaar van de bron puntenwolk. Dit is bepaald door naar de GPS tijd van de AHN punten voor dit pand. Indien een goede GPS tijd niet beschikbaar is, wordt de file creation date van het puntenwolk bestand gebruikt. |
| Source        | -                                                                                                                                                                                                                       |
| Data Type     | INT                                                                                                                                                                                                                     |
| Unit          | -                                                                                                                                                                                                                       |
| Scale         | interval                                                                                                                                                                                                                |
| Precision     | -                                                                                                                                                                                                                       |
| Value Format  | `YYYY`                                                                                                                                                                                                                  |
| Nullable      | False                                                                                                                                                                                                                   |
| Semantic Type | year                                                                                                                                                                                                                    |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | INTEGER  |

## `b3_pw_bron`

| Eigenschap    | Waarde                                      |
|---------------|---------------------------------------------|
| Description   | Bron van de puntenwolk, bijv. AHN3 of AHN4. |
| Source        | -                                           |
| Data Type     | STRING                                      |
| Unit          | -                                           |
| Scale         | tekst                                       |
| Precision     | -                                           |
| Value Format  | `-`                                         |
| Nullable      | -                                           |
| Semantic Type | text                                        |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | TEXT     |

## `b3_kas_warenhuis`

| Eigenschap    | Waarde                                                                                                                 |
|---------------|------------------------------------------------------------------------------------------------------------------------|
| Description   | Het gebouw is een kas of een warenhuis volgens de TOP10NL of heeft een oppervlakte van meer dan 70000 vierkante meter. |
| Source        | -                                                                                                                      |
| Data Type     | BOOL                                                                                                                   |
| Unit          | -                                                                                                                      |
| Scale         | nominaal                                                                                                               |
| Precision     | -                                                                                                                      |
| Value Format  | `-`                                                                                                                    |
| Nullable      | -                                                                                                                      |
| Semantic Type | flag                                                                                                                   |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | boolean  |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | BOOLEAN  |

## `b3_reconstructie_onvolledig`

| Eigenschap    | Waarde                                                                                      |
|---------------|---------------------------------------------------------------------------------------------|
| Description   | Geeft aan of de volledige LoD1.2/LoD1.3/LoD2.2 reconstructie is overgeslagen voor het pand. |
| Source        | -                                                                                           |
| Data Type     | BOOL                                                                                        |
| Unit          | -                                                                                           |
| Scale         | nominaal                                                                                    |
| Precision     | -                                                                                           |
| Value Format  | `-`                                                                                         |
| Nullable      | -                                                                                           |
| Semantic Type | flag                                                                                        |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | boolean  |

## `b3_h_dak_min`

| Eigenschap    | Waarde                                                                                                                   |
|---------------|--------------------------------------------------------------------------------------------------------------------------|
| Description   | Minimumhoogte op dakdeel gebaseerd op het gereconstrueerde 3D-model in LoD2.2. Gegeven als hoogte boven zeeniveau (NAP). |
| Source        | -                                                                                                                        |
| Data Type     | FLOAT                                                                                                                    |
| Unit          | meter                                                                                                                    |
| Scale         | ratio                                                                                                                    |
| Precision     | -                                                                                                                        |
| Value Format  | `-`                                                                                                                      |
| Nullable      | -                                                                                                                        |
| Semantic Type | elevation                                                                                                                |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde                |
|-------------------|--------------|-----------------------|
| CityJSON          | Locations    | RoofSurface, Building |
| CityJSON          | Data Type    | number                |

## `b3_h_dak_50p`

| Eigenschap    | Waarde                                                                                                                  |
|---------------|-------------------------------------------------------------------------------------------------------------------------|
| Description   | Medianhoogte op dakdeel gebaseerd op het gereconstrueerde 3D-model in LoD2.2. Gegeven als hoogte boven zeeniveau (NAP). |
| Source        | -                                                                                                                       |
| Data Type     | FLOAT                                                                                                                   |
| Unit          | meter                                                                                                                   |
| Scale         | ratio                                                                                                                   |
| Precision     | -                                                                                                                       |
| Value Format  | `-`                                                                                                                     |
| Nullable      | -                                                                                                                       |
| Semantic Type | elevation                                                                                                               |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde                |
|-------------------|--------------|-----------------------|
| CityJSON          | Locations    | RoofSurface, Building |
| CityJSON          | Data Type    | number                |

## `b3_h_dak_70p`

| Eigenschap    | Waarde                                                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------------------------------------|
| Description   | De 70e percentielhoogte op dakdeel gebaseerd op het gereconstrueerde 3D-model in LoD2.2. Gegeven als hoogte boven zeeniveau (NAP). |
| Source        | -                                                                                                                                  |
| Data Type     | FLOAT                                                                                                                              |
| Unit          | meter                                                                                                                              |
| Scale         | ratio                                                                                                                              |
| Precision     | -                                                                                                                                  |
| Value Format  | `-`                                                                                                                                |
| Nullable      | -                                                                                                                                  |
| Semantic Type | elevation                                                                                                                          |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde                |
|-------------------|--------------|-----------------------|
| CityJSON          | Locations    | RoofSurface, Building |
| CityJSON          | Data Type    | number                |

## `b3_h_dak_max`

| Eigenschap    | Waarde                                                                                                                                   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Maximumhoogte op dakdeel gebaseerd op het gereconstrueerde 3D-model in LoD2.2. Gegeven als hoogte boven zeeniveau (NAP). Eenheid: meter. |
| Source        | -                                                                                                                                        |
| Data Type     | FLOAT                                                                                                                                    |
| Unit          | meter                                                                                                                                    |
| Scale         | ratio                                                                                                                                    |
| Precision     | -                                                                                                                                        |
| Value Format  | `-`                                                                                                                                      |
| Nullable      | -                                                                                                                                        |
| Semantic Type | elevation                                                                                                                                |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde                |
|-------------------|--------------|-----------------------|
| CityJSON          | Locations    | RoofSurface, Building |
| CityJSON          | Data Type    | number                |

## `b3_val3dity_lod12`

| Eigenschap    | Waarde                                                                                                                                         |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | [Val3dity foutcodes](https://val3dity.readthedocs.io/2.5.1/errors.html) voor het LoD1.2 3D model. Een lege lijst betekent een valide geometrie. |
| Source        | -                                                                                                                                              |
| Data Type     | ARRAY<INT>                                                                                                                                     |
| Unit          | -                                                                                                                                              |
| Scale         | -                                                                                                                                              |
| Precision     | -                                                                                                                                              |
| Value Format  | `-`                                                                                                                                            |
| Nullable      | False                                                                                                                                          |
| Semantic Type | list                                                                                                                                           |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | array    |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | TEXT     |

## `b3_val3dity_lod13`

| Eigenschap    | Waarde                                                                                                                                         |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | [Val3dity foutcodes](https://val3dity.readthedocs.io/2.5.1/errors.html) voor het LoD1.3 3D model. Een lege lijst betekent een valide geometrie. |
| Source        | -                                                                                                                                              |
| Data Type     | ARRAY<INT>                                                                                                                                     |
| Unit          | -                                                                                                                                              |
| Scale         | -                                                                                                                                              |
| Precision     | -                                                                                                                                              |
| Value Format  | `-`                                                                                                                                            |
| Nullable      | False                                                                                                                                          |
| Semantic Type | list                                                                                                                                           |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | array    |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | TEXT     |

## `b3_val3dity_lod22`

| Eigenschap    | Waarde                                                                                                                                         |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | [Val3dity foutcodes](https://val3dity.readthedocs.io/2.5.1/errors.html) voor het LoD2.2 3D model. Een lege lijst betekent een valide geometrie. |
| Source        | -                                                                                                                                              |
| Data Type     | ARRAY<INT>                                                                                                                                     |
| Unit          | -                                                                                                                                              |
| Scale         | -                                                                                                                                              |
| Precision     | -                                                                                                                                              |
| Value Format  | `-`                                                                                                                                            |
| Nullable      | False                                                                                                                                          |
| Semantic Type | list                                                                                                                                           |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | array    |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | TEXT     |

## `b3_rmse_lod12`

| Eigenschap    | Waarde                                                                                               |
|---------------|------------------------------------------------------------------------------------------------------|
| Description   | Root Mean Square Error van de 3D afstanden tussen de puntenwolk en het LoD1.2 model. Eenheid: meter. |
| Source        | -                                                                                                    |
| Data Type     | FLOAT                                                                                                |
| Unit          | meter                                                                                                |
| Scale         | ratio                                                                                                |
| Precision     | -                                                                                                    |
| Value Format  | `-`                                                                                                  |
| Nullable      | -                                                                                                    |
| Semantic Type | error                                                                                                |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_rmse_lod13`

| Eigenschap    | Waarde                                                                                               |
|---------------|------------------------------------------------------------------------------------------------------|
| Description   | Root Mean Square Error van de 3D afstanden tussen de puntenwolk en het LoD1.3 model. Eenheid: meter. |
| Source        | -                                                                                                    |
| Data Type     | FLOAT                                                                                                |
| Unit          | meter                                                                                                |
| Scale         | ratio                                                                                                |
| Precision     | -                                                                                                    |
| Value Format  | `-`                                                                                                  |
| Nullable      | -                                                                                                    |
| Semantic Type | error                                                                                                |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_rmse_lod22`

| Eigenschap    | Waarde                                                                                               |
|---------------|------------------------------------------------------------------------------------------------------|
| Description   | Root Mean Square Error van de 3D afstanden tussen de puntenwolk en het LoD2.2 model. Eenheid: meter. |
| Source        | -                                                                                                    |
| Data Type     | FLOAT                                                                                                |
| Unit          | meter                                                                                                |
| Scale         | ratio                                                                                                |
| Precision     | -                                                                                                    |
| Value Format  | `-`                                                                                                  |
| Nullable      | -                                                                                                    |
| Semantic Type | error                                                                                                |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_mutatie_ahn3_ahn4`

| Eigenschap    | Waarde                                                                                                      |
|---------------|-------------------------------------------------------------------------------------------------------------|
| Description   | `true` als er een significante verandering is gedetecteerd in het pand tussen de AHN3 en AHN4 puntenwolken. |
| Source        | -                                                                                                           |
| Data Type     | BOOL                                                                                                        |
| Unit          | -                                                                                                           |
| Scale         | nominaal                                                                                                    |
| Precision     | -                                                                                                           |
| Value Format  | `-`                                                                                                         |
| Nullable      | -                                                                                                           |
| Semantic Type | flag                                                                                                        |

**Attribuutwaarden**

| Attribuutwaarde   | Omschrijving                                                                                          |
|-------------------|-------------------------------------------------------------------------------------------------------|
| `true`            | Er was een significante verandering is gedetecteerd in het pand tussen de AHN3 en AHN4 puntenwolken.  |
| `false`           | Er was geen significante verandering is gedetecteerd in het pand tussen de AHN3 en AHN4 puntenwolken. |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | boolean  |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | BOOLEAN  |

## `b3_nodata_fractie_ahn3`

| Eigenschap    | Waarde                                                                                                                              |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Fractie van het BAG polygon met onvoldoende AHN3 punten dekking. Alleen punten geclassificeerd als gebouw of grond worden gebruikt. |
| Source        | -                                                                                                                                   |
| Data Type     | FLOAT                                                                                                                               |
| Unit          | -                                                                                                                                   |
| Scale         | ratio                                                                                                                               |
| Precision     | -                                                                                                                                   |
| Value Format  | `-`                                                                                                                                 |
| Nullable      | -                                                                                                                                   |
| Semantic Type | fraction                                                                                                                            |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_nodata_fractie_ahn4`

| Eigenschap    | Waarde                                                                                                                              |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Fractie van het BAG polygon met onvoldoende AHN4 punten dekking. Alleen punten geclassificeerd als gebouw of grond worden gebruikt. |
| Source        | -                                                                                                                                   |
| Data Type     | FLOAT                                                                                                                               |
| Unit          | -                                                                                                                                   |
| Scale         | ratio                                                                                                                               |
| Precision     | -                                                                                                                                   |
| Value Format  | `-`                                                                                                                                 |
| Nullable      | -                                                                                                                                   |
| Semantic Type | fraction                                                                                                                            |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_nodata_radius_ahn3`

| Eigenschap    | Waarde                                                                                                                                                       |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Straal van de grootste cirkel die binnen het BAG polygoon valt en geen AHN3 punten bevat. Alleen punten geclassificeerd als gebouw of grond worden gebruikt. |
| Source        | -                                                                                                                                                            |
| Data Type     | FLOAT                                                                                                                                                        |
| Unit          | meter                                                                                                                                                        |
| Scale         | ratio                                                                                                                                                        |
| Precision     | -                                                                                                                                                            |
| Value Format  | `-`                                                                                                                                                          |
| Nullable      | -                                                                                                                                                            |
| Semantic Type | length                                                                                                                                                       |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_nodata_radius_ahn4`

| Eigenschap    | Waarde                                                                                                                                                       |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Straal van de grootste cirkel die binnen het BAG polygoon valt en geen AHN4 punten bevat. Alleen punten geclassificeerd als gebouw of grond worden gebruikt. |
| Source        | -                                                                                                                                                            |
| Data Type     | FLOAT                                                                                                                                                        |
| Unit          | meter                                                                                                                                                        |
| Scale         | ratio                                                                                                                                                        |
| Precision     | -                                                                                                                                                            |
| Value Format  | `-`                                                                                                                                                          |
| Nullable      | -                                                                                                                                                            |
| Semantic Type | length                                                                                                                                                       |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_pw_selectie_reden`

| Eigenschap    | Waarde                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------|
| Description   | Geeft achtergrond informatie met betrekking tot de puntenwolk selectie (zie `pw_bron` attribuut). |
| Source        | -                                                                                                 |
| Data Type     | STRING                                                                                            |
| Unit          | -                                                                                                 |
| Scale         | categorisch                                                                                       |
| Precision     | -                                                                                                 |
| Value Format  | `-`                                                                                               |
| Nullable      | -                                                                                                 |
| Semantic Type | category                                                                                          |

**Attribuutwaarden**

| Attribuutwaarde                      | Omschrijving                                                                                                                                                                                                                  |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PREFERRED_AND_LATEST`               | De geselecteerde puntenwolk heeft een goede puntdekking en er is geen recentere puntenwolk met voldoende puntdekking beschikbaar.                                                                                             |
| `PREFERRED_NOT_LATEST`               | De geselecteerde puntenwolk heeft een goede point puntdekking en er is een recentere puntenwolk met voldoende puntdekking beschikbaar. De nieuwere puntewolk is echter niet geselecteerd omdat er geen mutatie is gedecteerd. |
| `LATEST_WITH_MUTATION`               | De geselecteerde puntenwolk heeft een goede puntdekking en er is een mutatie ten opzichte van een oudere puntenwolk gedetecteerd.                                                                                             |
| `_HIGHEST_YET_INSUFFICIENT_COVERAGE` | De geselecteerde puntenwolk heeft hoogste puntdekking van alle kandidaat puntenwolken, maar de puntdekking is alsnog mogelijk niet voldoende. Dit gebouw vertoont mogelijk reconstructie fouten.                              |
| `_LATEST_BUT_OUTDATED`               | De geselecteerde puntenwolk is de meerst recente, maar is mogelijk alsnog te oud voor dit pand. Dit kan gebeurt als het oorspronkelijk bouwjaar gelijk aan of jonger is dan het inwin jaar van de puntenwolk.                 |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | string   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | TEXT     |

## `b3_puntdichtheid_ahn3`

| Eigenschap    | Waarde                                                                                                                               |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Puntdichtheid van de AHN3-puntenwolk voor het pand. Alleen punten geclassificeerd als gebouw of grond worden in beschouwing genomen. |
| Source        | -                                                                                                                                    |
| Data Type     | INT                                                                                                                                  |
| Unit          | punten per vierkante meter                                                                                                           |
| Scale         | ratio                                                                                                                                |
| Precision     | -                                                                                                                                    |
| Value Format  | `-`                                                                                                                                  |
| Nullable      | -                                                                                                                                    |
| Semantic Type | density                                                                                                                              |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | INTEGER  |

## `b3_puntdichtheid_ahn4`

| Eigenschap    | Waarde                                                                                                                                                                    |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Puntdichtheid van de AHN4-puntenwolk voor het pand. Alleen punten geclassificeerd als gebouw of grond worden in beschouwing genomen. Eenheid: punten per vierkante meter. |
| Source        | -                                                                                                                                                                         |
| Data Type     | INT                                                                                                                                                                       |
| Unit          | punten per vierkante meter                                                                                                                                                |
| Scale         | ratio                                                                                                                                                                     |
| Precision     | -                                                                                                                                                                         |
| Value Format  | `-`                                                                                                                                                                       |
| Nullable      | -                                                                                                                                                                         |
| Semantic Type | density                                                                                                                                                                   |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | INTEGER  |

## `b3_volume_lod12`

| Eigenschap    | Waarde                                               |
|---------------|------------------------------------------------------|
| Description   | Volume van het LoD1.2-model. Eenheid: kubieke meter. |
| Source        | -                                                    |
| Data Type     | FLOAT                                                |
| Unit          | kubieke meter                                        |
| Scale         | ratio                                                |
| Precision     | -                                                    |
| Value Format  | `-`                                                  |
| Nullable      | -                                                    |
| Semantic Type | volume                                               |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_volume_lod13`

| Eigenschap    | Waarde                                               |
|---------------|------------------------------------------------------|
| Description   | Volume van het LoD1.3-model. Eenheid: kubieke meter. |
| Source        | -                                                    |
| Data Type     | FLOAT                                                |
| Unit          | kubieke meter                                        |
| Scale         | ratio                                                |
| Precision     | -                                                    |
| Value Format  | `-`                                                  |
| Nullable      | -                                                    |
| Semantic Type | volume                                               |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_volume_lod22`

| Eigenschap    | Waarde                                               |
|---------------|------------------------------------------------------|
| Description   | Volume van het LoD2.2-model. Eenheid: kubieke meter. |
| Source        | -                                                    |
| Data Type     | FLOAT                                                |
| Unit          | kubieke meter                                        |
| Scale         | ratio                                                |
| Precision     | -                                                    |
| Value Format  | `-`                                                  |
| Nullable      | -                                                    |
| Semantic Type | volume                                               |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_bag_bag_overlap`

| Eigenschap    | Waarde                                                                                              |
|---------------|-----------------------------------------------------------------------------------------------------|
| Description   | Het oppervlakte van overlap van dit BAG polygon met andere BAG polygonen. Eenheid: vierkante meter. |
| Source        | -                                                                                                   |
| Data Type     | FLOAT                                                                                               |
| Unit          | vierkante meter                                                                                     |
| Scale         | ratio                                                                                               |
| Precision     | -                                                                                                   |
| Value Format  | `-`                                                                                                 |
| Nullable      | -                                                                                                   |
| Semantic Type | area                                                                                                |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_opp_grond`

| Eigenschap    | Waarde                                                     |
|---------------|------------------------------------------------------------|
| Description   | Totale oppervlakte begane grond. Eenheid: vierkante meter. |
| Source        | -                                                          |
| Data Type     | FLOAT                                                      |
| Unit          | vierkante meter                                            |
| Scale         | ratio                                                      |
| Precision     | -                                                          |
| Value Format  | `-`                                                        |
| Nullable      | -                                                          |
| Semantic Type | area                                                       |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_opp_dak_plat`

| Eigenschap    | Waarde                                                                        |
|---------------|-------------------------------------------------------------------------------|
| Description   | Totale oppervlakte van de platte delen van het dak. Eenheid: vierkante meter. |
| Source        | -                                                                             |
| Data Type     | FLOAT                                                                         |
| Unit          | vierkante meter                                                               |
| Scale         | ratio                                                                         |
| Precision     | -                                                                             |
| Value Format  | `-`                                                                           |
| Nullable      | -                                                                             |
| Semantic Type | area                                                                          |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_opp_dak_schuin`

| Eigenschap    | Waarde                                                                         |
|---------------|--------------------------------------------------------------------------------|
| Description   | Totale oppervlakte van de schuine delen van het dak. Eenheid: vierkante meter. |
| Source        | -                                                                              |
| Data Type     | FLOAT                                                                          |
| Unit          | vierkante meter                                                                |
| Scale         | ratio                                                                          |
| Precision     | -                                                                              |
| Value Format  | `-`                                                                            |
| Nullable      | -                                                                              |
| Semantic Type | area                                                                           |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_opp_scheidingsmuur`

| Eigenschap    | Waarde                                                                    |
|---------------|---------------------------------------------------------------------------|
| Description   | Totale oppervlakte van de pandscheidende muren. Eenheid: vierkante meter. |
| Source        | -                                                                         |
| Data Type     | FLOAT                                                                     |
| Unit          | vierkante meter                                                           |
| Scale         | ratio                                                                     |
| Precision     | -                                                                         |
| Value Format  | `-`                                                                       |
| Nullable      | -                                                                         |
| Semantic Type | area                                                                      |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `b3_opp_buitenmuur`

| Eigenschap    | Waarde                                                           |
|---------------|------------------------------------------------------------------|
| Description   | Totale oppervlakte van de buitenmuren. Eenheid: vierkante meter. |
| Source        | -                                                                |
| Data Type     | FLOAT                                                            |
| Unit          | vierkante meter                                                  |
| Scale         | ratio                                                            |
| Precision     | -                                                                |
| Value Format  | `-`                                                              |
| Nullable      | -                                                                |
| Semantic Type | area                                                             |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | FLOAT    |

## `labels`

| Eigenschap    | Waarde                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Pand-oppervlaksemantiek. Alleen beschikbaar in de GPKG 3D lagen. Dit is een array van integers, waarbij een integer verwijst naar een oppervlaktype (0: `GroundSurface`, 1: `RoofSurface`, 2: `OuterWallSurface`, 3: `InnerWallSurface`). Als een oppervlak geen semantische waarde heeft, wordt NULL gebruikt. De lengte van de array staat dus gelijk aan het aantal 3D polygonen van de geometrie, en de volgorde van waarden in de array correspondeert met de volgorde van de polygonen. |
| Source        | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Data Type     | ARRAY<INT>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Unit          | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Scale         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Precision     | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Value Format  | `-`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Nullable      | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Semantic Type | list                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde                       |
|-------------------|--------------|------------------------------|
| GeoPackage        | Locations    | lod22_3d, lod13_3d, lod12_3d |
| GeoPackage        | Data Type    | TEXT                         |

## `b3_bouwlagen`

| Eigenschap    | Waarde                                                                                                                                      |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Een schatting van het aantal bouwlagen in het gebouw. Schattingen zijn alleen beschikbaar voor gebouwen met maximaal 5 geschatte bouwlagen. |
| Source        | -                                                                                                                                           |
| Data Type     | INT                                                                                                                                         |
| Unit          | -                                                                                                                                           |
| Scale         | ratio                                                                                                                                       |
| Precision     | -                                                                                                                                           |
| Value Format  | `-`                                                                                                                                         |
| Nullable      | -                                                                                                                                           |
| Semantic Type | count                                                                                                                                       |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| CityJSON          | Locations    | Building |
| CityJSON          | Data Type    | number   |
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | INTEGER  |

## `b3_kwaliteitsindicator`

| Eigenschap    | Waarde                                                                                                                                                                                                                                                                  |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description   | Indicatie van de betrouwbaarheid van de gebouwreconstructie. `b3_kwaliteitsindicator = (b3_bag_bag_overlap == 0) AND (b3_val3dity_lod22 == []) AND ( (b3_pw_selectie_reden != _HIGHEST_YET_INSUFFICIENT_COVERAGE) AND (b3_pw_selectie_reden != _LATEST_BUT_OUTDATED) )` |
| Source        | -                                                                                                                                                                                                                                                                       |
| Data Type     | STRING                                                                                                                                                                                                                                                                  |
| Unit          | -                                                                                                                                                                                                                                                                       |
| Scale         | nominaal                                                                                                                                                                                                                                                                |
| Precision     | -                                                                                                                                                                                                                                                                       |
| Value Format  | `-`                                                                                                                                                                                                                                                                     |
| Nullable      | -                                                                                                                                                                                                                                                                       |
| Semantic Type | flag                                                                                                                                                                                                                                                                    |

**Attribuutwaarden**

| Attribuutwaarde   | Omschrijving                                     |
|-------------------|--------------------------------------------------|
| `true`            | De gebouwreconstructie is correct.               |
| `false`           | De gebouwreconstructie is mogelijk niet correct. |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde   |
|-------------------|--------------|----------|
| GeoPackage        | Locations    | pand     |
| GeoPackage        | Data Type    | TEXT     |

## `b3_azimut`

| Eigenschap    | Waarde                                                                        |
|---------------|-------------------------------------------------------------------------------|
| Description   | Azimut van dakdeel. Beschikbaar voor de LoD 2.2 dakdelen in de GPKG 2D lagen. |
| Source        | -                                                                             |
| Data Type     | FLOAT                                                                         |
| Unit          | graden                                                                        |
| Scale         | ratio                                                                         |
| Precision     | -                                                                             |
| Value Format  | `-`                                                                           |
| Nullable      | -                                                                             |
| Semantic Type | angle                                                                         |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde      |
|-------------------|--------------|-------------|
| CityJSON          | Locations    | RoofSurface |
| CityJSON          | Data Type    | number      |
| GeoPackage        | Locations    | lod22_2d    |
| GeoPackage        | Data Type    | FLOAT       |

## `b3_hellingshoek`

| Eigenschap    | Waarde                                                                             |
|---------------|------------------------------------------------------------------------------------|
| Description   | Hellingshoek van dakdeel. Beschikbaar voor de LoD 2.2 dakdelen in de GPKG 2D lagen |
| Source        | -                                                                                  |
| Data Type     | FLOAT                                                                              |
| Unit          | graden                                                                             |
| Scale         | ratio                                                                              |
| Precision     | -                                                                                  |
| Value Format  | `-`                                                                                |
| Nullable      | -                                                                                  |
| Semantic Type | angle                                                                              |

**Specificaties bestandsformaat**

| Bestandsformaat   | Eigenschap   | Waarde      |
|-------------------|--------------|-------------|
| CityJSON          | Locations    | RoofSurface |
| CityJSON          | Data Type    | number      |
| GeoPackage        | Locations    | lod22_2d    |
| GeoPackage        | Data Type    | FLOAT       |
