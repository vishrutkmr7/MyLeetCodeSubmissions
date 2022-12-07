class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        result = ""
        for i, v in enumerate(s[::-1]):
            if i % k == 0 and i != 0:
                result += "-"
            result += v
        return result[::-1]