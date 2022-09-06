class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = []
        for rng in ranges:
            for i in range(rng[0], rng[1] + 1):
                if i not in covered:
                    covered.append(i)
        
        for j in range(left, right + 1):
            if j not in covered:
                return False
        
        return True
