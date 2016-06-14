"""
Question: Given an array of numbers and a sliding window size, how to get the maximal numbers in all sliding windows?
"""
def maxSlideWindow(l,k):
    q = []
    for i in range(k-1):
        q.append(l[i])
    def appendQ(e):
        i = len(q)-1
        while i>=0:
            if e >= q[i]:
                q.pop(i)
                i-=1
            else:
                break
        q.append(e)
    def poplQ():
        q.pop(0)
    r = []
    import pdb
    pdb.set_trace()
    for x in range(k-1,len(l)):
        appendQ(l[x])
        print q
        r.append(q[0])
        poplQ()
    return r


def runTest(t,e):
    (l,k) = t
    a = maxSlideWindow(l,k)
    if a == e:
        print "success"
    else:
        print "fail:",t,"expected:",e,"actual:",a

def runTests():
    t = ([2,3,4,2,6],3)
    e = [4,4,6]

    runTest(t,e)

if __name__ == "__main__":
    runTests()
