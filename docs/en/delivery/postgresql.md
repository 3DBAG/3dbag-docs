[PostgreSQL](https://www.postgresql.org/) is an open source relational database. With the [PostGIS](https://postgis.net/) extension it is suitable for storing and managing very large geospatial databases. Therefore, we provide a PostgreSQL database dump of the complete 3D BAG.

The 3D BAG PostgreSQL backup file contains [all attributes](../schema/attributes.md) and [all layers](../schema/layers.md#data-layers) that are available for the 3D BAG. The backup file was created with `pg_dump`, using the options `--no-owner --no-privileges --format=directory`.

## Importing the PostgreSQL backup

The backup can be restored with the following command. Adapt it to your requirements if needed (read more at [pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html)).

```
pg_restore \
--no-owner \
--no-privileges \
--format=directory \
--jobs=8 \
<connection parameters> \
<path to the unzipped backup file>
```

The `<connection parameters>` are `--port` and `--username` for instance. The restore process can take a long time.