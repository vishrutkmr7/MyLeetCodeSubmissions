# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, lst: Optional[ListNode]) -> Optional[ListNode]:
         if lst is None or lst.next is None:
            return None
         slow = lst
         fast = lst
         # Move ahead
         slow = slow.next
         fast = fast.next.next

         while fast and fast.next and slow != fast:
             slow = slow.next
             fast = fast.next.next

         if slow != fast:
             return None
         slow = lst

         while slow != fast:
             slow = slow.next
             fast = fast.next

         return slow
