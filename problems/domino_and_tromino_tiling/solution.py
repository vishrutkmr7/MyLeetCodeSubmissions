
class Solution:
    def numTilings(self, n: int) -> int:
        def numTilingsDomino(N):
            if N in cacheD:
                return cacheD[N]
            if N <= 2:
                return N if N > 0 else 1
            cacheD[N] = (
                numTilingsDomino(N - 2)
                + numTilingsDomino(N - 1)
                + (2 * numTilingsTromino(N - 1))
            ) % ((10 ** 9) + 7)
            return cacheD[N]

        def numTilingsTromino(N):
            if N in cacheT:
                return cacheT[N]
            if N <= 2:
                return 0 if N == 1 else 1
            cacheT[N] = (numTilingsDomino(N - 2) + numTilingsTromino(N - 1)) % (
                (10 ** 9) + 7
            )
            return cacheT[N]

        cacheD, cacheT = {}, {}
        return numTilingsDomino(n)
