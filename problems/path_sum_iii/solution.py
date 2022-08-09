# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0

        stack = [(root, [root.val])]
        num = 0

        while stack:
            n, sums = stack.pop()
            num += len([s for s in sums if s == targetSum])

            if n.left: stack.append((n.left, [s + n.left.val for s in sums] + [n.left.val]))
            if n.right: stack.append((n.right, [s + n.right.val for s in sums] + [n.right.val]))

        return num