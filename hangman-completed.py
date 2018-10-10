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

# display "Welcome to Hangman!"" on the console
def greet_the_player():
  print("Welcome to Hangman!")

# generate a random word from the 'words' array
def pick_random_word():
  word = random.choice(words)
  return word.strip().lower()

# ask the player for her guess and return that letter
def ask_user_for_next_letter():
  letter = input("Guess your letter: ")
  return letter.strip().lower()

# prints out the current letters correctly guess and any missing ones are blanks
def generate_word_string(word, letters_guessed):
  output = ""
  for letter in word:
    if letter in letters_guessed:
      output += letter
    else:
      output += "_"
    output += " "
  return output

########### this is where the program begins ############

# greet the player
greet_the_player()

# pick a word from the words array
WORD = pick_random_word()

letters_to_guess = set(WORD)
correct_letters_guessed = set()
incorrect_letters_guessed = set()

# player starts the game with 6 guesses and loses one for each incorrect guess
num_guesses = 6

while (len(letters_to_guess) > 0) and num_guesses > 0:
  guess = ask_user_for_next_letter()

  # check if we already guessed that letter
  if guess in correct_letters_guessed or guess in incorrect_letters_guessed:
    # print out a message
    print("You already guessed that letter. Try again!")
  elif guess in letters_to_guess: # if the guess was correct
    # update the letters_to_guess
    letters_to_guess.remove(guess)
    # update the correct letters guessed
    correct_letters_guessed.add(guess)
  else: # if the guess was incorrect
    incorrect_letters_guessed.add(guess)
    # only update the number of guesses if you guess incorrectly
    num_guesses -= 1
    print_body_part(num_guesses)

  word_string = generate_word_string(WORD, correct_letters_guessed)
  print(word_string)
  print()
  print("You have " + str(num_guesses) + " guesses left")

# tell the user they have won or lost
if num_guesses > 0:
  print("Congratulations! You correctly guessed the word " + WORD)
else:
  print("Sorry, you lost! Your word was " + WORD)
