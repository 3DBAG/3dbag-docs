# Data Attributen


## `begingeldigheid`

De datum waarop een versie van een BAG-object geldig is in de werkelijkheid conform de ingangsdatum in het brondocument. Dit tijdstip wordt vastgelegd in de beginGeldigheid. Als er geen expliciete ingangsdatum van geldigheid is opgenomen, wordt de datum van het brondocument overgenomen.

*Datatype*: datum

*Eenheid*: `YYYY-MM-DD`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `dak_type`

Daktype van het pand.

*Datatype*: categorisch

*Eenheid*: -

*Waarden*:

| Waarden | Omschrijving |
| :----- | :----------- |
| `slanted` | Dat met ten minste één schuin oppervlak. |
| `multiple horizontal` | Dak met meerdere, uitsluitend horizontale oppervlakken. |
| `single horizontal` | Dak met een enkel horizontaal oppervlak. |
| `no points` | Er was geen punt gevonden voor het gebouw. |
| `could not detect` | Kon geen dakoppervlak detecteren, ondanks dat er punten gevonden waren. |

## `dd_id`

Dakdeel ID.

*Datatype*: nominaal getal

*Eenheid*: -


## `documentdatum`

De datum waarop het brondocument is vastgesteld, op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van een pand heeft plaatsgevonden.

*Datatype*: datum

*Eenheid*: `YYYY-MM-DD`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `documentnummer`

De unieke aanduiding van het brondocument op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van een pand heeft plaatsgevonden, binnen een gemeente.

*Datatype*: tekst

*Eenheid*: `YYYY-MM-DD`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `eindgeldigheid`

De datum waarop de periode van geldigheid van een versie van een BAG-object eindigt. Bijvoorbeeld als gevolg van de vaststelling van een nieuw brondocument. Wanneer er geen tijdstip is ingevuld, dan is de versie nog geldig. Dit tijdstip wordt vastgelegd in de eindGeldigheid.

*Datatype*: datum

*Eenheid*: `YYYY-MM-DD`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `fid`

Numeriek ID van een pand (feature).

*Datatype*: nominaal getal

*Eenheid*: -


## `geconstateerd`

Een aanduiding waarmee kan worden aangegeven dat een pand in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake was van een regulier brondocument voor deze opname.

*Datatype*: categorisch

*Eenheid*: yes/no

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `gid`

Geometrie ID.

*Datatype*: nominaal getal

*Eenheid*: -


## `h_dak_50p`

Elevatie boven zeeniveau (NAP) op dakniveau. Berekend als de mediaan van alle hoogtepunten op het corresponderende dakdeel.

*Datatype*: reëel getal

*Eenheid*: meter


## `h_dak_70p`

Elevatie boven zeeniveau (NAP) op dakniveau. Berekend als het 70e percentiel van alle hoogtepunten op het corresponderende dakdeel.

*Datatype*: reëel getal

*Eenheid*: meter


## `h_dak_max`

Elevatie boven zeeniveau (NAP) op dakniveau. Berekend als het maximum van alle hoogtepunten op het corresponderende dakdeel.

*Datatype*: reëel getal

*Eenheid*: meter


## `h_dak_min`

Elevatie boven zeeniveau (NAP) op dakniveau. Berekend als het minimum van alle hoogtepunten op het corresponderende dakdeel.

*Datatype*: reëel getal

*Eenheid*: meter


## `h_maaiveld`

Elevatie boven zeeniveau (NAP) op het maaiveldniveau van het pand. Berekend als het 5e percentiel van de maaiveldpunten gevonden binnen een radius van 4 meter van het pand.

*Datatype*: reëel getal

*Eenheid*: meter


## `identificatie`

BAG: De unieke aanduiding van een pand.

*Datatype*: tekst

*Eenheid*: -

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `kas_warenhuis`

Het gebouw is een kas of een magazijn (volgens de TOP10NL).

*Datatype*: categorisch

*Eenheid*: yes/no


## `lod11_replace`

Geeft aan of de LoD1.3/LoD2.2 reconstructie is overgeslagen voor deze feature (en ook LoD1.1 als `lod11_replace==false`). Dit kan bijvoorbeeld gebeuren wanneer er geen punten gevonden zijn.

*Datatype*: categorisch

*Eenheid*: yes/no


## `ondergronds_type`

Ondergronds-classificatie van het pand of panddeel.

*Datatype*: categorisch

*Eenheid*: -

*Waarden*:

