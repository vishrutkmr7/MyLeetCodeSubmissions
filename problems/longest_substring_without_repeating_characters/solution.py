class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        start = 0
        maxL = 0
        for ch in s:
            if ch not in curr:
                curr.add(ch)
            else:
                maxL = max(maxL, len(curr))
                while s[start] != ch:
                    curr.remove(s[start])
                    start += 1
                start += 1

        return max(maxL, len(curr))