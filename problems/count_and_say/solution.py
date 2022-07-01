class Solution:
    
    def say(self, n:str) -> str:
        res = ""
        stack = []
        for digit in map(int, n):
            if len(stack) == 0:
                stack.append(digit)
                continue

            if stack[-1] != digit:
                res += str(len(stack)) + str(stack[-1])
                stack = []

            stack.append(digit)

        return res + str(len(stack)) + str(stack[-1])
        
        
    def countAndSay(self, n: int) -> str:
        # Base
        if n == 1:
            return "1"
        said = "1"
        for _ in range(1, n):
            said = self.say(said)

        return said
            
        
        