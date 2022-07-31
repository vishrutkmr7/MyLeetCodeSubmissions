class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0
        ans = 0
        nums = sorted(nums)
        while sum(nums) > 0:
            x = 0
            for num in nums:
                if num > 0:
                    x = num
                    break
            nums = [num - x if num - x > 0 else 0 for num in nums]
                
            ans += 1
        
        return ans
            
        
            
