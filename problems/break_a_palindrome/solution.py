class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if(len(palindrome)==1):
            return ""
        for i,c in enumerate(palindrome):
            if(c != 'a' and i*2+1!=len(palindrome)):
                return palindrome[:i]+'a'+palindrome[i+1:]
        return palindrome[:-1]+'b'