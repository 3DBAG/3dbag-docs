# Data Attributen


## `b3_bag_bag_overlap`

Het oppervlakte van overlap van dit BAG polygon met andere BAG polygonen. Eenheid: vierkante meter.

*Datatype*: reëel getal

*Eenheid*: vierkante meter


## `b3_dak_type`

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

## `b3_dd_id`

Dakdeel ID.

*Datatype*: nominaal getal

*Eenheid*: -


## `b3_h_dak_50p`

Medianhoogte op dakdeel gebaseerd op het gereconstrueerde 3D-model in LoD2.2. Gegeven als hoogte boven zeeniveau (NAP).

*Datatype*: reëel getal

*Eenheid*: meter


## `b3_h_dak_70p`

De 70e percentielhoogte op dakdeel gebaseerd op het gereconstrueerde 3D-model in LoD2.2. Gegeven als hoogte boven zeeniveau (NAP).

*Datatype*: reëel getal

*Eenheid*: meter


## `b3_h_dak_max`

Maximumhoogte op dakdeel gebaseerd op het gereconstrueerde 3D-model in LoD2.2. Gegeven als hoogte boven zeeniveau (NAP). Eenheid: meter.

*Datatype*: reëel getal

*Eenheid*: meter


## `b3_h_dak_min`

Minimumhoogte op dakdeel gebaseerd op het gereconstrueerde 3D-model in LoD2.2. Gegeven als hoogte boven zeeniveau (NAP).

*Datatype*: reëel getal

*Eenheid*: meter


## `b3_h_maaiveld`

Elevatie boven zeeniveau (NAP) op het maaiveldniveau van het pand. Berekend als het 5e percentiel van de maaiveldpunten gevonden binnen een radius van 4 meter van het pand.

*Datatype*: reëel getal

*Eenheid*: meter


## `b3_kas_warenhuis`

Het gebouw is een kas of een warenhuis volgens de TOP10NL of heeft een oppervlakte van meer dan 70000 vierkante meter.

*Datatype*: categorisch

*Eenheid*: yes/no


## `b3_mutatie_ahn3_ahn4`

`true` als er een significante verandering is gedetecteerd in het pand tussen de AHN3 en AHN4 puntenwolken.

*Datatype*: categorisch

*Eenheid*: yes/no


## `b3_nodata_fractie_ahn3`

Fractie van het BAG polygon met onvoldoende AHN3 punten dekking. Alleen punten geclassificeerd als gebouw of grond worden gebruikt.

*Datatype*: reëel getal

*Eenheid*: -


## `b3_nodata_fractie_ahn4`

Fractie van het BAG polygon met onvoldoende AHN4 punten dekking. Alleen punten geclassificeerd als gebouw of grond worden gebruikt.

*Datatype*: reëel getal

*Eenheid*: -


## `b3_nodata_radius_ahn3`

Straal van de grootste cirkel die binnen het BAG polygoon valt en geen AHN3 punten bevat. Alleen punten geclassificeerd als gebouw of grond worden gebruikt.

*Datatype*: reëel getal

*Eenheid*: meter


## `b3_nodata_radius_ahn4`

Straal van de grootste cirkel die binnen het BAG polygoon valt en geen AHN4 punten bevat. Alleen punten geclassificeerd als gebouw of grond worden gebruikt.

*Datatype*: reëel getal

*Eenheid*: meter


## `b3_opp_buitenmuur`

Totale oppervlakte van de buitenmuren. Eenheid: vierkante meter.

*Datatype*: reëel getal

*Eenheid*: vierkante meter


## `b3_opp_dak_plat`

Totale oppervlakte van de platte delen van het dak. Eenheid: vierkante meter.

*Datatype*: reëel getal

*Eenheid*: vierkante meter


## `b3_opp_dak_schuin`

Totale oppervlakte van de schuine delen van het dak. Eenheid: vierkante meter.

*Datatype*: reëel getal

*Eenheid*: vierkante meter


## `b3_opp_grond`

Totale oppervlakte begane grond. Eenheid: vierkante meter.

*Datatype*: reëel getal

