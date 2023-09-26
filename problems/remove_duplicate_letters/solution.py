class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = Counter(s)
        visited = set()

        for char in s:
            counter[char] -= 1
            
            if char in visited:
                continue
            
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                visited.remove(stack.pop())
            
            stack.append(char)
            visited.add(char)
        
        return ''.join(stack)