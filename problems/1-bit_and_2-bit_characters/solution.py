class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        res = True
        for bit in bits[-2::-1]:
            if bit:
                res = not res
            else:
                break
        return res