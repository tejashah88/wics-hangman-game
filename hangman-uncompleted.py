import random
from useful_functions import *

words = [
  "hangman",
  "womenincs",
  "python",
  "computer",
  "engineering",
  "friends",
  "anime",
  "something"
]

# TODO: display "Welcome to Hangman!"" on the console
def greet_the_player():
  ____

# TODO: generate a random word from the 'words' array
def pick_random_word():
  ____

# TODO: ask the player for her guess and return that letter
def ask_user_for_next_letter():
  ____

# TODO: prints out the current letters correctly guess and any missing ones are blanks
def generate_word_string(word, letters_guessed):
  ____

########### this is where the program begins ############

# greet the player
greet_the_player()

# TODO: pick a word from the words array
WORD = ____

letters_to_guess = set(WORD)
correct_letters_guessed = set()
incorrect_letters_guessed = set()

# player starts the game with 6 guesses and loses one for each incorrect guess
num_guesses = 6

# TODO: check if user has enough guesses or user has guessed all correct letters
while ____:
  # TODO: prompt user for next letter
  guess = ____

  if ____:
    # TODO: if we already guessed that letter...
    ____
  elif ____:
    # TODO: if the guess was correct...
    ____
  else:
    # TODO: if the guess was incorrect...
    ____

  # TODO: generate the word string
  ____

  # TODO: tell the user how many guesses he/she has left
  ____

# tell the user they have won or lost
if ____:
  ____
else:
  ____
