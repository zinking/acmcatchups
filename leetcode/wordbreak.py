class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak1(self, s, dict):
	for t in dict:
	    if not t in s: return False
	toChar=lambda c:ord(c)
	sum=lambda x,y:x+y
	wordHash = lambda str:reduce(sum,map( toChar,str)) if len(str) > 0 else 0
	shash = wordHash(s) 
	dhash = [ wordHash(t) for t in dict]
	ddhash = reduce(sum,dhash,0)
	return ddhash == shash

    def wordBreak(self, s, dict):
	mask=[ 0 for i in range(len(s))]
	def isAllOne( s ):
	    for c in s:
		if c!=1:return False
	    return True
	def find( s,w,mask):
	    for i in range(len(s)-len(w)+1):
		allone = True
		match = True
		for j in range(len(w)):
		    if( s[i+j] != w[j] ):
			match=False
			break
		    if( mask[i+j] == 0 ):
			allone= False
		if allone: continue
		if match: return i
	    return -1
		
	while not isAllOne(mask):
	    cantFind=True
	    for word in dict:
		j =  find(s,word,mask)
		je = j+len(word)
		if( j != -1 ):
		    for k in range(j,je): mask[k]=1
		    cantFind=False
	    #print mask,cantFind
	    if cantFind: return False
	return True

        


s = Solution()
print s.wordBreak("leetcode",["leet", "code"])
print s.wordBreak("leetcode",["lt","ee","code"])
print s.wordBreak("",[])
print s.wordBreak("ss",["s","bbb","bb"])
print s.wordBreak("cars", ["car","ca","rs"])
        
