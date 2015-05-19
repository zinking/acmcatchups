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
	minHp[0][0] = -1*min(1,1-dungeon[0][0]) if curHp[0][0] <= 0 else 0
	
	for i in range(1,n):
	    curHp[0][i] = curHp[0][i-1] + dungeon[0][i]
	    minst = min( minHp[0][i-1], curHp[0][i])
	    minHp[0][i] = minst-1 if minst <= 0 else 0 

	for i in range(1,m):
	    curHp[i][0] = curHp[i-1][0] + dungeon[i][0]
	    minst = min( minHp[i-1][0], curHp[i][0])
	    minHp[i][0] = minst-1 if minst <= 0 else 0

	for i in range(1,m):
	    for j in range(1,n):
		fromUp = curHp[i-1][j] + dungeon[i][j]
		fromLe = curHp[i][j-1] + dungeon[i][j]
		if( fromUp > fromLe ):
		    curHp[i][j] = fromUp
		    minst = min( minHp[i-1][j], fromUp)
		    minHp[i][j] = minst-1 if minst <= 0 else 0
		else:
		    curHp[i][j] = fromLe
		    minst = min( minHp[i][j-1], fromLe)
		    minHp[i][j] = minst-1 if minst <= 0 else 0 

	return -1*minHp[m-1][n-1]

s = Solution()
d1 = [[-2,-3,3], [-5,-10,1], [10,30,-5]]
print s.calculateMinimumHP(d1)

d2 = [[2],[1]]
print s.calculateMinimumHP(d2)

d3 = [[0]]
print s.calculateMinimumHP(d3)

d4 = [[-200]]
print s.calculateMinimumHP(d4)

d5 = [[0,-3]]
print s.calculateMinimumHP(d5)

d6 = [[0,0]]
print s.calculateMinimumHP(d6)

