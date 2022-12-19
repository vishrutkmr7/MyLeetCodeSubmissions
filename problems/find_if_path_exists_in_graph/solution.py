class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        queue = [source]
        while queue:
            u = queue.pop(0)
            if u == destination:
                return True
            visited[u] = True
            queue.extend(v for v in graph[u] if not visited[v])
            
        return False
