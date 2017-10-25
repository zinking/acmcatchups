# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head):
    r = []
    i = 0
    while head:
        r.append(head.val)
        head = head.next
        i+=1
        if i > 20: break
    print r

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        h1 = ListNode(-1)
        h2 = ListNode(-2)
        
        c1 = h1
        c2 = None
        
        n = 0
        q = head
        r = q.next if q is not None else None
        while q is not None:
            n += 1
            if n%2 == 1:
                c1.next = q
                c1 = c1.next
            else:
                q.next = c2
                c2 = q
            q = r
            r = q.next if q is not None else None
        c1.next = None
        h2.next = c2
        p = h1.next
        q = h2.next
        pp = None
        qq = None
        import pdb
        pdb.set_trace()
        while p and q:
            pp = p.next
            qq = q.next
            p.next = q
            q.next = pp
            p = pp
            q = qq
        #q.next = pp

        
        return h1.next

ls = map(lambda x:ListNode(x), range(0,10))
for i in range(5):
    ls[i].next = ls[i+1]

solver = Solution()

r = solver.reorderList(ls[1])
printList(r)

