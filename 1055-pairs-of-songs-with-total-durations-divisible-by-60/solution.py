class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dp = [0] * 60
        count = 0
        for i in enumerate(time):
            temp = time[i[0]] % 60
            count += dp[-temp % 60]
            dp[temp] += 1
        return count
