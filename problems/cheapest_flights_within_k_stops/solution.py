class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G = defaultdict(list)
        for v, w, d in flights:
            G[v].append((w,d))
        h = [(0, 0, src)]
        visited = set()
        while h:
            d, curk, v = heappop(h)
            if v == dst: return d
            if (v, curk) in visited or curk > k: continue
            visited.add((v, curk))
            for w, ecost in G[v]:
                heappush(h, (d+ecost, curk + 1, w))
        return -1