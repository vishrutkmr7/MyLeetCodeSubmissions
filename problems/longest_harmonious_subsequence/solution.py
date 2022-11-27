class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = 0
        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        for num in num_count.items():
            if num[0] + 1 in num_count:
                count = max(count, num_count[num[0]] + num_count[num[0] + 1])

        return count