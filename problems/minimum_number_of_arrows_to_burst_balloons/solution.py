class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        res = 0
        last_max = -float('inf')
        for start, end in points:
            if start > last_max:
                res += 1
                last_max = end
        
        return res