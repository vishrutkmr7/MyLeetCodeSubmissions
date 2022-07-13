class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return res