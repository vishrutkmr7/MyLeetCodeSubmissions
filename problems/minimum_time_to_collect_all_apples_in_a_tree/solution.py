class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        globalCnt = 0
        visited = [False for i in range(n)] 
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)  

        def dfs(root,graph,apple,visited):
            nonlocal globalCnt
            ret = False
            if apple[root]:
                ret = True
            visited[root] = True

	    	# Mark this visited
            for neighbor in graph[root]:
                if not visited[neighbor]:
                    if dfs(neighbor,graph,apple,visited):
                        globalCnt += 2
                        ret = True
            return ret

        dfs(0,graph,hasApple,visited)
        return globalCnt