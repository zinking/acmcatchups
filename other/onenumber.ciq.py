"""
Problem: In an array, all numbers appear three times except one which only appears only once. Please find the unique number.
"""

def theNumber(ll):
    l = ll[:]
    r = 0L
    nl = len(l)
    for i in range(32):
        bitSum = 0
        d = 0
        #print l
        for j in range(nl):
            bitSum += (l[j]&1)
            l[j] = l[j] >> 1
        d = bitSum%3
        r = (d << i) + r
        #print d,i,r
    return r

def runTest(t,e):
    a = theNumber(t)
    if a == e:
        print "pass"
    else:
        print "fail:",t,"expected:",e,"actual:",a
def runTests():
    t1 = [1,1,3,1]
    e1 = 3
    runTest(t1,e1)

    t2 = [2,2,2,3,3,3,4]
    e2 = 4 
    runTest(t2,e2)

if __name__ == "__main__":
    runTests()
