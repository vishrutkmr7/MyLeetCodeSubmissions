# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        
        def height(node):
            nonlocal ans
            if not node:
                return -1
            
            left, right = height(node.left), height(node.right)
            ans = max(ans, 2 + left + right)
            
            return 1 + max(left,right)
        
        height(root)
        return ans