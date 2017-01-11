#Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
#http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

#(I thought we need a square)
size = int(input("Enter the game board`s size You want: "))

def board_printer():
    for i in range(size):
        print(" ---"*size)
        print("|   "*(size+1))
    print(" ---" * size)

#board_printer()

#with return lst
def board_creator():
    board = []
    for i in range(size):
        board.append(" ---"*size)
        board.append("|   "*(size+1))
    board.append(" ---" * size)
    return board

def board_print(board):
    for i in board_creator():
        print("".join(i))

#oard_print(board_creator())