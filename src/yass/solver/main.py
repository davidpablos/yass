from sudoku_solver import SudokuSolver

grid = [
    [8, 0, 0, 3, 4, 0, 7, 6, 0],
    [0, 0, 0, 7, 1, 4, 3, 5, 0],
    [0, 7, 3, 0, 0, 0, 8, 1, 0],
    [2, 0, 9, 7, 6, 0, 0, 0, 0],
    [7, 3, 4, 0, 9, 0, 0, 0, 0],
    [0, 0, 0, 1, 3, 2, 0, 0, 9],
    [5, 0, 8, 0, 0, 7, 1, 0, 0],
    [3, 4, 2, 9, 0, 0, 0, 6, 0],
    [1, 0, 0, 0, 6, 8, 0, 0, 0]
]

solver = SudokuSolver(grid)
solution = solver.solve()

if solution:
    for row in solution:
        print(row)
else:
    print("There are no solution")