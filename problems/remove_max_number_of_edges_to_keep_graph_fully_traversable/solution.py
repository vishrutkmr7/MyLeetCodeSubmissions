class UnionFind:
    """A minimalist standalone union-find implementation."""

    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        """Find with path compression."""
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        """Union with ranking."""
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt:
            return False
        self.count -= 1
        if self.rank[prt] > self.rank[qrt]:
            prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        ufa = UnionFind(n)
        ufb = UnionFind(n)

        ans = 0
        edges.sort(reverse=True)
        for t, u, v in edges:
            u, v = u - 1, v - 1
            if t == 3:
                ans += not (ufa.union(u, v) and ufb.union(u, v))
            elif t == 2:
                ans += not ufb.union(u, v)
            else:
                ans += not ufa.union(u, v)
        return ans if ufa.count == 1 and ufb.count == 1 else -1
