# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def helper(root):
            if not root:
                return True
            left = helper(root.left)
            right = helper(root.right)
            if left and right:
                if root.left and root.left.val != root.val:
                    return False
                if root.right and root.right.val != root.val:
                    return False
                self.count += 1
                return True
            return False

        helper(root)

        return self.count