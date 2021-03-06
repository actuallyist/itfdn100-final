import sys
from random import randint
from sortedcontainers import SortedDict


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

	def __init__(self, difficulty):
		self.difficulty = difficulty
	
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
		inst_dict[3] = "This is instance 3.1"
		inst_dict[4] = "This is instance 3.2"
		inst_dict[5] = "This is instance 4.1"
		inst_dict[6] = "This is instance 4.2"
		inst_dict[7] = "This is instance 5.1"
		inst_dict[8] = "This is instance 5.2"
		inst_dict[9] = "This is instance 5.3"
		inst_dict[10] = "This is instance 5.4"
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


	@staticmethod
	def view_stats(battle_dict):
		for x,y in battle_dict.items():
			print("{}: {}".format(x, y))

class InstanceProg():

	game_counter = 1

	def __init__(self, instance_dict, stats):
		self.instance_dict = instance_dict
		self.stats = stats


def straight_instance(self, instance_dict, stats):
	print(self.instance_dict[InstanceProg.game_counter()])
	user_input = input("Please enter your selection: ")
	if user_input == "stats".strip().lower():
		print(self.stats)
		continue
	elif user_input == "straight".strip().lower():
		if InstanceProg.game_counter == 1:
			InstanceProg.game_counter = InstanceProg.game_counter + 1
		elif InstanceProg.game_counter == 3 or 4:
			InstanceProg.game_counter = InstanceProg.game_counter + 2
		

def branched_instance(self, instance_dict, stats, game_counter):
	print(self.instance_dict[InstanceProg.game_counter()])
	user_input = input("Please enter your selection: ")
	if user_input == "stats".strip().lower():
		print(self.stats)
		continue
	elif user_input == "left".strip().lower():
		if InstanceProg.game_counter == 2:
			InstanceProg.game_counter = InstanceProg.game_counter + 1
		elif InstanceProg.game_counter == 5:
			InstanceProg.game_counter = InstanceProg.game_counter + 2
		elif InstanceProg.game_counter == 6:
			InstanceProg.game_counter = InstanceProg.game_counter + 3
	elif user_input == "right".strip().lower():
		if InstanceProg.game_counter == 2:
			InstanceProg.game_counter = InstanceProg.game_counter + 2
		elif InstanceProg.game_counter == 5:
			InstanceProg.game_counter = InstanceProg.game_counter + 3
		elif InstanceProg.game_counter == 6:
			InstanceProg.game_counter = InstancePro.game_counter + 4

@staticmethod
def instance_prog():
	while InstanceProg.game_counter <= 6:
		if InstanceProg.game_counter == 1 or 3 or 4:
			content = InstanceProg.straight_instance(instance_dict, stats)
		elif InstanceProg.game_counter == 2:
			content = InstanceProg.branched_instance(instance_dict, stats)
	if InstanceProg.game_counter == 5 or 6:
		content = InstanceProg.branched_instance(instance_dict, stats)
		print("Congratulations! You finished the game!")
		break




# sets gender and pronouns for story based on user input
play_start = StartGame(username, gender, 0)
pronoun = play_start.set_pronoun(gender)
possessive = play_start.set_possessive(gender)

#show the start menu
play_start.start_menu()

counter = play_start.menu_choices()

if counter == 1:
	gameplay = Gameplay(difficulty)








	














play_start.menu_choices()

gameplay = Gameplay(difficulty, play_start)
char_dict = gameplay.battle_dict(difficulty)
print(char_dict)
print(gameplay.instance_dict())
