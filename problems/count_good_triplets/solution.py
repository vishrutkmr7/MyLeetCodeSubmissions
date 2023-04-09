class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        C = list(combinations(arr, 3))
        C = [self.checkGood(x, a, b, c) for x in C]
        C = [x for x in C if x is not None]
        return len(C)

    def checkGood(self, tup, a, b, c):
        if (
            abs(tup[0] - tup[1]) <= a
            and abs(tup[0] - tup[2]) <= c
            and abs(tup[2] - tup[1]) <= b
        ):
            return tup
