# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if m > n:
            return head
        prev = None
        curr = head
        i = 1
        while curr is not None and i < m:
            prev = curr
            curr = curr.next
            i = i + 1
            
        start = curr
        end = None
        
        while curr is not None and i <= n:
            next = curr.next
            curr.next = end
            end = curr
            curr = next
            i = i + 1
            
        if start:
            start.next = curr
            if prev is None:        # when m = 1, `prev` is None
                head = end
            else:
                prev.next = end
                
        return head
        
        
