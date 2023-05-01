# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # Step 1: Traverse the linked list and count the occurrences of each value
        count = {}
        curr = head
        while curr:
            count[curr.val] = count.get(curr.val, 0) + 1
            curr = curr.next
        
        # Step 2: Find the values that appear more than once
        duplicates = set()
        for val, freq in count.items():
            if freq > 1:
                duplicates.add(val)
        
        # Step 3: Delete nodes with duplicate values
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            if curr.val in duplicates:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next