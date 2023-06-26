# Data sources

The quality and characteristics of the 3D BAG partly depend on the source data that we use. The better the input, the better the 3D BAG. Several of our choices were governed by the characteristics of these input data sets. Therefore, in order to better understand the 3D BAG, it is important to take a look at the data sources first.

## BAG

The [Register of Buildings and Addresses](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag) (BAG) is the most detailed, openly available data set on buildings and addresses in the Netherlands. It contains information about each address in a building, such as its current use, construction date or registration status. The data set is regularly updated as new buildings are registered, built or demolished. The municipalities are responsible for the acquisition, maintenance and quality assurance of the data within their boundaries. The data from all municipalities together are centralised and published by Kadaster.

The BAG contains several types of geometrical objects. For the 3D BAG only the *buildings* are used. The polygons in the BAG represent the outline of the building as the projection of the building as seen from above (including underground parts). While in comparison, the BGT registers the footprint of the building as it touches the terrain. The geometry of BAG buildings is acquired from aerial photos and terrestrial measurements and the data positional data accuracy is 30 cm. An overview of the attributes of the BAG can be found [in the BAG manual](https://imbag.github.io/praktijkhandleiding/attributen). 

As source for the 3D BAG we always use the most recent [BAG 2.0](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag/bag-2.0-producten/bag-2.0-wat-is-er-veranderd) data.

## AHN

The [National Height Model](https://www.ahn.nl) of the Netherlands (AHN) is the openly available elevation data set of the Netherlands. This is acquired through airborne laser scanning (LiDAR), with an average point density of 8 points per square meter for the current version.

For the 3D BAG we use a smart combination of AHN3 and AHN4. AHN4 was acaquired between 2014 and 2019, and AHN4 between 2020 and 2022. [Here](https://www.ahn.nl/historie) you can find the collection dates for each region in the Netherlands. Be aware that if a building was very recently constructed or changed, it can happen that this building does not exist or is no longer correct in the the 3D BAG.

For the latest version of the 3D BAG we use both AHN3 and AHN4. This is to guarantee the best possible 3D reconstruction for each building. If a building has no mutation since the acquisition of AHN3, we pick the pointcloud with the best point coverage. This reduces the odds that a building contains small errors due to large no data gaps in the point cloud.

There can always be some variation in the point density between buildings and even within one building. There can be no data gaps in the point cloud, caused by an occlusion through objects, water ponds on roofs and scan angle. The number of available points, their distribution and accurate classification has a very significant impact on the quality of the reconstructed models. The quality attributes that we calculate for and assign to each model provide an indication of this quality.

## TOP10NL

The TOP10NL is part of the [TOPNL data sets](https://www.kadaster.nl/zakelijk/producten/geo-informatie/topnl), which belong to the [Topographic Register](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brt) of the Netherlands. The TOP10NL can be used at various scales, ranging from 1:5,000 to 1:25,000. It models several object types, including buildings and their function. The TOPNL data can be used as data source, as well as base maps in visualisations.

From the TOP10NL we only use the buildings in order to identify the greenhouses and large warehouses among the BAG objects. Due to their glass roof, greenhouses are problematic for our reconstruction algorithm. Therefore we only model these with a simplified shape.
