# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = raw_input()
n = int(n)
n1 = n
i = 1
k = n1//(5**i)
n0 = 0
while k:
    n0+=k
    i+=1
    k = n1//(5**i)

m = n0+10
a = [0]*m
a[0] = 1

def mul(A,b,C):
    #print 'mul ',b
    for i in range(0,m):
        C[i]=A[i]*b
    for i in range(0,m-1):
        C[i+1] += C[i]//10
        C[i] = C[i]%10


for i in range(1,n+1):
    cc = [0]*m
    mul(a,i,cc)
    a=cc
    #print a
r=""

s=0
for i in range(m-2,-1,-1):
    if a[i]==0:continue
    s=i
    break

for i in range(s,n0-1,-1):
    r+=str(a[i])
print r


