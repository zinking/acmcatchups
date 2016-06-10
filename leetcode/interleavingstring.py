class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        def match1( s1, s2, s3):
	    l1,l2,l3=len(s1),len(s2),len(s3)
	    if l1+l2!=l3: return False
	    if l1==0 and l2==0 and l3==0 : return True
	    p1=False;p2=False
	    if l3>0 and l1>0 and s3[0]==s1[0]:
		p1 = match(s1[1:],s2,s3[1:])
	    if l3>0 and l2>0 and s3[0]==s2[0]:
		p2 = match(s1,s2[1:],s3[1:])
	    return p1 or p2
	def match( q ):
	    while q:
		(s1,s2,s3)=q.pop()
		l1,l2,l3=len(s1),len(s2),len(s3)
		if l1+l2!=l3: return False
		if l1==0 and l2==0 and l3==0 : return True
		if l3>0 and l1>0 and s3[0]==s1[0]:
		    q.append( (s1[1:],s2,s3[1:]) )
		if l3>0 and l2>0 and s3[0]==s2[0]:
		    q.append( (s1,s2[1:],s3[1:]) )
	    return False
	#return match( s1, s2, s3)
	return match( [(s1,s2,s3)])

s = Solution()

print s.isInterleave("aabcc","dbbca","aadbbcbcac")
print s.isInterleave("aabcc","dbbca","aadbbbaccc")
print s.isInterleave("aa","ab","aaba")
		
	    
s1="abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb"
s2="ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc"
s3="cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"
print s.isInterleave(s1,s2,s3)


s1="bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
s2="babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
s3="babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"

print s.isInterleave(s1,s2,s3)
