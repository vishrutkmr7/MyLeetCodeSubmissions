"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # if root is None:
        #     return 0
        # if root.children is None:
        #     return 1
        # return 1 + max(self.maxDepth(child) for child in root.children)
        if(root==None):
            return 0
        
        q=collections.deque()
        q.append(root)
        level=0
        while(q):
            level+=1
            for i in range(len(q)):
                node=q.popleft()
                for i in node.children:
                    q.append(i)
        return level