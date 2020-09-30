#!/usr/bin/env python
# Matthew Hui
# SoftDev
# K07 -- Aim: Worked with standard io in python
# 2020-09-30
# Team TLK: Matthew Hui, Yi Ling Wu, and Carlos "Karl" Hernandez

import csv
from random import choices


def get_random_occupations():
    # need to open file
    with open("./occupations.csv", "r", newline='') as csv_file:
        # we are lazy so we used the csv library
        reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_file) # we wanted to get rid of the header
        occupations = {} # initialize the dictionary
        for row in reader:
            occupations[row[0]] = float(row[1]) # populated the dictionary
        del occupations['Total'] # deleted the last row
        # next two lines are so we can use random.choices()
        key = list(occupations.keys())
        values = list(occupations.values())
        print(choices(key, weights=values, k=1)[0]) # print the occupation


if __name__ == "__main__":
    get_random_occupations()
