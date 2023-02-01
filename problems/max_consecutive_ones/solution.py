class Solution:
    def findMaxConsecutiveOnes(self, bits: List[int]) -> int:
        count = 0
        max_count = 0
        for bit in bits:
            if bit == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)