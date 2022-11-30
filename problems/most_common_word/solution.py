class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        words = re.findall(r"\w+", paragraph.lower())
        return Counter(w for w in words if w not in ban).most_common(1)[0][0]