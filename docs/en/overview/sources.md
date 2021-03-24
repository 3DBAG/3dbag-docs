# Data sources

The quality and characteristics of the 3D BAG partly depend on the source data that we use. The better the input, the better the 3D BAG. Several of our choices were governed by the characteristics of these input data sets. Therefore, in order to better understand the 3D BAG, it is important to take a look at the data sources first.

## BAG

The [Register of Buildings and Addresses](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag) (BAG) is the most detailed, openly available data set on buildings and addresses in the Netherlands. It contains information about each address in a building, such as its current use, construction date or registration status. The data set is regularly updated as new buildings are registered, built or demolished. The municipalities are responsible for the acquisition, maintenance and quality assurance of the data within their boundaries. The data from all municipalities together are centralised and published by Kadaster.

The BAG contains several types of geometrical objects. For the 3D BAG only the *buildings* are used. The polygons in the BAG represent the outline of the building as the projection of the building as seen from above (including underground parts). While in comparison, the BGT registers the footprint of the building as it touches the terrain. The geometry of BAG buildings is acquired from aerial photos and terrestrial measurements and the data positional data accuracy is 30cm. An overview of the attributes of the BAG can be found [in the BAG manual](https://imbag.github.io/praktijkhandleiding/attributen). 

## AHN

The [National Height Model](https://www.ahn.nl) of the Netherlands (AHN) is the openly available elevation data set of the Netherlands. This is acquired through airborne laser scanning (LiDAR), with an average point density of 8 points per square meter for the current version.

For the 3D BAG we currently use the third version, AHN3. This version was collected in stages, between 2014 and 2019. [Here](https://www.ahn.nl/historie) you can find the collection dates for each region in the Netherlands.

One of the arguments against using the AHN for 3D reconstruction is that is deemed to be out dated by design, due to long mission times for acquiring the scans. However, the building stock changes in a relatively slow pace. This pace being faster in metropolitan regions and slower in remote areas of the country. Unfortunately, timestamps are not provided with the point data in the AHN3, but we can only compare the acquisition years for a region to the construction years of the buildings. From this we estimate that about 95% of the measured building heights are still valid (estimated for the 3D BAG generated in March 2021).

Additionally, there is a variation in the point density between buildings. There can be gaps in the point cloud, caused by an occlusion through objects or water ponds on roofs. The number of available points, their distribution and accurate classification has a very significant impact on the quality of the reconstructed models.

### AHN4?

At the moment of writing the new [AHN4](https://www.ahn.nl/ahn-4) will soon become available for a part of the country. While the AHN3 was acquired in 5 years, the AHN4 must be done in 3 years. The new AHN will have a different, improved quality, compared to the AHN3, and we expect that this will have a visible impact on the 3D BAG as well. As soon as the first region is available, we will integrate it into our process.

## BGT

The [Large Scale Topographic Map](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bgt) of the Netherlands contains many object types besides buildings, such as roads, water ways, railways, and it forms a complete coverage of the country. The responsible source providers are organisations that have a task to maintain public space, such as the provinces, municipalities and water boards, each in their own administration.

For the 3D BAG, the BGT is used for detecting the buildings that overlap with other objects, such as roads and other buildings. Such overlapping buildings are marked and excluded from the reconstruction process.

## TOP10NL

The TOP10NL is part of the [TOPNL data sets](https://www.kadaster.nl/zakelijk/producten/geo-informatie/topnl), which belong to the [Topographic Register](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brt) of the Netherlands. These are topographic maps at various scales, ranging from 1:10,000 to 1:1,500,000. They can be used as data source, as well as base maps in visualisations.

From the TOP10NL we only use the buildings in order to identify the greenhouses and large warehouses among the BAG objects. Due to their glass roof, greenhouses are problematic for our reconstruction algorithm. Therefore we only model them with a simplified shape.
