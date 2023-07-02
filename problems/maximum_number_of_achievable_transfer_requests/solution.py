class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        for k in range(len(requests), 0, -1):
            for c in combinations(requests, k):
                if Counter(a for a, b in c) == Counter(b for a, b in c):
                    return k
        return 0