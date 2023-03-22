class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for index, val in enumerate(nums):
            right_sum -= val
            if left_sum == right_sum:
                return index
            left_sum += val
        return -1