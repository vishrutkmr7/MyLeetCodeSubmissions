class Solution:
    def decodeString(self, s: str) -> str:
        def helper(cur):
            if len(cur) == 0: 
                return ''
            
            i, num, prefix, level, depth, start = 0, '', '', 0, 0, math.inf
            
            while i < len(cur) and 97 <= ord(cur[i]) <= 122: # letter 
                prefix += cur[i]
                i += 1
            while i < len(cur) and 48 <= ord(cur[i]) <= 58: # num
                num += cur[i]
                i += 1
                
            while i < len(cur): 
                if cur[i] == '[': 
                    level += 1 # tracks how many opening bracket I have 
                    depth = max(depth, level) # tracks how far I ever reached 
                    start = min(start, i + 1) # tracks where first opening bracket was 
                elif cur[i] == ']': 
                    level -= 1
                    if level == 0: 
                        if depth > 1: 
                            return prefix + helper(cur[start:i]) * int(num) + helper(cur[i+1:])
                        else: 
                            return prefix + cur[start:i] * int(num) + helper(cur[i+1:])
                i += 1
            return prefix
                    
        return helper(s)