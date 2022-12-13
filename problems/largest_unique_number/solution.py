class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return next((nums[i] for i in range(len(nums)) if nums.count(nums[i]) == 1), -1)
