class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        seen = {0: -1}
        res, cur = 0, 0
        for i, c in enumerate(s):
            if c in vowels:
                cur ^= 1 << vowels[c]
            if cur not in seen:
                seen[cur] = i
            else:
                res = max(res, i - seen[cur])
        return res