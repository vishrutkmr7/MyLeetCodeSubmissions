class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operator = ""
        num =""
        for i,c in enumerate(s):
            if '0' <= c <= '9':
                num += c

            if c == '+' or c == '*' or c == '-' or c == '/' or i == len(s) - 1:
                if operator == '*':
                    stack.append(stack.pop()*int(num))
                elif operator == '-':
                    stack.append(-1*int(num))
                elif operator == '/':
                    stack.append(int(stack.pop()/int(num)))

                elif operator in ["", '+']:
                    stack.append(int(num))
                num = ""
                operator = c

        return sum(stack)