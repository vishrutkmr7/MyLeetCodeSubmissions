class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        return [
            list(x)
            for i in range(2, len(nums) + 1)
            for x in set(combinations(nums, i))
            if all(a <= b for a, b in zip(x, x[1:]))
        ]