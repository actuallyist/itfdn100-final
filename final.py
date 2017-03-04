import sys
from random import randint
from sortedcontainers import SortedDict

""" The player should input three options when running this script:
First, enter Name of their character
Second, enter their character's gender
Third, enter difficulty.  Accepted answers are Easy, Normal, and Hard
"""
# accept user input from command line
username = sys.argv[1].strip().capitalize()
gender = sys.argv[2].strip().lower()
difficulty = sys.argv[3].strip().lower()

# create menu: start new game of quit
def start_menu():
	print("Welcome to the game, {}!".format(username))
	print("Press 1 to start a new game")
	print("Press 2 to quit")

# display menu
start_menu()

menu_choice = 0

#try:
	#while menu_choice != 2:
		#menu_choice = int(input("Please enter your selection: "))
#except ValueError:
	#print("That is not a valid selection.  Please try again")

# create random number generator
def random_number(num1, num2):
	rand_val = randint(num1, num2)
	return rand_val

# function to set pronouns in the story based on user input
def set_gameplay_pronoun(gender):
	if gender == "female" or "woman" or "girl":
		char_pronoun = "she"
	elif gender == "male" or "man" or "boy":
		char_pronoun = "he"
	else:
		char_pronoun = "they"
	return char_pronoun

# function to set possessive in the story based on user input
def set_gameplay_possessive(gender):
	if gender == "female" or "woman" or "girl":
		char_possessive = "her"
	elif gender == "male" or "man" or "boy":
		char_possessive = "his"
	else:
		char_possessive = "their"
	return char_possessive


char_pronoun = set_gameplay_pronoun(gender)
char_possessive = set_gameplay_possessive(gender)

print("{} is playing the game".format(char_pronoun.capitalize()))
print("It is {} game".format(char_possessive))

# create function for difficulty
# difficulty determines player's health level range
# health random in all cases

# create function for room sequence (can use classes here maybe)?

# create function for battle sequence
# damage is random number between 1-10

# create function for find potion
# potion adds 10 health 