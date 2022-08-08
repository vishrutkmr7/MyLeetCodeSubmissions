class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        out=[nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            out.append(max(out[i-1], nums[i] + out[i-2]))
        return out[len(out)-1]
