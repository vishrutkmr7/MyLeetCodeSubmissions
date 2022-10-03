class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, ans = 0, 0
        while i < len(colors):
            j = i + 1
            while j < len(colors) and colors[i] == colors[j]:
                if neededTime[i] <= neededTime[j]:
                    ans += neededTime[i]
                    i = j
                    j += 1
                elif neededTime[j] < neededTime[i]:
                    ans += neededTime[j]
                    j += 1
            i = j
        return ans