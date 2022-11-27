class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        dp = [defaultdict(int) for _ in range(len(nums))]
        res = 0
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
                res += dp[j].get(diff, 0)
        return res