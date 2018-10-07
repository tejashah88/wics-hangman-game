import random
from useful_functions import *

#display "Welcome to Hangman!"" on the console
def greet_the_player():
  print("Welcome to Hangman!")

def pick_random_word():
	# open the sowpods dictionary
	with open("words.txt", 'r') as inf:
		words = inf.readlines()
	# generate a random index
	# -1 because len(words) is not a valid index into the list `words`
	index = random.randint(0, len(words) - 1)
	# print out the word at that index
	word = words[index].strip()
	return word

#ask the player for her guess and return that letter
def ask_user_for_next_letter():
	letter = input("Guess your letter: ")
	return letter.strip().lower()

def generate_word_string(word, letters_guessed):
	output = []
	for letter in word:
		if letter in letters_guessed:
			output.append(letter.lower())
		else:
			output.append("_")
	return " ".join(output)

########### this is where the program begins ############

#greet the player
greet_the_player()

#pick a word from the words.txt file
WORD = pick_random_word()

letters_to_guess = set(WORD)
correct_letters_guessed = set()
incorrect_letters_guessed = set()

#player starts the game with 6 guesses and loses one for each incorrect guess
num_guesses = 6

while (len(letters_to_guess) > 0) and num_guesses > 0:
  guess = ask_user_for_next_letter()

  # check if we already guessed that
  # letter
  if guess in correct_letters_guessed or \
      guess in incorrect_letters_guessed:
    # print out a message
    print("You already guessed that letter.")

  # if the guess was correct
  if guess in letters_to_guess:
    # update the letters_to_guess
    letters_to_guess.remove(guess)
    # update the correct letters guessed
    correct_letters_guessed.add(guess)
  else:
    incorrect_letters_guessed.add(guess)
    # only update the number of guesses
    # if you guess incorrectly
    num_guesses -= 1

  print_body_part(num_guesses)
  word_string = generate_word_string(WORD, correct_letters_guessed)
  print(word_string)
  print()
  print("You have {} guesses left".format(num_guesses))

# tell the user they have won or lost
if num_guesses > 0:
  print("Congratulations! You correctly guessed the word {}!".format(WORD))
else:
  print("Sorry, you lost! Your word was {}".format(WORD))
