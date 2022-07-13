# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, tree: Optional[TreeNode]) -> List[str]:
        if not tree:
            return []
        result = []
        path = []
        self.root_to_leaf_helper(tree, path, result)
        return result
    
    def root_to_leaf_helper(self, tree, path, result):
        if not tree:
            return
        path.append(tree.val)
        if not tree.left and not tree.right:
            result.append('->'.join(map(str, path)))
        self.root_to_leaf_helper(tree.left, path, result)
        self.root_to_leaf_helper(tree.right, path, result)
        path.pop()
