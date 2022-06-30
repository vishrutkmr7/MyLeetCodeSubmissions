class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        sortd = sorted(nums)
        med = sortd[int(len(sortd) / 2)]
        minMoveCount = 0
        for n in sortd:
            minMoveCount += abs(n-med)
        return minMoveCount
        