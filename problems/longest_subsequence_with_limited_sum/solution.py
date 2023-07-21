class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        preSum = [0]
        preSum.extend(preSum[-1]+n for n in nums)
        res = []
        for q in queries:
            indx = bisect_right(preSum,q)
            res.append(indx-1)
        return res