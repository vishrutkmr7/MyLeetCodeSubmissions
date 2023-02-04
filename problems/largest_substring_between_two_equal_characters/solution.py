class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = {}
        maxer = -1
        for i, val in enumerate(s):
            if val in dic:
                diff = i - dic[val] - 1
                maxer = max(maxer, diff)
            else:
                dic[val] = i
        return maxer