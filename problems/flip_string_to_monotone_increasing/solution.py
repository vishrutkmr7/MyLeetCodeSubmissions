class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        @cache
        def dp(i, last):
            if i == len(s): return 0  # Reach to the end
            d = ord(s[i]) - ord('0')
            cand = []
            if d >= last: cand.append(dp(i + 1, d))  # Don't flip
            if 1 - d >= last: cand.append(dp(i + 1, 1 - d) + 1)  # Flip
            return min(cand)  # Choose the minimum number of flips

        return dp(0, 0)