class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def partitions(nums):
            if len(nums) <= 2:
                return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            return (
                comb(len(left) + len(right), len(right))
                * partitions(left)
                * partitions(right)
            )

        return (partitions(nums) - 1) % (10**9 + 7)