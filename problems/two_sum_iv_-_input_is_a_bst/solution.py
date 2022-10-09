# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash_set = set()
        def target_sum(node , target):
            if not node:
                return False
            if node.val in hash_set:
                return True
            else:
                hash_set.add(target-node.val)
            return target_sum(node.left , k) or target_sum(node.right , k)
            
        return target_sum(root, k)