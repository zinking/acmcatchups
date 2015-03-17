class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
	def walkAndMatch( s,p):
	    np = len(p)
	    ns = len(s)
	    if np == 0 :
		if ns==0: return True
	    else:
		if p[0] == "*":
		    if np == 1: #* is the only thing left
			return True
		    else:
			nc = p[1]
			mf = False#match found
			for i in range(ns):
			    if s[i] == nc :
				if( walkAndMatch(s[i+1:],p[2:])):
				    mf = True
				    break
			if( not mf ):return False
		elif p[0] == "?":
		    if np == 1 and ns == 1:
			return True
		    else:
			return walkAndMatch(s[0:],p[1:]) or walkAndMatch(s[1:],p[1:])
		else:
		    if np>0 and ns>0 and p[0] == s[0]:
			return walkAndMatch(s[1:],p[1:])

	    return False
	import re
	pp=re.sub("\*+","*", p)
	return walkAndMatch(s,pp)
		    
        

s=Solution()

print s.isMatch("aa","a") == False
print s.isMatch("aa","aa") == True
print s.isMatch("aaa","aa") == False
print s.isMatch("aa", "*") == True 
print s.isMatch("aa", "a*") == True
print s.isMatch("ab", "?*") == True
print s.isMatch("aab", "c*a*b") == False

print s.isMatch("abacbc","a*b")
print s.isMatch("a","aa")

print s.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb", "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a")
