import sys
from random import randint
from sortedcontainers import SortedDict

# create menu: start new game of quit
def start_menu():
	print("Welcome to the game!")
	print("Press 1 to start a new game")
	print("Press 2 to quit")

# display menu
start_menu()

# create random number generator
def random_number(num1, num2):
	rand_val = randint(num1, num2)
	return rand_val
	

# create function for difficulty
# difficulty determines player's health level range
# health random in all cases

# create function for room sequence (can use classes here maybe)?

# create function for battle sequence
# damage is random number between 1-10

# create function for find potion
# potion adds 10 health 