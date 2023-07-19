class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, count = float("-inf"), 0
        for start, finish in sorted(intervals, key=lambda x:x[1]):
            if start >= end:
                end = finish
            else:
                count += 1

        return count
