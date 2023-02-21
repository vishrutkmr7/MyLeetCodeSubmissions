class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            flag = all(word.count(i) <= chars.count(i) for i in word)
            if flag:
                count += len(word)
        return count