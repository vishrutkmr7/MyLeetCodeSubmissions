class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        matrix = defaultdict(int)
        count = 0

        for row in grid:
            matrix[str(row)] += 1

        for i in range(len(grid[0])):
            col = [item[i] for item in grid]
            count += matrix[str(col)]
        return count