class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        for i in reversed(range(last_index)):
            if i + nums[i] >= last_index:
                last_index = i
        return last_index == 0