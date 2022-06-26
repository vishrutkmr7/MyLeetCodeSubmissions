# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, tree: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if tree is None:
            return
        self.flatten(tree.left)
        self.flatten(tree.right)
        if tree.left is not None:
            temp = tree.left
            while temp.right is not None:
                temp = temp.right
            temp.right = tree.right
            tree.right = tree.left
            tree.left = None
        return tree
        
