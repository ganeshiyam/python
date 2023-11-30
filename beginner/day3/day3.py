# Conditional Statements, Logical Operators, Code Blocks & Scope

# If / Else
water_level = 50
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")

# Exercise RollerCoaster

print("Welcome to the roller-coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller-coaster!\n")
else:
    print("Sorry, you have to grow taller before you can ride.\n")

# Comparison Operators:
# Greater than (>),
# Smaller than (<),
# Greater than or equal to (>=),
# Smaller than or equal to (<=)
# Equal to (==)
# Not Equal to (=!)

# Exercise Find the given number is odd or even
print("Check your is odd or even!\n")
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.\n")
else:
    print("This is an odd number.\n")

# Nested if/else statement
# If you are < 12 - $5, >= 18 - $7, > 18 - $12

print("Welcome to the roller-coaster!\n")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller-coaster!\n")
    age = int(input("What is your age? "))
    if age < 12:
        print("Your ticket price is $5.\n")
    elif age <= 18:
        print("Your ticket price is $7.\n")
    else:
        print("Your ticket price is $12.\n")
else:
    print("Sorry, you have to grow taller before you can ride.\n")

# Exercise - BMI Calculator and decide if you are obese or not
print("Welcome to BMI Calculator\n")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi_calculator = weight / height ** 2
bmi = round(bmi_calculator)
print(f"Your BMI is {bmi}\n")
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.\n")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.\n")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.\n")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.\n")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.\n")

# Exercise - Leap year
# On every year that is evenly divisible by 4,
#   except every year that is evenly divisible by 100,
#       unless the year is also evenly divisible by 400

print("Find the given year is a Leap Year or not!\n")
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 != 0:
        print("Leap year.")
    elif year % 400 == 0:
        print("Leap year.")
else:
    print("Not leap year.")

# Multiple if statement in succession Using RollerCoaster problem

print("Welcome to the roller-coaster!\n")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller-coaster!\n")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.\n")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.\n")
    else:
        bill = 12
        print("Adult tickets are $12.\n")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.\n")

# Exercise - Pizza Order

print("Pizza Order")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0

if size == "S" or size == "s":
    price = 15
elif size == "M" or size == "m":
    price = 20
elif size == "L" or size == "l":
    price = 25

if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "S" or size == "s":
        price += 2
    else:
        price += 3

if extra_cheese == "Y" or extra_cheese == "y":
    price += 1

print(f"Your final bill is: ${price}\n")

# Logical Operators

print("Logical Operators\n")

a = 12
if 10 < a < 13:
    print(a)

# Roller-coaster Midlife Crisis (Age 45-55 Free tickets)

print("Welcome to the roller-coaster!\n")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the roller-coaster!\n")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.\n")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.\n")
    elif age >= 45 and age <= 55:
        print("Tickets on us")
    else:
        bill = 12
        print("Adult tickets are $12.\n")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or wants_photo == "y":
        if age >= 45 and age <= 55:
            print("Have a happy ride!")
        else:
            bill += 3
            print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.\n")

# Exercise - Love Calculator

'''To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number. '''

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
full_name = name1.lower() + name2.lower()
t = full_name.count("t")
r = full_name.count("r")
u = full_name.count("u")
e = full_name.count("e")
true = t + r + u + e

l1 = full_name.count("l")
o = full_name.count("o")
v = full_name.count("v")
e = full_name.count("e")
love = l1 + o + v + e

true_love = str(true) + str(love)
love_score = int(true_love)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.\n")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.\n")
else:
    print(f"Your score is {love_score}.\n")

# Project - Treasure Island

print("Treasure Island\n")
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
cross_road = input('You\'re at a cross road. Where do you want to go? Type "left" or "right".\n')

if cross_road.lower() == "left":
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a '
                 'boat. Type "swim" to swim across.\n')
    if lake.lower() == "wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one "
                      "blue. Which colour do you choose? \n")
        if color.lower() == "yellow":
            print("You found the treasure! You Win!")
        elif color.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif color.lower() == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
