#Matthew Hui
#SoftDev
#K<05> -- <Python/Dictionary/Printing out a random value in a dictionary given a user input>
#2020-09-29

Note: Angle brackets (<>) denote a field. Replace them with the indicated info.
(e.g., Replace "<mm>" with "09" for September).

import random

KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDIE', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

team = input("Please enter a team you would like to target: ")

while team not in KREWES.keys():
    team = input("Please re-enter a valid team name: ")

print(random.choice(KREWES[team]))

