# Randomisation & Python Lists

# Random Module
import random

print("Random Number")
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

print(random_float * random_integer)
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")

# Module

# Exercise - Toss a coin

coin_toss = random.randint(0, 1)
if coin_toss == 1:
    print("Heads")
else:
    print("Tails")

# Lists

fruits = ["Cherry", "Apple", "Pear"]
number = [1, 2, 3, 4]

states_of_america = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland',
                     'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island',
                     'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois',
                     'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin',
                     'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado',
                     'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma',
                     'New Mexico', 'Arizona', 'Alaska', 'Hawaii']

print(states_of_america[12])
states_of_america.append("Mexico")
print(states_of_america)
states_of_america.extend(["Cuba", "Caribbean"])
print(states_of_america)
states_of_america.sort()
print(states_of_america)

# Exercise Banker Roulette - Who will pay the bill?

print("Banker Roulette - Who will pay the bill?")

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")  # Angela, Ben, Jenny, Michael, Chloe
print(len(names))
rand_int = random.randint(0, len(names) - 1)

print(f"{names[rand_int]} is going to buy the meal today!")

print(random.choice(names))

# List index out of range error
print(states_of_america[len(states_of_america) - 1])

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
               "Tomatoes", "Celery", "Potatoes"]

fruits1 = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
veg = ["Tomatoes", "Celery", "Potatoes", "Spinach", "Kale"]

dirty_dozen1 = [fruits, fruits1, veg]
print(dirty_dozen1)

# Exercise 3 - Treasure Map
print("Exercise - Treasure Map\n")
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

# Rock Paper Scissor Game

# What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
# Rocks win against scissor. (0 wins against 2)
# Scissors wins against paper. (2 wins against 1)
# Paper wins against rock. (1 wins against 0)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissor]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if your_choice > 2:
    print("You entered a wrong number! You lose")
else:
    bot_random = random.randint(0, 2)
    print(f"{game[your_choice]}")
    print(f"Computer chose:\n {game[bot_random]}")

    if your_choice == bot_random:
        print("It's a draw")
    elif your_choice == 0 and bot_random == 2:
        print("You win")
    elif your_choice == 2 and bot_random == 0:
        print("You lose")
    elif your_choice > bot_random:
        print("You win")
    else:
        print("You lose")
