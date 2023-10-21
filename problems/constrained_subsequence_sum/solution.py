class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = collections.deque()
        for i in range(len(nums)):
            nums[i] += dq[0] if dq else 0
            while len(dq) and nums[i] > dq[-1]:
                dq.pop()

            if nums[i] > 0:
                dq.append(nums[i])
            if i >= k and dq and dq[0] == nums[i - k]:
                dq.popleft()
        
        return max(nums)
        