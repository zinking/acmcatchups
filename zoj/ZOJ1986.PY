import sys

"""
max_note = {}
def max_sub( ar, l, r, st_val ):
    if max_note.has_key( (l,r,st_val) ):
        return max_note[ (l,r,st_val) ]
    result = 0;
    if l <= r:
        if( ar[l]>=st_val ):
            result = max( 1+max_sub(ar,l+1,r,ar[l]), max_sub(ar,l+1,r,st_val))
        else:
            result = max_sub(ar,l+1,r,st_val)
            
    max_note[(l,r,st_val)] = result 
    return result

    
def max_sub2( ar , n ):
    f = [1] * n
    r = range(0,n) #all point its previous to self
    for i in range(0,n):
        for j in range(0,i):
            if ar[j] < ar[i] and f[i]<(f[j]+1):
                f[i] = f[j]+1
                r[i] = j
    print max(f)
    #print r
    #print f
"""
def max_sub3( ar, n ):
    f = [0] * n
    f[0] = ar[0]
    len = 1
    for i in range(1,n):
        if ar[i] > f[len-1]:
            f[len] = ar[i]
            len+=1
            continue
        l = 0
        r = len-1
        while( l<=r ):
            m = ( l+r )/2
            if f[m]<ar[i] :
                l = m+1
            else:
                r = m-1
        f[l] = ar[i]
    print len
    #print f

def process( ar,sn ):
    max_sub3( ar, sn )

   
if __name__=="__main__":
    n = int( sys.stdin.readline() )
    for i in range(0,n):
        sn = int( sys.stdin.readline() )
        ar = []
        for j in range(0,sn):
            ar.append( int( sys.stdin.readline() ) )
        process(ar,sn)
    