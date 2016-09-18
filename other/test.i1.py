
class Node(object):
    def __init__(self,val):
        self.l = None
        self.r = None
        self.n = None
        self.v = val

def levelTraversal(node):
    def connectToNeighbor(node):
        if (node is None): return
        if (node.n is not None): connectToNeighbor(node.n)
        if (node.l is not None):
            if (node.r is not None):
                node.l.n = node.r
                node.r.n = getNeighborMostLeftChild(node)
            else:
                node.l.n = getNeighborMostLeftChild(node)
            connectToNeighbor(node.l)
        elif (node.r is not None):
            node.r.n = getNeighborMostLeftChild(node)
            connectToNeighbor(node.r)
        else:
            nl = getNeighborMostLeftChild(node)
            connectToNeighbor(nl)
    def getNeighborMostLeftChild(node):
        nb = node.n
        while (nb is not None):
            if nb.l is not None:
                return nb.l
            elif nb.r is not None:
                return nb.r
            nb = nb.n
        return None

    def getMostLeftChild(node):
        nb = node
        while (nb is not None):
            if nb.l is not None:
                return nb.l
            elif nb.r is not None:
                return nb.r
            nb = nb.n
        return None

    #import pdb
    #pdb.set_trace() 
    connectToNeighbor(node)
    #concat level ends
    nd = node
    ml = getMostLeftChild(node)
    while ml is not None:
        nd.n = ml
        while nd.n is not None: nd = nd.n
        ml = getMostLeftChild(ml)

    r = []
    nd2 = node
    while nd2 is not None:
        r.append(nd2.v)
        nd2 = nd2.n
    return r


def runT1Test(t,e):
    a = levelTraversal(t)
    if a == e :
        print "pass"
    else:
        print "fail:",t,"expected:",e,"actual:",a

def runT1Tests():
    nds = [Node(i) for i in range(4)]
    nds[2].l = nds[1]
    nds[2].r = nds[3]
    t1 = nds[2]
    e1 = [2,1,3]
    runT1Test(t1,e1)

    nds = [Node(i) for i in range(4)]
    nds[1].l = nds[2]
    nds[2].l = nds[3]
    t2 = nds[1]
    e2 = [1,2,3]
    runT1Test(t2,e2)

    nds = [Node(i) for i in range(6)]
    nds[1].l = nds[2]
    nds[1].r = nds[3]
    nds[2].l = nds[4]
    nds[3].r = nds[5]
    t3 = nds[1]
    e3 = [1,2,3,4,5]
    runT1Test(t3,e3)

    runT1Test(None, [])

    nds = [Node(i) for i in range(6)]
    nds[1].l = nds[2]
    nds[1].r = nds[3]
    nds[2].l = nds[4]
    nds[3].l = nds[5]
    t4 = nds[1]
    e4 = [1,2,3,4,5]
    runT1Test(t4,e4)

    nds = [Node(i) for i in range(6)]
    nds[5].l = nds[2]
    nds[5].r = nds[3]
    nds[2].r = nds[4]
    nds[3].l = nds[1]
    t4 = nds[5]
    e4 = [5,2,3,4,1]
    runT1Test(t4,e4)


    

    
def findExtraElement(i1,i2):
    adder = lambda x,y:x+y
    s1 = reduce(adder, map(ord,i1)) if len(i1) > 0 else 0
    s2 = reduce(adder, map(ord,i2)) if len(i2) > 0 else 0
    return chr(s2-s1) if s2>s1 else chr(s1-s2)

def runT2Test(t,e):
    (i1,i2) = t
    a = findExtraElement(i1,i2)
    if a == e:
        print "pass"
    else:
        print "failure:",t,"expected:",e,"actual:",a

def runT2Tests():
    t1 = ("", "a")
    e1 = "a"
    runT2Test(t1,e1)
    runT2Test(("a",""),"a")
    runT2Test(("abcdef","badcfeg"),"g")
    #randomly test 10 cases
    for i in range(10):
        import random
        n = random.randint(0,10)
        a = random.sample("abcdefghijklmnABCDEFG",n)
        b = random.sample("abcdefghijklmnABCDEFG",1)[0]
        pos = random.randint(0,n)
        c = a[:]
        c.insert(pos,b)
        aa = "".join(a)
        cc = "".join(c)
        print aa,cc,b
        runT2Test((aa,cc),b)
        runT2Test((cc,aa),b)


if __name__ == "__main__":
    #O(1) space required, but scanned the tree twice
    runT1Tests()

    #O(1) space required, O(n) time complexity
    runT2Tests()
