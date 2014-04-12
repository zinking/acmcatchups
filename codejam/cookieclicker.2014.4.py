import sys
import math
from math import *



def cookieclicker( case, c, f, x ):
    n = (x*f-c*f-2.0*c)/(c*f)
    n = int( max(0,ceil(n)) )
    total = 0.0
    r = 0.0
    if n>0:#calculate farm building cost
	for i in range(0,n):
	    r += c/(i*f+2.0)
	    
    #print n,c,f,x
    total+=r
    total+=x/((n)*f + 2.0)
    print "Case #%d: %.7f"%(case,total)

if __name__=="__main__":
    n = int( sys.stdin.readline() )
    for i in range(0,n):
        line = sys.stdin.readline()
        line = line.split()
        l = map(lambda x:float(x), line)
        c = l[0]; f=l[1]; x=l[2];
        cookieclicker(i+1,c,f,x)
        
