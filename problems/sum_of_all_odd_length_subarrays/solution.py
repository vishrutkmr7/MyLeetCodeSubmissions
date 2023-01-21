class Solution:
    def sumOddLengthSubarrays(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(i, len(nums), 2):
                total += sum(nums[i : j + 1])
        return total