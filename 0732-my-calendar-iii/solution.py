from sortedcontainers import SortedList


class MyCalendarThree:

    def __init__(self):
        self.k=1
        self.events = SortedList()

    def book(self, start: int, end: int) -> int:
        self.events.add((start, 1))
        self.events.add((end, -1))

        active = 0

        for _,inc in self.events:
            active += inc
            self.k = max(self.k, active)
        
        return self.k
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
