class Solution:
    def numDecodings(self, s: str) -> int:
        dp={}
        def check(idx):
            if idx<len(s) and s[idx]=="0":
                return 0
            if idx>=len(s)-1:
                return 1
            if idx in dp:
                return dp[idx]
            if idx+1< len(s) and int(s[idx]+s[idx+1])<=26:
                dp[idx]=check(idx+1)+check(idx+2)
            else:
                dp[idx]=check(idx+1)
            return dp[idx]
        return check(0)
