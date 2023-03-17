board = [" "] * 9
players = ["X", "O"]
current_player = players[0]

def draw_board():
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))

def get_move():
    while True:
        move = input("Enter a number between 1 and 9: ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
        print("Invalid move, try again.")

def game_ended():
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != " ":
            return True
        if board[i] == board[i+3] == board[i+6] and board[i] != " ":
            return True
    if board[0] == board[4] == board[8] and board[0] != " ":
        return True
    if board[2] == board[4] == board[6] and board[2] != " ":
        return True
    return False

def play(current_player):
    while not game_ended():
        draw_board()
        move = get_move()
        board[move] = current_player
        current_player = players[(players.index(current_player) + 1) % len(players)]
    draw_board()
    print("Game over.")

play(current_player)
