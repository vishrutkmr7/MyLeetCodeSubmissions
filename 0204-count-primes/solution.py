class Solution:
    def countPrimes(self, n: int) -> int:
        if n in {0, 1, 2}:
            return 0

        pf = [True] * (n + 1)
        pf[0], pf[1] = False, False
        i = 2
        while i**2 < n:
            if pf[i]:
                j = i**2
                while j < n:
                    pf[j] = False
                    j = j + i

            i += 1
        count = sum(1 for k in range(1, len(pf)) if pf[k])
        return count - 1
