# This is a client part
import socket
import sys

HOST = 'localhost'
PORT = 8080
# create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
try:
    client_socket.connect((HOST, PORT))
except:
    print("Unable to connect to server.")
    sys.exit()

# receive initial board state from server
start_msg = client_socket.recv(1024).decode()
if start_msg != "START":
    print("Unexpected message received from server.")
    sys.exit()

board = [" "] * 9


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
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != " ":
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != " ":
            return True
    if board[0] == board[4] == board[8] and board[0] != " ":
        return True
    if board[2] == board[4] == board[6] and board[2] != " ":
        return True
    if " " not in board:
        return True  # All squares are filled and no player has won
    return False


def play(s):
    while not game_ended():
        draw_board()
        move = get_move()
        board[move] = "X"
        # draw_board()
        if game_ended():
            print("Game over.You win!")
            s.send(str(move).encode('utf-8'))
            s.send("Game over.".encode('utf-8'))
            break
        else:
            s.send(str(move).encode('utf-8'))
        message = s.recv(1024).decode('utf-8')
        if message=="Game over.":
            print("Game over.You lose!")
            break
        # print(f"Message from server is: {message} ")
        moveO = int(message)
        board[moveO] = "O"
        if game_ended():
            print("Game over.")
            s.send("Game over.".encode('utf-8'))
            break
        # draw_board()
    draw_board()
    print("Game over.")
    s.close()


# while True:
# draw_board()
play(client_socket)
