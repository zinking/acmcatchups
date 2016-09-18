import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = int(math.sqrt(n))
        ss = map(lambda x:x*x, range(s,-1,-1))
        rr = [10**8]
        def findChange(r,i,c):
            if r<0 or i>=len(ss): return
            if r==0:
                rr[0] = min(rr[0],c)

            n1 = int(n/)




        return count

    

solver = Solution()

print ""
print solver.numSquares(13)
print solver.numSquares(1024)
