#!/usr/bin/env python
# coding:utf-8
from random import randint


ComputerLife = 5
PlayerLife = 5

# available weapon => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]


def winorlose(status):
# handle win or lose funciton instead of the procedural way
	print("called the win or lose function")
	print("**************************")
	print("You", status, "!", "Would you like to try again?")
	choice = input("Y / N:")

	if choice == "Y" or choice == "y":
		# reset the game
		# change global variables
		global PlayerLife
		global ComputerLife
		global player
		global Computer

		PlayerLife = 5
		ComputerLife = 5
		player = False
		computer = choices[randint(0, 2)]
	elif choice == "N" or choice == "n":
		print("You quit!")
		exit()
# show the computer's choice in the terminal window
# print("Computer chooses: ", computer)					   

while player is False:
	print("=======================================")
	print("You life:", PlayerLife,"/5", "Com. life:", ComputerLife,"/5")
	print("=======================================")
	print("choose your weapon!")
	player = input("Rock, Paper or Scissors")
	print("player choose", player)

	# check to see if you picked the same thing
	if (player == computer):
		print("Tie! Live to shoot another day")
		

	elif player == "Rock":
		if computer == "Paper":
			# computer won
			PlayerLife = PlayerLife - 1
			
			print("You lose~", computer, "covers", player)
			
		else:
			ComputerLife = ComputerLife - 1
			print("You win!", player, "smashes", computer)	

	elif player == "Paper":
		if computer == "Scissors":
			PlayerLife = PlayerLife - 1
			print("You lose！", computer, "cuts", player)
			
		else:
			ComputerLife = ComputerLife - 1
			print("You win！", player, "covers", computer)
		
			
	elif player == "Scissors":
		if computer == "Rock":
			PlayerLife = PlayerLife - 1
			print("You lose", computer, "smashes", player)
			
		else:
			ComputerLife = ComputerLife - 1
			print("You win！", player, "cuts", computer)		

	elif player == "Quit":
		exit()

	else:
		print("Not a valid option. Check again, and check your spelling\n")

	if PlayerLife == 0:
		winorlose("lose")

	elif ComputerLife == 0:
		winorlose("win")

	player = False
	computer = choices[randint(0, 2)]	