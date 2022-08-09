class Solution:
    def longestPalindrome(self, s: str) -> int:
        stack = []
        count = 0
        for ch in s:
            if ch in stack:
                stack.remove(ch)
                count += 2
            else:
                stack.append(ch)

        return count + 1 if stack else count
        