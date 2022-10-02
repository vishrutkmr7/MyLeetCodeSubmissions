class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        return [i for i, value in dic.items() if value > 1]
