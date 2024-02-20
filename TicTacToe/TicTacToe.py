import random
random.seed()

# CURRENT ISSUES
# fix scoring -- for some reason 4, 0, 5 scores -- same with 7, 0, 2 [23, 11, 31]-- its 9 + 0 = 15? somehow 0 is 6? seems like 7 is translating to 1 for some reason -- DONE
# why are some totals going into negatives???? check the subtracting counts, maybe stop subtracting and just reset each time? -- DONE
# fix overlapping -- DONE

# top level variables
boardState = "aaaa"
boardSlots = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
magicSquare = [8, 1, 6, 3, 5, 7, 4, 9, 2] 
# magicSquare = [9, 2, 7, 4, 6, 8, 5, 10, 3] bad square to 18
gameOver = False;

def generate_board():
    boardState = "\n" + boardSlots[0] + " | " + boardSlots[1] + " | " + boardSlots[2] + "\n--+---+--\n" + boardSlots[3] + " | " + boardSlots[4] + " | " + boardSlots[5] + "\n--+---+--\n" + boardSlots[6] + " | " + boardSlots[7] + " | " + boardSlots[8] + "\n"
    print(boardState)

def turn(playerTurn):
    # win conditions
    global gameOver
    global boardSlots
    if gameOver == True:
        playAgain = input("Play again? (Y or N): ")
        if (playAgain == "Y"):
            gameOver = False
            boardSlots = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            generate_board()
            turn(True)
        return
    blackout = True
    for x in boardSlots:
        if (x == " "):
            blackout = False
    if (blackout == True):
        print("Game tied -- blackout!")
        gameOver = True
        turn(True)
        return

    # Check if X has won

    for itOne, a in enumerate(boardSlots):
        if a == 'X': # first count
            for itTwo, b in enumerate(boardSlots):
                if itOne != itTwo and b == 'X': # second count
                    for itThree, c in enumerate(boardSlots):
                        if itOne != itTwo and itTwo != itThree and itOne != itThree and c == 'X': # third count
                            if (magicSquare[itOne] + magicSquare[itTwo] + magicSquare[itThree] == 15):
                                print("The winning position is:")
                                print(str(itOne) + ", " + str(itTwo) + ", " + str(itThree))
                                print ("Game over -- you won!!")
                                gameOver = True
                                turn(True)
                                return

    # Check if O has won
    
    for itrOne, a in enumerate(boardSlots):
        if a == 'O': 
            for itrTwo, b in enumerate(boardSlots):
                if itrOne != itrTwo and b == 'O':
                    for itrThree, c in enumerate(boardSlots):
                        if itrOne != itrTwo and itrTwo != itrThree and itrOne != itrThree and c == 'O':
                            if (magicSquare[itrOne] + magicSquare[itrTwo] + magicSquare[itrThree] == 15):
                                print("The winning position is:")
                                print(str(itrOne) + ", " + str(itrTwo) + ", " + str(itrThree))
                                print ("Game over -- you lost :(")
                                gameOver = True
                                turn(True)
                                return
                    
                    
    if (playerTurn):
        nextMove = input('Your next move (x, y): ')
        if ((len(nextMove) != 2) or (nextMove[0] > '3') or (nextMove[1] > '3') or (nextMove[0] < '1') or (nextMove[1] < '1')):
            print("Invalid position")
            turn(True)
            return
        selectedCoords = [0, 0]
        selectedCoords[1] = int(nextMove[0]) - 1;
        selectedCoords[0] = int(nextMove[1]) - 1;

        # if boardSlots[((selectedCoords[0] % 3) * 3) + selectedCoords[1]] != "X" and boardSlots[((selectedCoords[0] % 3) * 3) + selectedCoords[1]] != "O":
        if boardSlots[((selectedCoords[0] % 3) * 3) + selectedCoords[1]] == " ":
            boardSlots[((selectedCoords[0] % 3) * 3) + selectedCoords[1]] = "X"
            generate_board()
            turn(False)
        else:
            print("Invalid position")
            turn(True)

    if (not playerTurn):
        ran = random.randint(0, 8)
        if boardSlots[ran] != "X" and boardSlots[ran] != "O":
            boardSlots[ran] = "O"
            generate_board()
            turn(True)
        else:
            turn(False)
    
# init
print("Welcome to Tic-Tac-Toe. In order to make your move, input it into the console.\n You can do this by entering a set of numbers representing first the row, then the column. For example: rightmost column, middle row would be 32.")

generate_board()

turn(True)




    
