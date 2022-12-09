# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root, float("-inf"), float("inf"))

    def DFS(self, root: Optional[TreeNode], maxV: int, minV: int) -> int:
        if root is None:
            return 0
        maxVal = max(maxV, root.val)
        minVal = min(minV, root.val)
        return (
            maxVal - minVal
            if root.left == root.right
            else max(
                self.DFS(root.left, maxVal, minVal),
                self.DFS(root.right, maxVal, minVal),
            )
        )