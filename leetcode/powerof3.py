

def isPower3(n):
    if n == 1 or n == 3 or n == 9: return True

    def sumToDigit(n):
        while n > 10:
            s = sum(map(lambda x:int(x),str(n)))
            n = s
        return n

    return sumToDigit(n) == 9


#verify
p = []
for i in range(20):
    print 3**i, isPower3(3**i)

    
