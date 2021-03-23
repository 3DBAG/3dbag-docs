# Databronnen

De kenmerken en kwaliteit van de 3D BAG hangen af van de invoerdata die gebruikt wordt om het te ontwikkelen. Hoe beter de invoerdata, des te beter het eindproduct kan worden. Ook keuzes die niet per se met kwaliteit te maken hebben zijn daarin terug te zien. Om de 3D BAG beter te begrijpen is het derhalve belangrijk om te weten waarmee de data gecreëerd zijn.

## BAG

De [Basisregistratie Adressen en Gebouwen (BAG)](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag) is de meest gedetailleerde en openlijk beschikbare dataset van gebouwen en adressen in Nederland. Het bevat informatie over ieder adres in een gebouw, zoals het huidige gebruik, constructiedatum of registratiestatus. De dataset wordt regelmatig geüpdatet met geregistreerde, gebouwde of gesloopte gebouwen. Gemeenten hebben als bronhouders van de BAG de verantwoordelijk voor het opnemen van de gegevens in de BAG binnen hun grenzen en het waarborgen van de kwaliteit daarvan. Deze gegevens worden centraal beschikbaar gesteld door het Kadaster.

De BAG bevat meerdere objecttypen, maar voor de 3D BAG worden alleen de panden gebruikt. De polygonen in de BAG representeren de voetafdrukken van panden als genomen van het bovenaanzicht (inclusief ondergrondse delen), in tegenstelling tot de BGT die gebaseerd is op waar het pand het maaiveld raakt. De geometrie van BAG-panden wordt verkregen uit luchtbeelden en terrestriële metingen, met een positionele accuraatheid van 30 cm. Een overzicht van de attributen die behoren tot BAG-objecten is [hier](https://imbag.github.io/praktijkhandleiding/attributen) te vinden.

Als invoerdata voor de 3D BAG wordt altijd de meest recente [BAG 2.0](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag/bag-2.0-producten/bag-2.0-wat-is-er-veranderd) gebruikt. 

## AHN

Het [Actueel Hoogtebestand Nederland (AHN)](https://www.ahn.nl/>) is het openlijk beschikbare digitale hoogtemodel van Nederland. Vanuit de lucht worden door middel van LiDAR-metingen precieze en gedetailleerde hoogtegegevens ingewonnen, resulterend in een dataset met gemiddeld 8 punten per vierkante meter.

Voor de 3D BAG wordt er gebruikt gemaakt van AHN3. Gebieden in het land zijn opgenomen in verschilende jaren, tussen 2014 en 2019. Om te weten te komen in welk jaar de data van een specifiek gebied zijn opgenomen kun je [deze link](https://www.ahn.nl/historie) volgen.

Omdat het inwinnen van het AHN lang duurt, raken bepaalde gebieden verouderd wat problematisch kan zijn voor 3D reconstructie. Het gebouwenbestand verandert echter relatief langzaam, doch in stedelijke gebieden sneller dan in dunbevolktere. Het AHN3 bevat helaas geen specifieke temporele gegevens. Het bevat namelijk alleen de datum waarop een specifieke tegel gemaakt is; niet de precieze inwindatum per punt. Om deze reden wordt er in de 3D BAG aangegeven welke panden mogelijk zijn veranderd in het jaar waarin de hoogtepunten zijn opgenomen en welke panden zeker verouderd zijn. We schatten dat ongeveer 95% van de gemeten hoogten van de panden nog valide is (geschat voor de 3D BAG gegenereerd in maart 2021).

Verder is er variatie in de puntendichtheid van het AHN per pand-polygoon. Er kunnen gaten zijn, veroorzaakt door bijvoorbeeld occlusie, water/ramen op de daken of de scanhoek bij inwinning. De classificatie van de punten in grond- en gebouwpunten is ook niet altijd perfect. Het aantal beschikbare punten en de verdeling ervan over het dakvlak heeft een grote invloed op de nauwkeurigheid van de reconstructie. De kwaliteitsattributen bij de gebouwen geven hier een indicatie van.

### AHN4?

Op het moment van schrijven komt [het nieuwe AHN4](https://www.ahn.nl/ahn-4) binnenkort uit voor een deel van het land. Waar het AHN3 binnen een periode van 5 jaar is ingewonnen, moet dit voor AHN4 binnen 3 jaar gebeuren. Ook kan het zijn dat de kwaliteit ervan verandert wat (zeer waarschijnlijk positieve) impact zal hebben op de algoritmen van de 3D BAG. Het feit dat de nieuwe data up-to-date zijn zorgt er in ieder geval voor dat we de 3D BAG kunnen verbeteren, wat zo snel mogelijk gedaan wordt.

## BGT

De [Basisregistratie Grootschalige Topografie (BGT)](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bgt) is een nationale dataset die naast panden ook onder andere wegen, water, spoorlijnen en groen omvat en een echte kaart vormt. De bronhouders, ofwel verantwoordelijken voor de data in hun eigen gebied, zijn de provincies, gemeenten en waterschappen.

De BGT wordt benut in de 3D BAG om panden te detecteren die overlappen met een ander object; een pand, weg of water. Derhalve worden alleen de typen pand, wegdeel en waterdeel gebruikt. Deze panden kunnen dan in de BAG aangemerkt worden als overlappend, voordat de 3D BAG wordt geproduceerd.

## TOP10NL

TOP10NL is onderdeel van de [TOPNL-bestanden](https://www.kadaster.nl/zakelijk/producten/geo-informatie/topnl). Deze behoren tot de [Basisregistratie Topografie (BRT)](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brt) en zijn eveneens landsdekkende datasets, die gebruikt kunnen worden als gegevensbron en als ondergrond voor gegevensvisualisering. De TOP10NL in het specifiek kan gebruikt worden op schaalniveaus tussen 1:5.000 tot en met 1:25.000. Het bevat onder andere wegdelen, gebouwen en terreinen.

Uit deze dataset worden uitsluitend de gebouwen gebruikt. Uit de classificatie hiervan kunnen we kassen en warenhuizen identificeren, wat problematische gevallen zijn bij de 3D reconstructie. Daarom modelleren we ze uitsluitend in versimpelde vorm.