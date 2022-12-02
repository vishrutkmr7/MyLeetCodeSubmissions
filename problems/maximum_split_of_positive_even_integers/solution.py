class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        if finalSum % 2 == 1:
            return []
        
        n = set()
        total = 0
        for i in range(2, finalSum+1, 2):
            total += i
            n.add(i)
            if total == finalSum:
                return list(n)
            elif total >= finalSum:
                n.remove(total - finalSum)
                return list(n)