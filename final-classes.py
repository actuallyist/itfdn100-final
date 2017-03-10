import sys
from random import randint
from sortedcontainers import SortedDict
import pandas

# accept user input from command line
username = sys.argv[1].strip().capitalize()
gender = sys.argv[2].strip().lower()
difficulty = sys.argv[3].strip().lower()



class StartGame():
	
	# display message when game starts
	def __init__(self, username, gender, menu_choice):
		self.username = username
		self.gender = gender
		self.menu_choice = 0
		print("Welcome to The Eternal Battle, {}!".format(username))

		# function to set pronouns in the story based on user input
	def set_pronoun(self, gender):
		if self.gender == "female" or "woman" or "girl":
			char_pronoun = "she"
		elif self.gender == "male" or "man" or "boy":
			char_pronoun = "he"
		else:
			char_pronoun = "they"
		return char_pronoun

	# function to set possessive in the story based on user input
	def set_possessive(self, gender):
		if self.gender == "female" or "woman" or "girl":
			char_possessive = "her"
		elif self.gender == "male" or "man" or "boy":
			char_possessive = "his"
		else:
			char_possessive = "their"
		return char_possessive

	# display start menu
	def start_menu(self):
		print("Press 1 to start a new game.")
		print("Press 2 to view the Hall of Champions.")
		print("Press 3 to quit.")
		
	def menu_choices(self):
		self.menu_choice = (int(input("Please enter your selection: ")))
		if self.menu_choice != 3:
			if self.menu_choice == 1:
				menu_choice = 1
				print("Starting instance 1")
			elif self.menu_choice == 2:
				menu_choice = 2
				print("Hall of Champions: Here they are!")
		elif self.menu_choice == 3:
			quit()
		return menu_choice
		


class Gameplay():

	def __init__(self, difficulty, menu_choice):
		self.difficulty = difficulty
		self.menu_choice = menu_choice
	
	# create random number generator
	@staticmethod
	def random_number(val1, val2):
		rand_val = randint(val1, val2)
		return rand_val

	# build the character attribute dictionary
	@staticmethod
	def dict_builder(h_low, h_high, d_low, d_high, weapon, potions):
		battle_dict = {}
		battle_dict["Health"] = Gameplay.random_number(h_low, h_high)
		battle_dict["Weapon"] = weapon
		battle_dict["Damage"] = Gameplay.random_number(d_low, d_high)
		battle_dict["Potions"] = potions
		return battle_dict

	# build the instance dictionary
	@staticmethod
	def instance_dict():
		inst_dict = {}
		inst_dict[1] = "This is instance 1"
		inst_dict[2] = "This is instance 2"
		inst_dict[31] = "This is instance 3.1"
		inst_dict[32] = "This is instance 3.2"
		inst_dict[41] = "This is instance 4.1"
		inst_dict[42] = "This is instance 4.2"
		inst_dict[51] = "This is instance 5.1"
		inst_dict[52] = "This is instance 5.2"
		inst_dict[53] = "This is instance 5.3"
		inst_dict[54] = "This is instance 5.4"
		return inst_dict

	# assign attributes based on difficulty
	def battle_dict(self, difficulty):
		if self.difficulty == "easy":
			char_dict = Gameplay.dict_builder(75, 100, 50, 70, "sword", 2)
		elif self.difficulty == "normal":
			char_dict = Gameplay.dict_builder(50, 100, 40, 60, "bow", 1)
		elif self.difficulty == "hard":
			char_dict = Gameplay.dict_builder(40, 100, 30, 50, "seasponge", 0)
		return char_dict

	# create function to print stats
	def view_stats(battle_dict):
		for x,y in battle_dict.items():
			print("{}: {}".format(x, y))













play_start = StartGame(username, gender, 0)

pronoun = play_start.set_pronoun(gender)
possessive = play_start.set_possessive(gender)

play_start.start_menu()
play_start.menu_choices()

gameplay = Gameplay(difficulty, play_start)
char_dict = gameplay.battle_dict(difficulty)
print(char_dict)
print(gameplay.instance_dict())
