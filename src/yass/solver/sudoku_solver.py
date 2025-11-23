import copy

class SudokuSolver:
    def __init__(self, sudoku):
        self.sudoku = [[0 for _ in range(9)] for _ in range(9)]
        self.options = [[[True for _ in range(9)] for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                number = sudoku[row][col]
                if number != 0:
                    self.put_number(row, col, number)

    def put_number(self, row, col, number):
        self.sudoku[row][col] = number
        self.options[row][col] = [False]*9

        for i in range(9):
            self.options[i][col][number - 1] = False

        for j in range(9):
            self.options[row][j][number - 1] = False
        
        block_first_row = 3 * (row // 3)
        block_first_col = 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                self.options[block_first_row + i][block_first_col + j][number - 1] = False

    def is_valid(self, row, col, number):
        return self.options[row][col][number - 1]

    def get_least_options_cell(self):
        min_options = 10
        best_cell = None
        for row in range(9):
            for col in range(9):
                if self.sudoku[row][col] == 0:
                    options_count = sum(self.options[row][col])
                    if options_count < min_options:
                        min_options = options_count
                        best_cell = (row, col)
        
        return best_cell

    def solve(self):
        cell = self.get_least_options_cell()
        if cell is None:
            return self.sudoku

        row, col = cell
        for number in range(1, 10):
            if self.is_valid(row, col, number):
                sudoku_prev = copy.deepcopy(self.sudoku)
                options_prev = copy.deepcopy(self.options)
                self.put_number(row, col, number)
                if self.solve() is not None:
                    return self.sudoku
                self.sudoku = sudoku_prev
                self.options = options_prev

        return None