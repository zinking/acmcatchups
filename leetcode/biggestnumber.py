class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
    	def cmpStr(a,b):
    		if( b+a > a+b ): return 1
		elif( b+a < a+b ): return -1
		return 0
    			
        numstr = map( lambda x:str(x), num )
        numstr.sort(cmp=cmpStr)
        cb="".join(numstr)
        return int(cb)
        
s=Solution();
print s.largestNumber([3, 30, 34, 5, 9])


print s.largestNumber([220,2])
