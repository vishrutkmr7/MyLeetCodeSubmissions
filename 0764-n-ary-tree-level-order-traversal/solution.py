"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        hashMap = {}
        queue = [(root, 0)] if root else []
        while queue:
            node, lvl = queue.pop(0)
            hashMap[lvl] = hashMap.get(lvl,[]) + [node.val]
            queue.extend((child, lvl+1) for child in node.children)
                
        return list(hashMap.values())
        
