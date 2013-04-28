   
def process_testcase( line ):
    ops = line.split(" ");
    #to = 0;#time o robot cost
    #tb = 0;#time b robot cost
    t = { 'O':0, 'B':0 };
    other = { 'O':'B', 'B':'O'};
    lp = { 'O':1, 'B':1 };
    n = int( ops[0] );#total movements
    for i in range(0,n):
        cr = ops[1 + i*2];
        cp = int( ops[1 + i*2 +1] );
        #t[cr] += max( t[ other[cr] ], abs(cp -lp[cr]) + 1);
        time = abs(cp -lp[cr]) + 1;
        if ( t[ cr ] + time > t[ other[cr] ] ) : t[cr] += time;
        else: t[cr] = t[other[cr]]+1;
        lp[cr] = cp;
        
    return max( t['O'] , t['B'] );
    
infile  = open("BotTrust.in","r");
outfile = open("BotTrust.out","w");

ntest = int( infile.readline() );
for i in range(0,ntest):
    r = process_testcase( infile.readline() );
    line = "Case #%d: %d\n"%(i+1,r);
    outfile.write( line );
    
infile.close();
outfile.close();
            
        
    
    