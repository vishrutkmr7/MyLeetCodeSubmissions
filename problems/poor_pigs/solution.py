class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        res = 0
        time = minutesToTest / minutesToDie + 1
        while time ** res < buckets:
            res += 1
        
        return res