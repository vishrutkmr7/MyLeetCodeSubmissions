class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        m, n = len(str(k)), len(s)
        dp = [1] * (n + 1)
        # find out number of ways for each ending.
        for i in range(n):
            res, cur = 0, ""
            # For each ending digit i, we traves back, to find all the valid numbers which is no larger than k, and ending with this digit i.
            for idx in range(
                i, max(-1, i - m), -1
            ):  # In case we transpass the first digit.
                cur = s[idx] + cur
                if (
                    cur[0] != "0" and int(cur) <= k
                ):  # A number is valid if it has no leading zero and no larger than k.
                    res += dp[
                        idx
                    ]  # Whenever we have a valid ending number, we add the dp[idx] to dp[i].
            if res == 0:
                return 0
            else:
                dp[i + 1] = res % (10**9 + 7)
        return dp[-1]