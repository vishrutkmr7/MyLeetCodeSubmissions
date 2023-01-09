class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        for i in words[0]:
            if all(i in word for word in words):
                result.append(i)
                words = [word.replace(i, "", 1) for word in words]
        return result