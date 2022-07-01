class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        sortd = sorted(nums)
        med = sortd[len(sortd) // 2]
        return sum(abs(n-med) for n in sortd)
        