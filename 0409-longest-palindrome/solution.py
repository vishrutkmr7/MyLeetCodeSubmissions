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
                
        if len(stack) == 0:
            return count
        return count + 1
        
