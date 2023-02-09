class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        A = [set() for _ in range(26)]
        for idea in ideas:
            A[ord(idea[0]) - ord('a')].add(idea[1:])
        
        ans = 0

        for i in range(25):
            for j in range(i + 1, 26):
                k = len(A[i] & A[j])
                ans += 2 * (len(A[i]) - k) * (len(A[j]) - k)
        return ans