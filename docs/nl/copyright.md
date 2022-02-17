# Copyright en licentie

## Data en documentatie

 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://3dbag.nl">3D BAG</a> door de <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://3d.bk.tudelft.nl/">3D geoinformation onderzoeksgroep</a> is gelicentieerd onder <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p> 

De 3D BAG is open data. Dit geldt ook voor alle downloadbare databestanden en data verspreid via webservices. Het staat je vrij om de 3D BAG data te kopiëren, verspreiden en aan te passen, zo lang je:

1. credits geeft aan de 3D geoinformation group,
2. een link naar de licentie bijvoegt,
3. en aangeeft als je enige veranderingen aan hebt gebracht aan de data.

*Let op dat sommige inhoud van de documentatie hergebruikt is uit andere teksten. De bron van deze inhoud is expliciet aangegeven, en het is belangrijk om je te houden aan diens respectievelijke licentie wanneer je deze gebruikt.*

### Hoe credits te geven aan de 3D BAG data

We vereisen dat je de regel “© 3D BAG by tudelft3d” gebruikt bij je toepassing.

In digitale media moet je eveneens een link naar [deze copyright-pagina](https://docs.3dbag.nl/en/copyright) bijvoegen. In geprinte media, of waar links niet mogelijk zijn, is de beste manier om de regel "3D BAG by 3D geoinformation research group, TU Delft" bij te voegen, en de lezers te verwijzen naar "3dbag.nl".

De naam *tudelft3d* is een korte alias van de volledige naam van onze groep, *3D geoinformation research group*. We gebruiken *tudelft3d* vaak bij onze communicatie.

Als je de 3D BAG data integreert in een interactieve elektronische kaart/visualisatie, moet je de genoemde tekstregel plaatsen in de rechteronderhoek van de kaart.

### Citeren van 3DBAG

Er is een [preprint](https://arxiv.org/abs/2201.01191) beschikbaar voor een publicatie in het maart 2022 uitgave van [*Journal of Photogrammetric Engineering & Remote Sensing*](https://www.asprs.org/asprs-publications/pers).

```
@misc{peters2021automated,
      title={Automated 3D reconstruction of LoD2 and LoD1 models for all 10 million buildings of the Netherlands}, 
      author={Ravi Peters and Balázs Dukai and Stelios Vitalis and Jordi van Liempt and Jantien Stoter},
      year={2021},
      eprint={2201.01191},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## Software

De software en componenten die we hebben ontwikkeld voor het maken en aanbieden van de 3D BAG zijn onafhankelijk van de 3D BAG data en documentatie gelicentieerd.

Voor onze viewer maken we gebruik van [3DTilesRendererJS](https://github.com/NASA-AMMOS/3DTilesRendererJS) ([licentie](https://github.com/NASA-AMMOS/3DTilesRendererJS/blob/master/LICENSE)) door NASA AMMOS en [pg2b3dm](https://github.com/Geodan/pg2b3dm/) ([licentie](https://github.com/Geodan/pg2b3dm/blob/master/LICENSE)) door Geodan.
