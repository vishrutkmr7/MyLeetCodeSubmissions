class Solution:
    def canThreePartsEqualSum(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 3 != 0:
            return False
        target = total // 3
        count = 0
        temp = 0
        for num in nums:
            temp += num
            if temp == target:
                count += 1
                temp = 0
        return count >= 3