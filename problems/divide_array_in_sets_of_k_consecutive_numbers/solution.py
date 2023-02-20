class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(k)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True