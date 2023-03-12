# This is a server part
import random
import socket

HOST = '172.31.96.1'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
board = ['1','2','3','4','5','6','7','8','9']
def print_table():
    print("Current Board:")
    print("-------------")
    print(f"{board[0]} ║ {board[1]} ║ {board[2]}")
    print("══╬═══╬══")
    print(f"{board[3]} ║ {board[4]} ║ {board[5]}")
    print("══╬═══╬══")
    print(f"{board[6]} ║ {board[7]} ║ {board[8]}")
    print("-------------")

def s_num(lista):
    return random.choice(lista)
while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message} ")
    board = list(message.split(" "))
    n_list =[]
    for x in board:
        if x.isnumeric():
            n_list.append(int(x))
    x = s_num(n_list)
    board[x]="O"
    print_table()
    #communication_socket. send(F" Got your message! Thank you!".encode ('utf-8'))
    listToStr = ' '.join([str(elem) for elem in board])
    print(listToStr)
    communication_socket.send(listToStr.encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")