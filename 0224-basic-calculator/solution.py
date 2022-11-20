class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        res = 0
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+":
                res += sign * num
                sign = 1
                num = 0
            elif c == "-":
                res += sign * num
                sign = -1
                num = 0
            elif c == "(":
                stack.extend((res, sign))
                sign = 1
                res = 0
            elif c == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + sign * num

