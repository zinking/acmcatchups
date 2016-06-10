"""
Problem:Given a binary search tree, please check whether there are two nodes in it whose sum equals a given value.
"""

class Node(object):
    def __init__(self,x,p):
        self.x = x
        self.p = p
        self.l = None
        self.r = None

    def prev(self):
        #if node has left child
        if self.l is not None:
            return self.l
        else:
            p = self.p
            c = self
            while p is not None and c == p.l:
                c = p
                p = p.p
            return p

    def next(self):
        if self.r is not None:
            return self.r
        else:
            p = self.p
            c = self
            while p is not None and c == p.r:
                c = p
                p = p.p
            return p

class Tree(object):
    def __init__(self, arr):
        n = len(arr)
        if n == 0:
            self.root = None
        else:
            root = Node(arr[0],None)
            for i in range(1,n):
                self.insert(root,arr[i])
            self.root = root

    def insert(self, root,x):
        if (x<=root.x):
            if root.l is None:
                root.l = Node(x,root)
            else:
                self.insert(root.l, x)
        else:
            if root.r is None:
                root.r = Node(x,root)
            else:
                self.insert(root.r, x)

    def min(self):
        m = self.root
        while m.l is not None: m = m.l
        return m

    def max(self):
        m = self.root
        while m.r is not None: m = m.r
        return m



def nodesSum(l, r, x):
    if l.x + r.x == x:
        print "l:",l.x,"r:",r.x
        return 1
    if l.x + r.x < x:
        #try enlarge
        nl = l.next()
        if nl is None:
            return -1
        else:
            return nodesSum(nl,r,x)
    else:
        #try smallre
        pr = r.prev()
        if pr is None:
            return -1
        else:
            return nodesSum(l,pr,x)


def nodesSumBST(arr,x):
    root = Tree(arr)
    l = root.min()
    r = root.max()
    return nodesSum(l,r,x)

def runTest(t,e):
    (arr,x) = t
    a = nodesSumBST(arr,x)
    if a == e:
        print "succss"
    else:
        print "fail:",t,"expected:",e,"actual:",a

def runTests():
    t1 = ([5,4,1,3,2],7)
    e1 = 1
    runTest(t1,e1)

    t1 = ([4,1,3,2],7)
    e1 = 1
    runTest(t1,e1)

    t1 = ([5,4,1,3,2],11)
    e1 = -1
    runTest(t1,e1)



if __name__ == "__main__":
    runTests()
