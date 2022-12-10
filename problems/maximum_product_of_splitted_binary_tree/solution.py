# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return root.val + self.sum(root.left) + self.sum(root.right)
    
    def updateMax(self, x: int) -> None:
        self.currentMax = max(self.currentMax, (x * (self.total - x)))
    
    def dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            # leaf node
            self.updateMax(node.val)
            return node.val
        currentSum = node.val + self.dfs(node.left) + self.dfs(node.right)
        self.updateMax(currentSum)
        return currentSum
    
    def maxProduct(self, root: TreeNode) -> int:
        self.total = self.sum(root)
        self.currentMax = 0
        self.dfs(root.left)
        self.dfs(root.right)
        return self.currentMax % (10**9 + 7)