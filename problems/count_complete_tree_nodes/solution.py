# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left, right, l, r = root.left, root.right, 1, 1
        while left:
            left, l = left.left, l + 1
        while right:
            right, r = right.right, r + 1

        if l == r:
            return 2 ** l - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)