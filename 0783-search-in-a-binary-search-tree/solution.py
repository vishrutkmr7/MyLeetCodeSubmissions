# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if val == root.val:
            return root
        elif val < root.val:
            return None if root.left is None else self.searchBST(root.left, val)
        else:
            return None if root.right is None else self.searchBST(root.right, val)
        
