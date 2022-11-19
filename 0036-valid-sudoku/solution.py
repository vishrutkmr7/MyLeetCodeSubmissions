from itertools import product


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return (
            self.is_valid_rows(board)
            and self.is_valid_columns(board)
            and self.is_valid_boxes(board)
        )

    def is_valid_rows(self, board: list[list[str]]) -> bool:
        return all(self.is_valid_set(row) for row in board)

    def is_valid_columns(self, board: list[list[str]]) -> bool:
        return all(self.is_valid_set(column) for column in zip(*board))

    def is_valid_boxes(self, board: list[list[str]]) -> bool:
        for i, j in product(range(0, 9, 3), range(0, 9, 3)):
            box = [board[i + k][j + l] for k in range(3) for l in range(3)]
            if not self.is_valid_set(box):
                return False
        return True

    def is_valid_set(self, values: list[str]) -> bool:
        values = [value for value in values if value != "."]
        return len(values) == len(set(values))

