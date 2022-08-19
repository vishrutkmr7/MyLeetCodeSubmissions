# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import itertools

class Solution(object):
        
    def addTwoNumbers(self, l1, l2):
        c=0
        s=0
        l = ListNode()
        n = l
        s1 = ''
        s2 = ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        s = int(s1[::-1]) + int(s2[::-1])
        t = 1
        for i in str(s)[::-1]:
            n.val = int(i)
            print(t)
            if t == len(str(s)):
                break
            t += 1
            n.next = ListNode()
            n = n.next
        return l