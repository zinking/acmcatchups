
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(n, b):
            if n <= 1: return 1
            if n == 2: return 2 if b==0 else 1
            bb = (b+1)%2
            if n%2 == 1: return 2*f(n/2, bb)
            else:
                if b == 0: return 2*f(n/2,bb)
                else: return 2*f(n/2,b)+1

        return f(n,0)


    def expect(self,n):
        l = range(1,n+1)
        b = 0
        print l
        while len(l) > 1:
            ll = []
            bb = 0 if b == 0 else len(l)-1
            for i in range(len(l)):
                if i%2 != bb%2: ll.append(l[i])

            b = (b+1)%2
            l = ll
            print ll

        return l[0]

    def evaluate(self, inputs):

        for i in inputs:
            print '#'*20
            actual = self.lastRemaining(i)
            expect = self.expect(i)
            if actual == expect:
                print "input:",i,"Pass: ",expect
            else:
                print "input:",i,"Actual:",actual," Expect:",expect
            #print "input:",i,"Expect:",expect


solver = Solution()
print ""

#solver.evaluate([9])
#solver.evaluate(range(1,100))
solver.evaluate([24,28,32,36])




