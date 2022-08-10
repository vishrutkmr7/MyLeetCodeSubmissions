class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, minLeft, minLength = 0 , -1 , len(s) + 1
        count = Counter(t)
        required = len(t)
        
        for index,char in enumerate(s):
            count[char] -= 1
            if count[char] >= 0:
                required -= 1
            while required == 0:
                if index -l + 1 < minLength:
                    minLength = index - l + 1
                    minLeft = l
                count[s[l]] += 1
                if count[s[l]] > 0:
                    required +=1
                    
                l += 1
        return "" if minLeft == -1 else s[minLeft:minLeft+minLength]      
