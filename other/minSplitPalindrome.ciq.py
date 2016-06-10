"""
Problem: A string can be partitioned into some substrings, such that each substring is a palindrome. For example, there are a few strategies to split the string “abbab” into palindrome substrings, such as: “abba”|”b”, “a”|”b”|”bab” and “a”|”bb”|”a”|”b”.

Given a string str, please get the minimal numbers of splits to partition it into palindromes. The minimal number of splits to partition the string “abbab” into a set of palindromes is 1.
"""
def minSplitPalindrome(s):
    n = len(s)
    pl = [
        [ 1 if i==j else 0 for i in range(n)] for j in range(n)
    ]
    def isPalindrome(i,j):
        if i==j:
            return True

        if s[i] == s[j]:
            if j-1<=i+1 or pl[i+1][j-1] == 1:
                pl[i][j] = 1
                return True
        return False
    splits = range(n)
    for i in range(1,n):
        if isPalindrome(0,i):
            splits[i] = 0
            continue

        for j in range(i):
            if isPalindrome(j+1,i) and splits[i]>splits[j]+1:
                splits[i] = splits[j]+1

        #print splits

    return splits[n-1]

    

def runTest(t,e):
    a = minSplitPalindrome(t)
    if a == e :
        print "success"
    else:
        print "failure:",t,"expected:",e,"actual:",a

def runTests():
    t1 = "abbab"
    e1 = 1
    runTest(t1,e1)

    t2 = "abacd"
    e2 = 2
    runTest(t2,e2)

if __name__ == "__main__":
    runTests()
