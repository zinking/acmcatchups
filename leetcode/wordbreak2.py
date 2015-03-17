class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
	dd = filter( lambda x:x in s, dict)
	ns = len(s)
	jl = [ 0 for i in range(ns+1) ];jl[0]=1
	rr = [ [] for i in range(ns+1)];
	for i in range(1,ns+1):
	    for j in range(0,i):
		cw = s[j:i]
		dd = filter( lambda x:x in cw, dict)
		if jl[j]==1 and cw in dd:
		    jl[i] = 1
		    iw = dd.index(cw)
		    prev = rr[j]
		    if len(prev) == 0:
			rr[i].append([cw])
		    else:
			for w in prev:
			    w.append( cw )
			    rr[i].append( w )
	
	return rr[-1]
		
s=Solution()

print s.wordBreak("a",["a"])
print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])


print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])	    
