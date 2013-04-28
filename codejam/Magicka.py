   
def process_testcase( line ):
    def get_process_part( line ):
        index = 1;
        parts = line.split(" ");
        combine_number = int( parts[0] );
        combine ={};
        for i in range(0,combine_number):
            mapstr = parts[ index+i];
            ##print mapstr;
            key=mapstr[0:2];
            ##print key;
            combine [ key ] = mapstr[2];
            combine[ key[::-1] ] = mapstr[2];
            
        index += combine_number;
        opposed =[];
        oppose_number = int( parts[index] );
        
        for i in range(0,oppose_number):
            oppstr = parts[ index+i+1 ];
            opposed.append( oppstr );
        
        magic = list( parts[-1] );
        return ( combine, opposed, magic[0:-1] );
        
    def oppose( ma, ops ):
        for op in ops:
            if( op[0] in ma and op[1] in ma ):
                """lma = len(ma);
                i = ma[::-1].index( op[0] );
                j = ma[::-1].index( op[1] );
                i,j=lma-i-1,lma-j-1;
                if( i > j ): (i,j)=(j,i);
                del ma[i:j+1];"""
                ma = [];
        return ma;
        
    def combine( ma, combine):
        """
        s = "".join(ma);
        for k,v in combine.items():
            s = s.replace( k,v );
        i=0;
        while ( i < len(ma)-1 ):
            ck = (ma[i]+ma[i+1]);
            if( ck in combine.keys() ):
                del ma[i:i+2];
                ma[i:i] = combine[ck];
            i+=1;"""
        ck = "".join( ma[-2:]);

        if(  ck in combine.keys() ):
            del ma[-2:];
            ma.append( combine[ck] );
        return ma;
    #function definition start
    (co,op,ma) = get_process_part(line);
    """#print "".join(ma);
    #print co;
    #print op;
    old_len = 0;
    while( old_len != len(ma) ):
        old_len = len(ma);
        ma = combine(ma,co);
        ma = oppose(ma,op);"""
    n = len( ma );
    spell = ma[0:1];
    #print co;
    #print op;
    #print ma;
    for i in range( 1,n ):
        spell.append( ma[i] );
        #print 'spell,',spell;
        spell = combine( spell, co);
        #print 'spell,combine',spell;
        spell = oppose( spell, op);
        #print 'spell,oppose',spell;
        
    str = ", ".join( list(spell) );
    return "[%s]"%( str );
    
infile  = open("Magika.in","r");
outfile = open("Magika.out","w");

ntest = int( infile.readline() );
for i in range(0,ntest):
    r = process_testcase( infile.readline() );
    line = "Case #%d: %s\n"%(i+1,r);
    outfile.write( line );
    print line;
    
infile.close();
outfile.close();
            
        
    
    