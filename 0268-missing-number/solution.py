class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        if len(nums) == 1:
            return 1
        n = max(nums)
        AP_sum = n * (n + 1) / 2
        nums_sum = sum(nums)
        return int(n + 1 if AP_sum == nums_sum else AP_sum - nums_sum)
