import fileinput

data_rows = []
N = 0
K = 0
numbers = []
for idx, line in enumerate( fileinput.input() ):
	if idx == 0 :
		row1 = line.split(' ')
		N = int( row1[0] )
		K = int( row1[1] )
	elif idx == 1:
		row2 = line.split(' ')
		numbers = map(lambda x:int(x), row2 )
COUNT = 0
#print N,K
#print numbers
#for i in numbers:
#	for j in numbers:
#		if i-j == K :
#			COUNT+=1
#i=0
#j=0
#while i<N:
#	j=i+1
#	while j<N:
#		if abs(numbers[i] - numbers[j]) == K:
#			COUNT += 1
#		j+=1
#	i+=1
hitmap = {}
for i in numbers:
	hitmap[i] = 0
for i in numbers:
	if hitmap.has_key((i+K) ) or hitmap.has_key( (i-K) ):
		COUNT+=1
	del hitmap[i]
#l = filter( lambda x:x>=1, hitmap.values() )

#print len(l)
print COUNT
	
