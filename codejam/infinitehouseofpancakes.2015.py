
import sys

lines="""3
1
3
2
6 6
4
1 2 1 2
1
4""".split("\n")
"""
consider the case: always one diner served
1
N
you split: N/2 cost
f(N) = f(N/2)+1
f(4) = f(2)+1 = f(1)+2 = 3
observe:
you have infinitely many diners, so you never move dine
to plates with food that will slow down the process
so f([x...]) = f( max([...]))

#attempt 2
not correct as the biggest one get consumed, you never dealt with
others , so it's  time to do this recursively
this is going to be very slow

the bottle neck is the reallocation,because diner is infinite
so how long does it take to redistribute...
"""
m={1:0,2:1}
def f( c ):
    if m.has_key(c): return m[c]
    else:
	r = 2*f(c/2) if c%2 == 0 else f(c/2)+f(c-c/2)
	m[c]=r
	return r

def g( c ):
    return f(c)+1
    
if __name__ == '__main__':
    #print lines
    #lines = sys.stdin.readlines()
    caseno = int(lines[0])
    j=1
    for case in range(caseno):
	dn = int(lines[j])
	plates = map(int,lines[j+1].split())
	t = 0
	while( len(plates)>0 ):
	    maxPlate = max(plates)
	    dcost = g(maxPlate)
	    plates.remove(maxPlate)
	    plates=filter(lambda x:x>0, map(lambda x:x-dcost,plates))
	    t += dcost
	print "Case #%d: %d"%(case+1,t)
	j+=2;