*Eenheid*: vierkante meter


## `b3_opp_scheidingsmuur`

Totale oppervlakte van de woningscheidende muren. Eenheid: vierkante meter.

*Datatype*: reëel getal

*Eenheid*: vierkante meter


## `b3_pand_deel_id`

Panddeel ID. Een pand kan meerdere delen hebben wanneer het is opgedeeld vanwege ondergrondse delen.

*Datatype*: nominaal getal

*Eenheid*: -


## `b3_puntdichtheid_ahn3`

Puntdichtheid van de AHN3-puntenwolk voor het pand. Alleen punten geclassificeerd als gebouw of grond worden in beschouwing genomen.

*Datatype*: nominaal getal

*Eenheid*: punten per vierkante meter


## `b3_puntdichtheid_ahn4`

Puntdichtheid van de AHN4-puntenwolk voor het pand. Alleen punten geclassificeerd als gebouw of grond worden in beschouwing genomen. Eenheid: punten per vierkante meter.

*Datatype*: nominaal getal

*Eenheid*: punten per vierkante meter


## `b3_pw_bron`

Bron van de puntenwolk, bijv. AHN3 of AHN4.

*Datatype*: tekst

*Eenheid*: -


## `b3_pw_datum`

Inwinjaar van de bron puntenwolk. Dit is bepaald door naar de GPS tijd van de AHN punten voor dit pand. Indien een goede GPS tijd niet beschikbaar is, wordt de file creation date van het puntenwolk bestand gebruikt.

*Datatype*: datum

*Eenheid*: `YYYY`


## `b3_pw_selectie_reden`

Geeft achtergrond informatie met betrekking tot de puntenwolk selectie (zie `pw_bron` attribuut).

*Datatype*: categorisch

*Eenheid*: -

*Waarden*:

| Waarden | Omschrijving |
| :----- | :----------- |
| ``PREFERRED_AND_LATEST`` | De geselecteerde puntenwolk heeft een goede puntdekking en er is geen recentere puntenwolk met voldoende puntdekking beschikbaar. |
| ``PREFERRED_NOT_LATEST`` | De geselecteerde puntenwolk heeft een goede point puntdekking en er is een recentere puntenwolk met voldoende puntdekking beschikbaar. De nieuwere puntewolk is echter niet geselecteerd omdat er geen mutatie is gedecteerd. |
| ``LATEST_WITH_MUTATION`` | De geselecteerde puntenwolk heeft een goede puntdekking en er is een mutatie ten opzichte van een oudere puntenwolk gedetecteerd. |
| ``_HIGHEST_YET_INSUFFICIENT_COVERAGE`` | De geselecteerde puntenwolk heeft hoogste puntdekking van alle kandidaat puntenwolken, maar de puntdekking is alsnog mogelijk niet voldoende. Dit gebouw vertoont mogelijk reconstructie fouten. |
| ``_LATEST_BUT_OUTDATED`` | De geselecteerde puntenwolk is de meerst recente, maar is mogelijk alsnog te oud voor dit pand. Dit kan gebeurt als het oorspronkelijk bouwjaar gelijk aan of jonger is dan het inwin jaar van de puntenwolk. |

## `b3_reconstructie_onvolledig`

Geeft aan of de volledige LoD1.2/LoD1.3/LoD2.2 reconstructie is overgeslagen voor het pand.

*Datatype*: None

*Eenheid*: None


## `b3_rmse_lod12`

Root Mean Square Error van de 3D afstanden tussen de puntenwolk en het LoD1.2 model. Eenheid: meter.

*Datatype*: reëel getal

*Eenheid*: meter


## `b3_rmse_lod13`

Root Mean Square Error van de 3D afstanden tussen de puntenwolk en het LoD1.3 model. Eenheid: meter.

*Datatype*: reëel getal

*Eenheid*: meter


## `b3_rmse_lod22`

Root Mean Square Error van de 3D afstanden tussen de puntenwolk en het LoD2.2 model. Eenheid: meter.

*Datatype*: reëel getal

*Eenheid*: meter


## `b3_val3dity_lod12`

