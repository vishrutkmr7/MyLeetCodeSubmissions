class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Newton Method
        r = num
        while r**2 > num:
            r = (r + num / r) // 2
        return r**2 == num
