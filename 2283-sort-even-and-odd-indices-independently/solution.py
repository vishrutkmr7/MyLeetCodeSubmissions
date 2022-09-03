class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = [nums[i] for i in range(0 , len(nums)) if i % 2 == 0]
        odd = [nums[i] for i in range(0 , len(nums)) if i % 2 != 0]

        even.sort()
        odd = sorted(odd , reverse = True)
        return [even.pop(0) if i % 2 == 0 else odd.pop(0) for i in range(len(nums))]

