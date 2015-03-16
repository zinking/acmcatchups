class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
	r1 = dungeon[0]
	m = len(dungeon)
	n = len(r1)
	minHp = [ [ 0 for i in range(n)] for j in range(m) ]
	curHp = [ [ 0 for i in range(n)] for j in range(m) ]
	curHp[0][0] = dungeon[0][0]
	minHp[0][0] = min(-1,dungeon[0][0])
	for i in range(1,n):
	    curHp[0][i] = curHp[0][i-1] + dungeon[0][i]
	    minHp[0][i] = min(minHp[0][i-1],curHp[0][i])

	#import pdb
	#pdb.set_trace()
	for i in range(1,m):
	    curHp[i][0] = curHp[i-1][0] + dungeon[i][0]
	    minHp[i][0] = min(minHp[i-1][0],curHp[i][0])

	for i in range(1,m):
	    for j in range(1,n):
		fromUp = curHp[i-1][j] + dungeon[i][j]
		fromLe = curHp[i][j-1] + dungeon[i][j]
		if( fromUp > fromLe ):
		    curHp[i][j] = fromUp
		    minHp[i][j] = min(curHp[i][j],minHp[i-1][j])
		else:
		    curHp[i][j] = fromLe
		    minHp[i][j] = min(curHp[i][j],minHp[i][j-1])

	#print curHp
	#print minHp
	print -1*minHp[m-1][n-1]

s = Solution()
d1 = [[-2,-3,3], [-5,-10,1], [10,30,-5]]
s.calculateMinimumHP(d1)

d2 = [[2],[1]]
s.calculateMinimumHP(d2)

d3 = [[0]]
s.calculateMinimumHP(d3)
