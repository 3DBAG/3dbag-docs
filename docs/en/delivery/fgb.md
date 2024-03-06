[FlatGeobuf](https://flatgeobuf.org/) is a performant binary encoding for geographic data. We make the tile index for each 3DBAG release available in this format.

## QGIS
You can directly load the FlatGeobuf tile index with the URL that you find on the 3DBAG download page. No need to download the file. To to this go to `Layer > Add layer > Add Vector Layer`. Then select for `Source type` the option `HTTP(S),cloud,etc.`, paste the URL in the URI field and click the 'Add' button.

