class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            stone1 = stones.pop(0)
            stone2 = stones.pop(0)
            # if stone1 - stone2 != 0:
            stones.append(stone1 - stone2)
                
        return stones[0]
