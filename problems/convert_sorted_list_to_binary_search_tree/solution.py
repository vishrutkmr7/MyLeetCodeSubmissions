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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def convertToArray(head):
            arr = []
            while head is not None:
                arr.append(head.val)
                head = head.next
            return arr

        def dfs(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(arr[mid])
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        arr = convertToArray(head)
        return dfs(0, len(arr) - 1)