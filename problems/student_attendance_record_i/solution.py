class Solution:
    def checkRecord(self, s: str) -> bool:
        return False if s.count("A") > 1 else "LLL" not in s