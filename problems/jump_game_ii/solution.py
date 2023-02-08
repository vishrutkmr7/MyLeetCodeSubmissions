class Solution:
    def jump(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(index):
            if(index >= len(nums) - 1):
                return 0
            maxval = float("inf")
            for i in range(1, nums[index] + 1):
                maxval = min(maxval, 1 + dp(index + i))
            return maxval
        return dp(0)