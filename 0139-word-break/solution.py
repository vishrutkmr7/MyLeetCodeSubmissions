class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m, n = len(s), len(wordDict)
        dp = [False] * (m + 1)
        dp[0] = True
        for i in range(1, m + 1):
            for j in range(n):
                if (
                    dp[i - len(wordDict[j])]
                    and s[i - len(wordDict[j]) : i] == wordDict[j]
                ):
                    dp[i] = True
                    break
        return dp[m]
