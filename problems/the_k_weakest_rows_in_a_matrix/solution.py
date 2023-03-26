class Solution:
    def kWeakestRows(self, matrix: List[List[int]], k: int) -> List[int]:
        return [
            i[0]
            for i in sorted(
                [[i, sum(matrix[i])] for i in range(len(matrix))], key=lambda x: x[1]
            )
        ][:k]