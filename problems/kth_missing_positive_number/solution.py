class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        class Count(object):
            def __getitem__(self, i):
                return arr[i] - i - 1

        return k + bisect.bisect_left(Count(), k, 0, len(arr))