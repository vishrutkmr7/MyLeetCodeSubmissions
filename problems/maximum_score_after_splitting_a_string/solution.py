class Solution:
    def maxScore(self, binary: str) -> int:
        start, end = 0, len(binary)
        left = right = ""
        for i in range(1, end):
            left, right = binary[:i], binary[i:]
            count_0 = left.count("0")
            count_1 = right.count("1")
            start = max(start, count_0 + count_1)
        return start