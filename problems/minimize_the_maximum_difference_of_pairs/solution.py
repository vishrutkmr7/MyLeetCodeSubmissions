class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        # Binary search
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            k = 0
            i = 1
            while i < n:
                if nums[i] - nums[i - 1] <= mid:
                    k += 1
                    i += 1
                i += 1
            if k >= p:
                right = mid
            else:
                left = mid + 1
        return left
