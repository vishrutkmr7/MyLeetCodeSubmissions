# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def addRow(parent, val, depth):
            if parent is None:
                return
            if depth == 1:
                parent.left = TreeNode(val, parent.left)
                parent.right = TreeNode(val, None, parent.right)
            else:
                addRow(parent.left, val, depth - 1)
                addRow(parent.right, val, depth - 1)
        
        sentinel = TreeNode(-1, root)
        addRow(sentinel, val, depth)
        return sentinel.left
