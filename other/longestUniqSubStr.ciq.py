"""
Problem:Given a string, please get the length of the longest substring which does not have duplicated characters. Supposing all characters in the string are in the range from ‘a’ to ‘z’.
"""

"""
abcda
12344
abcaa
12333
abceeeafgh
1234112345
1234444
"""

def longestUniqSubstr(s):
    t = [-1 for i in range(30)]
    maxLen = 0 
    curLen = 0
    n = len(s)
    for i in range(n):
        c = s[i]
        ci = ord(c) - ord('a') #character index in table
        p = t[ci]
        if p<0 or (i-p) > curLen:
            curLen += 1
        else:
            maxLen = max(maxLen,curLen)
            curLen = i-p
        t[ci] = i
        
    maxLen = max(maxLen, curLen)
    return maxLen
    

def runTest(t,e):
    a = longestUniqSubstr(t)
    if a == e :
        print "pass"
    else:
        print "fail:",t,"expected:",e,"actual:",a

def runTests():
    t1 = "abcda"
    e1 = 4
    runTest(t1,e1)

    t2 = 
    pass

if __name__ == "__main__":
    runTests()
