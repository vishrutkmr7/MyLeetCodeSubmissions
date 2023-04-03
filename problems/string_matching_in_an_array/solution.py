class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = {
            words[i]
            for i, j in itertools.product(range(len(words)), range(len(words)))
            if i != j and words[i] in words[j]
        }
        return list(substrings)