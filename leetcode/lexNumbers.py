class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        i = 1
        r = [0]*n
        r[0] = 1
        total = 1
        
        while total<n:
            while i*10 <= n:
                #r.append(i*10)
                r[total] = i*10
                i*=10
                total += 1

            while i%10 != 9:
                if i+1 <= n:
                    #r.append(i+1)
                    r[total] = i+1
                    total += 1
                i+=1

            i += 1 #the 10th increment
            while i%10 == 0 : i/=10

            if i<=n and i != 1:
                #r.append(i)
                r[total] = i
                total += 1

        return r




print ""
#s = range(1,122)
#print sorted(s, key=lambda x:str(x))
#solver = Solution()
#print solver.lexicalOrder(121)

solver = Solution()
def testSolution(i1):
    actual = solver.lexicalOrder(i1)
    r = range(1,i1+1)
    expected = sorted(r, key=lambda x:str(x))
    if actual == expected:
        print "case:",i1,"pass"
    else:
        print "case %d fail"
        print "actual:"
        print actual
        print "exptected:"
        print expected


testSolution(10)
testSolution(21)
testSolution(1000)
testSolution(1)
testSolution(2)


