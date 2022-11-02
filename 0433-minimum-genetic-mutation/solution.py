class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        def checkNeighbor(a, b):
            return sum(a[i] != b[i] for i in range(len(a))) == 1

        q = deque([start])
        visited = {start}
        mutations = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == end:
                    return mutations
                for neighbor in bank:
                    if checkNeighbor(cur, neighbor) and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            mutations += 1
        return -1

