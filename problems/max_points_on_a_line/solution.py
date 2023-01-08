class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) < 3:
            return len(points)
        max_points = 0
        for i in range(len(points)):
            slopes = {}
            duplicates = 1
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    duplicates += 1
                else:
                    slope = self.get_slope(points[i], points[j])
                    if slope in slopes:
                        slopes[slope] += 1
                    else:
                        slopes[slope] = 1
            max_points = max(max_points, max(slopes.values(), default=0) + duplicates)
        return max_points

    def get_slope(self, point1: list[int], point2: list[int]) -> float:
        if point1[0] == point2[0]:
            return float("inf")
        return (point1[1] - point2[1]) / (point1[0] - point2[0])
