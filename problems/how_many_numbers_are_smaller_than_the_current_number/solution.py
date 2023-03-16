class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        mapping = {}
        for i, val in enumerate(temp):
            if val not in mapping:
                mapping[val] = i

        return [mapping[i] for i in nums]