[Val3dity foutcodes](https://val3dity.readthedocs.io/en/latest/errors) voor het LoD1.2 3D model. Lege lijst betekent valide geometry.

*Datatype*: lijst

*Eenheid*: -


## `b3_val3dity_lod13`

[Val3dity foutcodes](https://val3dity.readthedocs.io/en/latest/errors) voor het LoD1.3 3D model. Lege lijst betekent valide geometry.

*Datatype*: lijst

*Eenheid*: -


## `b3_val3dity_lod22`

[Val3dity foutcodes](https://val3dity.readthedocs.io/en/latest/errors) voor het LoD2.2 3D model. Lege lijst betekent valide geometry.

*Datatype*: lijst

*Eenheid*: -


## `b3_volume_lod12`

Volume van het LoD1.2-model. Eenheid: kubieke meter.

*Datatype*: reëel getal

*Eenheid*: kubieke meter


## `b3_volume_lod13`

Volume van het LoD1.3-model. Eenheid: kubieke meter.

*Datatype*: reëel getal

*Eenheid*: kubieke meter


## `b3_volume_lod22`

Volume van het LoD2.2-model. Eenheid: kubieke meter.

*Datatype*: reëel getal

*Eenheid*: kubieke meter


## `begingeldigheid`

De datum waarop een versie van een BAG-object geldig is in de werkelijkheid conform de ingangsdatum in het brondocument. Dit tijdstip wordt vastgelegd in de beginGeldigheid. Als er geen expliciete ingangsdatum van geldigheid is opgenomen, wordt de datum van het brondocument overgenomen.

*Datatype*: datum

*Eenheid*: `YYYY-MM-DD`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


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


## `eindregistratie`

Houdt verband met de geschiedenis van de pandregistratie en de versie.

*Datatype*: datum-tijd

*Eenheid*: `YYYY-MM-DDThh:mm:ss.sss`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `geconstateerd`

Een aanduiding waarmee kan worden aangegeven dat een pand in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake was van een regulier brondocument voor deze opname.

*Datatype*: categorisch

*Eenheid*: yes/no

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `identificatie`

De unieke BAG aanduiding van een pand.

*Datatype*: tekst

*Eenheid*: -

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `labels`

Pand-oppervlaksemantiek. Alleen beschikbaar in de GPKG 3D lagen. Dit is een array van integers, waarbij een integer verwijst naar een oppervlaktype (0: `GroundSurface`, 1: `RoofSurface`, 2: `OuterWallSurface`, 3: `InnerWallSurface`). Als een oppervlak geen semantische waarde heeft, wordt NULL gebruikt. De lengte van de array staat dus gelijk aan het aantal 3D polygonen van de geometrie, en de volgorde van waarden in de array correspondeert met de volgorde van de polygonen.

*Datatype*: lijst

*Eenheid*: -


## `oorspronkelijkbouwjaar`

De aanduiding van het jaar waarin een pand oorspronkelijk als bouwkundig gereed is of zal worden opgeleverd.

*Datatype*: datum

*Eenheid*: `YYYY`


## `status`

De fase van de levenscyclus van een pand, waarin het betreffende pand zich bevindt.

*Datatype*: categorisch

*Eenheid*: -

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


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


## `tijdstipregistratie`

Houdt verband met de geschiedenis van de pandregistratie en de versie.

*Datatype*: datum-tijd

*Eenheid*: `YYYY-MM-DDThh:mm:ss.sss`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `tijdstipregistratielv`

Dit is het tijdstip waarop een versie van een BAG-object is opgenomen in de registratie van de landelijke voorziening. De gegevens komen daarmee beschikbaar voor afnemers.

*Datatype*: datum-tijd

*Eenheid*: `YYYY-MM-DDThh:mm:ss.sss`

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)


## `voorkomenidentificatie`

Houdt verband met de geschiedenis van de pandregistratie en de versie.

*Datatype*: ordinaal getal

*Eenheid*: -

*Bron*: BAG. Zie [BAG Catalogus](https://www.geobasisregistraties.nl/documenten/publicatie/2018/03/12/catalogus-2018)

