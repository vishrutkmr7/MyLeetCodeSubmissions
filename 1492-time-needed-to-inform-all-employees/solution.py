class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)
        
        def dfs(head):
            ans = 0
            for vector in graph[head]:
                ans = max(dfs(vector) + informTime[head], ans)
            return ans
        
        return dfs(headID)
