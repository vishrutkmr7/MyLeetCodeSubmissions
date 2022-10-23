class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n, total, total_og = len(nums), sum(nums), sum(set(nums))
        s = n * (n + 1) // 2
        return [total - total_og, s - total_og]