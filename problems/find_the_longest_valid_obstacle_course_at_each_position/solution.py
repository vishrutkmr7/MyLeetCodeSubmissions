class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: list[int]) -> list[int]:
        lis = []
        for i, v in enumerate(nums):
            if len(lis) == 0 or lis[-1] <= v:
                lis.append(v)
                nums[i] = len(lis)
            else:
                idx = bisect_right(lis, v)
                lis[idx] = v
                nums[i] = idx + 1
        return nums