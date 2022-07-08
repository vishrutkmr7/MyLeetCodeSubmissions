from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        counts = [(k, v) for k,v in counts.most_common()]
        counts.sort(key=lambda s:s[0])
        counts.sort(key=lambda s:s[1], reverse=True)
        return [k for k,v in counts][0:k]
        