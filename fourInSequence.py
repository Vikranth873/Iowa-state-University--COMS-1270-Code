# Vikranth Pydeti                                 04-03-2025
# Assignment 4 
# The code helps creat a game called connect four, which can be played as a 1-player mode (Vs AI) or
#  2 - player mode (Vs human). Where players are given alternating chances to drop pieces 
# to form a sequence of four. 

# CITATION: ACCESSED: 3-15-2023
# CITATION: URL: https://chat.openai.com

import random 
import sys

def printTitleMaterial():
    print ("Four In Sequence!")
    print()
    
    print ("By: Vikranth Pydeti")
    print("[COMS 1270 - B]")
    print()

def initialChoice():
    """Allows the user to choose whether to [p]lay, get [i]nstructions, or [q]uit.

    :return string: choice - A string containing either 'p', 'i', or 'q'.
    """

    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

def chooseNumPlayers():
    """Allows the user to choose whether to play a game with [1] or [2] players.

    :return int: numPlayers - An integer, limited to strictly 1 or 2, to indicate the number of players in the game.
    """
    numPlayers = int(input("Number of Players? [1] / [2]: "))
    while numPlayers != 1 and numPlayers != 2:
        print("ERROR: Please enter either 1 or 2...")
        numPlayers = int(input("Number of Players? [1] / [2]: "))
    return numPlayers

def printBanner():
    """Prints out a nice header to delineate the game from the previous text output.
    """
    print("#######################################################################")
    print()
    print("~~ Starting New Round ~~")
    print()

def getPlayerPiece(playerNumber):
    """Returns a string corresponding to the 'player' under consideration. Player 0 corresponds to an 'empty' square. 
    Player 1 corresponds to the 'X' pieces. Player 2 corresponds to the 'O' pieces.

    :param int playerNumber: The 'player' whose piece we wish to know.
    :return string: piece - A string containing either '.', 'X', or 'O' for player 0 (empty), 1, or 2, respectively.
    """
    piece = ""
    if playerNumber == 0:
        piece = "."
    elif playerNumber == 1:
        piece = "X"
    elif playerNumber == 2:
        piece = "O"
    return piece

def createBoard(width, height):
    """Creates the underlying data structure for the game - a list of lists. This function also sets all the 'spaces' 
    in the 'gameboard' to be 'empty' (player 0) spaces.

    An example 6x7 gameboard (7 width, 6 height) would be created/ indexed into as follows:
    # 0.......
    # 1.......
    # 2.......
    # 3.......
    # 4.......
    # 5.......
    #  0123456

    Each 'sub-list' in the outer list represents a 'row' of the board. Each entry in a 'row' represents the 'column' space
    at that position for that row.

    :param int width: How many 'spaces' wide to make the gameboard.
    :param int height: How many 'spaces' high to make the gameboard.
    :return list of lists: board - The data structure that contains the contents of the gameboard. Only contains 'Player 0' pieces by default.
    """
    empty = getPlayerPiece(0)
    board = []
    for i in range(0, height):
        board.append([])
        for j in range(0, width):
            board[i].append(empty)
    return board

def printBoard(board):
    """Prints out the gameboard to the screen - including a row of digits at the bottom which correspond to columns the players can choose.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    """
    for row in board:
        for column in row:
            print(column, end="")
        print()
    for i in range(0, len(board[0])):
        print(i, end="")
    print()
    print()

def getColumnInt(board, playerNumber):
    """Take in user input as a string, and convert it to an integer. This function constructs a prompt based on the
    playerNumber, and the number of columns on the gameboard.

    NOTE: This function does not apply any filtering or input validation of any kind - it just gets the number from the user.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int playerNumber: The player number to display on the text output.
    :return int: The number that the user entered.
    """
    return int(input("Player {0}, please select a column between (0-{1}): ".format(playerNumber, len(board[0]) - 1)))

def getInputInRange(board, playerNumber):
    """Prompt the user to enter an integer between 0 and the number of columns on the board minus one. 
    This function will enforce this range, and will not allow values outside of it.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int playerNumber: The player number to display on the text output.
    :return int: col - The column the player wants to drop a piece inside.
    """
    col = getColumnInt(board, playerNumber)
    while col < 0 or col > len(board[0]) - 1:
        print("ERROR: Value must be between (0-{0}). You entered: {1}".format(len(board[0]) - 1, col))
        col = getColumnInt(board, playerNumber)
    return col

