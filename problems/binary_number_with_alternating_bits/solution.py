class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return all(n >> i & 1 != n >> i + 1 & 1 for i in range(len(bin(n)) - 3))