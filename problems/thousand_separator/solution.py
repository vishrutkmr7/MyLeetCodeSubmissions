class Solution:
    def thousandSeparator(self, num: int) -> str:
        num = str(num)
        num = num[::-1]
        res = ""
        for i, digit in enumerate(num):
            if i % 3 == 0 and i != 0:
                res += "."
            res += digit
        return res[::-1]