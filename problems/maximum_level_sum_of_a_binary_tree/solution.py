# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        total, l, ans = float("-inf"), 1, 0
        q = [root]

        while len(q):
            n, s = len(q), 0

            for _ in range(n):
                temp = q.pop(0)
                s += temp.val
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            if s > total:
                total = s
                ans = l
            l += 1

        return ans
