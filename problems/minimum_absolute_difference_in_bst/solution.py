# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res


    def min_difference_in_array(self, arr):
        min_diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] < min_diff:
                min_diff = arr[i] - arr[i - 1]
        return min_diff

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 0
        tree = self.inorderTraversal(root)
        return self.min_difference_in_array(tree)