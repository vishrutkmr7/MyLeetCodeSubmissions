class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls,cow = 0,0
        s = list(secret)
        g = list(guess)
        i,j=0,0
        while i<len(secret):
            if s[j]==g[j]:
                bulls+=1
                s.pop(j)
                g.pop(j)
            else:
                j+=1
            i+=1
        count = Counter(s)
        for char in g:
            if char in count and count[char]>0:
                cow+=1
                count[char]-=1
        return f'{bulls}A{cow}B'