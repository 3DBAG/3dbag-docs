<a href=http://paulbourke.net/dataformats/obj/>Wavefront OBJ</a> is een open bestandsformaat voor 3D graphics. Het bevat dus geen attributen van de 3D BAG gebouwen, maar uitsluitend de geometrieën. Het is voornamelijk beschikbaar voor het integreren van de 3D BAG data in CAD-software (voor bijvoorbeeld architecturele doeleinden) en software voor 3D-modellering (bijvoorbeeld <a href=https://www.blender.org/>Blender</a>).

### Blender

![Screenshot](../images/blender.jpg)

*Een 3D BAG tegel in OBJ-formaat geopend in Blender*

OBJ kan makkelijk geïmporteerd worden in Blender. Overigens is er ook een <a href=https://github.com/cityjson/Up3date>CityJSON plugin</a> beschikbaar.

Omdat de bestanden werkelijke (en dus grote) coördinaten bevatten en niet gecentreerd zijn rondom de origin (0, 0, 0) in Blender zie je in eerste instantie dat de objecten flikkeren. Het is een goed idee om ze te verplaatsen naar het midden van de scene.

![Screenshot](../images/blender2.jpg)

Kies bij het importeren van de data voor `Z Up` zodat het model juist georiënteerd wordt. Om het makkelijker te maken kan je ook `Split by Object` uitzetten, zodat alle gebouwen als één object geladen worden. Je kan na het importeren de camera focussen op het model door het te selecteren in `Scene Collection` rechts op het scherm, en vervolgens op `.` op het numpad te drukken (de normale `.` op het toetsenbord werkt niet).

![Screenshot](../images/blender3.jpg)

Selecteer vervolgens het object (of alle individuele objecten als je ze op die manier ingeladen hebt) en druk op Tab om de Edit Mode te openen. Klik op het pijltje dat gemarkeerd is in bovenstaande screenshot...

![Screenshot](../images/blender4.jpg)

En verander X en Y naar 0. Druk wederom op `.` op het numpad om de camera weer te focussen op het model.

