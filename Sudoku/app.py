def print_board(board):
    """
    Print the Sudoku board
    """
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def find_empty_location(board):
    """
    Find the next empty location on the board
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, num, row, col):
    """
    Check if the placement of a number is valid in a certain row, column and 3x3 box
    """
    # Check row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    """
    Solve the Sudoku board recursively
    """
    empty_location = find_empty_location(board)
    if empty_location is None:
        # No empty location left, puzzle solved
        return True

    row, col = empty_location
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            # Place the number on the board
            board[row][col] = num

            # Recursively solve the board
            if solve_sudoku(board):
                return True

            # Backtrack if the current placement didn't lead to a solution
            board[row][col] = 0

    # No valid number found, backtrack further
    return False

# Example board
board = [
    [0, 2, 0   , 0, 0, 0   , 0, 0, 0],
    [0, 0, 0   , 6, 0, 0   , 0, 0, 3],
    [0, 7, 4   , 0, 8, 0   , 0, 0, 0],
    [0, 0, 0   , 0, 0, 3   , 0, 0, 2],
    [0, 8, 0   , 0, 4, 0   , 0, 1, 0],
    [6, 0, 0   , 5, 0, 0   , 0, 0, 0],
    [0, 0, 0   , 0, 1, 0   , 7, 8, 0],
    [5, 0, 0   , 0, 0, 9   , 0, 0, 0],
    [0, 0, 0   , 0, 0, 0   , 0, 4, 0]
]

# Solve the board
if solve_sudoku(board):
    print("Solution:")
    print_board(board)
else:
    print("No solution exists.")
