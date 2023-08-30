class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        prev = nums[n - 1]
        for i in range(n - 2, -1, -1):
            num = nums[i]
            k = math.ceil(num / prev)
            ans += k - 1 # min times to split
            prev = num // k

        return ans
