from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        counts = list(counts.most_common())
        counts.sort(key=lambda s:s[0])
        counts.sort(key=lambda s:s[1], reverse=True)
        return [k for k,v in counts][:k]
        