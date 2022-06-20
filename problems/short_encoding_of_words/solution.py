class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        counter = Counter(word[i:] for word in words for i in range(len(word)))
        return sum(len(word)+1 for word in words if counter[word] == 1)