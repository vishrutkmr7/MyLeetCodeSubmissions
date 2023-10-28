class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[1] * 5] + [[0] * (5) for _ in range(n - 1)]
        mod = math.pow(10, 9) + 7
        for i in range(1, n):
            # For vowel a
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % mod
            # For vowel e
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % mod
            # For vowel i
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % mod
            # For vowel o
            dp[i][3] = (dp[i - 1][2]) % mod
            # For vowel u
            dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % mod
            
        return int(sum(dp[-1]) % mod)