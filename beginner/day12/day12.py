# Namespace: Local vs Global Scope
import random

################### Scope ####################

enemie = 1


def increase_enemies():
    enemie = 2
    print(f"enemies inside function: {enemie}")


increase_enemies()
print(f"enemies outside function: {enemie}")

# Local & Global scope
player_health = 10  # Global Scope (Variable)


def drink_potion():
    potion_strength = 2  # Local Scope (Variable)
    print(potion_strength)
    print(player_health)


drink_potion()
print(player_health)

# Block Scope? There is no block scope in python

if 3 > 2:
    a_variable = 10

game_level = 3


def create_enemy():
    enemy = ["skeleton", "zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemy[0]
    print(new_enemy)


create_enemy()

# Modifying the global scope, Don't modify the global scope inside a function. Its confusing and prone to create bugs

enemies = 1


def increase_enemies():
    # global enemies  # define the global variable , avoid modifying the global variable inside the function

    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Python Constants and Global Scope
# Global constants
PI = 3.14159  # Keep it in upper case, so you can make sure its a global variable which you should not change
URL = "https://ebay.com"
TWITTER_HANDLE = "@ganeshiyam"

# Project: The Number Guessing Game

from art import logo_gtn

print(logo_gtn)

EASY_LEVEL = 10
HARD_LEVEL = 5
TURNS = 0


def check_the_guess(guess, answer, turns):
    """ Check answer against the guess number and the number of guess remaining """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too Low.")
        return turns - 1
    elif guess == answer:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_guessed = random.randint(1, 100)
    # print(f"Pssst, the correct answer is {number_guessed}")

    turns = set_difficulty()

    player_guess = 0
    while player_guess != number_guessed:
        print(f"You have {turns} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        turns = check_the_guess(player_guess, number_guessed, turns)
        if turns == 0:
            print("You've run out of the guesses, you lose.")
            return
        elif player_guess != number_guessed:
            print("Guess again.")


game()
