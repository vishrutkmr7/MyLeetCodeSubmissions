class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        out=[nums[0], max(nums[0], nums[1])]

        out.extend(max(out[i-1], nums[i] + out[i-2]) for i in range(2, len(nums)))
        return out[-1]