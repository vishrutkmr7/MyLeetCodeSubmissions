class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = {}
        for num in arr:
            res[num] = res[num - difference] + 1 if (num - difference) in res else 1
        return max(res.values())