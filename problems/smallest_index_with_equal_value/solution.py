class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        ans = [i for i, v in enumerate(nums) if i % 10 == v]
        return min(ans, default=-1)