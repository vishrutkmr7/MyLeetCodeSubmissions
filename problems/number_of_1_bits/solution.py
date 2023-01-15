class Solution:
    def hammingWeight(self, n: int) -> int:
        return list(str(bin(n))).count("1")