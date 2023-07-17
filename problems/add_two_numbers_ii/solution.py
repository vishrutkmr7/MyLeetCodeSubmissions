# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1=''
        a2=''
        while l1:
            a1=a1+str(l1.val)
            l1=l1.next
        while l2:
            a2=a2+str(l2.val)
            l2=l2.next
        a1=int(a1)+int(a2)
        a1=str(a1)
        c=h=ListNode(a1[0])
        for i in a1[1:]:
            tem=ListNode(i)
            c.next=tem
            c=c.next
        return h