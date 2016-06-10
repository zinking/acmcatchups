"""
Question: When some elements at the beginning of an array are moved to the end, it gets a rotation of the original array. Please implement a function to search a number in a rotation of an increasingly sorted array. Assume there are no duplicated numbers in the array.
For example, array {3, 4, 5, 1, 2} is a rotation of array {1, 2, 3, 4, 5}. If the target number to be searched is 4, the index of the number 4 in the rotation 1 should be returned. If the target number to be searched is 6, -1 should be returned because the number does not exist in the rotated array.
"""
""" discussion
in terms of why the assumption of no duplication elements in the array
consider the case [0 1 1 1 1]
[1 0 1 1 1] or [1 1 1 0 1] could both valid rotation array, but this case definitely fails the search 
"""
"""
search for 3 in rotated [1 2 3 4 5]
case [4 5 1 2 3]
m = 1 != 3, 1<3 and st 4>3 so drop first half
=> [2 3]
"""

def searchRotate(arr,x):
    r = -1
    n = len(arr)
    b = 0
    e = n-1
    while b<=e:
        m = (b+e)/2
        if arr[m] == x:
            return m
        if arr[m] > arr[b]: #increasing first half
            if x >= arr[b] and x<=arr[m]:
                e = m-1
            else:
                b = m+1
        else:
            if x >= arr[m] and x<=arr[e]:
                b = m+1
            else:
                e = m-1
    return r


def runTest(t,e):
    (arr,x) = t
    a = searchRotate(arr,x)
    if e == a :
        print "success"
    else:
        print "fail:", t, "expected:",e,"actual:",a

def runTests():
    t1 = ([4,5,1,2,3],3)
    e1 = 4
    runTest(t1,e1)

    t1 = ([4,5,1,2,3],4)
    e1 = 0
    runTest(t1,e1)

    t1 = ([4,5,1,2,3],5)
    e1 = 1
    runTest(t1,e1)

    t1 = ([4,5,1,2,3],6)
    e1 = -1
    runTest(t1,e1)



    #this is the symmetric case
    t2 = ([3,2,1,5,4],3)
    e2 = 0
    #runTest(t2,e2)


if __name__ == "__main__":
    runTests()
