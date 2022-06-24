class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        added = 0
        for i in nums:
            added += i
            result.append(added)
        return result