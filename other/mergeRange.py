
"""
Questions: Given an array of ranges, please merge the overlapping ones. For example, four ranges [5, 13], [27, 39], [8, 19], [31, 37] (in blue in  Figure1) are merged into two ranges, which are [5, 19] and [27, 39] (in green in Figure 1).
"""

def rangeOverlap(r1,r2):
    (m,n) = r1
    (o,p) = r2
    def between(r,p1):
        (x,y) = r
        return p1>=x and p1<=y
    return between(r1,o) or between(r1,p) or between(r2,m) or between(r2,n)

def mergeRange(r1,r2):
    """
    required: r1 overlaps r2
    if r1 overlaps r2 then return merged range
    """
    (m,n) = r1
    (o,p) = r2
    #print 'merge:',r1,r2
    return (min(m,o),max(n,p))

def mergeRanges(ranges):
    if len(ranges) == 0 : return []
    sr = sorted(ranges, key=lambda x:x[0])
    results = []
    for r in sr:
        if len(results) == 0:
            results.append(r)
        else:
            tp = results[-1]
            if rangeOverlap(tp,r):
                tp = results.pop()
                mr = mergeRange(tp,r)
                results.append(mr)
            else:
                results.append(r)
    return results 

def runMergeRange(input, expected):
    actual = mergeRanges(input)
    if actual == sorted(expected,key=lambda x:x[0]) :
        print 'Pass'
    else:
        print 'Fail:',input,'expected:',expected,'actual:',actual


def run_tests():
    t1 = [(5,15),(20,30),(35,45),(15,15),(50,50)]
    e1 = [(5,15),(20,30),(35,45),(50,50)]
    runMergeRange(t1,e1)

    t2 = [(5,15),(20,30),(35,45),(10,25),(30,40)]
    e2 = [(5,45)]
    runMergeRange(t2,e2)

    t3 = [(5,15),(35,45),(20,30)]
    e3 = [(5,15),(35,45),(20,30)]
    runMergeRange(t3,e3)

    pass

if __name__ == "__main__":
    run_tests()
