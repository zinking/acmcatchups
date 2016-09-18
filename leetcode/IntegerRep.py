class Solution(object):
    def integerReplacement(self, n):
        if n == 0: return 0
        rr = [10000]
        def f(n,c):
            #print n,c
            if n <= 0: return
            if n == 1:
                rr[0] = min(rr[0],c)
                return
            else:
                if n%2 == 0:
                    f(n>>1,c+1)
                else:
                    f(n+1,c+1)
                    f(n-1,c+1)
        f(n,0)
        return rr[0]


    def integerReplacement1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return -1
        if n == 1: return 0
        if n == 2: return 1
        if n == 3: return 2
        rr = [0 for i in range(n+1)]
        rr[0] = 0
        rr[1] = 0
        rr[2] = 1
        rr[3] = 2

        for j in range(4,n+1):
            if j%2 == 0: rr[j] = rr[j>>1] + 1
            if j%2 == 1:
                r1 = rr[(j+1)>>1] + 2
                r2 = rr[j-1] + 1
                rr[j] = min(r1,r2)
        #print rr
        return rr[n]


solver = Solution()

print solver.integerReplacement(7)
print solver.integerReplacement(8)
print solver.integerReplacement(10000000)
