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
board[client_x-1]="X"
print_table()
print(board)