class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [-1] * (len(s) + 1)
        st = set(dictionary)
        return self.find(0, s, st, dp)
    
    def find(self, idx, s, st, dp):
        if idx == len(s):
            return 0
        if dp[idx] != -1:
            return dp[idx]
        res = float('inf')
        for j in range(idx, len(s)):
            substr = s[idx:j + 1]
            if substr in st:
                res = min(res, 0 + self.find(j + 1, s, st, dp))
            else:
                res = min(res, j - idx + 1 + self.find(j + 1, s, st, dp))
        dp[idx] = res
        return res
        