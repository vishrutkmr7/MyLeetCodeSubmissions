# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def BST_array(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        return self.BST_array(root.left) + [root.val] + self.BST_array(root.right)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        values = self.BST_array(root)
        return sum(val for val in values if low <= val <= high)
        
