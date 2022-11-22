class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        res = ""
        i = 0
        while i < cols:
            j = i
            while j < n:
                res += encodedText[j]
                j += cols + 1
            i += 1
        
        return res.rstrip()
