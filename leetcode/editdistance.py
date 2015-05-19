class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
	word1=" "+word1
	word2=" "+word2
	m = len(word1)
	n = len(word2)
	a = [ [0 for j in range(n)] for i in range(m)]
	for i in range(m): a[i][0]=i
	for j in range(n): a[0][j]=j
	import pdb
	for i in range(1,m):
	    for j in range(1,n):
		e = 0 if word1[i]==word2[j] else 1
		a[i][j] = min(a[i-1][j-1]+e,a[i][j-1]+1,a[i-1][j]+1)
	return a[m-1][n-1]
	    

s = Solution()	
print s.minDistance("abc","abd")
print s.minDistance("abc","ac")
print s.minDistance(" abc"," ac")
print s.minDistance(" ac"," abc")
print s.minDistance("","")
print s.minDistance("","a")
print s.minDistance("","ab")
print s.minDistance("a","")
print s.minDistance("ab","")
print s.minDistance("a","b")
