from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue = deque([0])
        
        for i in range(1, len(nums)):
            while queue and queue[0] < i - k:
                queue.popleft()
            nums[i] += nums[queue[0]]
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        return nums[-1]
