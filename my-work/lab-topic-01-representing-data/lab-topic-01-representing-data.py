# Program to read in the data and output each line as a list
# Cian Gallagher

import csv

FILENAME= "data.csv"

with open (FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        count +=1
print (f"average is {total/(count)}") 