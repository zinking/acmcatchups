def gcd(a,b):
    if b == 0 :
        return a
    else:
        return gcd(b,a%b)

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        #ax+by=z
        #b 0...n
        #a = (z-by)/x
        if z>(x+y):
            return False
        if z==x or z==y or z%x==0 or z%y==0:
            return True

        xy = gcd(x,y)
        return z % xy == 0


def testWaterJugg():
    s = Solution()
    print s.canMeasureWater(34,5,6)
    print s.canMeasureWater(3,5,4)
    print s.canMeasureWater (1,1,1)


if __name__ == '__main__':
    testWaterJugg()
