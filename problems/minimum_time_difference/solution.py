class Solution:
    def findMinDifference(self, times: List[str]) -> int:
        times = [int(time[:2]) * 60 + int(time[3:]) for time in times]
        times.sort()
        times.append(times[0] + 1440)
        return min(times[i + 1] - times[i] for i in range(len(times) - 1))