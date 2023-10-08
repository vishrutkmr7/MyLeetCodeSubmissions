class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(m + 1):
            dp[0][i] = -1e9

        for i in range(n + 1):
            dp[i][0] = -1e9

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                val = nums1[i - 1] * nums2[j - 1] + max(0, dp[i - 1][j - 1])
                dp[i][j] = max(val, max(dp[i - 1][j], dp[i][j - 1]))

        return dp[n][m]
        