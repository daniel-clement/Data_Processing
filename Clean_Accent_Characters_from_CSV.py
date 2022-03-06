# This script was written by Daniel Clement - 2022
# Python 3
"""
This script will take an input CSV file, search for any of characters with accents, as listed below,
and perform a find and replace for each of them to normal/non-accent characters.
"""

# set parameters
#######################################################################################################################
# input CSV
inCsv = r"C:\data\example.csv"

# output CSV
outCsv = r"C:\data\example_cleaned.csv"
#######################################################################################################################

# make lists of accent characters
upperA = ["À", "Á", "Â", "Ã", "Ä"]
lowerA = ["à", "á", "â", "ã", "ä"]
upperC = ["Ç"]
lowerC = ["ç"]
upperE = ["È", "É", "Ê", "Ë"]
lowerE = ["è", "é", "ê", "ë"]
upperI = ["Ì", "Í", "Î", "Ï"]
lowerI = ["ì", "í", "î", "ï"]
upperN = ["Ñ"]
lowerN = ["ñ"]
upperO = ["Ò", "Ó", "Ô", "Õ", "Ö"]
lowerO = ["ò", "ó", "ô", "õ", "ö"]
upperS = ["Š"]
lowerS = ["š"]
upperU = ["Ú", "Û", "Ü", "Ù"]
lowerU = ["ù", "ú", "û", "ü"]
upperY = ["Ý", "Ÿ"]
lowerY = ["ý", "ÿ"]
upperZ = ["Ž"]
lowerZ = ["ž"]

# create a empty dictionary
masterDict = {}

# build the dictionary using a reverse lookup
masterDict.update({_: "A" for _ in upperA})
masterDict.update({_: "a" for _ in lowerA})
masterDict.update({_: "C" for _ in upperC})
masterDict.update({_: "c" for _ in lowerC})
masterDict.update({_: "E" for _ in upperE})
masterDict.update({_: "e" for _ in lowerE})
masterDict.update({_: "I" for _ in upperI})
masterDict.update({_: "I" for _ in lowerI})
masterDict.update({_: "N" for _ in upperN})
masterDict.update({_: "n" for _ in lowerN})
masterDict.update({_: "O" for _ in upperO})
masterDict.update({_: "o" for _ in lowerO})
masterDict.update({_: "S" for _ in upperS})
masterDict.update({_: "s" for _ in lowerS})
masterDict.update({_: "U" for _ in upperU})
masterDict.update({_: "u" for _ in lowerU})
masterDict.update({_: "Y" for _ in upperY})
masterDict.update({_: "y" for _ in lowerY})
masterDict.update({_: "Z" for _ in upperZ})
masterDict.update({_: "z" for _ in lowerZ})

# for each key in the dictionary, loop through and do a find and replace for each accent letter with the corresponding
# key value. Then write that new line out to a new CSV file
for key in masterDict:
    # open the csv
    text = open(inCsv, "r")

    # do the find and replace
    text = ''.join([i for i in text]).replace(key, masterDict[key])

    # open the output csv
    x = open(outCsv, "w")

    # write each line to the output csv
    x.writelines(text)

    # close the output csv
    x.close()
