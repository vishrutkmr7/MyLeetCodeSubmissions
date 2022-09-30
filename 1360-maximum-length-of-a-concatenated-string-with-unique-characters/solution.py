class Solution:
    def maxLength(self, words: List[str]) -> int:
        dp = [set()]
        for word in words:
            if len(set(word)) < len(word):
                continue
            word = set(word)
            dp.extend(word | entry for entry in dp[:] if not word & entry)
        return max(len(word) for word in dp)
