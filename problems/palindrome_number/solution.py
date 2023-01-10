class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num < 0:
            return False
        original = num
        reverse = 0
        while num > 0:
            reverse = reverse * 10 + num % 10
            num //= 10
        return original == reverse