class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        L = lcm(p,q)

        return 2 if (L//q)%2 == 0 else (L//p)%2