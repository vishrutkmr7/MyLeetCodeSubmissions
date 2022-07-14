# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leaf_sequence(self, tree):
        if not tree:
            return []
        if tree.left or tree.right:
            return self.get_leaf_sequence(tree.left) + self.get_leaf_sequence(tree.right)
        else:
            return [tree.val]
        
    def leafSimilar(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if tree1 or tree2:
            return self.get_leaf_sequence(tree1) == self.get_leaf_sequence(tree2)
        else:
            return True
        
