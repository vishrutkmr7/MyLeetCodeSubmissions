class Solution:
    def checkStraightLine(self, points: List[List[int]]) -> bool:
        if len(points) == 2:
            return True

        x1, y1 = points[0]
        x2, y2 = points[1]

        for i in range(2, len(points)):
            x, y = points[i]
            if (y2 - y1) * (x - x1) != (y - y1) * (x2 - x1):
                return False

        return True