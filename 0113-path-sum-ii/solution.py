# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(root, path):
            nonlocal result
            if not root:
                return []
            path += [root.val]
            if not root.left and not root.right and sum(path) == targetSum:
                result.append(path.copy())
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
            return result

        return dfs(root, [])
