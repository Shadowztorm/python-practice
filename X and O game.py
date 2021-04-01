# ---------------GLOBAL VARIABLE--------------

# board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

check_game_running = True

# check who's the winner or a tie
winner = None

# who's turn is it
current_player = "X"


# display board
def display_board():
    # print(" _____________")
    print("  | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("  | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("  | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
    # print(" -------------")


# basic instruction for playing game
def instruction():
    print("\n\nWelcome to Tic Tac Toe Game!\n")
    print(" Board example\n")
    print(" | 1 | 2 | 3 | ")
    print(" | 4 | 5 | 6 | ")
    print(" | 7 | 8 | 9 | ")

    print("\nThe board will have 9 position from which player have to choose where to place their 'X' and 'O'\n")
    print("Player 1 will have 'X'\nPlayer 2 will have 'O' \n")

    print("Let's Start the game!\n")


# handle players
def handle_player(player):
    print(f"\t{player}'s Turn ")
    position = input("\nChoose a position between 1-9:")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input: choose from 1-9")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there")

    board[position] = player
    display_board()


def check_if_game_over():
    game_win()
    game_tie()


# Check who wins game
def game_win():
    global winner
    # check row
    row_winner = check_row()
    # check column
    column_winner = check_column()
    # check diagonal
    diagonal_winner = check_diagonal()

    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
    elif diagonal_winner:
        # there was a win
        winner = diagonal_winner
    return


# Check row winner
def check_row():
    global check_game_running
    global winner
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any row has a match flag it as win
    if row_1 or row_2 or row_3:
        check_game_running = False
    # return winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_column():
    global check_game_running
    global winner
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any row has a match flag it as win
    if column_1 or column_2 or column_3:
        check_game_running = False
    # return winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return


def check_diagonal():
    global check_game_running
    global winner
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # if any row has a match flag it as win
    if diagonal_1 or diagonal_2:
        check_game_running = False
    # return winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


# Check if game tie
def game_tie():
    global check_game_running

    if "-" not in board:
        check_game_running = False
    return


# Change player from X to O
def flip_player():
    global current_player
    # if current player was X, change it to O
    if current_player == "X":
        current_player = "O"
    # if current player was O, change it to X
    elif current_player == "O":
        current_player = "X"
    return


def play_game():
    global check_game_running
    global current_player
    instruction()
    display_board()
    while check_game_running:
        # handle single player each turn
        handle_player(current_player)
        # check if game has ended
        check_if_game_over()
        # change X to O
        flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print(f"\n\t'{winner}' Won")
    elif winner is None:
        print("\nTie")
    else:
        print("\nError")


# its like a main func
play_game()
