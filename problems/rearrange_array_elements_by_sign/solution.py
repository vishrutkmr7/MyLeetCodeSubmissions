class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [
            val
            for t in zip([x for x in nums if x > 0], [x for x in nums if x < 0])
            for val in t
        ]
