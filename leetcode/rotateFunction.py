class Solution(object):
    def maxRotateFunction(self, A):
        n = len(A)
        if n == 0: return 0
        si = A[0]
        for i in range(1,n):
            s1 = si + i*A[i]
            s2 = si



    def maxRotateFunction1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n == 0: return 0
        ZA = zip(A,range(n))
        SZA = sorted(ZA, key=lambda x:x[0])
        ZAI = map(lambda x:x[1], SZA)
        def rotateSum(i):
            print '##',i
            B = A[i+1:] + A[0:i+1]
            C = range(n)
            s = 0
            for i in range(n):
                s += B[i] * C[i]
            return s

        print '#', ZAI
        rr = -9223372036854775807
        i1 = ZAI.pop()
        s1 = rotateSum(n-1-i1)
        while len(ZAI) > 0 and s1 > rr:
            rr = s1
            i1 = ZAI.pop()
            s1 = rotateSum(n-1-i1)

        rr = max(i1,s1)
        return rr
        


solver = Solution()
print solver.maxRotateFunction([4,3,2,6])
print solver.maxRotateFunction([-2147483648,-2147483648])
#print solver.maxRotateFunction(range(100000))
