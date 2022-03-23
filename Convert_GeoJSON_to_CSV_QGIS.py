# this script was written by Daniel Clement - 2022

# this script uses qgis to convert a GeoJSON to a CSV file. Only works for point data.

# use the QGIS interpreter at ~ "C:\Program Files\QGIS 3.14\bin\python-qgis.bat"
# written for QGIS 3.14.5

# do imports
from qgis.core import *
from glob import glob

# set input parameters
#######################################################################################################################
# the folder where the GeoJSON's are located
inDir = r"C:\Data\Example_Folder"
#######################################################################################################################

# create list of all GeoJSON files in the input folder
inFiles = glob(inDir + "/*.geojson")

# Ensure there are input files in inDir, else throw an error and stop the script
if len(inFiles) > 0:
    pass
else:
    print("ERROR - No input files found...")
    exit()

# loop through each geojson in inFiles and convert to a csv
for f, file in enumerate(inFiles, start=1):
    # Print completion progress number
    countValue = ("%s of %s"%(f, len(inFiles)))
    print("\n" + countValue)

    # create the output CSV name/path
    outCsv = file.replace(".geojson", "_Qgis.csv")

    # create a QGIS vector layer from the input GeoJSON file
    layer = QgsVectorLayer(file, "geojson_file", "ogr")

    print("Converting GeoJSON...")
    # use the QGIS vector file writer to write/convert the GeoJSON to CSV
    QgsVectorFileWriter.writeAsVectorFormat(layer,
                                            outCsv,
                                            "utf-8",
                                            driverName="CSV",
                                            layerOptions=['GEOMETRY=AS_XY']
                                            )

    print("GeoJSON successfully converted!")

# get number of files processed
numInFiles = len(inFiles)
numOutFiles = len(glob(inDir + "/*.csv"))

print("\n####################################################################################")
# check to see if number of in files equal out files
if numOutFiles == numInFiles:
    print("All GeoJSON's successfully converted to CSV!")
else:
    print("Error! - Not all GeoJSON's successfully converted. :(")
print("####################################################################################")