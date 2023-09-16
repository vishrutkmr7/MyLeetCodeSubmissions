class Weighted_UF:
    def __init__(self, n: int):
        self.ids = list(range(n))
        self.weights = [0] * n
    
    def union(self, p: int, q: int):
        parent_p = self.find(p)
        parent_q = self.find(q)
        
        if parent_p == parent_q:
            return
        
        if self.weights[parent_p] > self.weights[parent_q]:
            parent_p, parent_q = parent_q, parent_p
        
        self.ids[parent_p] = parent_q
        self.weights[parent_q] += self.weights[parent_p]
    
    def find(self, p: int) -> int:
        while p != self.ids[p]:
            self.ids[p] = self.ids[self.ids[p]]
            p = self.ids[p]
        return p
    
    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

        
class Solution:
    # Kruskal’s MST algorithm
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        edges = self.collectEdges(heights)
        heapify(edges)
        uf = Weighted_UF(m * n)
        weight = source = 0
        target = m * n - 1
        while not uf.connected(source, target):
            weight, root, child = heappop(edges)
            uf.union(root, child)
        
        return weight
    
    # treat the matrix as a graph and collect all possible edges
    def collectEdges(self, heights: List[List[int]]) -> List[tuple]:
        m = len(heights)
        n = len(heights[0])
        edges = []
        for i, j in product(range(m), range(n)):
            from_id = i * n + j
            if i:
                diff = abs(heights[i][j] - heights[i-1][j])
                to_id = (i-1) * n + j
                edges.append((diff, from_id, to_id))
            if j:
                diff = abs(heights[i][j] - heights[i][j-1])
                to_id = i * n + j - 1
                edges.append((diff, from_id, to_id))
        
        return edges