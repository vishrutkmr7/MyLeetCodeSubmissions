class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # base case
        if n == 1:
            return "0"

        # calculate length of S_n
        l = 2**n - 1

        # recursion
        mid = l // 2 + 1
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            return str(1 - int(self.findKthBit(n - 1, l - k + 1)))