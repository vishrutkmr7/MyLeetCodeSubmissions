class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        i, N = 0, len(nums)
        nums.sort()
        m = math.inf
        res = None
        if len(nums) == 3:
            return sum(nums)
        if nums[0] + nums[1] + nums[2] >= target:
            return nums[0] + nums[1] + nums[2]
        if nums[-3] + nums[-2] + nums[-1] <= target:
            return nums[-3] + nums[-2] + nums[-1]
        for i in range(N - 2):
            
            left = i + 1
            right = N - 1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if abs(target - s) < m:
                    m = abs(target - s)
                    res = s
                
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return target
                
        return res