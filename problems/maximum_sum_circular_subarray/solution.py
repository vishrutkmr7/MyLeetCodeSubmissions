class Solution:
    def maxSublist(self, nums):
        localMax = 0
        globalMax = float('-inf')
        for num in nums:
            localMax = max(num, num + localMax)
            globalMax = max(localMax, globalMax)
                
        return globalMax
    
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxElement = max(nums)
        if maxElement < 0:
            return maxElement
        temp = [-num for num in nums]

        neg_max_sum = self.maxSublist(temp)
        return max(self.maxSublist(nums), sum(nums) + neg_max_sum)
        