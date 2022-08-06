class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [float(-inf) for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])
        return max(dp)