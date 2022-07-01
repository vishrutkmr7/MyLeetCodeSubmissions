# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

INT_MAX = 4294967296
INT_MIN = -4294967296

class Solution:
    def isBSTUtil(self, root, min_int, max_int):
        if root is None:
            return True
        if root.val < min_int or root.val > max_int:
            return False
        return (self.isBSTUtil(root.left, min_int, root.val -1) and
          self.isBSTUtil(root.right, root.val+1, max_int))
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return (self.isBSTUtil(root, INT_MIN, INT_MAX))