from itertools import chain


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        n = max(chain(*matches)) + 1
        players = [0] * n
        for win, loss in matches:
            if players[win] >= 0:
                players[win] = 1
            if players[loss] < 0:
                players[loss] -= 1
            if players[loss] >= 0:
                players[loss] = -1

        lostZero, lostOne = [], []
        for i in range(n):
            if players[i] == 1:
                lostZero.append(i)
            elif players[i] == -1:
                lostOne.append(i)

        return [lostZero, lostOne]
