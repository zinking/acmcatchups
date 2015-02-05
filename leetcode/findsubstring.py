#!/usr/bin/python


class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
	bookLen = len(S);
	wordLen = len(L[0]);
	dictLen = len(L);
	sentLen = wordLen*dictLen;
	wordHash = [
	    hash( S[i:i+wordLen] ) if S[i:i+wordLen] in L else 0
	                            for i in xrange(bookLen-wordLen+1)]
	hashDict = sum( [hash(w) for w in L] )
	return [ i for i in xrange(bookLen-sentLen+1)
		 if sum(wordHash[i:i+sentLen:wordLen])==hashDict ]
	

if __name__ == '__main__':
    S = "barfoothefoobarman"
    L = ["foo", "bar"]
    solution = Solution()
    print solution.findSubstring(S,L)
