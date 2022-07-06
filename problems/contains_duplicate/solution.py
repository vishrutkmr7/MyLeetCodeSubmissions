class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        return not len(nums) == len(numSet)
        