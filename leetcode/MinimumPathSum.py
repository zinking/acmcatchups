"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        mpath = [
            [0 for j in range(n)] for i in range(m)
        ]
        for i in range(m):
            for j in range(n):
                if i==0: 
                    t=0x9ffff
                else:
                    t = grid[i][j]+mpath[i-1][j]
                if j==0: 
                    l=0x9ffff
                else:
                    l = grid[i][j]+mpath[i][j-1]
                mpath[i][j] = min(t,l)
                mpath[0][0] = grid[0][0]

        #print mpath
        return mpath[m-1][n-1]

def runTest(t,e):
    s = Solution()
    a = s.minPathSum(t)
    if e == a :
        print "success"
    else:
        print "fail:",t,"expected:",e,"actual:",a

def runTests():
    t1 = [[1,3,2,4],[1,2,3,4],[4,3,2,1],[4,1,3,2]]
    e1 = 12
    runTest(t1,e1)

if __name__ == "__main__":
    runTests()
