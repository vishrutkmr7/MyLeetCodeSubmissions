class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def rec(a, b):
            if(b == []):
                ans.append(a[:])
                return
            for i in range(len(b)):
                rec(a + [b[i]], b[:i] + b[i + 1:])
        rec([], nums)
        return ans
