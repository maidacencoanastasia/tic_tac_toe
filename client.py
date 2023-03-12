# This is a client part
import socket

HOST = '172.31.96.1'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


# display the board
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

print("Welcome to tic-Tac-Toe")
print("You make you first move")
print_table()
client_x = int(input("Enter the number of cell:"))
poz=client_x-1
board[poz]="X"
print_table()
listToStr = ' '.join([str(elem) for elem in board])
print(listToStr)
s.send(listToStr.encode('utf-8'))
otvet = s.recv(1024).decode('utf-8')
print(otvet)
board = list(otvet.split(" "))
print_table()