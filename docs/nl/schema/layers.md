# Datalagen

![3dbag_layers](../images/3d_bag_layers_nl.png){ width=100% }

De bovenstaande figuur laat het verband zien tussen een gebouw in het echt en hoe het is gemodelleerd en beschikbaar in de 3DBAG. De BAG modelleert gebouwen in 2D als de grootste omtrek, gezien vanaf boven. Dat komt neer op een enkele 2D polygon per gebouw, zoals de zwarte polygoon in de figuur. Om deze reden bevat het **BAG-polygoon** ook de delen van het gebouw die zich ondergronds bevinden.

Om een nauwkeurig model van de <span style="color:#24a1c8ff">**bovengrondse**</span> delen van een gebouw te maken, snijden we het <span style="color:#ff0000ff">**ondergrondse**</span> deel van de BAG-polygoon eraf. We nemen alleen bovengrondse delen mee, aangezien we geen data hebben over de 3D omvang van ondergrondse delen.

Voor de bovengrondse delen genereren we vervolgens de 3D modellen in LoD1.2, 1.3 en 2.2. We weten dat het bij sommige toepassingen makkelijker is om 2D polygonen in te lezen, en de informatie over de gebouwhoogte als attributen. Daarom bieden we ook een 2D versie aan voor iedere LoD. Bovendien kan de gebruiker hierdoor kiezen uit de verschillende referentiehoogtes die we berekenen per gebouw.

