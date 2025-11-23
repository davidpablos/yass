import time

from sudoku_solver import SudokuSolver

# ai_escargot = [
#     [1, 0, 0, 0, 0, 7, 0, 9, 0],
#     [0, 3, 0, 0, 2, 0, 0, 0, 8],
#     [0, 0, 9, 6, 0, 0, 5, 0, 0],
#     [0, 0, 5, 3, 0, 0, 9, 0, 0],
#     [0, 1, 0, 0, 8, 0, 0, 0, 2],
#     [6, 0, 0, 0, 0, 4, 0, 0, 0],
#     [3, 0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 4, 0, 0, 0, 0, 0, 0, 7],
#     [0, 0, 7, 0, 0, 0, 3, 0, 0]
# ]

platinum_blonde = [
    [0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 2, 3, 0, 0, 4, 0, 0],
    [0, 0, 1, 8, 0, 0, 0, 0, 5],
    [0, 6, 0, 0, 7, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 8, 5, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 4, 0, 5, 0, 0],
    [4, 7, 0, 0, 0, 6, 0, 0, 0],
]

solver = SudokuSolver(platinum_blonde)

start = time.time()
solution = solver.solve()
end = time.time()
solve_time_ms = (end - start) * 1000

if solution:
    for row in solution:
        print(row)
else:
    print("There are no solution")

print(f"Solving time: {solve_time_ms:.3f} ms")