class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        missing = 0
        for i in range(1, nums[-1]):
            if i not in nums:
                missing += 1
                if missing == k:
                    return i

        return nums[-1] + k - missing