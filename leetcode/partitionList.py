# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None: return None
        d1 = ListNode(-1)
        p1 = d1
        d2 = ListNode(-2)
        p2 = d2
        d3 = ListNode(-3)
        p3 = d3
        p = head
        while p is not None:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            elif p.val == x:
                p3.next = p
                p3 = p3.next
            elif p.val > x:
                p2.next = p
                p2 = p2.next
            p = p.next
        p1.next = d3.next
        p3.next = d2.next
        p2.next = None
        return d1.next

solver = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l2.next = l1
n1 = solver.partition(l2,1)
while n1 is not None:
    print n1.val
    n1 = n1.next
