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

"""
this problem has an extension, which is more difficult (**), which got me
stuck so long on it.

if we add the condition that, the sequence of the line can be
re-arranged. then the result will be quite different.

take line 1 , 2, 3, 4 for example.
arrange 1 2 3 4 then at least 10 candies need to be allocated
arrange 1 4 2 3 then 1 2 1 2 only 6 candies need to be callocated 
arrange 1 4 3 2 then 1 3 2 1 7 candies need to be allocated.

so seems interleaving them makes the minimum allocation
1 2 1 2

problem: is this always possible to interleaving them?
egg:
1 4 2 3
+ 5
5 1 4 2 3
+6
1 5 6 3 4 2
seems always possible, how to prove that?

proval:
1 2 3 -> 3 1 2
assume for 0....N it holds
we can arrange it to 0'...N'

for N+1
assuming  N-1' > N'
    if N+1 > N' then append N+1 after N' make it zigzag interleaving \/
    if N+1 < N' then N-1' > N', so we can append N+1 and then swap N+1
with N' make it interleaving. \/
assuming  N-1' < N' similar scenario.

"""
