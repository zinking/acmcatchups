def g(i,w):
    sw = w[i-5:i+4]
    lc = [1,2,3,5,6,7]
    uc = [0,4,8]
    alc = map(lambda i:sw[i].isupper(),lc)
    auc = map(lambda i:sw[i].islower(),uc)
    if( all(alc) and all(auc) ):
            print sw[1:-1]
            
