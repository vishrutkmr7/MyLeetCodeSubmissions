class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_list = ["[","{","("]
        close_list = ["]","}",")"]

        for i in s: 
            if i in open_list: 
                stack.append(i)
            elif i in close_list: 
                pos = close_list.index(i)
                # compare with the top of the stack
                if stack and open_list[pos] == stack[-1]:
                    stack.pop()
                else: 
                    return False

        return not stack