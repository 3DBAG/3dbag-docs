# Databronnen

De kenmerken en kwaliteit van de 3D BAG hangen af van de invoerdata die gebruikt wordt om het te ontwikkelen. Hoe beter de invoerdata, des te beter het eindproduct kan worden. Ook keuzes die niet per se met kwaliteit te maken hebben zijn daarin terug te zien. Om de 3D BAG beter te begrijpen is het derhalve belangrijk om te weten waarmee de data gecreëerd zijn.

## BAG

<a href=https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag>De Basisregistratie Adressen en Gebouwen (BAG)</a> is de meest gedetailleerde en open beschikbare dataset van gebouwen en adressen in Nederland. Het bevat informatie over ieder adres in een gebouw, zoals het huidige gebruik, constructiedatum of registratiestatus. Gemeenten hebben als bronhouders van de BAG de verantwoordelijk voor het opnemen van de gegevens in de BAG binnen hun grenzen en het waarborgen van de kwaliteit daarvan. Deze gegevens worden centraal beschikbaar gesteld door het Kadaster.

De BAG bevat meerdere objecttypen, maar voor de 3D BAG worden alleen de panden gebruikt. De (2D) geometrieën in de BAG representeren de voetafdrukken van gebouwen als genomen van het bovenaanzicht, in tegenstelling tot de BGT die gebaseerd is op het maaiveld. Een overzicht van de attributen die behoren tot BAG-objecten is <a href=https://imbag.github.io/praktijkhandleiding/attributen>hier</a> te vinden.

Als invoerdata voor de 3D BAG wordt altijd de meest recente <a href=https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag/bag-2.0-producten/bag-2.0-wat-is-er-veranderd>BAG 2.0</a> gebruikt. 

## AHN

<a href=https://www.ahn.nl/>Het Actueel Hoogtebestand Nederland (AHN)</a> is het openlijk beschikbare digitale hoogtemodel van Nederland. Vanuit de lucht worden door middel van LiDAR-metingen precieze en gedetailleerde hoogtegegevens ingewonnen, resulterend in een dataset met gemiddeld 8 punten per vierkante meter.

Voor de 3D BAG wordt er gebruikt gemaakt van AHN3. Gebieden in het land zijn opgenomen in verschilende jaren, tussen 2014 en 2019. Om te weten te komen in welk jaar de data van een specifiek gebied zijn opgenomen kan je <a href=https://www.ahn.nl/historie>deze link</a> volgen.

De temporele data van AHN3 kan niet tot op de dag bepaald worden. Het bevat namelijk alleen de datum waarop een specifieke tegel gemaakt is; niet de precieze inwindatum per punt. Om deze reden wordt er in de 3D BAG aangegeven welke gebouwen mogelijk zijn veranderd in het jaar waarin de hoogtepunten zijn opgenomen en welke gebouwen zeker verouderd zijn.

Verder is er variatie in de puntendichtheid van het AHN per pand-polygoon. Er kunnen gaten zijn, veroorzaakt door bijvoorbeeld occlusie, water/ramen op de daken of de scanhoek bij inwinning. De classificatie van de punten in grond- en gebouwpunten is ook niet altijd perfect. Het aantal beschikbare punten en de verdeling ervan over het dakvlak heeft een grote invloed op de nauwkeurigheid van de reconstructie. De kwaliteitsattributen bij de gebouwen geven hier een indicatie van.

### AHN4?

Op het moment van schrijven komt <a href=https://www.ahn.nl/ahn-4>het nieuwe AHN4</a> binnenkort uit voor een deel van het land. Waar het AHN3 binnen een periode van 5 jaar is ingewonnen, moet dit voor AHN4 binnen 3 jaar gebeuren. Ook kan het zijn dat de kwaliteit ervan verandert wat (zeer waarschijnlijk positieve) impact zal hebben op de algoritmen van de 3D BAG. Het feit dat de nieuwe data up-to-date zijn zorgt er in ieder geval voor dat we de 3D BAG kunnen verbeteren, wat zo snel mogelijk gedaan wordt.

## BGT

De Basisregistratie Grootschalige Topografie (BGT) is een nationale dataset die naast gebouwen ook onder andere wegen, water, spoorlijnen en groen omvat en een echte kaart vormt. De bronhouders, ofwel verantwoordelijken voor de data in hun eigen gebied, zijn de provincies, gemeenten en waterschappen.

De BGT wordt benut in de 3D BAG om gebouwen te detecteren die overlappen met een ander object; een gebouw, weg of water. Derhalve worden alleen de typen pand, wegdeel en waterdeel gebruikt. Deze gebouwen kunnen dan in de BAG aangemerkt worden als overlappend, voordat de 3D BAG wordt geproduceerd.

## TOP10NL

TOP10NL is onderdeel van de <a href=https://www.kadaster.nl/zakelijk/producten/geo-informatie/topnl>TOPNL-bestanden</a>. Deze behoren tot de <a href=https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brt>Basisregistratie Topografie (BRT)</a> en zijn eveneens landsdekkende datasets die gebruikt kunnen worden ten behoeve van het bekijken en bewerken van geo-informatie, als ondergrond voor gegevensvisualisering, en als geometrische referentie. De TOP10NL in het specifiek kan gebruikt worden op schaalniveaus tussen 1:5.000 tot en met 1:25.000. Zoals op <a href=https://www.kadaster.nl/zakelijk/producten/geo-informatie/topnl>de link</a> te vinden is, bevat het onder andere wegdelen, gebouwen en terreinen.

Uit deze dataset worden uitsluitend de gebouwen gebruikt. Uit de classificatie hiervan kunnen we kassen en warenhuizen identificeren, wat problematische gevallen zijn bij de 3D-reconstructie, en dit ook linken aan de BAG-panden. 