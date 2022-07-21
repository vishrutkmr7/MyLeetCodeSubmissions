# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        p, slow, fast = None, head, head
        
        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
            
        p.next = None
        
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, l1, l2):
        dummy = ListNode(None)
        cur = dummy
        
        while l1 and l2:
            if l1.val > l2.val:
                cur.next, l2 = l2, l2.next
            else:
                cur.next, l1 = l1, l1.next
            cur = cur.next
            
        if l1:
            cur.next=l1
        if l2:
            cur.next=l2
        return dummy.next
    
