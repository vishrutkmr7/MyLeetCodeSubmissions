class Solution:
    def checkIfExist(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        return any(2 * x in cnt and x != 0 for x in nums) or cnt[0] > 1