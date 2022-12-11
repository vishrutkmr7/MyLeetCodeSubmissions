class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        return all(d.get(n) == num[~i] for i, n in enumerate(num))