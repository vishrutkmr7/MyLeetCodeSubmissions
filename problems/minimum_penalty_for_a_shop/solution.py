class Solution:
    def bestClosingTime(self, customers: str) -> int:
        h = m = s = 0
        for i, ch in enumerate(customers):
            s += (ch == "Y") * 2 - 1
            if s > m:
                m, h = s, i + 1

        return h