!!! note "b3_kas_warenhuis"
    In het geval van kassen en grote magazijnen snijden we geen delen van het BAG-pand en nemen we de polygoon zoals die is en genereren we slechts een LoD1.1 blokmodel. Dit soort gebouwen hebben dus alleen een LoD1.1 model en zijn gemarkeerd met de attribuutwaarde [`b3_kas_warenhuis`](attributes.md#b3_kas_warenhuis)` = true`.

Bij de 2D modellen representeren de polygonen de 2D projectie van de dakvlakken van het 3D model. Voor LoD1.2 en LoD1.3 kan het 3D model volledig gereconstrueerd worden uit het 2D model, door de 2D polygonen te nemen en elk van deze op te trekken tot een van hun [`b3_h_dak_*`](attributes.md#b3_h_dak_50p) hoogtewaarden vanaf hun hoogte op maaiveld, welke is vastgelegd in [b3_h_maaiveld](attributes.md#b3_h_maaiveld). Echter is dit niet het geval voor de LoD2.2 modellen, omdat deze schuine daken hebben die niet gerepresenteerd kunnen worden door een 2D polygoon en een enkele hoogtewaarde.

De 3DBAG heeft 6 geometrische representaties van een BAG-object (een *feature*). De 6 representaties zijn de 2D en 3D varianten van de LoD1.2, LoD1.3 en LoD2.2 modellen van de feature. Afhankelijk van de representatie kan een enkele feature meerdere geometrie-delen hebben.

Sommige gebouwen hebben meerdere niet-verbonden bovengrondse delen, terwijl ze aan elkaar verbonden zijn door bijvoorbeeld een ondergrondse garage. In deze gevallen kan het attribuut [`b3_pand_deel_id`](attributes.md#b3_pand_deel_id) kan deze verschillende delen identificeren binnen dezelfde feature.

De onderstaande figuur illustreert de relatie tussen de **feature** en de verschillende <span style="color:#24a1c8ff">**bovengrondse**</span> geometrie-delen.

![3dbag_ref](../../../images_common/3d_bag_layers_reference.png){ width=100% }

## Berekening van hoogtes

Elke LoD van een gebouw in de 3DBAG heeft een maaiveld hoogte (`h_maaiveld`) en een of meerdere dag hoogtes (`b3_h_dak_*`). Alle hoogtes zijn gegeven in  RD/NAP (EPSG:7408, onderdeel van EPSG:7415).

De maaiveld hoogte is bepaald as het 5e hoogte percentiel van alle AHN punten binnen een straal van 4 meter rondom het BAG polygon van het gebouw.

De dak hoogtes ([`b3_h_dak_*`](attributes.md#b3_h_dak_50p)) voor een pand zijn berekend op basis van het meest getetailleerde gereconstrueerde 3D model (LoD2.2). Per dakvlak berekenen we altijd het 0e (minimum), 50e (mediaan), 70e, en 100e (maximum)  percentiel. [`b3_h_dak_50p`](attributes.md#b3_h_dak_50p) is bijvoorbeeld berekend als de mediaan van een dakvlak.

### Hoogtes in de 2D vs 3D lagen
Voor de 2D lagen zijn de hoogtes altijd gegeven als attribuut per gemodelleerd dakdeel zoals hierboven beschreven.

Voor de 3D lagen zijn de hoogtes niet gegeven als attributen omdat ze al expliciet zijn gemodelleerd in de 3D geometrie van het model. Voor de LoD1.2 en LoD1.3 lagen (waar ieder dakdeel op een constante hoogte is gemodelleerd) is het 70e percentiel gebruikt voor de extrusie.  In de LoD2.2 3D (`lod22_3d`) laag zijn de daken direkt met de dakvlakken gemodelleerd zoals die in de AHN puntenwolk gedetecteerd zijn.

!!! note "Hoogtes klikken in de 3D webviewer"
    Als je op een gebouw in onze 3D webviewer klikt, zal er een links onder in het scherm een hoogte getoond worden. Dit is de hoogte gemeten vanaf het maaiveld rondom het gebouw, oftewel `b3_h_maaiveld` is hier al vanaf getrokken.

<!-- start layers (DO NOT REMOVE THIS MARKER AND DO NOT EDIT THE TEXT BELOW. SEE README.) -->
## `ondergrond`

De ondergrondse delen van een BAG-polygoon die zijn verwijderd tijdens de reconstructie van de LoD1.2-, LoD1.3- en LoD2.2-modellen.


## `pand`

Bevat de attributen en geometrie van het `Pand`-object van de BAG, plus de attributen van de 3DBAG die verband hebben met het gehele gebouw. Omvat uitsluitend de gebouwen die daadwerkelijk door de reconstructie gegaan zijn. Het attribuut `fid` is het unieke, numerieke ID van de objecten. Naast dat het de primaire *key* is, wordt `fid` ook gebruikt voor het samenvoegen van andere lagen met `pand`.


## `lod12_3d`

Een 3D model van de bovengrondse gebouwdelen, gemodelleerd in LoD1.2. Kan samengevoegd worden met `pand` op `fid`.


## `lod12_2d`

De 2D projectie van het LoD1.2 model. De elevatie van de gedetecteerde LoD1.2 dakoppervlakken zijn opgeslagen als hoogteattributen ([`h_dak_*`](attributes.md#h_dak_50p)). Alleen de bovengrondse delen van de BAG-voetafdruk zijn meegenomen. Kan samengevoegd worden met `pand` op `fid`.


## `lod13_3d`

Een 3D model van de bovengrondse gebouwdelen, gemodelleerd in LoD1.3. Kan samengevoegd worden met `pand` op `fid`.


## `lod13_2d`

De 2D projectie van het LoD1.3 model. De elevatie van de gedetecteerde LoD1.3 dakoppervlakken zijn opgeslagen als hoogteattributen ([`h_dak_*`](attributes.md#h_dak_50p)). Alleen de bovengrondse delen van de BAG-voetafdruk zijn meegenomen. Kan samengevoegd worden met `pand` op `fid`.


## `lod22_3d`

Een 3D model van de bovengrondse gebouwdelen, gemodelleerd in LoD2.2. Kan samengevoegd worden met `pand` op `fid`.


## `lod22_2d`

De 2D projectie van het LoD2.2 model. De elevatie van de gedetecteerde LoD2.2 dakoppervlakken zijn opgeslagen als hoogteattributen ([`h_dak_*`](attributes.md#h_dak_50p)). Alleen de bovengrondse delen van de BAG-voetafdruk zijn meegenomen. Kan samengevoegd worden met `pand` op `fid`.

<!-- end layers (DO NOT REMOVE THIS MARKER) -->
