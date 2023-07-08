class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        B = [a + b for a,b in pairwise(weights)]
        return sum(nlargest(k - 1, B)) - sum(nsmallest(k - 1, B))