#tictactoe

def init_game():
    game_state = []
    for i in range(3):
        row = ['-'] * 3
        game_state.append(row)
    return game_state

def move():
    row = input("Which Row?: ")
    column = input("Which Column?: ")
    return (int(row), int(column))

def show_board(board):
    print("\nGame Board:\n")
    print(f"{board[0][0]}  {board[0][1]}  {board[0][2]}")
    print(f"{board[1][0]}  {board[1][1]}  {board[1][2]}")
    print(f"{board[2][0]}  {board[2][1]}  {board[2][2]}\n")

def check_game(board):
    for i in range(len(board)):
        for j in range(len(board)-2):
            if board[i][j] == board[i][j+1] == board[i][j+2] and board[i][j] != '-':
                return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '-':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    elif board[2][0] == board[1][1] == board[0][2] and board [2][0] != '-':
        return True

def board_full(board):
    full = True
    for i in board:
        for j in i:
            if j == '-':
                full = False
    return full
        
def tic_tac_toe():
    turn = 1
    game_state = init_game()
    while game_state:
        user_move = move()
        if user_move[0] < 1 or user_move[0] > 3 or user_move[1] < 1 or user_move[1] > 3:
            print("\nINVALID POSITION, TRY AGAIN\n")
            continue
        elif game_state[user_move[0]-1][user_move[1]-1] == "X" or game_state[user_move[0]-1][user_move[1]-1] == "O":
            print("\nCANNOT OVERWRITE EXISTING TILE, TRY AGAIN\n")
            continue
        if turn % 2 != 0:
            game_state[user_move[0]-1][user_move[1]-1] = "X"
        else:
            game_state[user_move[0]-1][user_move[1]-1] = "O"
        turn += 1
        show_board(game_state)
        if check_game(game_state):
            if turn % 2 != 0:
                print("\nO WIN")
                break
            else:
                print("\nX WIN")
                break
        if board_full(game_state):
            print("\nDRAW")
            break

    
tic_tac_toe()

        