def getHumanInput(board, playerNumber):
    """This function collects input from a player corresponding to the column they want to drop a piece into.
    It enforces a range of columns between 0 and the number of columns on the board minus one by way of the getInputInRange() function.
    It also ensures that a column has at least one empty space to drop a piece in with the getOpenRow() function.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int playerNumber: The player number to display on the text output. It will be passed into the getInputInRange() function.
    :return int: col - The column the player wants to drop a piece inside.
    """
    col = getInputInRange(board, playerNumber)
    while getOpenRow(board, col) == -1:
        print("ERROR: Column {0} is full! Please choose a different column...".format(col))
        col = getInputInRange(board, playerNumber)
    return col

def checkForNextMoveWin(board, playerNumber):
    """This function iterates through all the columns on the board and checks if each column has an open row.
    If the column has an open row, the function checks to see if placing a piece in this column (and thus in
    the open row) will result in a 'win condition' being present. 

    If there is a 'win condition' present, this function will immediately terminate its execution, and return
    the column where placing a piece resulted in the win.

    Please note: This function does not make permanent changes to the gameboard. It will always revert whatever
    'test piece' it places in the board back to an 'empty' piece.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int playerNumber: The player number whose piece this function is to test for a 'win condition.'
    :return int: col - The column where the 'win condition' was found. It returns -1 if there is no 'win condition.'
    """
    empty = getPlayerPiece(0)
    piece = getPlayerPiece(playerNumber)
    for col in range(0, len(board[0])):
        row = getOpenRow(board, col)
        if row != -1:
            placePiece(board, row, col, piece)
            if checkWinner(board, playerNumber):
                placePiece(board, row, col, empty)
                return col
            placePiece(board, row, col, empty)
    return -1

def checkAdjacent(board, playerNumber):
    """This function aids the computer in choosing which column to drop a piece into. It iterates through all available columns, finds
    an available row, and considers all the surrounding pieces relative to that space on the gameboard. If it finds an adjacent piece
    belonging to the player, the current column is added to a list called 'adjacents' as a candidate to have a piece dropped into.
    If multiple pieces surround the space on the gameboard, the column will be added multiple times to the 'adjacents' list. Finally,
    after all of the columns have been analyzed, a random entry in the 'adjacents' list is chosen as the column for the computer to 
    drop a piece into. 

    This function has the benefit of being quite simple, but will create 'runs' of pieces which 'connect' to one another. This is 
    behavior that would be expected in this type of game. It will make the game appear that it is being played by something more
    advanced than a simple random number generator. 
    
    Furthermore, the more pieces which are adjacent to the candidate board space, the greater the probability that this space will 
    be selected. However - all the entries in the 'adjacents' list have an equal chance of being picked, so it is not a 'given' 
    that a certain column will be chosen.

    NOTE: This portion of the AI algorithm is (mostly) the original thought/ creation of Matthew Holman - *NOT* ChatGPT. However, the initial
          column/ row looping scheme was taken from ChatGPT generated code.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int playerNumber: The player number whose piece this function is to test for adjacent pieces.
    :return int: col - The value that is randomly chosen from the 'adjacents' list. It returns -1 if the 'adjacents' list has < 2 entries.
    """
    col = -1
    piece = getPlayerPiece(playerNumber)
    adjacents = []
    for column in range(0, len(board[0])):
        row = getOpenRow(board, column)
        if row != -1:
            if row - 1 >= 0 and column - 1 >= 0:                 #upper left piece (up one row, left one column)
                if board[row-1][column-1] == piece:
                    adjacents.append(column)

            if column - 1 >= 0:                                  # left piece (left one column)
                if board [row][column - 1] == piece:
                    adjacents.append(column)

            if row + 1 < len(board) and column - 1 >= 0:          # lower left piece (dowm one row, left one column)
                if board[row + 1][column - 1] == piece:
                    adjacents.append(column)

            if row + 1 < len(board):                            #lower piece (down one row)
                if board[row + 1][column] == piece:
                    adjacents.append(column)

            if row + 1 < len(board) and column + 1 < len(board[0]):          # lower right piece (down one row, right one column)
                if board [row + 1][column + 1] == piece:
                    adjacents.append(column)

            if column + 1 < len(board[0]):               # right piece (right one column)
                if board [row][column + 1] == piece:
                    adjacents.append(column)

            if row - 1 >= 0 and column + 1 < len(board[0]):                  # upper right piece (up one row, right one column)
                if board [row - 1][column + 1] == piece:
                    adjacents.append(column)

    if len(adjacents) > 1:
        randVal = random.randrange(0, len(adjacents))
        col = adjacents[randVal]
    return col

