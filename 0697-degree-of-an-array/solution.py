class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        first, count, res, degree = {}, {}, 0, 0
        for index, value in enumerate(nums):
            first.setdefault(value, index)
            count[value] = count.get(value, 0) + 1
            if count[value] > degree:
                degree = count[value]
                res = index - first[value] + 1
            elif count[value] == degree:
                res = min(res, index - first[value] + 1)
        return res
