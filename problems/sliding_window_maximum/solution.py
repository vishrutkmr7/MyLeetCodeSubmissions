class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h, ans = [], []
        for i in range(0, len(nums)):
            heappush(h, (-nums[i], i))
            while h[0][1] <= i - k:
                heappop(h)
            if i >= k - 1:
                ans.append(-h[0][0])
        return ans