# Databronnen

De kenmerken en kwaliteit van de 3D BAG hangen af van de inputdata die gebruikt wordt voor de 3D reconstructie. Hoe beter de inputdata, des te beter de kwaliteit van het gereconstrueerde 3D model. Onze implementatiekeuzes zijn dan ook deels gebaseerd op specifieke eigenschappen van de input data. Om beter te begrijpen wat de 3D BAG nu eigenlijk is, geven we hier meer details over de inputdata op basis waarvan de 3D BAG is gecreëerd.

## BAG

De [Basisregistratie Adressen en Gebouwen (BAG)](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag) is de meest gedetailleerde en openlijk beschikbare dataset van gebouwen en adressen in Nederland. Het bevat informatie over ieder adres in een gebouw, zoals het huidige gebruik, constructiedatum of registratiestatus. De dataset wordt regelmatig geüpdatet met geregistreerde, gebouwde of gesloopte gebouwen. Gemeenten zijn als bronhouders van de BAG verantwoordelijk voor de inwinning van de BAG-gegevens binnen hun grenzen en het waarborgen van de kwaliteit daarvan. Deze gegevens worden centraal beschikbaar gesteld door het Kadaster.

De BAG bevat meerdere objecttypen. Voor de 3D BAG worden alleen de panden gebruikt. De polygonen in de BAG representeren de omlijning van panden als de projectie van bovenaf (inclusief ondergrondse delen), in tegenstelling tot de BGT die de geometrie van gebouwen modelleert daar waar het pand het maaiveld raakt, de zogenaamde footprint. De geometrie van BAG-panden wordt verkregen uit luchtfoto's en terrestrische metingen en kent een positionele nauwkeurigheid van 30 cm. Een overzicht van de attributen van BAG-objecten is [hier](https://imbag.github.io/praktijkhandleiding/attributen) te vinden.

Als inputdata voor de 3D BAG wordt altijd de meest recente [BAG 2.0](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag/bag-2.0-producten/bag-2.0-wat-is-er-veranderd) gebruikt. 

## AHN

Het [Actueel Hoogtebestand Nederland (AHN)](https://www.ahn.nl/>) is het openlijk beschikbare digitale hoogtemodel van Nederland. Vanuit de lucht worden door middel van LiDAR-metingen precieze en gedetailleerde hoogtegegevens ingewonnen, resulterend in een dataset met gemiddeld 8 punten per vierkante meter voor de huidige AHN versie (AHN3).

Voor de 3D BAG wordt er gebruikt gemaakt van AHN3. De data is in verschillende jaren ingewonnen tussen 2014 en 2019, afhankelijk van het gebied. Informatie over het precieze inwinjaar van een specifiek gebied kun je [hier](https://www.ahn.nl/historie) vinden.

De inwinperiode van het AHN is tamelijk lang. Dit kan leiden tot verouderde data wat problematisch kan zijn voor 3D reconstructie. Het gebouwenbestand verandert echter relatief langzaam, alhoewel in stedelijke gebieden sneller dan in landelijk gebied. Het AHN3 bevat helaas geen specifieke temporele gegevens. Het bevat namelijk alleen de datum waarop een specifieke tegel gemaakt is; niet de precieze inwindatum per punt. Om deze reden wordt er in de 3D BAG aangegeven welke panden mogelijk zijn veranderd in het jaar waarin de hoogtepunten zijn opgenomen en welke panden zeker verouderd zijn. We schatten dat ongeveer 95% van de panden nog valide zijn (voor de 3D BAG gegenereerd in maart 2021).

Verder is er variatie in de puntendichtheid van het AHN per pand-polygoon. Gaten in de puntenwolk worden veroorzaakt door bijvoorbeeld occlusie, water/ramen op de daken of de scanhoek bij inwinning. De classificatie van de punten in grond- en gebouwpunten in het AHN is ook niet altijd correct. Het aantal beschikbare punten en de verdeling ervan over het dakvlak heeft een grote invloed op de nauwkeurigheid van de reconstructie. De kwaliteitsattributen bij de gebouwen geven hier een indicatie van.

### AHN4?

Op het moment van schrijven komt [het nieuwe AHN4](https://www.ahn.nl/ahn-4) binnenkort beschikbaar voor een deel van het land. Waar het AHN3 binnen een periode van 5 jaar is ingewonnen, moet de inwinning van AHN4 binnen 3 jaar gebeuren. Ook kan het zijn dat de kwaliteit ervan verandert wat (zeer waarschijnlijk positieve) impact zal hebben op de algoritmen van de 3D BAG. Het feit dat de nieuwe data up-to-date er zijn zorgt er in ieder geval voor dat we de 3D BAG kunnen verbeteren. Zodra de AHN4 beschikbaar is, zullen we dit zo snel mogelijk integreren in ons proces.

## BGT

De [Basisregistratie Grootschalige Topografie (BGT)](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bgt) is een nationale dataset die naast panden ook onder andere wegen, water, spoorlijnen en groen omvat. De bronhouders zijn organisaties met een publieke taak voor het beheer van de openbare ruimte zoals provincies, gemeenten en waterschappen.

De BGT wordt gebruikt in de 3D BAG om panden te detecteren die overlappen met een ander object; een ander pand (uit de BAG), weg of water. Hierdoor gebruiken we alleen wegdeel en waterdeel uit de BGT. Deze panden kunnen dan in de BAG aangemerkt worden als overlappend, voordat de 3D BAG wordt geproduceerd.

## TOP10NL

TOP10NL is onderdeel van de [TOPNL-bestanden](https://www.kadaster.nl/zakelijk/producten/geo-informatie/topnl). Deze behoren tot de [Basisregistratie Topografie (BRT)](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brt). Ditzijn eveneens landsdekkende datasets, die gebruikt kunnen worden als gegevensbron en als ondergrond voor visualisatie. De TOP10NL kan gebruikt worden op schaalniveaus tussen 1:5.000 tot en met 1:25.000. Het bevat onder andere wegdelen, gebouwen en terreinen.

Uit deze dataset worden uitsluitend de gebouwen gebruikt. Uit de classificatie hiervan kunnen we kassen en warenhuizen identificeren, wat problematische gevallen zijn bij de 3D reconstructie. Daarom modelleren we ze uitsluitend in versimpelde vorm.
