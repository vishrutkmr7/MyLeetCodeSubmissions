class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return[i, hashMap[diff]]
            hashMap[nums[i]] = i