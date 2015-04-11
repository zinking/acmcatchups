
import sys

lines="""3
1
3
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
"""
m={}
def f( cakes ):
    if m.has_key(cakes): return m[cakes]
    if cakes == 1:
	m[1]=1
	return 1
    else:
	r = f(cakes/2)+1 if cakes%2 == 0 else f(cakes/2)+2
	m[cakes]=r
	return r
    
if __name__ == '__main__':
    #print lines
    lines = sys.stdin.readlines()
    caseno = int(lines[0])
    j=1
    for case in range(caseno):
	dn = int(lines[j])
	plates = map(int,lines[j+1].split())
	maxCakes = max(plates)
	t = f(maxCakes)
	print "Case #%d: %d"%(case+1,t)
	j+=2;
