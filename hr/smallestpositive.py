

def  smallestpositive( arr):
	l1 = arr.split(',')
	l2 = map( lambda x:int(x),  l1 )
	m = {}
	for n in l2:
		m[n] = 1
	import math
	
	smallest = 0
	while m.has_key( smallest+1 ):
		smallest += 1
		
	return smallest + 1
	
#print smallestpositive("-8,-10,0,7,-1,8,1,4,2")