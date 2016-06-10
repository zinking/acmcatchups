# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
import math
import sys

class CoinTable(object):
    dirs = {
        'U':(-1,0),
        'D':(1,0),
        'L':(0,-1),
        'R':(0,1),
    }
    
    def __init__(self, m, n, k, smap):
        self.mincost = 0
        self.m=m
        self.n=n
        self.k=k
        self.smap=smap
        self.findtarget()
        self.bt=[]
        self.vmap = [ [ 0 for j in range(self.m) ] for i in range(self.n)]


    def findtarget(self):
        for i in range(self.n):
            for j in range(self.m):
                if (self.smap[i][j] == '*' ):
                    self.tr = i
                    self.tc = j
        
    def search(self,frame):
        (r,c,vmap,ck,cc)=frame
        if (ck>self.k):
            self.mincost = -1
            return
        if (smap[r][c]=='*' ):
            self.mincost = cc
            return
        for d in "UDLR":
            dir=self.dirs[d]
            nr = r+dir[0]
            nc = c+dir[1]
            if( (nr>=0 and nr<=n-1) and (nc>=0 and nc<=m-1) and vmap[nr][nc]==0 ):
                mcost= 0 if smap[r][c] == d else 1

    def solve(self ):
                vmap[0][0]=1
        frame = (0,0,vmap,0,0)
        self.search(frame)
        

if __name__ == '__main__':
    rows=[]
    for line in sys.stdin.readlines():
	rows.append( line )
    row1 = map( lambda x:int(x), rows[0].split(' ') )
    N = row1[0]
    M = row1[1]
    K = row1[2]

    mymap = rows[1:N+1]
    
    cointable = CoinTable(M,N,K,mymap)
    cointable.solve()


	

	
