class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        prefix_sum.extend(prefix_sum[-1] + num for num in nums)
        
        queue = deque()
        shortest_length = float("inf")
        for index, value in enumerate(prefix_sum):
            while queue and value <= prefix_sum[queue[-1]]:
                queue.pop()

            while queue and value - prefix_sum[queue[0]] >= k:
                shortest_length = min(shortest_length, index - queue.popleft())

            queue.append(index)

        return shortest_length if shortest_length != float("inf") else -1