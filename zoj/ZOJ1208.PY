import sys

def roll_the_die( top, front, sequences ):
    pass

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
