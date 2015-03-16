class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
	nd = len(s)+1
	m = [ 0 for i in range(nd)];m[0]=1;
	for i in range(nd):
	    for j in range(0,i+1):
		if ( m[j] and s[j:i] in dict):
		    m[i]=1
		    break
	return m[-1]==1
	
	        


s = Solution()
print s.wordBreak("leetcode",["leet", "code"])
print s.wordBreak("leetcode",["lt","ee","code"])
print s.wordBreak("",[])
print s.wordBreak("ss",["s","bbb","bb"])
print s.wordBreak("cars", ["car","ca","rs"])
        
