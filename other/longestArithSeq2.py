"""
Question 3:Given an array, please get the length of the longest consecutive sequence. A consecutive sequence is an arithmetic sequence with common difference 1. The element order in the consecutive sequence is not necessarily same as the element order in the array. The solution should not cost more than O(n) time and space if the length of the input array is n. For example, in the array {1, 6, 3, 5, 9, 7}, the longest consecutive sequence is 5, 6, and 7 whose length is 3.
"""

def longestArithSeq(seq):
    ss = set(seq)
    maxCount = 0
    while len(ss)>0:
        top = ss.pop()
        count = 1
        n = top+1
        while n in ss:
            ss.remove(n)
            count += 1
            n += 1
        n = top-1
        while n in ss:
            ss.remove(n)
            count += 1
            n -= 1
        maxCount = max(maxCount,count)
    return maxCount

def runTest(input,expected):
    a1 = longestArithSeq(input)
    if a1 == expected:
        print "pass"
    else:
        print "fail:",input,"expected:",expected,"actual:",a1
    pass


def runTests():
    t1 = [1, 3, 2, 4, 5]
    e1 = 5
    runTest(t1,e1)

    t2 = [1, 2, 3, 4, 5]
    e2 = 5
    runTest(t2,e2)

    t3 = [6,5,4,3,2,1]
    e3 = 6
    runTest(t3,e3)

    pass

if __name__ == "__main__":
    runTests()
