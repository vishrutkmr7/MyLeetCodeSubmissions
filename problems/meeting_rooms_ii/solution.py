class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i[0] >= heap[0]: 
            # means two intervals can use the same room
                heapq.heapreplace(heap, i[1])
            else:
            # a new room is allocated
                heapq.heappush(heap, i[1])
        return len(heap)