def getComputerInput(board, currentPlayerTurn):
    """This is the 'AI'/ brain/ decision making structure the computer uses in the single player game. The final decision comes after
    several different 'phases' in the computer choosing what to do. These phases are governed by the content of the 'col' variable. If
    'col == -1', then, clearly, one of the phases has failed, and the next phase should procede. 'col' will remain -1 until one of the
    phases succeeds. These phases are as follows:

    Firstly: If there is a winning move, the computer must take it no matter what.
    Secondly: If there is no winning move, but the opponent has a winning move, the computer must block it no matter what.
    Thirdly: If the first two steps fail, check all the columns for adjacent pieces and pick one where pieces would connect to one another.
    Finally: If the third step fails, meaning that there are not any moves that would result in at least two pieces connecting, then
             just pick a random column and end the turn.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int currentPlayerTurn: The player number for whom its turn it is.
    :return int: col - The column where the computer will place its piece.
    """
    opponentPlayerTurn = switchTurns(currentPlayerTurn)
    col = checkForNextMoveWin(board, currentPlayerTurn)
    if col == -1:
        col = checkForNextMoveWin(board, opponentPlayerTurn)
    if col == -1:
        col = checkAdjacent(board, currentPlayerTurn)
    if col == -1:
        col = random.randrange(0, len(board[0]))
        while getOpenRow(board, col) == -1:
            col = random.randrange(0, len(board[0]))
    print("Player {0}, please select a column between (0-{1}): {2}".format(currentPlayerTurn, len(board[0]) - 1, col))
    return col

def getOpenRow(board, col):
    """Iterates through all the rows of a given column (col), from bottom to top in the gameboard, and returns the first open row it finds.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int col: The column to check.
    :return int: row - The row index of the first empty row from the bottom of the gameboard. It returns -1 if no empty row is found.
    """
    empty = getPlayerPiece(0)
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == empty:
            return row
    return -1

def placePiece(board, row, col, piece):
    """Inserts a piece into the gameboard a a specific position.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int row: The row on the gameboard to insert the piece into.
    :param int col: The column on the gameboard to insert the piece into.
    :param string piece: The actual piece (should be "X", "O", or ".") to place into the gameboard
    """
    board[row][col] = piece

def dropPieceIntoBoard(board, col, playerNumber):
    """Inserts a piece into the gameboard in a given column. This is the function that should be called once either a 
    human or computer player determines which column to drop their piece into. It finds the lowest available row on the
    gameboard, given the specified column, and places the appropriate piece at that location.

    Before this function is called, it will have previously been determined whether the column (col) is valid or not. 
    Therefore, there is no need to worry about that here.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int col: The column on the gameboard to insert the piece into.
    :param int playerNumber: The player number whose piece this function is to 'drop' into the board.
    """
    row = getOpenRow(board, col)
    placePiece(board, row, col, getPlayerPiece(playerNumber))

def checkDraw(board):
    """This function checks to see if all the spaces on the board have been filled up. If they have been, then there has likely been
    a 'draw' as there are no possible additional moves available for any player.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :return boolean: Returns False immediately if it finds a single empty space on the board - meaning there cannot be a draw. It returns True otherwise.
    """
    empty = getPlayerPiece(0)
    for row in board:
        for column in row:
            if column == empty:
                return False
    return True

def checkWinner(board, playerNumber):
    """This function checks the gameboard to see if a winning condition is present. Meaning, if a given piece (determined by the
    playerNumber variable) occurs four (4) times in a row, column, positively sloped diagonal, or negatively sloped diagonal.

    These checks should occur one at a time, and should be done by considering a 'window' for each pattern of length 4. Meaning,
    if checking for a horizontal win, then it does not make sense to start a check beyond column index 3 (assuming the board is 7
    columns wide). The reason for this is because, if such a check started at index 5, for example, then the board would 'run out
    of spaces' before 4 pieces could even be inserted! 
    
    As there are 4 different 'winning condition' configurations there are, therefore, 4 different 'windows' to be considered. Each
    'window' will be different from all the other 'windows,' and should accommodate all possible 'winning condition' configurations
    of that type. For example, assuming a 6 row x 7 col gameboard, there should be a window that accommodates a positively sloped 
    diagonal from (3, 3) to (0, 6). This diagonal would include gameboard spaces (3, 3), (2, 4), (1, 5), and (0, 6). The 'check' for
    this configuration should likely start at (3, 3) - placing the 'window' in the bottom-left of the gameboard.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int playerNumber: The player number whose piece this function checks to see if there is a winning condition.
    :return boolean: Returns True if a winning condition is found. It returns False if a winning condition is not found.
    """

    piece = getPlayerPiece(playerNumber)

    for row in range(0, len(board)):                                      # check horizontal locations
        for column in range(0, len(board[0]) - 3):
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece:
                return True
                
    for row in range (len(board) - 3):                           # check vertical locations
        for column in range (len(board[0])):
            if board[row][column] == piece and board[row+1][column] == piece and board[row+2][column] == piece and board[row+3][column] == piece:
                return True
            
    for row in range (len(board) - 3):                       # check negatively sloped diagonals
        for column in range (len(board[0]) - 3):
            if board[row][column] == piece and board[row+1][column+1] == piece and board[row+2][column+2] == piece and board[row+3][column+3] == piece:
                return True

    for row in range(3, len(board)):                            # check positively sloped diagonals
        for column in range (len(board[0]) - 3):
            if board[row][column] == piece and board[row-1][column+1] == piece and board[row-2][column+2] == piece and board[row-3][column+3] == piece:
                return True
            
    return False

