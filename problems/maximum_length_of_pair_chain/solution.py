class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        count = 0
        prev = float("-inf")
        for pair in pairs:
            if pair[0] > prev:
                count += 1
                prev = pair[1]
        return count