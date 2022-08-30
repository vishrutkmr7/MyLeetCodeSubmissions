class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def rotateImg(i, k):
            for j in range(k):
                t = matrix[i][i + j]
                matrix[i][i + j] = matrix[n - i - 1 - j][i]
                matrix[n - i - 1 - j][i] = matrix[n - i - 1][n - i - 1 - j]
                matrix[n - i - 1][n - i - 1 - j] = matrix[i + j][n - i - 1]
                matrix[i + j][n - i - 1] = t

        i = 0
        n = len(matrix)
        k = n - 1
        while k > 0:
            rotateImg(i, k)
            i += 1
            k -= 2
        return
