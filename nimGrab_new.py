#Vikranth Pydeti                                      03-03-2025
# Assigment # 3
#This is the classic game of NIM called NIMGRUB !! - The idea of the game is simple where player take turn removing a set of number of 
# items from  a pile, The player who taken the last item loses. This game can be played both 1 player (Against computer) 
# or 2 players (against human).

import random

def print_header():
    print ("\n NIMGRAB !!")
    print ("By: Vikranth Pydeti")
    print ("COMS 1270 - 1")
    print ("--------------------------------------------------------/n")

def print_rules():
    print("\nRules of NIMGRAB: ")
    print("1. The game starts with a pile of items (between 20 - 25 items).")
    print("2. Players take turn removing items (between 1 and 3 per turn).")
    print("3. The players who takes the last item loses the game. ")
    print("4. In a single player game, computer plays against the human.")
    print("5. The computer will make reasonable moves.")
    print("6. Players can not take more items than are available in the pile. \n ")

def player_input(max_choice, remaining):
        while True:
             try:
                  choice = int (input(f"How many items do you want to take out 1-{min(max_choice, remaining)}]"))


