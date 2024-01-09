# Functions with inputs
import math

from learning.beginner import art


# def my_function():
# Do this
# Then do this
# Finally do this

# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("Hello")
    print("Welcome to Python Learning")
    print("Functions")


greet()


# Function that allows for input

def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"Welcome to Python Learning, {name}")


greet_with_name("Ganesh")


# name (parameter) = Ganesh (Argument)

# Functions with more than 1 inputs

def greet_with(name, location):
    print(f"Welcome {name}")
    print(f"How is your travel to {location}?")


greet_with("Twisha", "INDIA")
# Positional Argument (Twisha, INDIA)


# Keyword Argument a=1, b=2, c=3
# def my_fun(a, b, c):
# Do this with a
# Do this with b
# Do this with c

# my_fun(a=1, b=2, c=3)


greet_with(name="Priya", location="Pattukkottai")
greet_with(location="USA", name="Shastik")


# Exercise - Area Calculator Exercise

# Write your code below this line 👇
def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")


# Function to roundup a number
def roundup(number):
    return round(number + .5)


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Prime number checker

# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# You need to write a function that checks whether if the number passed into it is a prime number or not.
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            # Not a prime
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("it's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)

# Caesar Cipher coding

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo_Guessthenumber)
should_continue = True


def caesar(message, move, cipher_direction):
    message_text = ""
    if cipher_direction == "decode":
        move *= -1
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + move
            message_text += alphabet[new_position]
        else:
            message_text += char
    print(f"The {cipher_direction} text is {message_text}")


'''
def encrypt(message, move):
    message_enc = ""
    for letter in message:
        position = alphabet.index(letter)
        new_position = position + move
        message_enc += alphabet[new_position]
        ''''''
        if new_position > (len(alphabet) - 1):
            message_enc = message_enc + (alphabet[new_position - len(alphabet)])
        else:
            message_enc = message_enc + (alphabet[new_position])
        ''''''
    print(f"The encoded text is {message_enc}")


def decrypt(message, move):
    message_dec = ""
    for letter in message:
        position = alphabet.index(letter)
        new_position = position - move
        message_dec = message_dec + (alphabet[new_position])
    print(f"The decoded text is {message_dec}")
'''
'''if direction == "encode":
    encrypt(message=text, move=shift)
elif direction == "decode":
    decrypt(message=text, move=shift)
'''
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(message=text, move=shift, cipher_direction=direction)
    restart_cipher = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if restart_cipher == 'no':
        should_continue = False
        print("Goodbye")
