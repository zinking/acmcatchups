"""
Problem: Reorder the digits of a number, in order to get the next number which is the least one that is greater than the input number. For example, the number 34724126 is the next number of 34722641 when reordering digits.
"""

def nextNumber(ns):
    #number in string format
    nn = map(lambda x:int(x),ns)
    n = len(ns)
    iseq = [nn[-1]] #increasing sequence
    pos = n-2
    while nn[pos] >= iseq[-1]:
        iseq.append(nn[pos])
        pos -= 1
    if len(iseq) == n :
        #in the case of no biggest,return current
        return ns
    else:
        tl = nn[pos]
        for j in range(len(iseq)):
            if iseq[j] > tl:
                #swap tail with the bigger one
                temp = iseq[j]
                iseq[j] = tl
                nn[pos] = temp
                break
        #the new number list
        nnl = nn[0:pos+1] + sorted(iseq)
        return "".join(map(lambda x:str(x),nnl))

def runTest(t, e):
    a = nextNumber(t)
    if a == e :
        print "pass"
    else:
        print "fail:",t,"expected",e,"actual:",a

def runTests():
    t1 = "38276"
    e1 = "38627"
    runTest(t1, e1)
    t2 = "34722641"
    e2 = "34724126"
    runTest(t2, e2)
    t3 = "321"
    e3 = "321"
    runTest(t3,e3)
    pass

if __name__ == "__main__":
    runTests()
