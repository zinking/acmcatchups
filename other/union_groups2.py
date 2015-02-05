import math
import sys

import pdb


class UnionGroup():
    def __init__(self,N):
        self.p=range(N)
	self.n=[1]*N

    def union(self,x,y):
	self.link( self.find(x), self.find(y))

    def link(self,x,y):
	if( x<y ):
	    self.p[y]=x
	    self.n[x]+=self.n[y]
	    self.n[y]=0
	elif( y<x ):
	    self.p[x]=y
	    self.n[y]+=self.n[x]
	    self.n[x]=0
	#print self.p
	#print self.n

    def find(self,a):
	if( a != self.p[a] ):
	    #print self.p[a],a
	    return self.find(self.p[a])
	return self.p[a]

    def isSameGroup(self, a, b):
	return self.find(a) == self.find(b)

    def sizeGroup(self, a):
	n = self.n[(self.find(a) )]
	return n if n>0 else 1

    def numGroup(self ):
	roots = filter( lambda x:x>1, self.n )
	return len(roots)

if __name__ == '__main__':
   lines = sys.stdin.readlines()
   g = None
   for line in lines:
       if not "," in line and not "(" in line:
	   N=int(line)
	   g = UnionGroup(N)
       elif line[0:4]=="size":
	   tc = 'g.'+line
	   print tc
	   print eval(tc)
	   continue
       elif line[0:3]=="num":
	   tc = 'g.'+line
	   print tc
	   print eval(tc)
	   continue
       elif line[0:2]=="is":
	   tc = 'g.'+line
	   print tc
	   print eval(tc)
	   continue
       elif "," in line:
	   nums=line.split(",")
	   g.union( int(nums[0]), int(nums[1]))
	   #print g.p

	
