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
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return -1
        arr = self.inorderTraversal(root)
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        max_val = max(d.values())
        mode = []
        for key, value in d.items():
            if value == max_val:
                mode.append(key)
        
        return mode
            
