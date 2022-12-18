class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        bunches = []
        start = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if i - start > 2:
                    bunches.append([start, i - 1])
                start = i
        if len(s) - start > 2:
            bunches.append([start, len(s) - 1])
        return bunches