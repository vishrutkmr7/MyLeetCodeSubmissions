class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        cnt = curr = 0
        for num in nums:
            if num == 0:
                curr += 1
                cnt += curr
            else:
                curr = 0
        return cnt