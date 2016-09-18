import math
import pdb
#pdb.set_trace()
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        m = {}
        rn = int(math.sqrt(n))
        for i in range(0,rn+1):m[i*i] = 1
        def minSquares(n1):
	    
            print 'calc:',n1
            if m.has_key(n1): return m[n1]
            rn1 = int(math.sqrt(n1))
	    #pdb.set_trace()
            rr = n1
            for i in range(rn1,0,-1):
		print '#2',n1,'-','i*i',i,i*i
                cnt = minSquares(n1-i*i)+1
                rr = min(rr,cnt)
            m[n1] = rr
            return rr

        return minSquares(n)

    
solver = Solution()

print solver.numSquares(10)
print solver.numSquares(1001)
print solver.numSquares(10001)
