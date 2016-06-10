"""
Problem: Please get the least number after deleting kdigits from the input number. For example, if the input number is 24635, the least number is 23 after deleting 3 digits.
"""

"""
12321
remove each
2321
1321
1221
1231
1232

12324
2324
1324
1224
....
find the turning point and delete the turning point
"""

def biggestAfterDelete(n,k):
    #print "*******",n,k
    if k==0:
        return n
    nl = []
    n1 = n
    while n1>0:
        nl.insert(0,n1%10)
        n1 /= 10
    #print nl
    ll = len(nl)
    j=1
    st = nl[0]
    while j<ll and nl[j]>st:
        st = nl[j]
        j += 1
    #print "st:",st,"j:",j
    #nl.remove(j)
    nl.pop(j-1)
    rr = 0
    for d in nl:
        rr *= 10
        rr += d
    return biggestAfterDelete(rr,k-1)


def runTest(t,e):
    (n,k) = t
    a = biggestAfterDelete(n,k)
    if a == e:
        print "pass"
    else:
        print "fail:",t,"expected:",e,"actual:",a

def runTests():
    t1 = (12321,1)
    e1 = 1221
    runTest(t1,e1)

    t2 = (123, 1)
    e2 = 12
    runTest(t2, e2)

    t21 = (1324,1)
    e21 = 124
    runTest(t21,e21)

    t3 = (13243221,5)
    e3 = 121
    runTest(t3, e3)

    t4 = (7654321,3)
    e4 = 4321
    runTest(t4, e4)


if __name__ == "__main__":
    runTests()
