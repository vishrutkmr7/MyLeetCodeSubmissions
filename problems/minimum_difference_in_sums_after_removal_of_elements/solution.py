class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = int(len(nums)//3)
        count = 0
        left = [0] * len(nums)
        right = [0] * len(nums)
        left[n - 1] = sum(nums[:n])
        q1 = [-a for a in nums[:n]]
        heapify(q1)

        for k in range(n, 2*n):
            heappush(q1, -nums[k])
            left[k] = left[k - 1] + nums[k] + heappop(q1)
        right[2*n] = sum(nums[2*n:])
        q2 = nums[2*n:]
        heapify(q2)

        for k in range(2*n - 1, n - 1, -1):
            heappush(q2, nums[k])
            right[k] = right[k + 1] + nums[k] - heappop(q2)
        res=float('inf')
        for i in range(n - 1, 2*n):
            res=min(res, left[i] - right[i + 1])
        return res
        