class Solution:
    def threeConsecutiveOdds(self, nums: List[int]) -> bool:
        count = 0
        for i in nums:
            if i % 2 != 0:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False
