# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return (
            self.dfs(head, root)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
            if root
            else False
        )

    def dfs(self, head, root):
        if not head:
            return True
        if not root or root.val != head.val:
            return False
        return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)