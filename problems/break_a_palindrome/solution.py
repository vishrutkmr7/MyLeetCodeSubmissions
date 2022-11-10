class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if(len(palindrome)==1):
            return ""
        return next(
            (
                f'{palindrome[:i]}a{palindrome[i + 1:]}'
                for i, c in enumerate(palindrome)
                if (c != 'a' and i * 2 + 1 != len(palindrome))
            ),
            f'{palindrome[:-1]}b',
        )