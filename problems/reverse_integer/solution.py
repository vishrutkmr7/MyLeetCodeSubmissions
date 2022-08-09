class Solution:
    def reverse(self, x: int) -> int:
        if x < -1 * (2)**31 or x > 2**31 - 1:
            return 0

        s = ""
        x_s = str(x)
        if x < 0:
            x_s = x_s[1:]
        for idx, i in enumerate(x_s):
            if s and idx >= 9 and int(s) >= 147483647 and idx <= len(x_s) - 1 and int(x_s[idx])>= 2:
                return 0
            s = i + s
        return -1 * int(s) if x < 0 else int(s)