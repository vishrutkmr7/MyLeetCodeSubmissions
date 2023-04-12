class Solution:
    def canConvert(self, s: str, t: str) -> bool:
        if s == t:
            return True
        dp = {}
        return next(
            (False for i, j in zip(s, t) if dp.setdefault(i, j) != j),
            len(set(t)) < 26,
        )