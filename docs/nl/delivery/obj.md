[Wavefront OBJ](http://paulbourke.net/dataformats/obj/) is een open bestandsformaat voor 3D graphics. Het bevat dus geen attributen van de 3D BAG gebouwen, maar uitsluitend de geometrieën. Het is voornamelijk beschikbaar voor het integreren van de 3D BAG data in 3D CAD software (waar mogelijk conversie van de data voor benodigd is) en software voor 3D-modellering (bijvoorbeeld [Blender](https://www.blender.org/)).

De OBJ-bestanden van de 3D BAG bevatten alleen de 3D geometrieën en [elke 3D laag](../schema/layers.md#data-layers) is opgeslagen in een apart bestand. Ze zijn gecomprimeerd in een ZIP-bestand per tegel. De object-coördinaten zijn in het [Amersfoort / RD New + NAP height](http://epsg.io/7415) geodetisch coördinatensysteem.

## Blender

<figure>
  <img src="../../../images_common/blender.jpg" />
  <figcaption>Een 3D BAG tegel in OBJ-formaat geopend in Blender.</figcaption>
</figure>

OBJ kan makkelijk geïmporteerd worden in Blender. Overigens is er ook een [CityJSON plugin](https://github.com/cityjson/Up3date) beschikbaar.

Omdat de bestanden werkelijke (en dus grote) coördinaten bevatten en niet gecentreerd zijn rondom de origin (0, 0, 0) in Blender zie je in eerste instantie dat de objecten flikkeren. Het is daarom een goed idee om ze te verplaatsen naar het midden van de scene.

![Screenshot](../../../images_common/blender2.jpg)

Kies bij het importeren van de data voor `Z Up` zodat het model juist georiënteerd wordt. Om het makkelijker te maken kan je ook `Split by Object` uitzetten, zodat alle gebouwen als één object geladen worden. Je kunt na het importeren de camera focussen op het model door het te selecteren in `Scene Collection` rechts op het scherm, en vervolgens op `.` op het numpad te drukken (de normale `.` op het toetsenbord werkt niet).

![Screenshot](../../../images_common/blender3.jpg)

Selecteer vervolgens het object (of alle individuele objecten als je ze op die manier ingeladen hebt) en druk op Tab om de Edit Mode te openen. Klik op het pijltje dat gemarkeerd is in bovenstaande screenshot...

![Screenshot](../../../images_common/blender4.jpg)

En verander X en Y naar 0. Druk wederom op `.` op het numpad om de camera weer te focussen op het model.

