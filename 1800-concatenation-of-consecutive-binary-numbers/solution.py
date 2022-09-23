class Solution:
    def concatenatedBinary(self, n: int) -> int:
        bin_str = "".join(bin(i)[2:] for i in range(1, n + 1))
        return int(bin_str, 2) % (10 ** 9 + 7)
