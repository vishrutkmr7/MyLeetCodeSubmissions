class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                cur = 1
                temp = num
                while temp + 1 in num_set:
                    cur += 1
                    temp += 1
                res = max(res, cur)

        return res
                
                