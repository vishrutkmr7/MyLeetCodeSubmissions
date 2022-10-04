class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, n = 0, len(nums)
        prefixSum = [nums[0]]
        dic = {}
        dic[0] = 1
        for i in nums[1:]:
            prefixSum.append(i+prefixSum[-1])
        for i in prefixSum:
            if i-k in dic:
                res+=dic[i-k]
            dic[i] = dic.get(i,0) + 1 
        return res