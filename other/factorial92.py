__author__ = 'awang'

n = raw_input()
n = int(n)


r=1
for i in range(1,n+1):
    r*=i
    while r%10==0:r/=10
    r=r%(10**12)

print r%(10**9)