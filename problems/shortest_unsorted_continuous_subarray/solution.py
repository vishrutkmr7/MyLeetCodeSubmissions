class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        prev = nums[0]
        end = 0
        # find the largest index not in place
        for i, v in enumerate(nums):
            if v < prev:
                end = i
            else:
                prev = v

        start = len(nums) - 1
        prev = nums[start]

        # find the smallest index not in place
        for i in range(len(nums) - 1, -1, -1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]

        return end - start + 1 if end != 0 else 0
