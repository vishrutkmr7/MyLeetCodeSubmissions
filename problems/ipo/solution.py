class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        zipped = sorted(zip(capital, profits), reverse=True)

        for _ in range(k):
            while zipped and zipped[-1][0] <= w: 
                heapq.heappush(heap, -zipped.pop()[1]) #maxHeap

            if heap:
                w -= heapq.heappop(heap)
                
        return w