class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        min_diff = min(nums[i + 1] - nums[i] for i in range(len(nums) - 1))
        return [
            [nums[i], nums[i + 1]]
            for i in range(len(nums) - 1)
            if nums[i + 1] - nums[i] == min_diff
        ]