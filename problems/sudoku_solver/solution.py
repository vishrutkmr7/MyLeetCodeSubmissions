import itertools


class Solution:
    possible = set(str(nr) for nr in range(1, 10))

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.dfs()

    def dfs(self):
        rx, cx, complete = self.findEmpty()
        if complete:
            return True

        available = self.getPossible(rx, cx)

        if not available:
            return False

        for number in available:
            self.board[rx][cx] = number
            if self.dfs():
                return True

            self.board[rx][cx] = "."

        return False

    def findEmpty(self):
        return next(
            (
                (rx, cx, False)
                for rx, cx in itertools.product(
                    range(len(self.board)), range(len(self.board[0]))
                )
                if self.board[rx][cx] == "."
            ),
            (-1, -1, True),
        )

    def getPossible(self, rx, cx):
        return (
            self.possible
            - self.getBox(rx, cx)
            - self.getRow(rx, cx)
            - self.getCol(rx, cx)
        )

    def getRow(self, rx, cx):
        return set(self.board[rx])

    def getCol(self, rx, cx):
        return {row[cx] for row in self.board}

    def getBox(self, rx, cx):
        result = set()
        for rx in range(rx // 3 * 3, rx // 3 * 3 + 3):
            result.update(self.board[rx][cx // 3 * 3 : cx // 3 * 3 + 3])
        return result
