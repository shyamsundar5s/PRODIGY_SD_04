# PRODIGY_SD_04
# Sudoku Solver
A simple Python implementation of a Sudoku solver using the backtracking algorithm.

## Features
- Solves standard 9x9 Sudoku puzzles.
- Uses backtracking to find a valid solution.
- Input the puzzle directly in the script as a 2D list.
- Prints the solved Sudoku board in a formatted way.

## How It Works
1. The puzzle is represented by a 9x9 nested list (`sudoku_board`), where empty cells are represented by `0`.
2. The program attempts to fill the empty cells with numbers from 1 to 9, ensuring every row, column, and 3x3 subgrid contains only unique numbers.
3. The `solve_sudoku` function uses recursion and backtracking to find a solution.
4. On success, the solved board is printed. If no solution exists, a message is displayed.
