class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n > 0 and 4**int(math.log(n, 4)) == n)
