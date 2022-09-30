import bisect


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        tops = []
        for l, r, h in buildings:
            tops.extend([[l, -h], [r, h]])

        tops.sort()
        n = len(tops)
        res = []
        heights = [0]

        for i in range(n):
            x, h = tops[i]
            if h < 0:
                bisect.insort_left(heights, h)
            else:
                ind = bisect.bisect_left(heights, -h)
                heights.pop(ind)

            if not res or res[-1][1] != -heights[0]:
                res.append((x, -heights[0]))

        return res

