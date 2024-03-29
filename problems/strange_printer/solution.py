class Solution(object):
    def strangePrinter(self, s):
        cache = {}

        def solve(s):
            if not s:
                return 0
            if s in cache:
                return cache[s]

            cost = solve(s[:-1]) + 1

            char_to_insert = s[-1]
            for i, c in enumerate(s[:-1]):
                if c == char_to_insert:
                    cost = min(cost, solve(s[:i + 1]) + solve(s[i + 1:-1]))
            cache[s] = cost
            return cost

        return solve(s)