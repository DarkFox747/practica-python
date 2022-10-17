import random
from tabnanny import check


board =["-","-","-",
        "-","-","-",
        "-","-","-",]
currentPlayer = "X"
winner = None
gameRunning = True

#Print the game boar
def printGame(board):
    print(board[0]+ " | " + board[1]+ " | " + board[2])
    print(board[3]+ " | " + board[4]+ " | " + board[5])
    print(board[6]+ " | " + board[7]+ " | " + board[8])


#player imput 
def playerImput(board):
    inp = int(input("Elegi un numero del 1 al 9: "))
    if inp >= 1  and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("SPOT TAKEN!!!")

# check win 
def checkHorizontal(board):
    global winner 
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printGame(board)
        print("ES UN EMPATE MANCOS")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkHorizontal(board) or checkVertical(board) or checkDiag(board):
        gameRunning = False
        print("The winner of the game if {}".format(winner))
        printGame(board)

#Fix switch palyers
def countPlayrMoves(player):
    moves = board.count(player)
    return moves
#switch players 
def switchPlayers():
    global currentPlayer
    if currentPlayer == "X" and countPlayrMoves(currentPlayer) > countPlayrMoves("O"):
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#computer:
def computer(board):
    while currentPlayer == "O":
        pissition = random.randint(0,8)
        if board[pissition] == "-":
            board[pissition] = "O"
            switchPlayers()

while gameRunning:
    printGame(board)
    playerImput(board)
    checkWin()
    checkTie(board)
    switchPlayers()
    computer(board)
    checkWin()
    checkTie(board)
