class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        lines = [''] * numRows
        period = 2*numRows - 2
        half_period = period //2
        for i in range(len(s)):
            line_num = abs(abs((i % period) - half_period) - half_period)
            lines[line_num] += s[i]
        return ''.join(lines)