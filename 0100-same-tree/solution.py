# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if tree1 is None and tree2 is None:
            return True
        elif tree1 is None or tree2 is None or tree1.val != tree2.val:
            return False
        else:
            return self.isSameTree(tree1.left, tree2.left) and self.isSameTree(
                tree1.right, tree2.right
            )
        
