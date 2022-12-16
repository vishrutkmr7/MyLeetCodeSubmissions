class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.insert(i, 0)
                nums.pop()
                i += 1
            i += 1