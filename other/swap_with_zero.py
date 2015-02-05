swapCount=0;
def swap_with_zero( arr, len, n):
    global swapCount
    i0 = arr.index(0)
    ix = arr.index(n)
    arr[i0] = n
    arr[ix] = 0
    swapCount+=1
    #print 'swap ',n,' with 0'
    

def solve( arr, n ):
    global swapCount
    def bfs( arr , n):
	#print 'bfs',arr
	for i in range(n) :
	    ai = arr[i]
	    aai = arr[ai]
	    if( i!=ai and aai == 0 ):
		swap_with_zero(arr,len,ai)
		bfs(arr,n)
	for i in range(n):
	    ai = arr[i]
	    if( i!=ai ):
		swap_with_zero(arr,len,ai)
		bfs(arr,n)

    bfs(arr,n)
    print arr
    print swapCount



if __name__=='__main__':
    a = [3,1,4,0,2]
    solve(a,len(a))
    a = [1,2,3,4,0]
    solve(a,len(a))
    
