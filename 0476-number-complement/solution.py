class Solution:
    def findComplement(self, num: int) -> int:
        return int("".join(["1" if i == "0" else "0" for i in bin(num)[2:]]), 2)
