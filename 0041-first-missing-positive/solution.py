class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        arr = set(nums)
        data = (i for i in range(1, len(arr) + 2) if i not in arr)
        return min(data)
