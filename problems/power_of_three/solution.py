class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>=1 and 3**20%n==0