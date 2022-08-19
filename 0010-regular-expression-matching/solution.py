class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        dp[0][0] = True
        
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 2][0]
            for j in range(1, m + 1):
                if p[i - 1] in {s[j - 1], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = (p[i - 2] in {s[j - 1], '.'} and dp[i][j - 1]) or dp[i - 2][j]
					
        return dp[n][m]
