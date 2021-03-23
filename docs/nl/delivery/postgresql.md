<a href=https://www.postgresql.org/>PostgreSQL</a> is een open source systeem voor object-relationele databases. Met toevoeging van de <a href=https://postgis.net/>PostGIS</a> extensie is er ondersteuning voor geografische objecten. Het is geschikt om big geodata mee te verwerken. Om deze reden bieden wij de volledige 3D BAG data aan als PostgreSQL dump.

### De dump inladen

Met het volgende commando kan je de dump inladen (lees <a href=https://www.postgresql.org/docs/current/app-pgrestore.html>hier</a> voor meer informatie):

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
