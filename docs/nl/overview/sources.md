# Databronnen

De kenmerken en kwaliteit van de 3DBAG hangen af van de inputdata die gebruikt wordt voor de 3D reconstructie. Hoe beter de inputdata, des te beter de kwaliteit van het gereconstrueerde 3D model. Onze implementatiekeuzes zijn dan ook deels gebaseerd op specifieke eigenschappen van de input data. Om beter te begrijpen wat de 3DBAG nu eigenlijk is, geven we hier meer details over de inputdata op basis waarvan de 3DBAG is gecreëerd.

## BAG

De [Basisregistratie Adressen en Gebouwen (BAG)](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag) is de meest gedetailleerde en openlijk beschikbare dataset van gebouwen en adressen in Nederland. Het bevat informatie over ieder adres in een gebouw, zoals het huidige gebruik, constructiedatum of registratiestatus. De dataset wordt regelmatig geüpdatet met geregistreerde, gebouwde of gesloopte gebouwen. Gemeenten zijn als bronhouders van de BAG verantwoordelijk voor de inwinning van de BAG-gegevens binnen hun grenzen en het waarborgen van de kwaliteit daarvan. Deze gegevens worden centraal beschikbaar gesteld door het Kadaster.

De BAG bevat meerdere objecttypen. Voor de 3DBAG worden alleen de panden gebruikt. De polygonen in de BAG representeren de omlijning van panden als de projectie van bovenaf (inclusief ondergrondse delen), in tegenstelling tot de BGT die de geometrie van gebouwen modelleert daar waar het pand het maaiveld raakt, de zogenaamde footprint. De geometrie van BAG-panden wordt verkregen uit luchtfoto's en terrestrische metingen en kent een positionele nauwkeurigheid van 30 cm. Een overzicht van de attributen van BAG-objecten is [hier](https://imbag.github.io/praktijkhandleiding/attributen) te vinden.

Als inputdata voor de 3DBAG wordt altijd de meest recente [BAG 2.0](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag/bag-2.0-producten/bag-2.0-wat-is-er-veranderd) gebruikt. 

## AHN

Het [Actueel Hoogtebestand Nederland (AHN)](https://www.ahn.nl/>) is het openlijk beschikbare digitale hoogtemodel van Nederland. Vanuit de lucht worden door middel van LiDAR-metingen precieze en gedetailleerde hoogtegegevens ingewonnen, resulterend in een dataset met gemiddeld 8 punten per vierkante meter voor de huidige AHN versie (AHN3).

Voor de 3DBAG wordt er gebruikt gemaakt van een slimme combinatie van AHN3 en AHN4. AHN3 is tussen 2014 en 2019 ingewonnen, en AHN4 tussen 2020 en 2022. Informatie over het precieze inwinjaar van een specifiek gebied kun je [hier](https://www.ahn.nl/historie) vinden. Let op dat indien een gebouw gebouwd of gewijzigd is na de inwindatum van de meeste recente AHN puntenwolk, het voor kan komen dat dit gebouw nog niet bestaat of niet meer klopt in de 3DBAG.

Voor de laatste versie van de 3DBAG gebruiken we zowel AHN3 als AHN4. Zo kunnen we voor ieder BAG pand de best mogelijke 3D reconstructie realiseren. Als een pand sinds de inwinning van AHN3 niet gemuteerd is kiezen we de puntenwolk die de beste puntdekking biedt. Hiermee wordt de kans op foutjes in 3D reconstructie door grote delen zonder punten verminderd.

Dit neemt niet weg dat de puntendichtheid van het AHN tuseen verschillende panden maar ook binnen een pand-polygoon kan varieren. Gaten in de puntenwolk kunnen worden veroorzaakt door bijvoorbeeld occlusie, water/ramen op de daken of de scanhoek bij inwinning. De classificatie van de punten in grond- en gebouwpunten in het AHN is ook niet altijd correct. Het aantal beschikbare punten en de verdeling ervan over het dakvlak heeft een grote invloed op de nauwkeurigheid van de reconstructie. De kwaliteitsattributen bij de gebouwen geven hier een indicatie van.

## TOP10NL

TOP10NL is onderdeel van de [TOPNL-bestanden](https://www.kadaster.nl/zakelijk/producten/geo-informatie/topnl). Deze behoren tot de [Basisregistratie Topografie (BRT)](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brt). Ditzijn eveneens landsdekkende datasets, die gebruikt kunnen worden als gegevensbron en als ondergrond voor visualisatie. De TOP10NL kan gebruikt worden op schaalniveaus tussen 1:5.000 tot en met 1:25.000. Het bevat onder andere wegdelen, gebouwen en terreinen.

Uit deze dataset worden uitsluitend de gebouwen gebruikt. Uit de classificatie hiervan kunnen we kassen en warenhuizen identificeren, wat problematische gevallen zijn bij de 3D reconstructie. Daarom modelleren we die uitsluitend in versimpelde vorm.
