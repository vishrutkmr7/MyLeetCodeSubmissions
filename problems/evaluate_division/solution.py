class Solution:
    def answer(self, current, end, scalar):
        if current == end:
            return scalar
        self.visited.add(current)
        if current in self.graph:
            for i in self.graph[current]:
                if i[0] not in self.visited:
                    a = self.answer(i[0], end, scalar * i[1])
                    if a != -1:
                        return a
        return -1

    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        self.graph, self.visited = {}, set()
        for i, val in enumerate(equations):
            if val[0] not in self.graph:
                self.graph[val[0]] = []
            if val[1] not in self.graph:
                self.graph[val[1]] = []
            self.graph[val[0]].append((val[1], 1 / values[i]))
            self.graph[val[1]].append((val[0], values[i]))

        v = []
        for i in queries:
            self.visited = set()
            if i[0] not in self.graph or i[1] not in self.graph:
                v.append(-1)
                continue
            v.append(1 / self.answer(i[0], i[1], 1) if i[0] != i[1] else 1)
        return v
