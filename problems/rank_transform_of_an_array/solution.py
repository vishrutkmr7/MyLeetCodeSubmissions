class Solution:
    def arrayRankTransform(self, nums: List[int]) -> List[int]:
        rank = {}
        for i, n in enumerate(sorted(set(nums))):
            if n not in rank:
                rank[n] = i + 1
        return [rank[n] for n in nums]