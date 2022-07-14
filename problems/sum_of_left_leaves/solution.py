# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, tree: Optional[TreeNode]) -> int:
        if not tree:
            return 0
        if tree.left and not tree.left.left and not tree.left.right:
            return tree.left.val + self.sumOfLeftLeaves(tree.right)
        else:
            return self.sumOfLeftLeaves(tree.left) + self.sumOfLeftLeaves(tree.right)

        