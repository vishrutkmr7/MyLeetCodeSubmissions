class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        res = [-1] * len(nums)

        left, curWindowSum, diameter = 0, 0, 2 * k + 1
        for right, num in enumerate(nums):
            curWindowSum += num
            if right - left + 1 >= diameter:
                res[left + k] = curWindowSum // diameter
                curWindowSum -= nums[left]
                left += 1
        return res
