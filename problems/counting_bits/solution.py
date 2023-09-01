class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            res.append(res[i >> 1] + i % 2) # The bit count of a number n is the bit count of n // 2 + the last bit of n

        return res