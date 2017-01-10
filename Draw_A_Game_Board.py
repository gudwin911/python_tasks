#Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
#http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

#(I thought we need a square)
def board_creator1():
    size = int(input("Enter the game board`s size You want: "))
    board = []

    for i in range(size):
        board.append([" ---"]*size)
        board.append(["|   "]*(size+1))
    board.append([" ---"] * size)

    for i in board:
        print("".join(i))

board_creator1()
