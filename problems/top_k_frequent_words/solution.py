class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        return [x[0] for x in sorted(counts.items(), key=lambda x: (-x[1], x[0]))][:k]