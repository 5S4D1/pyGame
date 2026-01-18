from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    ok = False
    while not ok:
        move = input("Enter your move (1-9): ")
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        move = int(move)-1
        row = move // 3
        col = move % 3
        sign = board[row][col]
        ok = sign != 'O' and sign != 'X'
        if not ok:
            print("This square is already occupied. Choose another one.")
            continue
    board[row][col] = 'O'


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'O' and board[row][col] != 'X':
                free.append((row, col))
    return free


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if sign == 'X':
        who = 'me'
    elif sign == 'O':
        who = 'you'
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
            return who
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
            return who
        if board[rc][rc] != sign:
            cross1 = False
        if board[2-rc][2-rc] != sign:
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'


board = [[3*j+i+1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'
free = make_list_of_free_fields(board)
human_turn = True

while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("You won!")
elif victor == 'me':
    print("I won!")
else:
    print("It's a tie!")

