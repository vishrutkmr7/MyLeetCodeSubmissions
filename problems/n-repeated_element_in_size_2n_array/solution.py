class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if v in nums[i + 1 :]:
                return v