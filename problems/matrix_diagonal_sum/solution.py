class Solution:
    def diagonalSum(self, matrix: List[List[int]]) -> int:
        res = 0
        for i, v in enumerate(matrix):
            res += v[i]
            res += v[len(matrix) - i - 1]

        if len(matrix) % 2 == 1:
            res -= matrix[len(matrix) // 2][len(matrix) // 2]
        return res