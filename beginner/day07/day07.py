# Hangman Project
# For & While loops, If/else, Lists, Strings, Range, Modules

# Step 1
# TODO-11 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

import hangman_art
import hangman_words

print(hangman_art.logo)
end_of_game = False
# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
already_guessed_letter = []

# Testing Code
# print(f"Pssst, the solution {chosen_word}.")

# TODO-12: - Create an empty list called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
# guess.

display = []

for _ in range(word_length):  # for letter in chosen_word:
    display += "_"
print(display)

# TODO-13:- Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
#  letters in the chosen_word and 'display' has no more blanks ("_"). Then you cna tell the user they have won.

# TODO-14: - Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
while not end_of_game:
    # TODO-21:- Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    # TODO-54: - If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess not in already_guessed_letter:
        already_guessed_letter += guess
        # TODO-22 - Loop through each position in the chosen_word:
        # If the letter as that position matches "guess" then reveal that letter in the display at that position.
        # E.g. If the user guessed "p" and the chosen_word was "apple", then the display should be ["_", "p", "p",
        # "_", "_"]
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        # TODO-24: - If guess is not a letter in the chosen_word. Then reduce 'lives' by 1.
        #  If lives goes down to 0 then the game should stop and it should print "You lose."
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            if lives == 0:
                end_of_game = True
                print("You Lose!")
                print(f"The word is: {chosen_word}")
        # TODO-31 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        # TODO-32 - Print 'display' and you should see the guessed letter in the correct position and every other letter
        #  replace with "_".
        # Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in next step 3.

        print(display)
        if "_" in display:
            pass
        else:
            end_of_game = True
            print("You Win.")
        # TODO-34: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has
        #  remaining.

        print(hangman_art.stages[lives])
    else:
        print(f"You've already guessed {guess}")
