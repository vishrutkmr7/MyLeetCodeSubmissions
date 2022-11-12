from sortedcontainers import SortedList


class MedianFinder(object):
    def __init__(self):
        self.data = SortedList()

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.data.add(num)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.data)
        return (self.data[n//2] + self.data[(n-1)//2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

