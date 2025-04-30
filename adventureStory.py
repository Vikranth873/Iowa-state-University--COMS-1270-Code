# Vikranth Pydeti                                   02/22/2025
#Lab 5 - This code is an interactive adventure story with the user. 

def main():
    print("You are the year of 2078 and have a Virtual Reality set that is very realistic.") 
    print("You have special quest of being trapped in a village and must find a way to escape from the vilage.")

    choice = input("You are at the starting base. Do you want to go [left], [right], or [forward] ?")

    if choice == "left":
        print("You have found an ancient dragon's baby, crying in pain from sever injuries.")
        dragon_choice = input("Do you want to [tame] the dragon, [heal and leave], or [heal and tame]?")

        if dragon_choice == "tame":
            print("As you try to tame the dragon, the Ancient Dragon arrives and sees you as a threat.")
            print("You have been attacked by the ancient dragon's demonic blast and your existence is erased. GAME OVER!!")

        elif dragon_choice == "heal and leave" :
            print("You heal the baby dragon with the potions and leave. The ancient dragon arrives and sees your kindness.")
            print("It grants you special powers and decides you help you as a payback for helping its baby. You use this to leave the Village. YOU WIN!!")

        elif dragon_choice == "heal and tame":
            print("You use your healing potions to heal the baby dragon, and try to tame it.")
            print("As you try to tame the baby dragon, it suddenly attacks you in fear! You are severly injured and have no way to heal yourself. GAME OVER!!")

        else:
            print("Invalid choice. You hesitated to long , and the Ancient Dragon appeard. GAME OVER!!")


    elif choice == "right":
        print("You have enterd the village of Orcs and Goblins.")
        monster_choice = input("Do you [fight] with every monster stealthily, or [negotiate] with the wise goblin? ")

        if monster_choice == "fight":
            print("You have started a stealthy battle, and defeating all the monsters without getting caught.")
            print("You are exausted, but you have leveled up a lot and found a way to escape the village. YOU WIN!!")

        elif monster_choice == "negotiate":
            print("You speak with the wise goblin and agree to take care of the village.")
            print("In return, they give you their loyalty, two hidden treasures, and a way to leave the village. YOU WIN!!")

        else:
            print("Invalid choice. The orcs became suspicious of you and attacked you. GAME OVER!!")

    elif choice == "forward":
        print("You explord the village and found a unique house. Out of curiosity you enter the house.")
        village_choice = input("Inside the house you find a wise old man. Do you [talk] to him or [ignore] him ?")

        if village_choice == "talk":
            print("The old man understand you are the adventurer and hands you a map of the village, showing hidden treasures and the path to get out of the Village.")
            print("You follow the map recieve many hidden treasures and escaped the village succesfully. YOU WIN !!")
            
        elif village_choice == "ignore":
            print("You ignore the old man and wander aimlessly.")
            print("Without clues, you cannot leave and must return to the starting base. GAME OVER!!")

        else:
            print("Invalid choice. You hesitated too long, The old man left the place. GAME OVER!!")

    
    else: 
        print("Invalid choice, you are at the starting base. GAME OVER!!")


if __name__ == "__main__":
    main()