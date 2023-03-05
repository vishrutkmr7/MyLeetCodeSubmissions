class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        mx = -1
        for i in range(len(nums) - 1, -1, -1):
            nums[i], mx = mx, max(mx, nums[i])
        return nums