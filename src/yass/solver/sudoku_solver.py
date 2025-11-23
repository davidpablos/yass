class SudokuSolver:
    def __init__(self, sudoku):
        self._sudoku = [[0 for _ in range(9)] for _ in range(9)]
        self._rows_used  = [set() for _ in range(9)]
        self._cols_used  = [set() for _ in range(9)]
        self._boxes_used = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                number = sudoku[row][col]
                if number != 0:
                    self._sudoku[row][col] = sudoku[row][col]
                    box = self._get_box_idx(row, col)
                    self._put_number(row, col, box, number)

    def _get_box_idx(self, row, col):
        return (row // 3) * 3 + (col // 3)

    def _put_number(self, row, col, box, number):
        self._sudoku[row][col] = number

        self._rows_used[row].add(number)
        self._cols_used[col].add(number)
        self._boxes_used[box].add(number)

    def _is_valid(self, row, col, box, number):
        return number not in self._rows_used[row] and number not in self._cols_used[col] and number not in self._boxes_used[box]

    def _get_least_options_cell(self):
        ALL_NUMBERS = set(range(1, 10))

        best = None
        best_count = 10
        
        for row in range(9):
            for col in range(9):
                if self._sudoku[row][col] == 0:
                    box = self._get_box_idx(row, col)

                    candidates = ALL_NUMBERS - self._rows_used[row] - self._cols_used[col] - self._boxes_used[box]
                    count = len(candidates)

                    if count < best_count:
                        best_count = count
                        best = (row, col)

                        if count == 1:
                            return best

        return best

    def solve(self):
        cell = self._get_least_options_cell()
        if cell is None:
            return self._sudoku

        row, col = cell
        for number in range(1, 10):
            box = self._get_box_idx(row, col)
            if self._is_valid(row, col, box, number):
                self._put_number(row, col, box, number)

                if self.solve() is not None:
                    return self._sudoku

                self._sudoku[row][col] = 0

                self._rows_used[row].remove(number)
                self._cols_used[col].remove(number)
                self._boxes_used[box].remove(number)

        return None