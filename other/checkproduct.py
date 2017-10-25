#check product
#every product is given start and end time, 
#product owner asks that at the same time active product could not exceed N
#implement a validation to check this requirement

N = 2

class Product(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "(%d, %d)"%(self.start, self.end)

    def __unicode__(self):
        return u"(%d, %d)"%(self.start, self.end)

    def __repr__(self):
        return "(%d, %d)"%(self.start, self.end)


def checkProduct(newProduct, productList):
    def checkOverlap(r1, r2):
        a, b = r1
        c, d = r2
        if a > c:
            a, c = c, a
            b, d = d, b
        return c >= a and c < b

    candProductList = productList + [newProduct]
    times = set()
    for p in candProductList:
        times.add(p.start)
        times.add(p.end)

    times = sorted(times)
    n = len(times)
    #print 'times:', times
    for i in range(n-1):
        rr = times[i], times[i + 1]
        #print 'time range', rr
        rrn = 0
        for p in candProductList:
            if checkOverlap(rr, (p.start, p.end)):
                #print 'overlapping:', rr, p
                rrn += 1
            if rrn > N : return False #self overlap
    return True


def testCheckProduct(product, productList, expectedResult):
    actualResult = checkProduct(product, productList)
    if actualResult == expectedResult:
        print 'Pass'
    else:
        print 'Failed'
        print 'Input:', (product, productList)
        print 'ExpectedResult:', expectedResult
        print 'ActualResult:', actualResult

def checkProductTests():
    p1 = Product(1, 2)
    p2 = Product(3, 4)
    p3 = Product(1, 4)
    p4 = Product(5, 6)
    testCheckProduct(p1, [p1,p2,p3,p4], False)
    testCheckProduct(p4, [p1,p2,p3,p4], True)
    p5 = Product(6, 7)
    p6 = Product(6, 6)
    testCheckProduct(p6, [p4,p5,p6], False)
    p7 = Product(2, 4)
    testCheckProduct(p3, [p1,p2], True)

if __name__ == '__main__':
    checkProductTests()