class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(c):
            while roots[c] != c:
                c = roots[c]
                
            return c
        
        roots = list(range(26))
        for c1, c2 in zip(s1, s2):
            r1 = find(ord(c1) - ord('a'))
            r2 = find(ord(c2) - ord('a'))
            if r1 > r2:
                r1, r2 = r2, r1

            roots[r2] = r1
        
        return "".join(chr(ord('a') + find(ord(c) - ord('a'))) for c in baseStr)