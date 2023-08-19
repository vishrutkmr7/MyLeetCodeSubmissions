class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        windowStart=0
        count=0
        curr=0
        
        for windowEnd, num in enumerate(nums):
            if left <= num <= right:
                curr = windowEnd - windowStart + 1
            elif num > right:
                curr = 0
                windowStart = windowEnd + 1
            
            count += curr
        return count