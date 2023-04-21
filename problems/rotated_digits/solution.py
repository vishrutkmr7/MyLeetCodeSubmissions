class Solution:
    def rotatedDigits(self, n: int) -> int:
        return sum(bool(self.isFlippable(i)) for i in range(1, n + 1))

    def isFlippable(self, num: int) -> bool:
        flippable = False
        while num > 0:
            digit = num % 10
            if digit in [3, 4, 7]:
                return False
            if digit in [2, 5, 6, 9]:
                flippable = True
            num //= 10
        return flippable