
import sys

lines= [
"4",
"4 11111",
"1 09",
"5 110011",
"0 1"
]

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    caseno = int(lines[0])
    casestrs = lines[1:]
    j = 1
    for casestr in casestrs:
	des = casestr.split()
	smax = int(des[0])
	ss = des[1]
	cur = 0
	ned = 0
	for i in range(smax+1):
	    #i mean shyness level
	    shn = int( ss[i])
	    if i>cur and shn>0 :
		delta = i-cur
		ned += delta
		cur += delta+shn
		#print 'add',cur,ned,cur,shn
	    else:
		cur += shn
		#print 'pas',cur,shn
	print "Case #%d: %d"%(j,ned)
	j+=1
