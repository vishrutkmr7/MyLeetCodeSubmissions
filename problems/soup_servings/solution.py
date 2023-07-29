class Solution:
    memo = {}

    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1

        def prob(a, b):
            if (a, b) in self.memo:
                return self.memo[a, b]
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            self.memo[(a, b)] = 0.25 * (
                prob(a - 4, b)
                + prob(a - 3, b - 1)
                + prob(a - 2, b - 2)
                + prob(a - 1, b - 3)
            )
            return self.memo[(a, b)]

        n = math.ceil(n / 25.0)
        return prob(n, n)
