class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        memo = {}

        def dfs(i, target):
            if target == 0:
                return True
            if target < 0 or i == len(nums):
                return False
            if (i, target) in memo:
                return memo[(i, target)]

            if dfs(i + 1, target - nums[i]) or dfs(i + 1, target):
                memo[(i, target)] = True
                return True
            memo[(i, target)] = False
            return memo[(i, target)]

        return dfs(0, sum(nums) // 2)

