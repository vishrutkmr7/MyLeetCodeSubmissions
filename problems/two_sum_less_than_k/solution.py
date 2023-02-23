class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_sum = -1
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < k:
                max_sum = max(max_sum, nums[left] + nums[right])
                left += 1
            else:
                right -= 1
        return max_sum