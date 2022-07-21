# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(rt):
            if rt:
                rt.left,rt.right = rt.right,rt.left
                invert(rt.left)
                invert(rt.right)
        invert(root)
        return root