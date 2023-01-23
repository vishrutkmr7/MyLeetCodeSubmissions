class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        cur_sum = max_sum
        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, cur_sum)
        return max_sum / k