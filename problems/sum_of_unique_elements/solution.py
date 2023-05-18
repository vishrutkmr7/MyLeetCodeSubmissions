class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return sum(k for k, v in counts.items() if v == 1)