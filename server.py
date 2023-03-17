# This is a server part
import random
import socket

HOST = ''
PORT = 8080

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST, PORT))
#
# server.listen(5)
# create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket object to host and port
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen()
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
        if board[i] == board[i+1] == board[i+2] and board[i] != " ":
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != " ":
            return True
    if board[0] == board[4] == board[8] and board[0] != " ":
        return True
    if board[2] == board[4] == board[6] and board[2] != " ":
        return True
    if " " not in board:
        return True  # All squares are filled and no player has won
    return False


def s_num(lista):
    return random.choice(lista)


def play(s):
    while not game_ended():
        #draw_board()
        message = s.recv(1024).decode('utf-8')
        #print(f"Message from client is: {message} ")
        move = int(message)
        board[move] = "X"
        draw_board()
        move = get_move()
        board[move] = "O"
        s.send(str(move).encode('utf-8'))
    draw_board()
    print("Game over.")
    s.close()

conn1, addr1 = server_socket.accept()
print(f"Player connected from {addr1}")
conn1.send("START".encode())
play(conn1)
