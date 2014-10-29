#!/usr/bing/python


class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
	bookLen = len(S);
	wordLen = len(L[0]);
	dictLen = len(L);
	sentLen = wordLen*dictLen;

	hashDict = sum( [hash(w) for w in L] )
	"""
	paraHash = [
	    sum([  hash(S[w:w+wordLen])
	       for w in xrange(s,s+wordLen)] )
                   for s in xrange(bookLen-sentLen+1)
	]
	"""

	paraHash = [
	    sum([  hash(S[w:w+wordLen])
	       for w in xrange(s,s+sentLen-wordLen+1,wordLen)]) 
                   for s in xrange(bookLen-sentLen+1)
	]
	#print paraHash
	#print hashDict

	return [ i for i in xrange(bookLen-sentLen+1)
		 if paraHash[i]==hashDict ]
	

if __name__ == '__main__':
    S = "barfoothefoobarman"
    L = ["foo", "bar"]
    solution = Solution()
    print solution.findSubstring(S,L)
