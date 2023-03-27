class Solution:
    def imageSmoother(self, image: List[List[int]]) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in product(range(m), range(n)):
            count = 0
            for x, y in product(
                range(max(0, i - 1), min(m, i + 2)), range(max(0, j - 1), min(n, j + 2))
            ):
                result[i][j] += image[x][y]
                count += 1
            result[i][j] = result[i][j] // count
        return result