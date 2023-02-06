class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[x + n * y] for x in range(n) for y in range(2)]