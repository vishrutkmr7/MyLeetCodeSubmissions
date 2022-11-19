class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * n
        for start, end in requests:
            count[start] += 1
            if end < n - 1:
                count[end + 1] -= 1
        for i in range(1, n):
            count[i] += count[i - 1]
        count.sort()
        nums.sort()
        ans = sum(count[i] * nums[i] for i in range(n))
        return ans % (10**9 + 7)
