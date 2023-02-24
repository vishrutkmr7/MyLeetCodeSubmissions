class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dp = [(-1, -1)] * 26
        ans = cur = 0
        for e, i in enumerate(s):
            j = ord(i) - 65
            f, s = dp[j]
            dp[j] = (e, f)
            cur += e + s - 2 * f
            ans += cur
        return ans