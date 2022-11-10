# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0 #edge case 
        ans = 0
        queue = [(root, 0)]
        while queue: 
            ans = max(ans, queue[-1][1] - queue[0][1] + 1)
            temp = []
            for node, i in queue: 
                if node.left: temp.append((node.left, 2*i))
                if node.right: temp.append((node.right, 2*i+1))
            queue = temp
        return ans 
