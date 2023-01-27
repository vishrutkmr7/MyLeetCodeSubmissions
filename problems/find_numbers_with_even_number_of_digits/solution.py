class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([num for num in nums if len(str(num)) % 2 == 0])
