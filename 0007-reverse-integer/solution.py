class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -int(str(-x)[::-1]) if -int(str(-x)[::-1]) >= -(2**31) else 0
        return int(str(x)[::-1]) if int(str(x)[::-1]) <= 2**31 - 1 else 0
