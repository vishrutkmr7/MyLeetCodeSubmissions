# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if root.left is None:
            if root.right is None:
                return []
            return [root.right.val] + self.getLonelyNodes(root.right)
        if root.right is None:
            return [root.left.val] + self.getLonelyNodes(root.left)
        return self.getLonelyNodes(root.left) + self.getLonelyNodes(root.right)