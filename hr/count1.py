
"""
def countones(k):
	if k<10: return 1
	count = 0
	s = str(k)
	for c in s:
		if c=='1':
			count += 1
	return count + countones(k-1)
"""
#print countones(1300)


def countones(k):
	i=0
	j=1
	count = 0;
	for i in range(k+1):
		j=i
		while j != 0:
			if ( j%10 == 1 ):
				count+=1;
			j/=10
	return count

	
#print countones(13)
#print countones(1300)