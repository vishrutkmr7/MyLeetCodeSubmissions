class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res, running_sum = 0, 0
        dp = [1] + [0] * k
        for num in nums:
            running_sum += num
            res += dp[running_sum % k]
            dp[running_sum % k] += 1
        return res