import sys

def osmos( st, index, arr, op ):
    if index < len( arr ):
        if st > arr[index]:
            return osmos( st+arr[index], index+1, arr, op );
        else:
            remove_op = len(arr) - index;
            if ( st > 1 ):
                n = 0;
                while( st <= arr[index] ): 
                    st+= st-1;
                    n+=1;
                #n = ( arr[index] - st + (st-1) ) / ( st -1 ) 
                if ( n < ( remove_op ) ):
                    return osmos( st+arr[index], index+1, arr, op+n );
            return remove_op+op
    else:
        return op;

def osmos_wrap( case, st, index, arr, op ):
    op = osmos( st, index, arr, op );
    #print 'DEBUG case:%d, st:%d [%s]'%(case,st,arr)
    print 'Case #%d: %d'%(case, op );

"""    
2 3
3 5 5
"""
   
if __name__=="__main__":
    
    n = int( sys.stdin.readline() )
    for i in range(0,n):
        l1 = sys.stdin.readline()
        l1l = l1.split( );
        l2 = sys.stdin.readline()
        l2l = l2.split( );
        l2ll = map( lambda x:int(x), l2l )
        l2ll.sort();
        osmos_wrap( i+1,int( l1l[0] ), 0, l2ll, 0 );