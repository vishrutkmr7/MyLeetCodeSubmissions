class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(
            any(strs[i][j] < strs[i - 1][j] for i in range(1, len(strs)))
            for j in range(len(strs[0]))
        )