class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
	self.result = []
	def dfs( s, l, dict):
	    ss = set(s)
	    ds = set( "".join(dict))

	    for cs in ss:
		if cs not in ds:
		    return
	    if s == "" :
		self.result.append( " ".join(l)) 
		return
	    dd = filter( lambda x:x in s, dict)
	    for w in dd:
		nw = len(w)
		if s[0:nw] == w:
		    l.append(w)
		    dfs( s[nw:], l, dd )
		    l.pop()
	dfs( s,[],dict)
	return self.result


s=Solution()

print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])

print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])	    
