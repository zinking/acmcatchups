class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
	word1+=" "
	word2+=" "
	m = len(word1)
	n = len(word2)
	a = [ [0 for j in range(n)] for i in range(m)]
	for i in range(m): a[i][0]=i
	for j in range(n): a[0][j]=j
	for i in range(1,m):
	    for j in range(1,n):
		e = 0 if word1[i]==word2[j] else 1
		a[i][j] = min(a[i-1][j-1]+e,a[i][j-1]+1,a[i][j-1]+1)
	print a[m-1][n-1]
	    

s = Solution()	
s.minDistance("abc","abd")
s.minDistance("abc","ac")
s.minDistance(" abc"," ac")
s.minDistance(" ac"," abc")
s.minDistance("","")
s.minDistance("","a")
s.minDistance("","ab")
s.minDistance("a","")
s.minDistance("ab","")