| Waarden | Omschrijving |
| :----- | :----------- |
| `floating` | Pand of panddeel zweeft boven andere objecten. |
| `above ground` | Pand of panddeel is volledig bovengronds. |
| `underground` | Pand of panddeel is volledig ondergronds. |

## `oorspronkelijk_bouwjaar`

De aanduiding van het jaar waarin een pand oorspronkelijk als bouwkundig gereed is of zal worden opgeleverd.

*Datatype*: datum

*Eenheid*: `YYYY`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `pand_deel_id`

Panddeel ID. Een pand kan meerdere delen hebben wanneer het is opgedeeld vanwege ondergrondse delen.

*Datatype*: nominaal getal

*Eenheid*: -


## `pw_actueel`

Geeft aan of de puntenwolk actueel is ten opzichte van de leeftijd van het pand.

*Datatype*: categorisch

*Eenheid*: -

*Waarden*:

| Waarden | Omschrijving |
| :----- | :----------- |
| `yes` | De puntenwolk is ingewonnen na de constructiedatum van het pand. |
| `no` | De puntenwolk is ingewonnen voor de constructiedatum van het pand. |
| `uncertain` | De puntenwolk is ingewonnen in hetzelfde jaar als de constructiedatum van het pand. |

## `pw_bron`

Bron van de puntenwolk.

*Datatype*: tekst

*Eenheid*: -


## `pw_datum`

Inwinningsdatum van de puntenwolk. In het geval van de AHN3 is dit een veronderstelde inwinningsdatum, welke bepaald is als 1 december van het jaar *voor* het officieel gerapporteerde inwinjaar van een specifieke AHN3-tegel.

*Datatype*: datum

*Eenheid*: `YYYY-MM-DD`


## `reconstructie_methode`

Reconstructiemethode van het gebouwmodel.

*Datatype*: tekst

*Eenheid*: -


## `reconstruction_skipped`

Geeft aan of de volledige LoD1.2/LoD1.3/LoD2.2 reconstructie is overgeslagen voor deze feature (en ook LoD1.1 als lod11_replace==false).

*Datatype*: categorisch

*Eenheid*: yes/no


## `semantics_values`

Pand-oppervlaksemantiek. Dit is een array van integers, waarbij een integer verwijst naar een oppervlaktype (0: `GroundSurface`, 1: `RoofSurface`, 2: `OuterWallSurface`, 3: `InnerWallSurface`). Als een oppervlak geen semantische waarde heeft, wordt NULL gebruikt. De lengte van de array staat dus gelijk aan het aantal oppervlakken, en de volgorde van waarden in de array correspondeert met de volgorde van de oppervlakken.

*Datatype*: lijst

*Eenheid*: -


## `status`

De fase van de levenscyclus van een pand, waarin het betreffende pand zich bevindt.

*Datatype*: categorisch

*Eenheid*: -

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)

*Waarden*:

| Waarden | Omschrijving |
| :----- | :----------- |
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

Houdt verband met de geschiedenis van de pandregistratie en de versie.

*Datatype*: datum-tijd

*Eenheid*: `YYYY-MM-DDThh:mm:ss.sss`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `tijdstipinactief`

Houdt verband met de geschiedenis van de pandregistratie en de versie.

*Datatype*: datum-tijd

*Eenheid*: `YYYY-MM-DDThh:mm:ss.sss`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `tijdstipinactieflv`

Houdt verband met de geschiedenis van de pandregistratie en de versie.

*Datatype*: datum-tijd

*Eenheid*: `YYYY-MM-DDThh:mm:ss.sss`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `tijdstipnietbaglv`

Houdt verband met de geschiedenis van de pandregistratie en de versie.

*Datatype*: datum-tijd

*Eenheid*: `YYYY-MM-DDThh:mm:ss.sss`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `tijdstipregistratielv`

Dit is het tijdstip waarop een versie van een BAG-object is opgenomen in de registratie van de landelijke voorziening. De gegevens komen daarmee beschikbaar voor afnemers.

*Datatype*: datum-tijd

*Eenheid*: `YYYY-MM-DDThh:mm:ss.sss`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `val3dity_codes`

[Val3dity foutcodes](https://val3dity.readthedocs.io/en/latest/errors) voor het 3D model. `Null` betekent valide geometry.

*Datatype*: lijst

*Eenheid*: -


## `versie_methode`

Versie van de reconstructiemethode voor panden.

*Datatype*: tekst

*Eenheid*: -


## `voorkomenidentificatie`

Houdt verband met de geschiedenis van de pandregistratie en de versie.

*Datatype*: ordinaal getal

*Eenheid*: -

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)

