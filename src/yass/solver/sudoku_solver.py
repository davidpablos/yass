class SudokuSolver:
    def __init__(self, sudoku):
        self.sudoku = sudoku
    
    def is_valid_column(self, number, col):
        for row in range(9):
            if self.sudoku[row][col] == number:
                return False
        
        return True

    def is_valid_row(self, number, row):
        if number in self.sudoku[row]:
            return False
        
        return True

    def is_valid_block(self, number, row, col):
        block_first_row = 3 * (row // 3)
        block_first_col = 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.sudoku[block_first_row + i][block_first_col + j] == number:
                    return False

        return True

    def is_valid(self, number, row, col):
        return self.is_valid_column(number, col) and self.is_valid_row(number, row) and self.is_valid_block(number, row, col)

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.sudoku[row][col] == 0:
                    for number in range(1, 10):
                        if self.is_valid(number, row, col):
                            self.sudoku[row][col] = number
                            if self.solve() is not None:
                                return self.sudoku
                            self.sudoku[row][col] = 0
        
        return None