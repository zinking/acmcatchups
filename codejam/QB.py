import sys

def manage_energy( ti, E, R, nac, ac ):
    vv = [ E for ii in range(0,nac)];
    if E > R :
        vv = [ 0 for ii in range(0,nac)];
        total = nac-1
        ze = zip( range(0,nac), ac );
        ze.sort( key=lambda x:x[1] , reverse=True);
        print ze
        for i in range(0,nac):
            ith = ze[i][0]
            val = min( total, ith )
            vv[ith] += ith * R
            if i==0: vv[ith] += E;
            total -= val;
            if total <= 0 : break
            
    elif  E < R :
        vv[0] = E
    result = 0
    for  ii in range( 0, nac ):
        result += ac[ii]*vv[ii];
        
    print 'Case #%d: %d'%(ti,result)

   
if __name__=="__main__":
    
    n = int( sys.stdin.readline() )
    for i in range(0,n):
        l1 = sys.stdin.readline()
        l1l = l1.split( );
        l2 = sys.stdin.readline()
        l2l = l2.split( );
        l2ll = map( lambda x:int(x), l2l )
        manage_energy( i+1, int(l1l[0]), int(l1l[1]), int(l1l[2]), l2ll );