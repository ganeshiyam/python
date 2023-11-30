# Python Dictionaries & Nesting

# Dictionaries
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"
}

# Retrieving Items from Dictionary
print(programming_dictionary["Bug"])

# Adding new Items to Dictionary

programming_dictionary["String"] = "It is one of the variable type which can store any character"
print(programming_dictionary)

# Create an empty dictionary

empty_dictionary = {}

# Wipe an existing dictionary

programming_dictionary = {}
print(programming_dictionary)
print("\n")

programming_dictionary["Bug"] = "An error in a program that prevents the program from running as expected."
print(programming_dictionary)
programming_dictionary["Bug"] = "Insects which is small enough to crawl and eat."

print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Exercise - Grading Program
''' 
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the 
names of the students and the values are their exam scores.
Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary 
called student_grades that should contain student names for keys and their grades for values. The final version of 
the student_grades dictionary will be checked.
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"
'''
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 80:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] > 70:
        student_grades[student] = "Acceptable"
    elif student_scores[student] <= 70:
        student_grades[student] = "Fail"
print(student_grades)

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "India": "Delhi",
    "USA": "Washington",
    "China": "Shanghai"
}

# Nesting a list in a Dict
Country_states = {
    "India": ["Chennai", "Delhi", "Bangalore", "Kerala"],
    "USA": ["California", "Texas", "Nevada", "Alaska"],
    "France": ["Paris", "Lille", "Dijon"]
}

Country_cities_visited = {
    "India": {"cities_visited": ["Tamilnadu", "Delhi", "Bangalore", "Kerala"], "total_visits": 12},
    "USA": {"cities_visited": ["California", "Texas", "Nevada", "Alaska"], "total_visits": 23},
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 56}
}

# Nesting a dictionary inside a list
Country_cities_visited1 = [
    {
        "country": "India",
        "cities_visited": ["Tamilnadu", "Delhi", "Bangalore", "Kerala"],
        "total_visits": 12
    },
    {
        "country": "USA",
        "cities_visited": ["California", "Texas", "Nevada", "Alaska"],
        "total_visits": 23
    },
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 56
    }
]

# Exercise - DICTIONARY IN LIST

country = input()  # Add country name
visits = int(input())  # Number of visits
list_of_cities = input()  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.


def add_new_country(name, time_visits, cities_visited):
    temp_dict = {"country": name, "visits": time_visits, "cities": cities_visited}
    travel_log.append(temp_dict)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}")

# Blind Auction Program
'''
Welcome to the secret auction program. 
What is your name?: Angela
What's your bid?: $123
Are there any other bidders? Type 'yes' or 'no'.
yes
If there are other bidders, the screen should clear, so you can pass your phone to the next person. If there are no more bidders, then the program should display the name of the winner and their winning bid. 
The winner is Elon with a bid of $55000000000
'''
import os

from art import logo_auction

print(logo_auction)
bidders = {}
bidding_finished = False


def highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bidders[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bidders)
    elif should_continue == "yes":
        os.system('clear')
