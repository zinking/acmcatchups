import sys

def max_histogram( arr, n ):
    l = range(n)
    r = range(n)
    for i in range(n):
	j = i
	while( l[j]-1>=0 and arr[ l[j]-1 ] >= arr[i] ):
	    j = l[j]-1
	l[i]=j

    for i in range(n):
	j = i
	while( r[j]+1<=n-1 and arr[ r[j]+1 ] >= arr[i] ):
	    j = r[j]+1
	r[i] = j

    maxArea=0
    for i in range(n):
	width = r[i]-l[i]+1
	heigh = arr[i]
	maxArea = max( maxArea, width*heigh )

    #print arr
    #print l
    #print r
    print maxArea


	
   
if __name__=="__main__":
    lines = sys.stdin.readlines()
    for line in lines:
	ln = line.split(' ')
	n = int( ln[0] )
	if( n == 0): break;
	sn = map( lambda x:long(x), ln[1:])
	max_histogram(sn, n)
    
