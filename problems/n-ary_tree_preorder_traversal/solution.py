"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack=[]
        final=[]
        if(not root):
            return None
        stack.append(root)
        while(stack):
            node=stack.pop()
            final.append(node.val)
            for i in range(len(node.children)-1, -1, -1):
                stack.append(node.children[i])
        return final