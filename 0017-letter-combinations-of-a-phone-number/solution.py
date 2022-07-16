class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "0": "",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def backtrack(index, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return
            for letter in mapping[digits[index]]:
                backtrack(index + 1, curStr + letter)

        if digits:
            backtrack(0, "")

        return result
