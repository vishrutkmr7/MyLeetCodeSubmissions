class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        prev = 0
        curr = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                count += min(prev, curr)
                prev = curr
                curr = 1
        return count + min(prev, curr)