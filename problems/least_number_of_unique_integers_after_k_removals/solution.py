class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hp = list(Counter(arr).values())
        heapify(hp)
        while k > 0:
            k -= heappop(hp)
        return len(hp) + (k < 0)