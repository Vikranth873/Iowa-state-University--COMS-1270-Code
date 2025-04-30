#Vikranth Pydeti                                      03-03-2025
# Assigment # 3
#This is the classic game of NIM called NIMGRUB !! - The idea of the game is simple where player take turn removing 
# a set of number of  items from  a pile, The player who taken the last item loses. This game can be played 
# both 1 player (Against computer) or 2 players (against human).

import random

def print_header():
    print ("\n NIMGRAB !!")
    print ("By: Vikranth Pydeti")
    print ("COMS 1270 - 1")
    print ("--------------------------------------------------------\n")

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
                choice = int (input(f"How many items do you want to take out [1-{min(max_choice, remaining)}]? :"))
                if 1 <= choice <= min(max_choice, remaining):
                    return choice 
                else :
                    print ("Error!! wrong choice. Please choose again!")
                       
            except ValueError:
                 print ("Error !! Invalid input, Please enter a number!")


def computer_turn (remaining):
     if remaining == 1:
          return 1
     elif remaining == 2:
          return 1 
     elif remaining == 3:
          return 2 
     else:
          return random.randint(1, min(3, remaining))

def display_items (count):
     print("Items Left:", count)
     for i in range (count):
          print ("|", end= " ")
     print()

def play_game (players):
     items = random.randint (20, 25)
     print (f"This game starts with {items} items! \n")
     players_turn = 1 

     while items > 0:
          display_items (items)

          if players == 1 and players_turn == 2:
               choice = computer_turn(items)
               print (f"Computer takes: {choice} items out.")
          else:
               print (f"Player {players_turn}'s turn: ")
               choice = player_input (3, items)
               
          items -= choice

          if items == 0:
                    if players == 1 and players_turn == 2:
                         print("Computer took the last item.; Human wins!")
                    else:
                         print(f"Player {players_turn} took the last item. Player {3 - players_turn} wins!")
                    break
          players_turn = 2 if players_turn == 1 else 1 

def main():
    while True:
        print_header()
        choice = input("Do you want to [r] Read the rules, [p] Play the game, or [q] Quit? :")
        if choice == "r":
            print_rules()

        elif choice == "p":
            mode = input("Do you want to play single player i.e play against a [c] Computer or double player i.e against a [h] Human? :")
            if mode in ["h", "c"]:
                play_game(1 if mode == "c" else 2)

        elif choice == "q":
            print("Goodbye! Please play again.")
            break 

        else:
            print("ERROR! Choice not available, Please choose options from r, p, or q")

if __name__ == "__main__":
     main()
               







