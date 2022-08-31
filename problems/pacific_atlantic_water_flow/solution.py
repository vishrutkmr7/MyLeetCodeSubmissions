class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pac = set()
        atl = set()
        ROW = len(heights)
        COL = len(heights[0])

        for col in range(COL):
            self.dfs(0, col, pac, heights[0][col], heights)
            self.dfs(ROW-1, col, atl, heights[ROW-1][col], heights)

        for row in range(ROW):
            self.dfs(row, 0, pac, heights[row][0], heights)
            self.dfs(row, COL-1, atl, heights[row][COL-1], heights)

        for row in range(ROW):
            for col in range(COL):
                if (row, col) in pac and (row, col) in atl:
                    res.append([row, col])

        return res

    
    def dfs(self, row, col, vis, prev, heights):
        try:
            cur = heights[row][col]
        except:
            pass

        if (0<=row<len(heights) and 0<=col<len(heights[0])) \
            and (cur >= prev) \
                and ((row, col) not in vis):

            vis.add((row, col))

            self.dfs(row+1, col, vis, cur, heights)
            self.dfs(row-1, col, vis, cur, heights)
            self.dfs(row, col+1, vis, cur, heights)
            self.dfs(row, col-1, vis, cur, heights)
