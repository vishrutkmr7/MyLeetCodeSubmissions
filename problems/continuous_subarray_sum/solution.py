class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        dic, s = {0: -1}, 0
        for index, val in enumerate(nums):
            if k != 0:
                s = (s + val) % k
            else:
                s += val
            if s not in dic:
                dic[s] = index
            elif index - dic[s] >= 2:
                return True
        return False
