#choose difficulty level task 
default_borads={
  "easy": [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ],
            "medium": [
                [0, 0, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 0, 5, 0, 0, 0],
                [0, 0, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [0, 0, 0, 0, 2, 0, 0, 0, 0],
                [0, 6, 0, 0, 0, 0, 0, 8, 0],
                [0, 0, 0, 4, 1, 0, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 0]
            ],
            "hard": [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
}



def select_difficulty():
    difficulty = input("Select difficulty (easy, medium, hard): ").lower()
    while difficulty not in default_borads:
        print("Invalid choice. Please select easy, medium, or hard.")
        difficulty = input("Select difficulty (easy, medium, hard): ").lower()
    return  difficulty