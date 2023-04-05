class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for row in grid:
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            total += len(row) - left
        return total