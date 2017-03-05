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

# create function for difficulty
# difficulty determines player's health level range
# health random in all cases
def dict_builder(h_low, h_high, d_low, d_high, weapon, potions):
	battle_dict = {}
	battle_dict["Health"] = random_number(h_low, h_high)
	battle_dict["Weapon"] = weapon
	battle_dict["Damage"] = random_number(d_low, d_high)
	battle_dict["Potions"] = potions
	return battle_dict


def battle_dict(difficulty):
	if difficulty == "easy":
		char_dict = dict_builder(75, 100, 50, 70, "sword", 2)
	elif difficulty == "normal":
		char_dict = dict_builder(50, 100, 40, 60, "bow", 1)
	elif difficulty == "hard":
		char_dict = dict_builder(40, 100, 30, 50, "seasponge", 0)
	return char_dict

# create function to print stats
def view_stats(battle_dict):
	for x,y in battle_dict.items():
		print("{}: {}".format(x, y))

# likelyhood of encounter based on difficulty
def random_encounter(difficulty):
	counter = 0
	if difficulty == "easy":
		counter = random_number(1,4)
		if counter > 3:
			enc_indicator = 1
		else:
			enc_indicator = 0
	if difficulty == "normal":
		counter = random_number(1,3)
		if counter > 2:
			enc_indicator = 1
		else:
			enc_indicator = 0
	if difficulty == "hard":
		counter = random_number(1,2)
		if counter > 1:
			enc_indicator = 1
		else:
			enc_indicator = 0
	return enc_indicator

# trigger the random encounter
def trigger_encounter(indicator):
	if indicator == 1:
		print("You get a battle")
	else:
		pass


char_pronoun = set_gameplay_pronoun(gender)
char_possessive = set_gameplay_possessive(gender)
char_dict = battle_dict(difficulty)
print_stats = view_stats(char_dict)
test_indicator = random_encounter(difficulty)
test_trigger = trigger_encounter(test_indicator)

print("Your name is {} and you are {}".format(username, gender))
print(char_dict)
print_stats
print("Test indicagtor: {}".format(test_indicator))
test_trigger




# create function for room sequence (can use classes here maybe)?


# create function for battle sequence
# damage is random number between 1-10

# create function for find potion
# potion adds 10 health 