# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, lst: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = lst
        slow = lst

        for _ in range(n):
            fast = fast.next

        if not fast:
            return lst.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return lst
        
