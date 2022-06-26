# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, tree: 'TreeNode', a: 'TreeNode', b: 'TreeNode') -> 'TreeNode':
        if tree is None:
            return None
        if tree in [a, b]:
            return tree
        left = self.lowestCommonAncestor(tree.left, a, b)
        right = self.lowestCommonAncestor(tree.right, a, b)
        if left and right:
            return tree
        return left or right