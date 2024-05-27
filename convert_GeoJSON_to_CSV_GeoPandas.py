# this script was written by Daniel Clement - 2022
"""
This script uses qgis to convert a GeoJSON to a CSV file.
Only works for point data.
"""

# do imports
import geopandas as gpd
from glob import glob
from tqdm import tqdm

# set input parameters
##############################################################################
# the folder where the GeoJSON's are located
input_folder_path = r"C:\Data\folder_with_jsons"

##############################################################################


def convert_gjson_to_csv(in_gjson: str) -> str:
    # create the output CSV name/path
    out_csv = in_gjson.replace(".geojson", "_qgis.csv")

    # read the input geojson file into a geodataframe
    gdf = gpd.read_file(in_gjson)

    # save the geodataframe out as a csv file
    gdf.to_csv(out_csv)

    return out_csv


def main():
    # create list of all GeoJSON files in the input folder
    in_files = glob(input_folder_path + "/*.geojson")

    # make an empty list to hold output csv paths
    out_csv_path_list = []

    # Ensure there are input files in inDir, else throw an error and stop the
    # script
    if len(in_files) > 0:
        pass
    else:
        print("ERROR - No input files found...")
        exit()

    # loop through each geojson in inFiles and convert to a csv
    for file in tqdm(in_files, desc="Converting GeoJSONs to CSV"):
        out_csv = convert_gjson_to_csv(in_gjson=file)
        out_csv_path_list.append(out_csv)

    # get number of files processed
    num_in_files = len(in_files)
    num_out_files = len(out_csv_path_list)

    print("\n################################################################")
    # check to see if number of in files equal out files
    if num_out_files == num_in_files:
        print("All GeoJSON's successfully converted to CSV!")
    else:
        print("Error! - Not all GeoJSON's successfully converted. :(")
    print("##################################################################")


if __name__ == "__main__":
    main()
