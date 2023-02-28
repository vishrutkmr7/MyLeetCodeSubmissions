# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if root is None:
            return []

        subtrees = {}

        def traverse(root: Optional[TreeNode]) -> int:
            if root is None:
                return None

            left = traverse(root.left)
            right = traverse(root.right)
            node = (root.val, left, right)

            if node in subtrees:
                subtrees[node][1] = True
                return subtrees[node][0]
            else:
                subtree_id = len(subtrees)
                subtrees[node] = [subtree_id, False, root]
                return subtree_id

        traverse(root)

        return [subtree[2] for subtree in subtrees.values() if subtree[1] == True]
