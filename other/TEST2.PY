import fileinput

rrows=[]
rows=[]
for line in  fileinput.input():
	l = []
	for c in line:
		l.append(c)
	rows.append( l )
	rrows.append( line )
#rows = fileinput.readlines()
#print rows
row1 = map( lambda x:int(x), rrows[0].split(' ') )
N = row1[0]
M = row1[1]
K = row1[2]

mymap = rows[1:N+1]
starX = 0;
starY = 0;
#for idx,line in enumerate(mymap):
#	j = line.find('*')
#	if j!= -1:
#		starY = idx
#		starX = j

def move_fill( r, c ):
	if mymap[r][c] != '*': return
	#print mymap, r, c
	if c-1>=0 and mymap[r][c-1] == 'R':
		mymap[r][c-1] = '*'
	if c+1<M and mymap[r][c+1] == 'L':
		mymap[r][c+1] = '*'
	if r-1>=0 and mymap[r-1][c] == 'D':
		mymap[r-1][c] = '*'
	if r+1<N and mymap[r+1][c] == 'U':
		mymap[r+1][c] = '*'
for k in range(K):
	for i in range(N):
		for j in range(M):
			#print i,j,k,N,M,K
			move_fill(i,j)

	
#print mymap

i=0
j=0
mincost = 100000
#print 'here'
import math
for i in range(N):
	for j in range(M):
		#print i,j,N,M
		if mymap[i][j] == '*':
			cost = i+j
			#print cost
			mincost = min(mincost,cost)

if mincost <= K:
	print mincost
else:
	print -1

	
	

	
