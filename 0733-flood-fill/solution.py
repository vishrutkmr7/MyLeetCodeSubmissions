class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        n = len(image)
        m = len(image[0])
        
        q = deque()
        seen = set()
        
        q.append((sr,sc))
        seen.add((sr,sc))
        while q:
            i, j = q.popleft()
            image[i][j] = color
            for x, y in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i+x < n and 0 <= j+y < m and image[i+x][j+y] == starting_color and (i+x, j+y) not in seen:
                    q.append((i+x, j+y))
                    seen.add((i+x, j+y))
        
        return image
        
