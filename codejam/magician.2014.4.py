import sys

def read_arrangements():
    n = 4
    r = []
    ans = int( sys.stdin.readline() )
    for i in range(0,n):
	line = sys.stdin.readline()
	l = map( lambda x:int(x), line.split() )
	r.append(l)
    return r[ans-1]

def magician( case, r1, r2 ):
    r = list( set(r1)&set(r2))
    if len(r)==1:
	print "Case #%d: %d"%(case, r[0])
    elif len(r)>1:
	print "Case #%d: Bad magician!"%(case)
    else:
	print "Case #%d: Volunteer cheated!"%(case)
    
   
if __name__=="__main__":
    
    n = int( sys.stdin.readline() )
    for i in range(0,n):
	r1 = read_arrangements()
	r2 = read_arrangements()
	magician( i+1, r1, r2 )
        
