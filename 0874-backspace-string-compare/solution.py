class Solution:
    def prep_stack(self, string):
        """Using stack for this problem."""
        stack = []
        for char in string:
            if char == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.prep_stack(s) == self.prep_stack(t)
        
