def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
    (board[3] == player and board[4] == player and board[5] == player) or \
    (board[6] == player and board[7] == player and board[8] == player) or \
    (board[0] == player and board[3] == player and board[6] == player) or \
    (board[1] == player and board[4] == player and board[7] == player) or \
    (board[2] == player and board[5] == player and board[8] == player) or \
    (board[0] == player and board[4] == player and board[8] == player) or \
    (board[2] == player and board[4] == player and board[6] == player) :
        return True
    else:
        return False

def check_tie(board):
    if " " not in board:
        return True 
    else: 
        return False

def tic_tac_toe():
    board = [" " for _ in range(9)]
    player = "X"

    print_board(board)

    while True :
        move = input("It's " + player + "'s turn. Enter a position (1-9): ")
        move = int(move) -1 

        if board[move] == " ":
            board[move] = player
            print_board(board)

            if check_win(board, player):
                print("Congratulations! player " + player + " wins!")
                break
            elif check_tie(board):
                print("It's a tie")
                break
            else:
                player = "0" if player == "X" else "X"
        else:
            print("That postion is already taken. Try again")

tic_tac_toe()