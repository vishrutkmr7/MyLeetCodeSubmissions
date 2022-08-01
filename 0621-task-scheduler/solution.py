class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = Counter(tasks)
        maxfreq = max(hashMap.values())
        count = list(hashMap.values()).count(maxfreq)
        
        return max(maxfreq + (maxfreq-1)*n + count - 1, len(tasks))
        
        
        
