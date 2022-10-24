class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return list(
            reduce(
                lambda acc, x: {**acc, x[0]: [x[1], *acc.get(x[0], [])]},
                ((tuple(sorted(s)), s) for s in strs),
                {},
            ).values()
        )
        