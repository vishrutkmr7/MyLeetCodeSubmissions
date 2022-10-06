from sortedcontainers import SortedList
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.containers = defaultdict(SortedList)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.containers[key].add((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        idx = self.containers[key].bisect_left((timestamp, "|"))
        return self.containers[key][idx - 1][1] if idx != 0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)