# madrid-house-prices
scripts to generate both data for second-hand house prices and renting prices in Madrid respectively.

For the data contained un the csv file for second-hand prices, I made it by hand, except melting the columns for the years. So if you would like to replicate from source, you'd have to do some manual pre-processing.

Visualization of the data was made using Tableau public. Results can be found here:
https://public.tableau.com/profile/hugo.villanua#!/vizhome/Madridpricem2/Madridpricem2
https://public.tableau.com/profile/hugo.villanua#!/vizhome/Madridrentm2/Madridrentm2

A brief explanation on how to prepare the shapefiles and how to visualize on Tableau is given below:

To plot personalized maps on Tableau these are the global steps:
- Get the shapefile of the polygons we want to plot.
- Convert the shapefile to EPSG: 4326, WGS 84 if it's not already.
- Create csv file with the separate polygons.
- Import csv to Tableau, use Polygon to create map.

If you need to convert the shapefile from a geodetic reference system different to EPSG: 4326, WGS 84, here's how to:
Download and install QGIS. On the left panel, click the Add Vector Layer icon.
In the Add vector layer dialog box, do the following:
-Under Source type, click Directory.
-Under Source, click Browse, and then navigate to and select the folder containing the shapefile.
-Click Open.

When opening the shapefile, it may ask for the input coordinate system. Select the appropriate one.
If it doesn't appear, in the layers panel left click on the layer we just opened. Click on Establish layer SRC, select the appropriate input coordinate system and click OK.
	
Once it's opened, in the layers panel left click on the layer we just opened. Click on Save as... and do the following:
-Under Format, select ESRI shape file.
-Under File name, create an empty folder, navigate to it and write a name for the new shapefile.
-Under SRC, select EPSG:4326, WGS 84 and click OK.
	
The fastest way to create the csv file is to go to this link (https://gallery.alteryx.com/#!app/Tableau-Shapefile-to-Polygon-Converter/5296f89120aaf905b8e7fb48), click on Run and upload all the shape files in a single .zip (make sure the zip only contains the shapefiles, if you put them inside of a folder the upload will fail). Click on Run again and once it's finished select the csv output file and download it.
Alternatively you can use the intructions given in this link (https://onlinehelp.tableau.com/current/pro/desktop/en-us/maps_shapefiles.html). A detailed explanation on how to create the number sequence for the path can be found at (https://community.tableau.com/docs/DOC-5831).

To import the csv and create the map follow the instructions in (https://onlinehelp.tableau.com/current/pro/desktop/en-us/maps_shapefiles.html).

Source files are provided in the data folder, including the prcessed ones.
Original sources can be found here:
Data for second-hand house prices (you have to select the data you want on the filters): http://www-2.munimadrid.es/CSE6/control/seleccionDatos?numSerie=5040300200
Data for renting prices: https://www.idealista.com/informes-precio-vivienda
Shapefiles for districts and neighborhoods (scroll down the page to "Delimitaciones Territoriales" and select "Barrios Madrid" and "Distritos"): http://www.madrid.org/nomecalles/DescargaBDTCorte.icm