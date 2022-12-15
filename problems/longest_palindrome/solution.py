class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        odd_count = sum(value % 2 == 1 for value in char_count.values())
        return len(s) if odd_count == 0 else len(s) - odd_count + 1

        