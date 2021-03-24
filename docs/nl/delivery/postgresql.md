<a href=https://www.postgresql.org/>PostgreSQL</a> is een open source systeem voor object-relationele databases. Met toevoeging van de <a href=https://postgis.net/>PostGIS</a> extensie is er ondersteuning voor geografische objecten. Het is geschikt om big geodata mee te verwerken. Om deze reden bieden wij de volledige 3D BAG data aan als PostgreSQL dump.

Het 3D BAG PostgreSQL backup-bestand heeft [alle attributen](../schema/attributes.md) en [alle lagen](../schema/layers.md#data-layers) die de 3D BAG heeft. Het bestand is gecreëerd met `pg_dump`, met de opties `--no-owner --no-privileges --format=directory`.

### De dump inladen

Met het volgende commando kan je de dump inladen. Pas in ieder geval de laatste twee regels aan (lees  [pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html) voor meer informatie):

```
pg_restore \
--no-owner \
--no-privileges \
--format=directory \
--jobs=8 \
<connectieparameters>
<pad naar ongezipt bestand>
```

`<connectieparameters>` zijn bijvoorbeeld `--port` en `--username`. 

Het kan een aantal uur duren tot het inladen gereed is.
