class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curmin, curmax = 1, 1
        res = max(nums)

        for i in nums:
            if i == 0:
                curmin, curmax = 1, 1
                continue
            temp = curmax * i
            curmax = max(temp, curmin * i, i)
            curmin = min(temp, curmin * i, i)
            res = max(res, curmax)
        return res
