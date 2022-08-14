class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operator = ""
        num =""
        for i,c in enumerate(s):
            if '0' <= c <= '9':
                num += c
            
            if c == '+' or c == '*' or c == '-' or c == '/' or i == len(s) - 1:
                if operator == "":
                    stack.append(int(num))     
                if operator == '+': 
                    stack.append(int(num))        
                if operator == '*':
                    stack.append(stack.pop()*int(num))         
                if operator == '-':
                    stack.append(-1*int(num))
                if operator == '/':
                    stack.append(int(stack.pop()/int(num)))
                    
                num = ""
                operator = c
        
        return sum(stack)