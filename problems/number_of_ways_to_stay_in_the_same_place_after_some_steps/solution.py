class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if steps is None or steps < 0 or not arrLen:
            return 0
        memo = {}
        return self.dfs(steps, arrLen, 0, memo)

    def dfs(self, steps, arrLen, pos, memo):
        if (steps, pos) in memo:
            return memo[(steps, pos)]
        if pos < 0 or pos > arrLen - 1:
            memo[(steps, pos)] = 0
            return 0
        if steps == 0:
            return 1 if pos == 0 else 0
        memo[(steps, pos)] = self.dfs(steps - 1, arrLen, pos - 1, memo) + self.dfs(steps - 1, arrLen, pos, memo) \
                         + self.dfs(steps - 1, arrLen, pos + 1, memo) 
        return memo[(steps, pos)] % (10 ** 9 + 7)
        