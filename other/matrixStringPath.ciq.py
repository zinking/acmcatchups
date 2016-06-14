"""
Question: How to implement a function to check whether there is a path for a string in a matrix of characters?  It moves to left, right, up and down in a matrix, and a cell for a movement. The path can start from any entry in a matrix. If a cell is occupied by a character of a string on the path, it cannot be occupied by another character again.

For example, the matrix below with three rows and four columns has a path for the string “BCCED” (as highlighted in the matrix). It does not have a path for the string “ABCB”, because the first “B” in the string occupies the “B” cell in the matrix, and the second “B” in the string cannot enter into the same cell again.

A B C E
S F C S
A D E E

"""
def matrixStrPath(mp,p):
    m = len(mp)
    n = len(mp[0])
    v = [ [ 0 for i in range(n)] for j in range(m)]
    found = [False]

    def dfs(i,j,p):
        if found[0]: return
        def getDirs(i,j):
            r = []
            if i-1>=0: r.append( (i-1,j) )
            if j-1>=0: r.append( (i,j-1) )
            if i+1<m: r.append( (i+1,j) )
            if j+1<n: r.append( (i,j+1) )
            return r
        if p == "":
            found[0] = True
            return
        else:
            if mp[i][j] == p[0] and v[i][j] == 0:
                v[i][j] = 1
                dirs = getDirs(i,j)
                for dir in dirs:
                    (ni,nj)=dir
                    dfs(ni,nj,p[1:])
    
    for i in range(m):
        for j in range(n):
            dfs(i,j,p)
    return found[0]

def runTest(t,e):
    (m, p) = t
    a = matrixStrPath(m, p)
    if e == a :
        print "pass"
    else:
        print "fail:",t,"expected:",e,"actual:",a

def runTests():
    m = [
        "ABCE",
        "SFCS",
        "ADEE"
    ]

    t1 = (m, "BCCED")
    e1 = True
    runTest(t1,e1)

    t2 = (m, "ABCB")
    e2 = False
    runTest(t2,e2)

    t3 = (m, "ABCZ")
    e3 = False
    runTest(t3,e3)


if __name__ == "__main__":
    runTests()
