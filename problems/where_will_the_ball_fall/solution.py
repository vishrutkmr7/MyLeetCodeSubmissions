class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row, col = len(grid), len(grid[0])
        for i in range(row):
            grid[i].insert(0, 1)
            grid[i].append(-1)
        res = []
        
        for k in range(1, col + 1):
            i , j = 0 , k
            stuck = False
            while i < row:
                if grid[i][j] == 1:
                    if grid[i][j + 1] == 1:
                        j += 1
                    else:
                        stuck = True
                        break
                else:
                    if grid[i][j - 1] == -1:
                        j -= 1
                    else:
                        stuck = True
                        break
                i += 1
            if stuck:
                res.append(-1)
            else:
                res.append(j - 1)
                
        return res
        