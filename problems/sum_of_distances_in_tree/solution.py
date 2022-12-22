class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        size, up, down = [1] * N, [0] * N, [0] * N

        def post(parent, i):
            for kid in graph[i]:
                if kid != parent:
                    post(i, kid)
                    size[i] += size[kid]
                    up[i] += up[kid] + size[kid]

        def pre(parent, i):
            if parent != -1:
                down[i] = down[parent] + (up[parent] - up[i] - size[i]) + (N - size[i])
            for kid in graph[i]:
                if kid != parent:
                    pre(i, kid)

        post(-1, 0)
        pre(-1, 0)
        return [up[i] + down[i] for i in range(N)]