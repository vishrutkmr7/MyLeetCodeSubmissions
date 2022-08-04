class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return target in matrix[bisect_right([i[0] for i in matrix], target) - 1]
