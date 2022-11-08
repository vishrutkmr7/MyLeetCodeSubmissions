class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and ((s[i].isupper() and stack[-1].islower() and s[i].lower()==stack[-1]) or (s[i].islower() and stack[-1].isupper() and s[i]==stack[-1].lower())):
                stack.pop(-1)
            else:
                stack.append(s[i])
        return ''.join(stack)
