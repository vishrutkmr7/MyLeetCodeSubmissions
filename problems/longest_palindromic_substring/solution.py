class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        ans_l = 1
        dp = [[ i == j for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(i):
                if s[i] == s[j] and (j + 1 == i or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 >= ans_l:
                        ans_l = i - j + 1
                        ans = s[j: i+1]
        return ans