class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            sumN = sum(int(i)**2 for i in str(n))
            n = sumN
        return 1 in seen
