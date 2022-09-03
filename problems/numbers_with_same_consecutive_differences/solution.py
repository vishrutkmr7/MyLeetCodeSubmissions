from collections import deque


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:

        res = []
        q = deque((1, d) for d in range(1, 10))

        while q:
            pos, num = q.pop()
            if pos == n:
                res.append(num)
            else:
                for j in range(10):
                    if abs(num % 10 - j) == k:
                        q.append((pos + 1, num * 10 + j))

        return res
