import sys
import math
from math import *


def calculatewin( al, bl ):
    #print 'DEBUG', al, bl
    i = 0; j=0; nwin=0;
    while( i<n and j<n ):
	nm = al[i] #naomi max
	km = bl[j]
	while( nm < km and j<n ):
	    j+=1
	    if( j<n ):km=bl[j]
	if( j<n ):
	    nwin+=1
	    #print i,j
	    #print nm,km
	    j+=1
	i+=1
    return nwin

def decitifulwar(case, n, nl, kl ):#naomilist kenlist
    ncheat=0; nreal=0;#naomiboollist kenboollist
    nl.sort(reverse=True)
    kl.sort(reverse=True)
    ncheat = calculatewin( nl, kl )
    nreal  = n - calculatewin( kl, nl )
    print "Case #%d: %d %d"%(case,ncheat, nreal)

def readfloatlist():
    line = sys.stdin.readline()
    line = line.split()
    l = map(lambda x:float(x), line)
    return l

if __name__=="__main__":
    n = int( sys.stdin.readline() )
    for i in range(0,n):
        line = sys.stdin.readline()
	n = int(line)
	nl = readfloatlist()
	kl = readfloatlist()
        decitifulwar(i+1, n, nl, kl)
