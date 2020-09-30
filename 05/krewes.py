#Matthew Hui
#SoftDev
#K<05> -- <Python/Dictionary/Printing out a random value in a dictionary given a user input>
#2020-09-29


#Imported the random module
import random

#KREWES Dictionary
KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDIE', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

#Got the team name from user input
team = input("Please enter a team you would like to target: ").lower()

#While loop to make sure that team is going to be a valid key name
while team not in KREWES.keys():
    team = input("Please re-enter a valid team name: ")

#Prints out a random choice from the team
print("Random name from " + team + ": " +random.choice(KREWES[team.lower]))

