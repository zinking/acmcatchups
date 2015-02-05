import math
import sys

import pdb


class UnionGroup():
    def __init__(self,N):
        self.p=[-1]*N

    def union(self,x,y):
	self.link( self.find(x), self.find(y))

    def link(self,x,y):
	px = self.p[x]
	py = self.p[y]
	if( x<y ):
	    if py<0 : self.p[x]+=py
	    self.p[y]=x
	    #self.n[x]+=self.n[y]
	    #self.n[y]=0
	elif( y<x ):
	    if px<0 : self.p[y]+=px
	    self.p[x]=y
	    #self.n[y]+=self.n[x]
	    #self.n[x]=0
	#print self.p
	#print self.n

    def find(self,a):
	pa = self.p[a]
	if( pa>0 and a != pa):
	    #print self.p[a],a
	    return self.find(pa)
	return pa if pa>0 else a

    def isSameGroup(self, a, b):
	return self.find(a) == self.find(b)

    def sizeGroup(self, a):
	n = self.p[(self.find(a) )]
	return -n if n<0 else 1

    def numGroup(self ):
	roots = filter( lambda x:x<-1, self.p )
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

	
