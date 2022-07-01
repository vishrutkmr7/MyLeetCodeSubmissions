class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        marked = [False] * 256
        mapr = [-1] * 256

        for i in range(len(s)):
            if mapr[ord(s[i])] == -1:
                if marked[ord(t[i])] == True:
                    return False
                marked[ord(t[i])] = True
                mapr[ord(s[i])] = t[i]
            elif mapr[ord(s[i])] != t[i]:
                return False

        return True
    