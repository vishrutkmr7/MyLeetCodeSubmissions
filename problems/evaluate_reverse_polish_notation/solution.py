class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "*": lambda x,y: x*y,
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "/": lambda x,y: float(x)/y
        }

        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                result = operations[token](left, right)
                stack.append(int(result))
        return stack.pop()