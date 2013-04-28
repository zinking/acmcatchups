
"""
def anagrams( str1, str2):
	if len(str1)!=len(str2):
		return 0
	lookup = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523]
	sum1 = 1
	sum2 = 1
	for c in str1:
		sum1 *= lookup[(ord(c)-ord('A'))]
	for c in str2:
		sum2 *= lookup[(ord(c)-ord('A'))]
	if sum1 == sum2 :
		return 1
	else:
		return 0
		
print anagrams("aAzZhost","aAzZshot")
"""
def anagrams( str1, str2):
	if len(str1)!=len(str2):
		return 0
	l1 = map( lambda x:ord(x), str1 )
	l1.sort()
	l2 = map( lambda x:ord(x), str2 )
	l2.sort()
	n = len(str1)
	for i in range(n):
		if l1[i] != l2[i]:
			return 0
	return 1


#print anagrams("aAzZhost","aAzZshot")
#print anagrams("ass","saa")