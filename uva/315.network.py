
class Solution():
    def __init__( self, N ):
	self.adj = [ [0]*N for i in range(0,N)] 
	self.par = range(N)
	self.vis = [0]*N
	self.cri = 0
	self.n   = N-1
	self.t   = 0
	print self.n

    def add( self, e1, e2 ):
        self.adj[e1][e2]=1
	self.adj[e2][e1]=1

    def dfs( self, i, p ):
	print 'visit:',i,'from:',p
	self.t+=1
	self.vis[i] = self.t
	#self.par[i] = self.par[p]
	ap = False
	child = 0
	for v in range(1,self.n+1):
	    if( self.adj[i][v] == 1 and v!=p):
		if( self.vis[v] ):
		    if self.vis[v] < self.vis[self.par[i]]:
			print 'update pari to parv', i, v
			self.par[i] = self.par[v]
		else:
		    self.dfs(v,i)
		    child+=1
		    #if self.vis[i] < self.vis[v]:#dfs make this
		    #always satisfiable
		    if self.vis[ self.par[i]] > self.vis[self.par[v]]:
			#CRITICAL BUG FOUND
			print 'update ...',i,v
			self.par[i] = self.par[v]
		    if self.vis[self.par[v]] >= self.vis[i]:
			print 'judge'
			print v, self.par[v], self.vis[self.par[v]]
			print i, self.vis[i]
			print 'end judge'
			ap = True
    
	
	print 'par',self.par
	print 'vis',self.vis
	if( (i==p and child>1) or (i!=p and ap)):
	    self.cri+=1
	    print 'cri:',i
	print 'finish:',i

    def solve(self):
	for i in range(1,self.n+1): self.dfs(i,i)
	print self.cri,'total'
	
if __name__=='__main__':
    #import sys
    #lines = sys.stdin.readlines()
    lines="""17
17 6 13
6 7
7 13
0
4
4 3
3 2
2 1
1 4
0
5
5 1 2 3 4
0
6
2 1 3
5 4 6 2
0
17
1 14 11
6 7
10 15
8 10 15
14 11 1
9 7 12
3 1
7 12
4 8
13 17 7
17 6
5 11
11 8
2 5
16 9
15 17
0
0""".split("\n")
    nl = len(lines)
    cl = 0
    while( cl < nl ):
	line = lines[cl]
	n = int(line)
	if n==0 : break
	solver = Solution(n+1)
	cl+=1
	while( lines[cl][0] != '0'):
	    line = lines[cl]
	    strs = line.split(' ')
	    v = map( lambda x:int(x),strs )
	    cl+=1
	    for adjv in v[1:]: solver.add( v[0],adjv)
	print 'new case'
	solver.solve()
	cl+=1


