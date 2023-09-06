# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        length = 0
        while curr is not None:
            curr = curr.next
            length += 1
        quotient, remainder = divmod(length,k)
        curr = head
        final_array = []
        for i in range(k):
            temp = curr
            for j in range(quotient + (i < remainder) - 1):
                if curr:
                    curr = curr.next
            if curr:
                x = curr.next
                curr.next = None
                curr = x
            final_array.append(temp)
        return final_array
        