# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head

        current = head
        while current:
            for _ in range(m - 1):
                if current:
                    current = current.next

            if not current:
                break

            temp = current.next
            for _ in range(n):
                if temp:
                    temp = temp.next

            current.next = temp
            current = temp

        return head
