class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
        We can use a graph to represent the dislikes.
        We can color the nodes in the graph with two colors.
        If we can color the graph with two colors, then we can split the group into two groups.
        """
        graph = [[] for _ in range(n)]
        for dislike in dislikes:
            graph[dislike[0] - 1].append(dislike[1] - 1)
            graph[dislike[1] - 1].append(dislike[0] - 1)

        colors = [0] * n
        return not any(
            colors[i] == 0 and not self.dfs(graph, colors, 1, i) for i in range(n)
        )
    
    def dfs(
        self, graph: list[list[int]], colors: list[int], color: int, node: int
    ) -> bool:
        if colors[node] != 0:
            return colors[node] == color
        colors[node] = color
        return all(
            self.dfs(graph, colors, -color, neighbor) for neighbor in graph[node]
        )