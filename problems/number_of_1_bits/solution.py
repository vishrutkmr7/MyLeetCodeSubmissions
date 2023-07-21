class Solution:
    def hammingWeight(self, n: int) -> int:
        return list(bin(n)).count("1")