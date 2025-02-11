from termcolor import colored

# ... (بقیه کد بازی)

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0: 
            print("---------------------")
        for j in range(9):
            if j % 3 == 0 and j != 0: 
                print("| ", end="")

            cell = board[i][j]
            if cell == 0:
                print("  ", end=" ")
            elif (i, j) in initial_board:
                print(colored(str(cell), "white"), end=" ") 
            elif (i, j) in wrong_cells:
                print(colored(str(cell), "red"), end=" ")
            else:
                print(colored(str(cell), "yellow"), end=" ")

        print() 

    print("---------------------")  


initial_board = set([(0, 0), (0, 4), (0, 6), (1, 1), (1, 5), (1, 8), (2, 2), (2, 6), (3, 0), (3, 3), (3, 7), (4, 4), (4, 8), (5, 1), (5, 5), (5, 8), (6, 0), (6, 3), (6, 6), (7, 1), (7, 5), (7, 7), (8, 2), (8, 4), (8, 8)])
wrong_cells = set([(0, 1), (1, 2)]) 
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print_board(board)
