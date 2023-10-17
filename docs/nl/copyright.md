# Copyright en licentie

## Data en documentatie

 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://3dbag.nl">3DBAG</a> door de <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://3d.bk.tudelft.nl/">3D geoinformation onderzoeksgroep</a> en <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://3dgi.xyz/">3DGI</a> is gelicentieerd onder <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p> 

De 3DBAG is open data. Dit geldt ook voor alle downloadbare databestanden en data verspreid via webservices. Het staat je vrij om de 3DBAG data te kopiëren, verspreiden en aan te passen, zo lang je:

1. credits geeft aan de 3D geoinformation group en 3DGI,
2. een link naar de licentie bijvoegt,
3. en aangeeft als je enige veranderingen aan hebt gebracht aan de data.

*Let op dat sommige inhoud van de documentatie hergebruikt is uit andere teksten. De bron van deze inhoud is expliciet aangegeven, en het is belangrijk om je te houden aan diens respectievelijke licentie wanneer je deze gebruikt.*

### Hoe credits te geven aan de 3DBAG data

We vereisen dat je de regel “© 3DBAG door tudelft3d en 3DGI” gebruikt bij je toepassing.

In digitale media moet je eveneens een link naar [deze copyright-pagina](https://docs.3dbag.nl/en/copyright) bijvoegen. In geprinte media, of waar links niet mogelijk zijn, is de beste manier om de regel "3DBAG door de 3D geoinformation onderzoeksgroep (TU Delft) en 3DGI" bij te voegen, en de lezers te verwijzen naar "3dbag.nl".

De naam *tudelft3d* is een korte alias van de volledige naam *3D geoinformation research group*.

Als je de 3DBAG data integreert in een interactieve elektronische kaart/visualisatie, moet je de genoemde tekstregel plaatsen in de rechteronderhoek van de kaart.

### Citeren van 3DBAG

Verwijs naar het artikel [Automated 3D Reconstruction of LoD2 and LoD1 Models for All 10 Million Buildings of the Netherlands](https://doi.org/10.14358/PERS.21-00032R2).

```
@misc{peters2022,
      title={Automated 3D reconstruction of LoD2 and LoD1 models for all 10 million buildings of the Netherlands}, 
      author = "Ravi Peters and Bal{\'a}zs Dukai and Stelios Vitalis and {van Liempt}, Jordi and Jantien Stoter",
      year = "2022",
      doi = "10.14358/PERS.21-00032R2",
      language = "English",
      volume = "88",
      pages = "165--170",
      journal = "Photogrammetric Engineering and Remote Sensing",
      issn = "0099-1112",
      publisher = "American Society for Photogrammetry and Remote Sensing",
      number = "3",
}
```

## Software

De software en componenten die we hebben ontwikkeld voor het maken en aanbieden van de 3DBAG zijn onafhankelijk van de 3DBAG data en documentatie gelicentieerd.

Voor onze viewer maken we gebruik van [3DTilesRendererJS](https://github.com/NASA-AMMOS/3DTilesRendererJS) ([licentie](https://github.com/NASA-AMMOS/3DTilesRendererJS/blob/master/LICENSE)) door NASA AMMOS en [pg2b3dm](https://github.com/Geodan/pg2b3dm/) ([licentie](https://github.com/Geodan/pg2b3dm/blob/master/LICENSE)) door Geodan.
