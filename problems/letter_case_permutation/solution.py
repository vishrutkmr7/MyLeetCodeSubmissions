class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        return list(set(map("".join, itertools.product(*zip(s.upper(), s.lower())))))