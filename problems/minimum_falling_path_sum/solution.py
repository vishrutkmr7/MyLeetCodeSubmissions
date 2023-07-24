class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        result =[]
        col = len(matrix)
        row = len(matrix[0])
        dp = [list(range(col)) for _ in range(row)]
        for j in range(row):
                dp[0][j] = matrix[0][j]

        for i in range(1, col):
            for j in range(0, row):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1])
                elif j == row - 1:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j - 1],dp[i - 1][j])
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j - 1], dp [i - 1][j], dp[i - 1][j + 1])

        return min(dp[col - 1])