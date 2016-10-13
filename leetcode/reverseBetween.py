# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n: return head
        m1 = m-1
        n1 = n-m
        pm = head
        pmr = None
        while m1>0:
            if m1 == 1: pmr = pm
            pm = pm.next
            m1 -= 1
        pn = pm
        while n1>0:
            pn = pn.next
            n1 -= 1
        pn1 = pn.next
        pm0 = pm
        pm1 = pm0.next
        while pm0 != pn:
            pm0,pm1.next,pm1=pm1,pm0,pm1.next
        pm.next = pn1
        if pmr is not None: pmr.next = pm0
        if m == 1: head = pn
        return head

solver = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2

import pdb
pdb.set_trace()
nhead = solver.reverseBetween(n1,1,2)
while nhead:
    print nhead.val
    nhead = nhead.next
