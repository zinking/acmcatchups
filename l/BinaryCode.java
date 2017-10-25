class BinaryCode(object):
    def decode2(self,message):
    	r1 = self.decode1(message,0)
    	r2 = self.decode1(message,1)
    	return (r1,r2)
    
	def decode1(self,message,head):
		m = map(lambda ch:int(ch), message)
		lm = len(m)
		dm = [0]*lm
		dm[0] = head
		#m0=dm0+dm1
		dm[1] = m[0]-dm[0]
		if dm[1]!=0 and dm[1]!=1:
			return "NONE"
		for i in range(1,lm-1):
			#dm[i-1]+dm[i]+dm[i+1] = m[i]
			dm[i+1]=m[i]-(dm[i]+dm[i-1])
			if dm[i+1]!=0 and dm[i+1]!=1:
				return "NONE"
		rr="".join(map(lambda n:str(n),dm))
		return rr
		
	def decode(self,message):
		r1 = self.decode1(message,0)
		r2 = self.decode1(message,1)
		return (r1,r2)

