class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        m = min(arr)
        diff = (max(arr) - m) / (len(arr) - 1)
        if diff == 0:
            return True
        s = {num - m for num in arr}
        return len(s) == len(arr) and all(gap % diff == 0 for gap in s)
