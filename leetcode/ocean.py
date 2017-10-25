class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        m = len(matrix)
        if m == 0 : return []
        n = len(matrix[0])
        if n == 0 : return []

        pacific  = [ [ -1 for i in range(n)] for j in range(m)]
        atlantic = [ [ -1 for i in range(n)] for j in range(m)]
        for i in range(n):
            pacific[0][i] = 1
            atlantic[m-1][i] = 1
        for j in range(m):
            pacific[j][0] = 1
            atlantic[j][n-1] = 1

        def traverse(map, i, j, st=False):
            if i<0 or i>=m: return
            if j<0 or j>=n: return 
            if not st and map[i][j] == 1: return

            map[i][j] = 1
        
            if i>=1 and matrix[i][j] <= matrix[i-1][j]: traverse(map,i-1,j)
            if j>=1 and matrix[i][j] <= matrix[i][j-1]: traverse(map,i,j-1)
            if j<n-1 and matrix[i][j] <= matrix[i][j+1]: traverse(map,i,j+1)
            if i<m-1 and matrix[i][j] <= matrix[i+1][j]: traverse(map,i+1,j)

        for i in range(n):
            traverse(pacific,0,i, True)
            traverse(atlantic,m-1,i, True)
        for j in range(m):
            traverse(pacific,j,0, True)
            traverse(atlantic,j,n-1, True)

        print pacific
        print atlantic
        r = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    r.append((i,j))
        return r
        

solver = Solution()
input = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print solver.pacificAtlantic(input)
