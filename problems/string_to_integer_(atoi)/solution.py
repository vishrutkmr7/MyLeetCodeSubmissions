class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        res = 0
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s):
            if s[i] == "-":
                sign = -1
                i += 1
            elif s[i] == "+":
                i += 1
        while i < len(s) and s[i].isdigit():
            res = (res * 10) + (ord(s[i]) - ord("0"))
            i += 1
        res = res * sign
        high = (2**31) - 1
        low = -(2**31)
        if res > high:
            res = high
        elif res < low:
            res = low
        return res
