# This script was written by Daniel Clement - 2022
# Python 3
"""
This script will take an input CSV file, search for any of characters with
accents, as listed below, and perform a find and replace for each of them to
normal/non-accent characters.
"""
import os.path

# set parameters
#############################################################################
# path to input CSV
in_csv_path = r"C:\data\example.csv"

#############################################################################

accent_char_dict = {
    "upperA": ["À", "Á", "Â", "Ã", "Ä"],
    "lowerA": ["à", "á", "â", "ã", "ä"],
    "upperC": ["Ç"],
    "lowerC": ["ç"],
    "upperE": ["È", "É", "Ê", "Ë"],
    "lowerE": ["è", "é", "ê", "ë"],
    "upperI": ["Ì", "Í", "Î", "Ï"],
    "lowerI": ["ì", "í", "î", "ï"],
    "upperN": ["Ñ"],
    "lowerN": ["ñ"],
    "upperO": ["Ò", "Ó", "Ô", "Õ", "Ö"],
    "lowerO": ["ò", "ó", "ô", "õ", "ö"],
    "upperS": ["Š"],
    "lowerS": ["š"],
    "upperU": ["Ú", "Û", "Ü", "Ù"],
    "lowerU": ["ù", "ú", "û", "ü"],
    "upperY": ["Ý", "Ÿ"],
    "lowerY": ["ý", "ÿ"],
    "upperZ": ["Ž"],
    "lowerZ": ["ž"],
}


def replace_accents(input_csv: str, accent_dict: dict) -> str:
    """
    Replaces the accent marks in a csv file with normal non-accent characters
    Args:
        input_csv: the path to the input csv as a string
        accent_dict: the dictionary containing lists of all the accent mark
                     characters
    Returns:
        the path to the output csv as a string
    """

    # create an empty dictionary
    master_dict = {}

    # build the dictionary using a reverse lookup
    master_dict.update({_: "A" for _ in accent_dict["upperA"]})
    master_dict.update({_: "a" for _ in accent_dict["lowerA"]})
    master_dict.update({_: "C" for _ in accent_dict["upperC"]})
    master_dict.update({_: "c" for _ in accent_dict["lowerC"]})
    master_dict.update({_: "E" for _ in accent_dict["upperE"]})
    master_dict.update({_: "e" for _ in accent_dict["lowerE"]})
    master_dict.update({_: "I" for _ in accent_dict["upperI"]})
    master_dict.update({_: "I" for _ in accent_dict["lowerI"]})
    master_dict.update({_: "N" for _ in accent_dict["upperN"]})
    master_dict.update({_: "n" for _ in accent_dict["lowerN"]})
    master_dict.update({_: "O" for _ in accent_dict["upperO"]})
    master_dict.update({_: "o" for _ in accent_dict["lowerO"]})
    master_dict.update({_: "S" for _ in accent_dict["upperS"]})
    master_dict.update({_: "s" for _ in accent_dict["lowerS"]})
    master_dict.update({_: "U" for _ in accent_dict["upperU"]})
    master_dict.update({_: "u" for _ in accent_dict["lowerU"]})
    master_dict.update({_: "Y" for _ in accent_dict["upperY"]})
    master_dict.update({_: "y" for _ in accent_dict["lowerY"]})
    master_dict.update({_: "Z" for _ in accent_dict["upperZ"]})
    master_dict.update({_: "z" for _ in accent_dict["lowerZ"]})

    # open the csv
    in_text = open(input_csv, "r")

    # open the output csv
    out_csv_path = input_csv.replace(".csv", "_cleaned.csv")
    out_csv_obj = open(out_csv_path, "w")

    # For each key in the dictionary, loop through and do a find and replace
    # for each accent letter with the corresponding key value. Then write that
    # new line out to a new CSV file
    for key in master_dict:
        # do the find and replace
        in_text = ''.join([i for i in in_text]).replace(key, master_dict[key])

        # write each line to the output csv
        out_csv_obj.writelines(in_text)

        # close the output csv
        out_csv_obj.close()

    return out_csv_path


def main():
    # replace the accent marks
    out_csv = replace_accents(
        input_csv=in_csv_path,
        accent_dict=accent_char_dict,
    )

    # ensure the output file was created successfully
    try:
        # make sure the output file exists
        assert os.path.isfile(out_csv)
    except:
        Exception("Output file not created successfully :(")

    print("\nProcess Completed Successfully! Please find your output at:")
    print(f"{out_csv}\n")


if __name__ == "__main__":
    main()
