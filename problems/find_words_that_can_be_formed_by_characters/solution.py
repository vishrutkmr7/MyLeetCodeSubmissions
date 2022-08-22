class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char=set(chars)
        count=0
        for i in words:
            for j in i:
                if(chars.count(j)<i.count(j)):
                    break
            else:
                count+=len(i)
        return count