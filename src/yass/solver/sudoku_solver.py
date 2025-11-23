class SudokuSolver:
    def __init__(self, sudoku):
        self.sudoku = [[0 for _ in range(9)] for _ in range(9)]
        self.rows_used  = [set() for _ in range(9)]
        self.cols_used  = [set() for _ in range(9)]
        self.boxes_used = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                number = sudoku[row][col]
                if number != 0:
                    self.sudoku[row][col] = sudoku[row][col]
                    box = self.get_box_idx(row, col)
                    self.rows_used[row].add(number)
                    self.cols_used[col].add(number)
                    self.boxes_used[box].add(number)

    def get_box_idx(self, row, col):
        return (row // 3) * 3 + (col // 3)

    def put_number(self, row, col, number):
        self.sudoku[row][col] = number
        self.rows_used[row].add(number)
        self.cols_used[col].add(number)

        box = self.get_box_idx(row, col)
        self.boxes_used[box].add(number)

    def is_valid(self, row, col, number):
        box = self.get_box_idx(row, col)
        return number not in self.rows_used[row] and number not in self.cols_used[col] and number not in self.boxes_used[box]

    def get_least_options_cell(self):
        ALL_NUMBERS = set(range(1, 10))

        best = None
        best_count = 10

        for row in range(9):
            for col in range(9):
                if self.sudoku[row][col] == 0:
                    box = self.get_box_idx(row, col)

                    candidates = ALL_NUMBERS - self.rows_used[row] - self.cols_used[col] - self.boxes_used[box]
                    count = len(candidates)

                    if count < best_count:
                        best_count = count
                        best = (row, col)

                        if count == 1:
                            return best

        return best

    def solve(self):
        cell = self.get_least_options_cell()
        if cell is None:
            return self.sudoku

        row, col = cell
        for number in range(1, 10):
            if self.is_valid(row, col, number):
                self.put_number(row, col, number)

                if self.solve() is not None:
                    return self.sudoku

                self.sudoku[row][col] = 0
                self.rows_used[row].remove(number)
                self.cols_used[col].remove(number)

                box = self.get_box_idx(row, col)
                self.boxes_used[box].remove(number)

        return None