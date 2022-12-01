class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        vowels = set("aeiou")
        a = b = 0
        for i in range(len(s) // 2):
            if s[i] in vowels:
                a += 1
            if s[-i - 1] in vowels:
                b += 1
        return a == b