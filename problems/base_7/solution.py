class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            return f"-{self.convertToBase7(-num)}"
        ans = ""
        while num:
            ans += str(num % 7)
            num //= 7
        return ans[::-1]
