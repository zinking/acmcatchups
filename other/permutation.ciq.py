"""
Questions: Please print all permutations of a given string. For example, print “abc”, “acb”, “bac”, “bca”, “cab”, and “cba” when given the input string “abc”.
"""
import random

def permutation(str):
    r = []
    chs = list(str)
    n = len(chs)
    def swap(pstr, i, j):
        tmp = pstr[j]
        pstr[j] = pstr[i]
        pstr[i] = tmp
    def permutate(pstr,i):
        if i==n-1:
            r.append("".join(pstr))
        else:
            for x in range(i,n):
                #rd =  random.randrange(i,n)
                rd = x
                swap(pstr,i,rd)
                permutate(pstr,i+1)
                swap(pstr,i,rd)
    permutate(chs,0)
    return r

def runTest(t,e):
    a = permutation(t)
    if a == e :
        print "pass"
    else:
        print "fail:",t,"expected:",e,"actual:",a

def runTests():
    t1 = "ab"
    e1 = ["ab","ba"]
    runTest(t1,e1)

    t2 = 'abc'
    e2 = ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']
    runTest(t2,e2)


if __name__ == "__main__":
    runTests()
