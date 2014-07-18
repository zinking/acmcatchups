#from math import max
import math

class Node:
    def __init__(self, rate ):
	self.rate = rate
	self.alloc = 1

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
	nds = map( lambda x:Node(x), ratings)
	n = len(ratings)
	for i in range(n):
	    nd = nds[i]
	    nd.left = nds[i-1] if i>=1 else nd
	    nd.right = nds[i+1] if i<=n-2 else nd

	snds = sorted( nds, key=lambda nd:nd.rate)
	for nd in snds:
	    ll = nd.left.alloc+1 if nd.rate > nd.left.rate else nd.alloc
	    rr = nd.right.alloc+1 if nd.rate > nd.right.rate else nd.alloc
	    nd.alloc = max(ll,rr)

	#return reduce( lambda x,y:x.alloc+y.alloc, snds)
	return reduce( lambda x,y:x+y, map( lambda x:x.alloc, snds) )

class Solution1:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
	#ur = list( set( ratings) )
	ur = ratings
	r,r2i = self.numbersRank( ur )
	print 'rank:',r
	print 'rank2index:',r2i
	n = len(r)
	alloc = [1]*n
	total = 0
	for i in range(n):
	    #alloc candy for rank i
	    id = r2i[i]
	    left = id-1 if id-1>=0 else 0
	    right = id+1 if id+1<=n-1 else n-1
	    ll = alloc[left]+1 if r[id] > r[left] else alloc[left]
	    rr = alloc[right]+1 if r[id] > r[right] else alloc[right]
	    candyn = max(ll,rr)
	    alloc[id]=candyn
	    total+=candyn
	print 'alloc:',alloc
	return total
	    
    def numbersRank( self, ratings ):
	#ratings=[3,3,1,2]
	#target rank=[2,3,0,1]
	n = len(ratings)
	tpl = [ (ratings[i], i) for i in range(n)]
	print 'tpl',tpl
	#tpl = [(3,0),(3,1),(1,2),(2,3)]
	stpl = sorted( tpl, key=lambda t:t[0])
	print 'stpl', stpl
	#stpl = [(1,2), (2,3), (3,0), (3,1) ]
	#rank->(rating, index)
	rate2rank = dict( (stpl[i][0],i) for i in range(n))
	print 'rate2rank', rate2rank
	rank = [  rate2rank[r] for r in ratings]
	print 'rank',rank
	rank2index = dict( (i,(stpl[i][1]) )for i in range(n))
	print 'rank2index', rank2index
	return rank, rank2index
	

if __name__ == '__main__':
    sl = Solution()
    print sl.candy( [1,2,2]) == 4
    print sl.candy( [1,2,3]) == 6
    print sl.candy( [1,3,2]) == 4
    print sl.candy( [1,1,1]) == 3
    print sl.candy( [2,4,1,3]) == 6
