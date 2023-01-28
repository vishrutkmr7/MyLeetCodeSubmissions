class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.seen = set()

    def addNum(self, val: int) -> None:
        if val not in self.seen:
            self.seen.add(val)
            heapq.heappush(self.intervals, [val, val])

    def getIntervals(self) -> list[list[int]]:
        result = []
        while self.intervals:
            interval = heapq.heappop(self.intervals)
            if not result or result[-1][1] < interval[0] - 1:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        self.intervals = result
        return result
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()