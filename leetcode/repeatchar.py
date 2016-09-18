from collections import Counter
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if k > n : return 0
        if k == 1 : return n
        m = [ [ None for i in range(n)] for j in range(n) ]
        for i in range(n):
            for j in range(i,n):
                if i == j: 
                    m[i][j] = Counter(s[i])
                elif j > i:
                    nch = s[j]
                    ncter = Counter(m[i][j-1])
                    ncter[nch] += 1
                    m[i][j] = ncter
        def isRangeOk(cter,k):
            for ch, n1 in cter.items():
                if n1 < k: return False
            return True
        def printm():
            print "###m####"
            for r in m:
                print r
            print 
                
        #print s
        #printm()
        mlen = k
        for i in range(0,n-mlen+1):
            for j in range(n-1,i+mlen-2,-1):
                #print 'chcked ',i,j
                cter = m[i][j]
                if isRangeOk(cter,mlen): return j-i+1
        return 0
        

solver = Solution()

print solver.longestSubstring("ababbc",2)
print solver.longestSubstring("aaabb",3)
print solver.longestSubstring("abc",2)
print solver.longestSubstring("abc",4)
print solver.longestSubstring("abcdbc",1)
print solver.longestSubstring("",1)
