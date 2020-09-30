#!/usr/bin/env python
# Carlos "Karl" Hernandez
# SoftDev
# K06 -- Aim: Made 05 useless because we decided to do proper python
# 2020-09-30
# Made by Matthew Hui, Yi Ling Wu, and Carlos "Karl" Hernandez
from random import choice


KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDIE', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}


def get_random_name():
    # printed out names of teams to make user experience better
    print("Team name: orpheus, rex, and endymion!\n")
    team = input("Enter a team:\n").lower() # .lower to make code always work
    while team not in KREWES: # in case they did not submit correct team
        team = input("Please enter a correct team:\n").lower()
    random_name = KREWES[team] # stored variable to make file easy to read
    print(choice(random_name))


if __name__ == "__main__":
    get_random_name()
