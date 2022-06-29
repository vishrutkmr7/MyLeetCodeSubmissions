# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root, 0)]
        result = []
        total_level = 0
        if not root: return []
        while queue:
            node, level = queue.pop(0)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1)) 
            if not result:
                result.append([node.val])
            else:
                if total_level < level:
                    result.append([node.val])
                else:
                    result[-1].append(node.val)
            total_level = max(level, total_level)
        return result
        