def resetGameOptions():
    """Calling this function will reset all the relevant gameplay variables to their pre-gameplay state so a new game can begin.

    :return int, boolean, boolean: These positional return values will set 'currentPlayerTurn' to 1 and the 'winner' and 'draw' variables to False.
    """
    currentPlayerTurn = 1
    winner = False
    draw = False
    return currentPlayerTurn, winner, draw

def switchTurns(currentPlayerTurn):
    """Change the current turn from Player 1 to Player 2 and vice versa.

    :param int currentPlayerTurn: _description_
    :return int: If currentPlayerTurn was 1, it changes to 2. If currentPlayerTurn was 2, it changes to 1.
    """
    return ((currentPlayerTurn % 2) + 1)

def main():
    """The main function for the game. The primary gameplay loop is located here.
    """
    running = True
    currentPlayerTurn = 1
    winner = False
    draw = False
    printTitleMaterial()

    while running:
        choice = initialChoice()
        if choice == "p":
            currentPlayerTurn, winner, draw = resetGameOptions()
            numPlayers = chooseNumPlayers()
            board = createBoard(7, 6)
            printBanner()
            printBoard(board)

            while True:
                if numPlayers == 1:
                    if currentPlayerTurn == 1:
                        col = getHumanInput(board, currentPlayerTurn)
                    elif currentPlayerTurn == 2:
                        col = getComputerInput(board, currentPlayerTurn)
                    else:
                        print("ERROR: currentPlayerTurn is neither 1 or 2! It is actually: {0}".format(currentPlayerTurn))
                        sys.exit()
                elif numPlayers == 2:
                    col = getHumanInput(board, currentPlayerTurn)
                else:
                    print("ERROR: numPlayers is neither 1 or 2! It is actually: {0}".format(numPlayers))
                    sys.exit()

                dropPieceIntoBoard(board, col, currentPlayerTurn)

                printBoard(board)

                winner = checkWinner(board, currentPlayerTurn)

                draw = checkDraw(board)
                
                if winner == True:
                    print("~~ Player {0} ({1}) Wins! ~~".format(currentPlayerTurn, getPlayerPiece(currentPlayerTurn)))
                    print()
                    break
                elif draw == True:
                    print("~~ Draw! ~~")
                    print()
                    break
                else: # if the game is not over, print that the turn is over
                    print("~~ End Of Player {0} ({1}) Turn ~~".format(currentPlayerTurn, getPlayerPiece(currentPlayerTurn)))
                    print()
                    currentPlayerTurn = switchTurns(currentPlayerTurn)
                    
        elif choice == "i":
            print("\n ******* RULES OF THE GAME, HOW TO PLAY ??? *******")
            print ("1. Players take turn to drop their pieces X or O into the board")
            print ("2. When a player connects 4 of their pieces in a row they WIN !! [Can be Horizontally, vertically or diagonally]")
            print ("3. In 1-player mode, you play against the computer.")
            print ("4. In 2-player mode, you play against another human by taking alternative turns.")
            print ("5. The game ends when a player wins or the board is full.")
            print ("6. To select a column, enter its number (0 - 6) when ask for the it.")
            print ("7. you can't place piece when the columns are full. \n")

        elif choice == "q":
            running = False
            print ("\nThank you for Playoing Four In Sequence!! GoodBye, Please play again! \n")
            
        else:
            print("ERROR: Variable 'choice' should have been 'p', 'i', or 'q', but instead was:", choice)
            quit()

if __name__ == "__main__":
    main()
