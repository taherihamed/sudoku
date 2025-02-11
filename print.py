from termcolor import colored

# ... (بقیه کد بازی)

def print_board(board):
    for row in board:
        for cell in row:
            if cell == 0:  # خونه خالی
                print(" ", end=" ")
            elif cell in initial_board:  # خونه اولیه
                print(colored(str(cell), "white"), end=" ")
            elif cell in wrong_cells:  # خونه اشتباه
                print(colored(str(cell), "red"), end=" ")
            else:  # خونه‌ای که کاربر وارد کرده
                print(colored(str(cell), "yellow"), end=" ")
        print()