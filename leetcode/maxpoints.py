# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
from decimal import Decimal
#python is too slow for this
class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
	n = len(points)
	if n<=2 : return n
	lm = {}
	for i in range(n):
	    for j in range(i+1,n):
		#print i,j
		pa = points[i]
		pb = points[j]

		dx = Decimal( pb.x-pa.x)
		k = Decimal( pb.y-pa.y)/dx if dx!=0 else 0x0fffffff
		b = Decimal( pa.y-k*pa.x ) if dx!=0 else pa.x
		kb = (k, b)
		#print kb
		if not lm.has_key(kb):
		    lm[kb]=set([pa,pb])
		else:
		    lm[kb].add(pa)
		    lm[kb].add(pb)

	fl = map(lambda s:len(s),lm.values())
	fl.sort()
	#print lm.keys()
	return fl[-1]

s = Solution()

"""
p1 = Point(1,0);p2=Point(2,0);p3=Point(3,0)
points=[p1,p2,p3]
print s.maxPoints(points)

p1 = Point(0,1);p2=Point(0,2);p3=Point(0,3)
points=[p1,p2,p3]
print s.maxPoints(points)

p1=Point(1,1);p2=Point(2,2);p3=Point(3,3)
points=[p1,p2,p3]
print s.maxPoints(points)

p1=Point(0,0);p2=Point(0,0);
points=[p1,p2]
print s.maxPoints(points)

p1=Point(1,1);p2=Point(2,2);p3=Point(3,3);p4=Point(0,1);
points=[p1,p2,p3,p4]
print s.maxPoints(points)


p1=Point(1,1);p2=Point(0,0);p3=Point(1,-1)
points=[p1,p2,p3]
print s.maxPoints(points)
"""
ll=[(560,248),(0,16),(30,250),(950,187),(630,277),(950,187),(-212,-268),(-287,-222),(53,37),(-280,-100),(-1,-14),(-5,4),(-35,-387),(-95,11),(-70,-13),(-700,-274),(-95,11),(-2,-33),(3,62),(-4,-47),(106,98),(-7,-65),(-8,-71),(-8,-147),(5,5),(-5,-90),(-420,-158),(-420,-158),(-350,-129),(-475,-53),(-4,-47),(-380,-37),(0,-24),(35,299),(-8,-71),(-2,-6),(8,25),(6,13),(-106,-146),(53,37),(-7,-128),(-5,-1),(-318,-390),(-15,-191),(-665,-85),(318,342),(7,138),(-570,-69),(-9,-4),(0,-9),(1,-7),(-51,23),(4,1),(-7,5),(-280,-100),(700,306),(0,-23),(-7,-4),(-246,-184),(350,161),(-424,-512),(35,299),(0,-24),(-140,-42),(-760,-101),(-9,-9),(140,74),(-285,-21),(-350,-129),(-6,9),(-630,-245),(700,306),(1,-17),(0,16),(-70,-13),(1,24),(-328,-260),(-34,26),(7,-5),(-371,-451),(-570,-69),(0,27),(-7,-65),(-9,-166),(-475,-53),(-68,20),(210,103),(700,306),(7,-6),(-3,-52),(-106,-146),(560,248),(10,6),(6,119),(0,2),(-41,6),(7,19),(30,250)]
points=map(lambda t:Point(t[0],t[1]),ll)
print s.maxPoints(points)




        
