class MedianFinder(object):
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        if len(self.minHeap) == len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))
        else:
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))

    def findMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
            return -self.maxHeap[0]
