"""
MadLibs
Author: Maya Kline
Period/Core: 2

This program will tell a story about someone goin on a a vaction. The details will be decided by the User and put into the story.
"""
print("Let's play Silly Sentences!")

name = input("Give a name: ")           # this will ask the user for a name
pronoun = input ("Give a pronoun(he/she): ") #this will ask for the pronoun of the named person
country = input("Give a country: ")     #this will ask for a country
adj1 = input("Give an adjective: ")     #this will ask for an adjective
food = input("Give a food(plural): ")   #this will ask for a food
activity = input ("Give an activy: ")   #this will ask for an activity
adv1 = input("Give an adverb: ")        #this will ask for an adverb
adj2 = input("Give another adjective: ")#this will ask for another adjective
day = input("Give a day of the week: ") #this will ask for a day of the week
place = input("Give a place: ")
noun1 = input("Give a noun: ")          #this will ask for a noun
noun2 = input("Give another noun: ")    #this will ask for a noun
noun3 = input("Give another noun: ")    #this will ask for a noun
vehicle = input("Give a vehicle: ")

print("\n{} took a trip to {}.".format(name,country))
print("In {}, {} ate some {} {}.".format(country,pronoun,adj1,food))
print("Then {} decided to {}.".format(name, activity))
print(f"After the {activity}," + f" {pronoun} was {adj2}.")
print(f"On {day}, it was time for {name} to go home to {place}.")
print(f"At the airport, {pronoun} bought a {noun1}, a {noun2}, and a {noun3}.\n Then {name} went home on a {vehicle}")
print("The" + "End.")