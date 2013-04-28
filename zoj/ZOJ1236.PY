import sys

def eat_or_not_eat( cn, ar, tn ):
    days = 0
    e = [ 0 for i in range(cn) ]
    total_cen = 0
    #while True:
        
    """
    pn = 0
    for i in range(0,cn):
        if e[i] == 0:
            pn = max(tn[i],pn)
    """
    ip = 0
    cen = 0   #record the number of cow eaten in the cycle
    
    while total_cen < cn and ip<10: #in the largest cow cycle
        ci = -1   #record the minimum cow index
        mci = 260 #reocrd the minimum cow milk mount
        mcn = 0   #record the minimum cow numbers
        for i in range(0,cn):
            if e[i] == 0:
                ccmm = ar[i][days%(tn[i])] #curr cow milk amount
                if ccmm < mci:
                    mci = ccmm
                    ci  = i
                    mcn = 1
                elif ccmm == mci:
                    mcn += 1

        days+=1
        #print '[debug] cen=%d ci=%d mci=%d mcn=%d'%(cen,ci,mci,mcn)
        #print e
        if mcn == 1:#cow eate
            e[ci] = 1
            #cen += 1
            total_cen += 1
            ip=0
        else:
            ip+=1
        #no cow eaten on that day, good need to finish the cycle

    #total_cen += cen
    #if cen == 0 or total_cen == cn :
    if total_cen == 0:
        print 0,0
    else:
        print total_cen, days-ip
        
              
if __name__=="__main__1":   
    eat_or_not_eat( 4, [[7,1,2,9],[2],[7,1],[2]], [4,1,2,1] )
    print '###'
    eat_or_not_eat( 4, [[7,1,2,9],[2,1,3],[7,1],[2]], [4,3,2,1] )
    print '###'
    eat_or_not_eat( 4, [[2],[2],[2],[2]], [1,1,1,1] )


   
if __name__=="__main__":
    
    n = int( sys.stdin.readline() )
    for i in range(0,n):
        cn = int( sys.stdin.readline() )
        ar = []
        tn = []
        for j in range(0,cn):
            l = sys.stdin.readline()
            c = l.split()
            cc = map( lambda x:int(x), c )
            ar.append( cc[1:] )
            tn.append( cc[0]  )
        eat_or_not_eat( cn,ar,tn )
    