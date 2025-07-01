def is_valid(board, row, col, num):
    # Check if the number is already present in the row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is present in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    # Find an empty location (cell with 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    # Find an empty location
    empty_loc = find_empty_location(board)

    if not empty_loc:
        return True  # Sudoku solved

    row, col = empty_loc

    # Try placing a number from 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # If the number is valid, place it and recursively solve the rest of the puzzle
            board[row][col] = num

            if solve_sudoku(board):
                return True  # If the recursive call leads to a solution, return True

            # If placing the number doesn't lead to a solution, backtrack
            board[row][col] = 0

    return False  # No valid number found, trigger backtracking

def print_sudoku(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
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

if solve_sudoku(sudoku_board):
    print("Sudoku Solved:")
    print_sudoku(sudoku_board)
else:
    print("No solution exists.")
