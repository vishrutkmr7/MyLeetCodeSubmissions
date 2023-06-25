class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(i: int, f: int) -> int:
            return 0 if f < 0 else (1 if i == finish else 0) + sum(0 if i == j else dfs(j, f - abs(locations[j] - locations[i])) for j in range(len(locations)))
        
        return dfs(start, fuel) % 1000000007
