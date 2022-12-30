class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(i, cur):
            if i == nodes - 1:
                result.append(cur[:])
                return

            for j in graph[i]:
                dfs(j, cur + [j])

        nodes = len(graph)
        result = []
        dfs(0, [0])
        return result