# Program - Higher or Lower
import random

import game_data
from art import logo_hvl
from art import vs

# Start the game by printing the logo and pick Random Personality A & B
print(logo_hvl)


# personality1 = random.choice(game_data.data)
# personality = {}
# Pick a random personality from the list
def pick_random_personality():
    return random.choice(game_data.data)


personality = pick_random_personality()

'''
def personality_info(person):
    # personality = dict(name=person, follower_count=count, description=desc, country=location)
    for info in person:
        # return personality[info]
        print(person["name"])
        print(person["description"])
        print(person["follower_count"])
        print(person["country"])
'''


def compare(person1_f_count, person2_f_count):
    if person1_f_count > person2_f_count:
        return


print(f"Compare A: {personality1['name']}, a {personality1['description']}, from {personality1['country']}.")
print(vs)
personality2 = random.choice(game_data.data)
print(f"Against B: {personality2['name']}, a {personality2['description']}, from {personality2['country']}.")
more_followers = input("Who has more followers? Type 'A' or 'B': ")
if more_followers == 'A':
    compare(person)


def compare(person1_f_count, person2_f_count):
    if person1_f_count > person2_f_count:
        return

# print(personality1["name"])
# print(personality1["description"])
# print(personality1["country"])
# print(f"Compare A: {personality['name']}, a {personality['description']}, from {personality['country']}.")
# Pick a different personality B to compare with A
# personality_info(personality1)
# Look for who has more followers

# Return the winner by incrementing the score

# Pick an another personality to compare with B as the orginal B moves to A

# keep iterating this until the Answer is wrong and emit the final score
