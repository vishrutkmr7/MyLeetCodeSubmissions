class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [
                i
                for i in range(left, right + 1)
                if all(int(digit) != 0 and i % int(digit) == 0 for digit in str(i))
            ]