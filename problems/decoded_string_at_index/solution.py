class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        lens, n = [0], len(s)
        for c in s:
            if c.isdigit():
                lens.append(lens[-1] * int(c))
            else:
                lens.append(lens[-1] + 1)
                
        for i in range(n, 0, -1):
            k %= lens[i]
            if k == 0 and s[i - 1].isalpha():
                return s[i - 1]
        