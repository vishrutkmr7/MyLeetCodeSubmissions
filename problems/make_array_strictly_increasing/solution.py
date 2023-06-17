class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1: 0}
        arr2.sort()
        for i in arr1:
            tmp = defaultdict(lambda: float("inf"))
            for key, val in dp.items():
                if i > key:
                    tmp[i] = min(tmp[i], val)
                loc = bisect_right(arr2, key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]], val + 1)
            dp = tmp
        return min(dp.values()) if dp else -1