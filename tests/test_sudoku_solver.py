from copy import deepcopy
from src.yass.solver.sudoku_solver import SudokuSolver

def test_solve_simple_sudoku():
    sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    solver = SudokuSolver(sudoku)
    result = solver.solve()
    assert result is not None

    # Filas y columnas válidas
    for row in result:
        assert set(row) == set(range(1, 10))
    for col in range(9):
        col_values = {result[row][col] for row in range(9)}
        assert col_values == set(range(1, 10))


def test_already_solved_sudoku():
    solved = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]
    solver = SudokuSolver(deepcopy(solved))
    result = solver.solve()
    assert result == solved


def test_invalid_sudoku():
    sudoku = [
        [5, 5, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    solver = SudokuSolver(sudoku)
    result = solver.solve()
    assert result is None


def test_get_box_idx():
    solver = SudokuSolver([[0]*9 for _ in range(9)])
    assert solver._get_box_idx(0, 0) == 0
    assert solver._get_box_idx(4, 4) == 4
    assert solver._get_box_idx(8, 8) == 8
    assert solver._get_box_idx(3, 7) == 5
