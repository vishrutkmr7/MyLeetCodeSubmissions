class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i + 1 :]
                if new_word in dp:
                    dp[word] = max(dp[word], dp[new_word] + 1)
        return max(dp.values())