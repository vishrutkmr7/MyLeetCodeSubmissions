class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = 2**32 + num
        hex_map = "0123456789abcdef"
        hex_string = ""
        while num > 0:
            hex_string = hex_map[num % 16] + hex_string
            num //= 16
        return hex_string